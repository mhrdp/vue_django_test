import { createStore } from "vuex";

export default createStore({
  state: {
    accessToken: '',
    isLoading: false,
    authenticated: false,
  },
  mutations: {
	setAuth(state, status){
		state.authenticated = status
	},
	
    setAccessToken(state, access_token){
      state.accessToken = access_token
      state.authenticated = true
    },

	setUser(state, username){
		state.user = username
	},

	logOut(state){
		state.token = null
		state.authenticated = false
	},	
  },
  actions: {
  },
  modules: {},
})
