<template>
	<div class="row">
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
						<p class="card-subtitle fs-7 text-muted">
							<strong>Login Data</strong>
						</p>
						<hr/>
						
						<div class="form-floating mb-2 col-12">
							<input class="form-control floating-input" type="text" id="username" placeholder="Username" name="username" v-model="username" required>
							<label for="username">
								Username<span style="color:red">*</span>
							</label>
						</div>
						
						<div class="form-floating mb-2 col-12">
							<input class="form-control floating-input" type="password" id="password" placeholder="Password" name="password" v-model="password" required>
							<label for="password">
								Password<span style="color:red">*</span>
							</label>
						</div>
						
						<div class="form-floating mb-2 col-12">
							<input class="form-control floating-input" type="password" id="password2" placeholder="Repeat Password" name="password2" v-model="password2" required>
							<label for="password2">
								Repeat Password<span style="color:red">*</span>
							</label>
						</div>
						
						<div class="form-floating mb-5 col-12">
							<input class="form-control floating-input" type="email" id="email" placeholder="Email" name="email" v-model="email" required>
							<label for="email">
								Email<span style="color:red">*</span>
							</label>
						</div>
						
						<p class="card-subtitle fs-7 text-muted">
							<strong>User Data</strong>
						</p>
						<hr/>
						
						<div class="col-12 col-md-6">
							<div class="form-floating mb-2 col-12">
								<input class="form-control floating-input" type="text" id="first_name" placeholder="First Name" v-model="firs_tname" name="first_name" required>
								<label for="first_name">
									First Name
								</label>
							</div>
						</div>
						
						<div class="col-12 col-md-6">
							<div class="form-floating mb-2 col-12">
								<input class="form-control floating-input" type="text" id="last_name" placeholder="Last Name" v-model="last_name" name="last_name" required>
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
				</div>
			</div>
		</div>
	</div>
</template>

<script>
import axios from 'axios';

export default {
	name: 'Register',
	data(){
		return {
			username: '',
			password: '',
			password2: '',
			email: '',
			first_name: '',
			last_name: '',
			error: '',
			
			// To count character left in bio field
			/*
			bio: '',
			maxChr: 255,
			characterLeft: 255,*/
		}
	},
	beforeCreate(){
		localStorage.removeItem('token')
	},
	mounted(){
		this.document = 'Register | Wlog'
	},
	methods: {
		async submitForm(){
			if(this.username === ''){
				this.error.push('Username is missing')
			}
			if(this.password === ''){
				this.error.push('Password is missing')
			}
			if(this.password !== this.password2){
				this.error.push('Password did not match')
			}
			if(this.email === ''){
				this.error.push('Email is missing')
			}
			
			if(!this.error){
				const formData = {
					username: this.username,
					password: this.password,
					password2: this.password2,
					email: this.email,
					first_name: this.first_name,
					last_name: this.last_name,
				}
				
				axios
				.post('#')
				.then(response => {
					this.$router.push('/login')
				})
				.catch(error => {
					console.log(error)
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

.row {
	padding: 50px 15px 50px 15px;
}

.card {
    box-shadow: 0 0 5px 1px #ccc;
  }
</style>