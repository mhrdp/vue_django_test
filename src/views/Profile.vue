<template>
	<div class="container">
		<div class="outside row">
			<div class="col-md-3">
				<h4>Trending</h4>
				<button @click="getCurrentUser">Current User</button>
				<p>Look at console for output</p>
			</div>
			
			<div class="col-12 col-md-9">
				<div v-if="identifier === activeUser">
					<div class="alert alert-danger fs-7" role="alert" v-if="errors.length">
						<p v-for="error in errors" v-bind:key="error">
						  <i class="bi bi-exclamation-diamond-fill"></i> {{error}}
						</p>
					</div>
		
					<form method="POST" @submit.prevent="postPosts">
						<textarea
							class="form-control"
							v-model="post"
							placeholder="Thoughts?"
							style="height:130px"
							@keyup="minCharRequired"
							name="post">
						</textarea>
						
						<div class="row mt-2 mb-4">
							<div class="col-6">
								<span v-if="charLeft < 300">
									<span style="color:red">{{charLeft}}</span>
								</span>
								<span v-else>
									<span style="color:green">{{charLeft}}</span>
								</span>
							</div>

							<div class="col-6 d-flex justify-content-end">
								<button class="btn btn-primary">Post</button>
							</div>
						</div>
					</form>
				</div>
			
				<div v-if="isLoading">
					<div class="d-flex justify-content-center m-5">
						<div class="spinner-border text-info" role="status">
							<span class="visually-hidden">Loading...</span>
						</div>
					</div>
				</div>
				<div v-else>
					<div v-for="posts in timeline" v-bind:key="posts">
						<div class="card mb-4">
							<div class="card-body">
								<h5><strong>{{posts.userdata.username}}</strong></h5>
								<p class="text-muted fs-7 fw-light">
									{{posts.date_posted.slice(0, 10)}}
									<span>{{posts.date_posted.slice(11, 16)}}</span>
								</p>
								
								<p>{{posts.post.slice(0, 300)}} <span>...</span></p>
								<router-link v-bind:to="posts.get_absolute_url">
									<button class="btn btn-sm btn-secondary">
										Read in full	
									</button>
								</router-link>
							</div>
						</div>
					</div>
				</div>

				<div v-if="loadingNext">
					<div class="d-flex justify-content-center m-5">
						<div class="spinner-border text-info" role="status">
							<span class="visually-hidden">Loading...</span>
						</div>
					</div>
				</div>
				<div v-else>
					<!-- return none -->
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast';

export default{
	name: 'Profile',
	data(){
		return {
			post: '',
			errors: [],
			success: [],
			timeline: [],

			indetifier: '',
			activeUser: '',
			page: 1,
			hasNext: true,
			loadingNext: false,
			
			// Character count of the textarea
			charLeft: 0,
			isLoading: true,
		}
	},
	components: {
	},
	mounted(){
		document.title = 'Town Hall | Wlog'
		this.getTimeline()

		window.onscroll = () => {
			let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight

			if(bottomOfWindow && this.hasNext){
				// Activate spinner when reaching the bottom of the page
				// Then deactivate it after the API responded,
				// The call to deactivate it was inside getTimeline() function in methods:{...}
				this.loadingNext = true

				this.page += 1
				this.getTimeline()
			}
		}
	},
	created(){
		this.identifier = this.$route.params.username
		this.activeUser = localStorage.getItem('username')

	},
	watch: {
		// This is to watch for route change, so that the data could change dynamically
		// If you not implementing this, when you change the url the data won't get updated
		// unless you refresh the page.
		// the function is as following: $route(to, from){ *conditions* }
		$route(to){
			if(to.name === 'Profile'){
				this.getTimeline()
				this.identifier = this.$route.params.username
			}
		}
	},
	methods: {
		/* 
		   * Normally, for every authenticated axios requests you need to put an Authorization header,
		   * Like, axios
		   			.post('url', {data}, {
						headers: {'Authorization': token}
					}),
		   but the function in /src/refresh_api.js handle the headers' request
		   * This made wrote a headers inside axios request optional, because that function already made global by utilizing it inside main.js
		*/

		/*
		getCurrentUser(){
			axios
				.get('/backdoor/api/user/')
				.then(response => {
					console.log(response.data.id)
					console.log(response.data.username)
				})
				.catch(error => {
					console.log(error.response)
				})
		},
		*/

		async getTimeline(){
			this.errors = []
			const username = this.$route.params.username

			await axios
				.get(`/backdoor/api/posts/${username}/?page=${this.page}`)
				.then(response => {
					if(response.data){
						// Deactive spinner when API already returning a response
						// To activate the spinner, use the function in 'mounted(){...}'
						this.loadingNext = false
						this.hasNext = false

						if(response.data.next){
							this.hasNext = true
						}
						
						/*
							Append the data into variable so the page won't reloading
							each time it change the page
							- response.data return an Object
							- response.data.result return a List/an Array
						*/
						for(let i = 0; i < response.data.results.length; i++){
							this.timeline.push(response.data.results[i])
						}
					}
				})
				.catch(error => {
					if(error){
						this.errors.push('There \'s a loading problem, please refresh your browser.')
					}
				})

			this.isLoading = false
		},

		minCharRequired(){
			let left = this.post.length
			this.charLeft = left

			return this.charLeft
		},
	
		async postPosts(e){
			this.errors = []
			this.success = []
			
			
			if(this.post === ''){
				this.errors.push('Post field can\'t be empty')
			}
			if(this.post.length < 300){
				this.errors.push('You need more than 300 characters!')
			}
			
			if(!this.errors.length){
				const formData = {
					post: this.post,
				}

				await axios
					.post('/backdoor/api/posts/', formData,  {
						headers: {
							'Content-Type': 'application/json'
						}
					})
					.then(response => {
						if(response.data){
							toast({
								message: 'Your post has been successfully posted',
								type: 'is-success',
								dismissable: true,
								duration: 2000,
								position: 'top-center',
								animate: {
									in: 'fadeIn', out: 'fadeOut'
								},
							})
						}
						
						this.post = ''
						this.charLeft = 0

						// prevent form for submitting again
						e.preventDefault()
					})
					.catch(error => {
						if(error.response){
							for(const property in error.response.data){
								this.errors.push(`${property}: ${error.response.data[property]}`)
							}
						} else {
							this.errors.push('Something went wrong!')
						}
					})
			}
		},
	},
}
</script>

<style scoped>
.outside.row {
	padding: 100px 15px 50px 15px;
}

.fs-7 {
	font-size: .75rem;
}
</style>
