<template>
	<div class="row outside">
		<div class="container">
			<div v-if="isLoading">
				<div class="d-flex justify-content-center m-5">
					<div class="spinner-border text-info" role="status">
						<span class="visually-hidden">Loading...</span>
					</div>
				</div>
			</div>
			<div v-else>
				<div v-if="referredDetail">
					<div class="card">
						<div class="card-body">
							<router-link v-bind:to="referredDetail.userdata.get_absolute_url" class="link-dark">
								<h5>{{referredDetail.userdata.username}}</h5>
							</router-link>
							<p class="text-muted fs-7">
								{{referredDetail.date_posted.slice(0, 10)}}
								{{referredDetail.date_posted.slice(11, 16)}}
							</p>
							<p>{{referredDetail.post}}</p>
						</div>

						<div class="m-2">
						<div class="card">
							<div class="card-body">
								<h6>Refer to:</h6>
								<router-link v-bind:to="referredDetail.referred_post.userdata.get_absolute_url" class="link-dark">
									<h5>{{referredDetail.referred_post.userdata.username}}</h5>
								</router-link>
								<p class="text-muted">
									{{referredDetail.referred_post.post}}
								</p>

								<router-link v-bind:to="referredDetail.referred_post.get_absolute_url">
									Visit original post
								</router-link>
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
	name: 'ReferredPostDetail',
	data(){
		return {
			referredDetail: null,

			errors: [],

			isLoading: false,
		}
	},
	mounted(){
		document.title = 'Details | Wlog'
		this.getReferredPostDetail()
	},
	methods: {
		getReferredPostDetail(){
			this.errors = []
			this.isLoading = true

			const username = this.$route.params.username
			const post_slug = this.$route.params.post_slug
			const original_slug = this.$route.params.referred_post_slug

			axios
				.get(`/backdoor/api/referred/${username}/${post_slug}/referto/${original_slug}/`)
				.then(response => {
					this.referredDetail = response.data
					this.isLoading = false
				})
				.catch(error => {
					if(error.response){
						this.errors.push('There\'s something wrong when fetching the data, please refresh your page.')
					} else {
						this.errors.push('There\'s something wrong, but we\'re not sure why. :(')
					}
				})
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
