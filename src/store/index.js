import { createStore } from "vuex";
//import { axiosRefresh } from "@/refresh_api";

import axios from "axios";

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
		state.accessToken = localStorage.setItem('accessToken', access_token)
	},

	refreshAccess(state){
		state.accessToken = localStorage.removeItem('accessToken')
		state.refreshToken = localStorage.removeItem('refreshToken')
		state.authenticated = false
	},	
  },
  actions: {
	  // Refresh the token and update it to mutation
	  async refreshToken({state, commit}){
		  const refreshURL = '/backdoor/token/refresh/'
		  try {
			  await axios
			  	.post(refreshURL, {
					'refresh': state.refreshToken
				})
			  	.then(response => {
					if(response.status === 200){
						commit('updateAccessToken', response.data.access)
					}
				})
		  } catch(e){
			  console.log(e.response)
		  }
	  },
  },
  modules: {},
})
