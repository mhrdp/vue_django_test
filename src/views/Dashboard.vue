<template>
	<div class="outside row">
		<h1 class="p-15">Dashboard</h1>
		
		<!-- Latest Post -->
		<div class="row">
			<div class="col-12 col-md-6">
				<div class="card card-shadow" style="width: 100%; height:400px">
				  <div class="card-body">
					<h5 class="card-title"><strong>Latest Activity</strong></h5>
					<hr/>
					<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
					<a href="#" class="card-link">Card link</a>
					<a href="#" class="card-link">Another link</a>
				  </div>
				</div>
				
				<!-- Community Row -->
				<div class="row mt-4">
					<div class="col-12 col-lg-6">
						<div class="card card-shadow" style="width: 100%; height:400px">
						  <div class="card-body">
							<h5 class="card-title"><strong>Latest In Community</strong></h5>
							<hr/>
							<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
							<a href="#" class="card-link">Card link</a>
							<a href="#" class="card-link">Another link</a>
						  </div>
						</div>
					</div>
					
					<div class="col-12 col-lg-6">
						<div class="card" style="width: 100%; height:400px">
						  <div class="card-body">
							<h5 class="card-title"><strong>What's Hot?</strong></h5>
							<hr/>
							<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
							<a href="#" class="card-link">Card link</a>
							<a href="#" class="card-link">Another link</a>
						  </div>
						</div>
					</div>
				</div>
			</div>
			
			<!-- Your activity col derived from main row -->
			<div class="col-12 col-md-6">
				<h5 class="card-title">Post Something:</h5>
				<form method="POST" @submit.prevent="submitForm" class="mb-4">
					<textarea
						class="form-control" 
						style="height:130px;" 
						placeholder="Want to write something?" 
						v-model="post" 
						@keyup="minCharRequired">
					</textarea>
					
					<div class="d-grid d-flex gap-3 mt-2 justify-content-end align-items-center">
						<span v-if="charLeft < 300">
							<span style="color:red">{{charLeft}}</span>
						</span>
						<span v-else>
							<span style="color:green">{{charLeft}}</span>
						</span>
						
						<button class="btn btn-primary">Post</button>
					</div>
					
				</form>
				
				<div class="card card-shadow" style="width: 100%; height:400px">
				  <div class="card-body">
					<h5 class="card-title"><strong>Your Activities</strong></h5>
					<hr/>
					<p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
					<a href="#" class="card-link">Card link</a>
					<a href="#" class="card-link">Another link</a>
				  </div>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
	export default {
		name: 'Dashboard',
		data(){
			return {
				post: '',
				charLeft: 0,
			}
		},
		mounted(){
			document.title = 'Control Room | Wlog'
			
		},
		methods: {
			async submitForm(){
			},
			
			minCharRequired(){
				// count the length of the written post so user know whether they post qualified to submit or not
				let left = this.post.length
				this.charLeft = left
				return this.charLeft
			}
		}
	}
</script>

<style scoped>
.p-15 {
	padding: 15px;
}

.fs-7 {
	font-size: .9rem !important;
}

.outside.row {
	padding: 100px 15px 50px 15px;
}

.card-shadow {
    box-shadow: 0 0 5px 1px #ccc;
}
</style>