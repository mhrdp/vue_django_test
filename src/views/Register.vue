<template>
	<div class="outside row">
		<div class="col-12 col-md-6">
			<h2>Register Now</h2>
		</div>
		
		<div class="col-12 col-md-6">
			<div class="card mx-auto" style="width: 80%">
				<div class="card-header">
					<h4 class="text-muted"><strong>Registration</strong></h4>
				</div>
				
				<div class="card-body">
					<form method="POST" @submit.prevent="submitForm" class="row g-2">
						
						<p class="card-subtitle text-muted">
							<strong>Login Data</strong>
						</p>
						
						<hr/>
						
						<div class="alert alert-danger fs-7" v-if="error.length">
							<p v-for="err in error" v-bind:key="err">{{err}}</p>
						</div>
						
						<div class="form-floating mb-2 col-12">
							<input class="form-control floating-input" type="text" id="username" placeholder="Username" name="username" v-model="userdata.username" required>
							<label for="username">
								Username<span style="color:red">*</span>
							</label>
							<span class="text-muted fs-8">
								<i class="bi bi-exclamation-circle"></i> Unique with 150 characters maximal, no white space.
							</span>
						</div>
						
						
						<div class="form-floating mb-2 col-12">
							<input class="form-control floating-input" type="password" id="password" placeholder="Password" name="password" v-model="userdata.password" required>
							<label for="password">
								Password<span style="color:red">*</span>
							</label>
							<span class="text-muted fs-8">
								<i class="bi bi-exclamation-circle"></i> Minimum 8 in length with combination of letters and numbers.
							</span>
						</div>
						
						<div class="form-floating mb-2 col-12">
							<input class="form-control floating-input" type="password" id="password2" placeholder="Repeat Password" name="password2" v-model="userdata.password2" required>
							<label for="password2">
								Repeat Password<span style="color:red">*</span>
							</label>
							<span class="text-muted fs-8">
								<i class="bi bi-exclamation-circle"></i> Repeat your password correctly.
							</span>
						</div>
						
						<div class="form-floating mb-5 col-12">
							<input class="form-control floating-input" type="email" id="email" placeholder="Email" name="email" v-model="userdata.email" required>
							<label for="email">
								Email<span style="color:red">*</span>
							</label>
							<span class="text-muted fs-8">
								<i class="bi bi-exclamation-circle"></i> Please enter your valid email address.
							</span>
						</div>
						
						<p class="card-subtitle text-muted">
							<strong>User Data</strong>
						</p>
						<hr/>
						
						<div class="col-12 col-md-6">
							<div class="form-floating mb-2 col-12">
								<input class="form-control floating-input" type="text" id="first_name" placeholder="First Name" v-model="userdata.first_name" name="first_name">
								<label for="first_name">
									First Name
								</label>
							</div>
						</div>
						
						<div class="col-12 col-md-6">
							<div class="form-floating mb-2 col-12">
								<input class="form-control floating-input" type="text" id="last_name" placeholder="Last Name" v-model="userdata.last_name" name="last_name">
								<label for="last_name">
									Last Name
								</label>
							</div>
						</div>
						
						<!--
						<div class="form-floating mb-2 col-12">
							<textarea class="form-control floating-input" id="bio" placeholder="Bio" v-model="bio" style="height:200px" @keyup="charsLeft" required></textarea>
							<label for="bio">
								Short bio...
							</label>
							
							<span v-if="characterLeft >= 0" class="mt-2">
								<p class="fs-7">{{characterLeft}} chars</p>
							</span>
							<span v-else class="mt-2">
								<p class="fs-7" style="color:red">{{characterLeft}}</p>
							</span>
						</div>
						-->
						
						<div class="d-grid">
							<button class="btn btn-primary">Register</button>
						</div>
					</form>
					
					<hr />
					
					<h6 class="card-subtitles mt-2 text-muted">Already have an account? Let's <router-link to="/login">sign in</router-link> here!</h6>
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';
import {toast} from 'bulma-toast';

export default {
	name: 'Register',
	data(){
		return {
			userdata: {
				username: '',
				password: '',
				password2: '',
				email: '',
				first_name: '',
				last_name: '',
			},
			error: [],
			success: [],
			
			// To count character left in bio field
			/*
			bio: '',
			maxChr: 255,
			characterLeft: 255,*/
		}
	},
	mounted(){
		this.document = 'Register | Wlog'
	},
	methods: {
		async submitForm(){
			// Initialize the array once again to prevent it being stacked
			// This essentially refresh the array for each request
			this.error = []
			
			if(this.userdata.username === ''){
				this.error.push('Username is missing')
			}
			if(this.userdata.password === ''){
				this.error.push('Password is missing')
			}
			if(this.userdata.password !== this.userdata.password2){
				this.error.push('Password did not match')
			}
			if(this.userdata.email === ''){
				this.error.push('Email is missing')
			}
			
			if(!this.error.length){
				const formData = {
					username: this.userdata.username,
					password: this.userdata.password,
					email: this.userdata.email,
					first_name: this.userdata.first_name,
					last_name: this.userdata.last_name,
				}
				
				await axios
					.post('/backdoor/api/users/', formData)
					.then(response => {
						
						if(response.data){
							toast({
								message: 'Your account has been successfully created! Please login to continue',
								type: 'is-success',
								dismissable: true,
								pauseOnHover: true,
								duration: 5000,
								position: 'top-center',
								animate: {in: 'fadeIn', out: 'fadeOut'},
							})
							
							this.$router.push('/login')
						}
						
					})
					.catch(error => {
						if(error.response){
							for(const property in error.response.data){
								// This is using backquote (`), you need a backquote for string formatting in Vue.
								this.error.push(`${property}: ${error.response.data[property]}`)
							}
							console.log(JSON.stringify(error.response.data))
						} else if(error.message){
							this.error.push('Something went wrong, please try again.')
							console.log(JSON.stringify(error))
						}
					})
			}
		},
		/*
		charsLeft(){
			if(this.bio.length <= this.maxChr){
				let left = this.maxChr - this.bio.length
				this.characterLeft = left
			} else {
				let left = 'Exceed allowed characters!'
				this.characterLeft = left
			}
			return this.characterLeft
		}*/
	},
	computed: {
		
	}
}
</script>

<style scoped>
.p-15 {
	padding: 15px;
}

.fs-7 {
	font-size: 0.9rem !important;
}

.fs-8 {
	font-size: 0.7rem !important;
}

.outside.row {
	padding: 100px 15px 50px 15px;
}

.row {
	padding: 15px 15px 15px 15px;
}

.card {
    box-shadow: 0 0 5px 1px #ccc;
}
</style>