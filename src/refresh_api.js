import axios from 'axios';
import store from '@/store';

const APIUrl = 'http://localhost:8000';

// Refresh access token on request if it was expired
const axiosRefresh = axios.create({
	baseURL: APIUrl,
	headers: {
		'Content-Type': 'application/json'
	}
})

const getAPI = axios.create({
	baseUrl: APIUrl,
})

getAPI.interceptors.response.use(undefined, function(err){
	// if error status is 401, it means the token was expired
	if(err.config && err.response && err.response.status === 401){
		store
			.dispatch('refreshToken') // attempt to get new token by running this function
			.then(access_token => {
				axios
				.request({
					baseUrl: APIUrl,
					method: 'get',
					headers: {
						// store the token into Authorization header
						'Authorization': `Bearer ${access_token}`
					}
				})
				.then(response => {
					console.log(response.data)
					console.log('Successfully get new token')
				})
				.catch(error => {
					console.log('Probably got new access token, but something happened. Try using it, if nothing happened then all good!')
					return Promise.reject(error)
				})
			})
			.catch(error => {
				return Promise.reject(error)
			})
	}
})

export { axiosRefresh, getAPI }
