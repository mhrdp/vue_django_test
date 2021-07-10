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
						
						<div class="row mt-2">
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

				<div v-for="posts in timeline" v-bind:key="posts">
					<h5>{{posts.userdata.username}}</h5>
					<p class="subtitles p-1">{{posts.date_posted}}</p>
					<p>{{posts.post}}</p>
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
			
			// Character count of the textarea
			charLeft: 0,
		}
	},
	mounted(){
		document.title = 'Town Hall | Wlog'
	
		this.getTimeline()
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
		getTimeline(){
			this.errors = []
			const username = this.$route.params.username

			axios
				.get(`/backdoor/api/posts/${username}`)
				.then(response => {
					if(response.data){
						this.timeline = response.data
					}
				})
				.catch(error => {
					if(error){
						this.errors = 'There \'s a loading problem, please refresh your browser.'
					}
				})
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
						console.log(response.data)
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
		}
	},
}
</script>

<style scoped>
.outside.row {
	padding: 100px 15px 50px 15px;
}
</style>
