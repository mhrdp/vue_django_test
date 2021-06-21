import { createStore } from "vuex";

export default createStore({
  state: {
    token: '',
    isLoading: false,
    authenticated: false,
  },
  mutations: {
	setAuth(state, status){
		state.authenticated = status
	},
	
    setToken(state, token){
      state.token = token
      state.authenticated = true
    },
	
	/*removeToken(state, token){
		state.token = ''
		state.isAuthenticated = false
	},*/
  },
  actions: {},
  modules: {},
});
