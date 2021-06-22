<template>
  <nav class="navbar navbar-expand-lg sticky-top">
      <div class="container-fluid">
        <a class="navbar-brand">Wlog</a>
		
		<div v-if="!this.$store.state.authenticated">
			<div class="align-items-right">
				<ul class="navbar-nav">
					<li class="nav-item">
						<router-link to="/login" class="nav-link">
							Sign In
						</router-link>
					</li>
					<li class="nav-item">
						<router-link to="/register" class="nav-link">
							Sign Up
						</router-link>
					</li>
				</ul>
			</div>
		</div>
		
		<div v-else>
			<div class="align-items-right">
				<ul class="navbar-nav">
					<li class="nav-item">
						<router-link
							to="#"
							class="nav-link"
							@click="signOut"
							>
							Sign Out
						</router-link>
					</li>
				</ul>
			</div>
		</div>
      </div>
    </nav>
  <router-view />
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      showMobileMenu: false,
    }
  },
  beforeCreate(){
	// Check whether user is authenticated before start of every pages
	if(localStorage.getItem('token')){
		this.$store.commit('setAuth', true)
	
		const token = this.$store.state.token
		if(token){
			axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
		}
	}
	
  },
  methods: {
	signOut(){
		// Refresh all credentials
		localStorage.removeItem('token')
		axios.defaults.headers.common['Authorization'] = ''
		
		this.$store.commit('setToken', '')
		this.$store.commit('setAuth', false)
		
		this.$router.push('/login')
	}
  },
}
</script>

<style>
#app {
  font-family: 'Open Sans', sans-serif;
  color: #2c3e50;
}

.navbar {
  box-shadow: 0 1px 5px 1px #cccccc;
  background-color: #fff;
}

html {
	overflow-x: hidden;
}
</style>
