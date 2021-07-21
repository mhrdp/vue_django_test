<template>
	<div class="row outside">
		<div class="container" v-if="isLoading">
			<div class="d-flex justify-content-center m-5">
				<div class="spinner-border text-info" role="status">
					<span class="visually-hidden">Loading...</span>
				</div>
			</div>
		</div>

		<div v-else>
			<div v-if="referredPost" class="container">
				<div class="card mb-4" v-for="post in referredPost" v-bind:key="post">
					<div class="card-body">
						<router-link v-bind:to="post.userdata.get_absolute_url" class="link-dark">
							<h5>{{post.userdata.username}}</h5>
						</router-link>

						<p class="text-muted fs-7">{{post.date_posted.slice(0, 10)}}
						<span>{{post.date_posted.slice(11, 16)}}</span></p>

						<p>{{post.post.slice(0, 300)}}...</p>

						<div class="card">
							<div class="card-body">
								<p class="text-muted">
									Refer to post #<strong>{{post.referred_post.slug}}</strong><br/>
									<span class="fs-7">{{post.referred_post.post.slice(0, 100)}}...</span>
								</p>
							</div>
						</div>
						
						<router-link v-bind:to="post.get_absolute_url">
							<button class="btn btn-primary mt-3">Read in full</button>
						</router-link>
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

export default {
	name: 'ReferredPost',
	data(){
		return {
			referredPost: [],
			errors: [],

			isLoading: true,
			hasNext: true,
			loadingNext: false,
			page: 1,
		}
	},
	mounted(){
		document.title = `${this.$route.params.username} Referred Page | Wlog`
		this.getReferredPost()

		window.onscroll = () => {
			let bottomOfWindow = document.documentElement.scrollTop + window.innerHeight === document.documentElement.offsetHeight

			if(bottomOfWindow && this.hasNext){
				// Activate spinner when reaching the bottom of the page
				// Then deactivate it after the API responded,
				// The call to deactivate it was inside getTimeline() function in methods:{...}
				this.loadingNext = true
				this.page += 1
				this.getReferredPost()
			}
		}
	},
	watch: {
		$route(to){
			if(to.name === 'ReferredPost'){
				this.getReferredPost()
			}
		}
	},
	methods: {
		async getReferredPost(){
			// Initialize the array once again, to refresh ir on every request
			this.errors = []
			
			const username = this.$route.params.username
			await axios
				.get(`/backdoor/api/referred/${username}/?page=${this.page}`)
				.then(response => {
					// Take a closer look at the JSON's structure at the Web's Django Rest Framework API
					// For this particular API, the data was encapsulated inside nested array named 'results'
					// hence the 'response.data.results'
					// this.referredPost = response.data.results
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
					for(let i=0; i < response.data.results.length; i++){
						this.referredPost.push(response.data.results[i])
					}
				})
				.catch(error => {
					this.isLoading = false
					if(error.response){
						this.errors.push('There\'s an error happening when fetching the data, please try again')
					} else {
						this.errors.push('Something happened, but we don\'t know what :(')
					}
				})

				this.isLoading = false
		}
	}
}
</script>

<style scoped>
.row.outside {
	padding: 100px 15px 50px 15px;
}

.fs-7 {
	font-size: .75rem;
}
</style>
