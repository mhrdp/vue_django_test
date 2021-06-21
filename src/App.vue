<template>
  <nav class="navbar navbar-expand-lg sticky-top">
      <div class="container-fluid">
        <a class="navbar-brand">Wlog</a>
		
		<div v-if="!$store.state.authenticated">
			<div class="align-items-right">
				<ul class="navbar-nav">
					<li class="nav-item">
						<router-link to="/" class="nav-link">
							Sign In
						</router-link>
					</li>
					<li class="nav-item">
						<router-link to="#" class="nav-link">
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
	this.$store.commit('setAuth', true)
	
	const token = this.$store.state.token
	if(token){
		axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
	} else {
		axios.defaults.headers.common['Authorization'] = ''
	}
  },
  methods: {
	signOut(){
		localStorage.removeItem('token')
		axios.defaults.headers.common['Authorization'] = ''
		
		this.$store.commit('setToken', '')
		this.$store.commit('setAuth', false)
		
		this.$router.push('/')
	}
  }
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
</style>
