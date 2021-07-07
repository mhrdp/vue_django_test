/*
 * This file will handle Authorization headers of each requests being made from the frontend
 * And if the token was expired, it will generate a new one via refreah token
 * Which mean that using a header context in every authenticated axios request became optional because this file already handle it
*/

import axios from 'axios';
import store from './store';
import router from './router';

export default function axiosSetUp(){
	axios.default.baseURL = '<http://localhost:8000/backdoor/>';
	
	// request interceptors to add Authorization headers for each frontend's request'
	axios.interceptors.request.use(
		function(config){
			const token = localStorage.getItem('accessToken');
			if(token){
				config.headers.Authorization = `Bearer ${token}`;
			}
			return config;
		},
		function(error){
			return Promise.reject(error);
		}
	);
	
	// response interceptors to modify the behaviours on response
	axios.interceptors.response.use(
		function(response){
			// for any request statuses that within 2xx territory
			return response;
		},

		// This need to be async as the store's action need to be awaited
		async function(error){
			const originalRequest = error.config;
			if(error.response.status === 401 && originalRequest.url.includes('api/token/refresh/')){
				// logout user and redirect to login page
				store.commit('refreshAccess');
				router.push('/login');
				return Promise.reject(error);
			} else if(error.response.status === 401 && !originalRequest._retry) {
				originalRequest._retry = true;

				// wait for the store's action to be trigerred before return
				await store.dispatch('refreshToken');
				return axios(originalRequest);
			}
			return Promise.reject(error);
		}
	)
}
