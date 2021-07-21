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
									<a href="#" class="btn btn-link btn-sm" data-bs-toggle="modal" data-bs-target="#referFormModal">
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

					<div class="modal fade" id="referFormModal" aria-hidden="true" aria-labelledby="referFormModal" tabindex="-1">
						<div class="modal-dialog modal-lg modal-dialog-scrollable">
							<div class="modal-content">
								<div class="modal-header">
									<h5 class="modal-title" id="referFormModalLabel">Refer Post</h5>
									<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="close"></button>
								</div>

								<div class="modal-body">
									<p class="fs-7">Referred post:</p>
									<div class="card mb-4">
										<div class="card-body">
											<h6 class="text-muted"><b>{{post.userdata.username}}</b></h6>
											<p class="text-muted fs-7 fw-light">{{post.post.slice(0, 150)}} ...</p>
										</div>
									</div>


									<p>Post your comments here:</p>
									<form method="POST" @submit.prevent="referPostForm">
										<div class="form-floating mb-2">
											<textarea type="textarea" class="form-control" id="floatingInput" placeholder="Write your comment here" style="height:200px" v-model="yourComment"></textarea>
											<label for="post">Your comment here</label>
										</div>
										<button class="btn btn-primary" data-bs-dismiss="modal">Post</button>
									</form>
								</div>
								<div class="modal-footer">
									<button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
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
import {toast} from 'bulma-toast';

export default {
	name: 'PostDetail',
	data(){
		return {
			// Set the data value to null if for whatever reason you get UncaughtError: cannot read property ... of undefined
			// Then set v-if in parent html's tag so the page will wait until the data fully rendered
			// This problem basically exist because when the page was rendered, the data has not yet fully read which is why Vue throw an error
			post: null,
			yourComment: '',

			referForm: false,

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
			}
		}
	},
	created(){
		
	},
	methods: {
		referPost(){
			this.referForm = true
		},

		async referPostForm(){
			const username = localStorage.getItem('username')
			const referred_post = this.post.id

			const formData = {
				referred_post: referred_post,
				post: this.yourComment,
			}

			await axios
				.post(`/backdoor/api/referred/`, formData)
				.then(response => {
					if(response.data){

						toast({
							message: 'Your referral has been posted, thank you!',
							type: 'is-success',
							dismissable: true,
							pauseOnHover: true,
							duration: 2000,
							position: 'top-center',
							animate: {in: 'fadeIn', out: 'fadeOut'},
						})

						this.$router.push(`/${username}/referred`)
					}
				})
				.catch(error => {
					console.log(error.data)
					if(error.response){
						this.errors.push('There\'s an error happening, please try again.')
					}
				})
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

					this.isLoading = false
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
		},
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
