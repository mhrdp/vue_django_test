<template>
	<div class="container">
		<div class="row outside">
			<div v-if="isLoading">
				<div class="d-flex justify-content-center m-5">
					<div class="spinner-border text-info" role="status">
						<span class="visually-hidden">Loading...</span>
					</div>
				</div>
			</div>
			<div v-else>
				<div v-if="post">
					<div class="card">
						<div class="card-body">
							<div class="card-header mb-2">
								<h4 class="card-title">Post's Detail</h4>
							</div>

							<h5>{{post.userdata.username}}</h5>
							<p class="text-muted fs-7 fw-light">
								{{post.date_posted.slice(0, 10)}}
								<span>{{post.date_posted.slice(11, 16)}}</span>
							</p>
							<p>{{post.post}}</p>

							<div class="container d-flex justify-content-center">
								<div class="col-3">
									<a href="#" class="btn btn-link btn-sm" @click="referPost">
										<i class="bi bi-pen fs-5" title="Refer this article"></i>
									</a>
								</div>
								<div class="col-3">
									<a href="#" class="btn btn-link btn-sm">
										<i class="bi bi-bookmarks fs-5" title="Bookmark this"></i>
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'PostDetail',
	data(){
		return {
			// Set the data value to null if for whatever reason you get UncaughtError: cannot read property ... of undefined
			// Then set v-if in parent html's tag so the page will wait until the data fully rendered
			// This problem basically exist because when the page was rendered, the data has not yet fully read which is why Vue throw an error
			post: null,

			errors: [],
			post_slug: '',
			username: '',
			isLoading: false,
		}
	},
	mounted(){
		document.title = 'Post Detail | Wlog'
		this.getPost()
	},
	watch: {
		$route(to){
			if(to.name === 'PostDetail'){
				this.getPost()
				//this.post_slug = this.$route.params.post_slug
				//this.username = this.$route.params.username
			}
		}
	},
	created(){
		//this.post_slug = this.$route.params.post_slug
		//this.username = this.$route.params.username
	},
	methods: {
		referPost(){
			
		},

		async getPost(){
			this.errors = []
			this.isLoading = true

			const post_slug = this.$route.params.post_slug
			const username = this.$route.params.username

			await axios
				.get(`backdoor/api/posts/${username}/${post_slug}`)
				.then(response => {
					console.log(response.data)
					if(response.data){
						this.post = response.data
					}
				})
				.catch(error => {
					if(error.response){
						console.log(error.response)
						this.errors.push('The response from server was interrupted, please refresh your page.')
					} else {
						console.log(error)
						this.errors.push('Something happened, please refersh your page.')
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
</style>
