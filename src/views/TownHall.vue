<template>
	<div class="container">
		<div class="outside row">
			<div class="col-md-3 hidden">
				<h4>Trending</h4>
			</div>
			
			<div class="col-12 col-md-9">
				<form method="GET" @submit.prevent="postPosts">
					<textarea
						class="form-control"
						v-model="posts"
						placeholder="Thoughts?"
						style="height:130px"
						@keyup="minCharRequired">
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
		</div>
	</div>
</template>

<script>
export default{
	name: 'TownHall',
	data(){
		return {
			posts: '',
			timeline: [],
			
			// Character count of the textarea
			charLeft: 0,
		}
	},
	mounted(){
		document.title = 'Town Hall | Wlog'
	},
	methods: {
		minCharRequired(){
			let left = this.posts.length
			this.charLeft = left
			return this.charLeft
		}
	}
}
</script>

<style scoped>
.outside.row {
	padding: 100px 15px 50px 15px;
}
</style>