import { createStore } from "vuex";

export default createStore({
  state: {
    token: '',
    isLoading: false,
    isAuthenticated: false,
  },
  mutations: {
    setToken(state, token){
      state.token = token
      state.isAuthenticated = true
    }
  },
  actions: {},
  modules: {},
});
