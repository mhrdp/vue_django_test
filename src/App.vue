<template>
  <nav class="navbar navbar-expand-md fixed-top">
      <div class="container-fluid">
		<div class="d-inline-block">
			<div v-if="this.$store.state.authenticated">
				<a class="p-2" data-bs-toggle="offcanvas" href="#sidebar" role="button" aria-controls="sidebar" style="margin-right:15px;">
					<i class="bi bi-three-dots"></i>
				</a>
				<router-link to="/dashboard" class="navbar-brand test-start">Wlog</router-link>
			</div>
			<div v-else>
				<router-link to="/login" class="navbar-brand test-start">Wlog</router-link>
			</div>
		</div>
		
		<div class="align-items-right">
			<a class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#navbarCollapse" aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle Navigation">
				<span class="navbar-toggler-icon"><i class="bi bi-three-dots-vertical"></i></span>
			</a>
		</div>

			<div v-if="!this.$store.state.authenticated" class="collapse navbar-collapse flex-row-reverse" id="navbarCollapse">
					<ul class="navbar-nav navbar-nav-scroll" style="--bs-scroll-height: 150px">
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
		
			<div v-else class="collapse navbar-collapse flex-row-reverse" id="navbarCollapse">
				<ul class="navbar-nav">
					<li class="nav-item">
						<router-link to="/dashboard" class="nav-link">
							Dashboard
						</router-link>
					</li>
					<li class="nav-item">
						<router-link v-bind:to="username" class="nav-link">
							Profile
						</router-link>
					</li>
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
    </nav>
	<div class="offcanvas offcanvas-start" data-bs-scroll="true" tabindex="-1" id="sidebar" aria-labelledby="sidebarLabel">
	  <div class="offcanvas-header">
		<h5 class="offcanvas-title" id="sidebarLabel">Menu</h5>

		<div v-if="!this.$store.state.authenticated">
			<span></span>
		</div>
		<div v-else>
			<button type="button" class="btn-close text-reset" data-bs-dismiss="offcanvas" aria-label="Close"></button>
		</div>

	  </div>
	  <hr/>
	  <div class="offcanvas-body">
		<h6 class="card-subtitle">PUBLIC</h6>
		
		<div class="list-group list-group-flush">
		  <a class="list-group-item list-group-item-action town-active" href="#">
			<i class="bi bi-megaphone-fill p-2"></i>Town Hall
		  </a>
		</div>
		
		<h6 class="card-subtitle mt-4">COMMUNITY</h6>
		<div class="list-group list-group-flush">
		  <a class="list-group-item list-group-item-action dashboard-active" href="/dashboard">
			<i class="bi bi-tv-fill p-2"></i>Control Room
		  </a>
		  <router-link v-bind:to="username" class="list-group-item list-group-item-action private-active">
			<i class="bi bi-unlock-fill p-2"></i>Private Space
		  </router-link>
		  <a class="list-group-item list-group-item-action community-active" href="#">
			<i class="bi bi-people-fill p-2"></i>Community Space
		  </a>
		</div>
		  
		<h6 class="card-subtitle mt-4">EXTRAS</h6>
		<div class="list-group list-group-flush">
		  <a class="list-group-item list-group-item-action dashboard-active" href="/dashboard">
			<i class="bi bi-wrench p-2"></i>Settings
		  </a>
		</div>
	  </div>
	</div>
  <router-view />
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      showMobileMenu: false,
	  username : '',
    }
  },
  beforeCreate(){
	// Check whether user is authenticated before start of every pages
	if(localStorage.getItem('accessToken')){
		this.$store.commit('setAuth', true)
	}
  },
  created(){
	this.username = `/${localStorage.getItem('username')}`
  },
  methods: {
	signOut(){
		// Refresh all credentials
		localStorage.removeItem('accessToken')
		localStorage.removeItem('refreshToken')
		localStorage.removeItem('user_id')
		localStorage.removeItem('username')

		axios.defaults.headers.common['Authorization'] = ''
		
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

.is-success {
	background-color: #48c78e;
	color: #fff;
}

.offcanvas-start {
	/* override sidebar's default width */
	width: 300px !important;
}

html {
	overflow-x: hidden;
}
</style>
