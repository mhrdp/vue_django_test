import { createStore } from "vuex";
import { axiosRefresh } from "@/refresh_api";

export default createStore({
  state: {
    accessToken: localStorage.getItem('accessToken') || null,
	refreshToken: localStorage.getItem('refreshToken') || null,

    isLoading: false,
    authenticated: false,
  },
  mutations: {
	setAuth(state, status){
		state.authenticated = status
	},

	setUser(state, username){
		state.user = username
	},

	updateAccessToken(state, access_token){
		state.accessToken = access_token
	},

	logOut(state){
		state.token = null
		state.authenticated = false
	},	
  },
  actions: {
	  refreshToken(context){
		  return new Promise((resolve, reject) => {
			  axiosRefresh
				.post('/backdoor/token/refresh/', {
				  'refresh': context.state.refreshToken
			  })
			  	.then(response => {
					console.log('New token successfully generated!')
					context.commit('updateAccessToken', response.data.access)
					resolve(response.data.access)
				})
			  	.catch(error => {
					console.log('Error in generating token')
					reject(error)
				})
		  })
	  },
  },
  modules: {},
})
