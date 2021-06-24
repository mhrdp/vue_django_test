<template>
  <div class="row align-items-center h-80vh">
    <div class="col-12 col-sm-6">
      <div class="card text-start mx-auto" style="width:70%">
        <div class="card-body">
          <h4 class="card-title"><strong>Log In</strong></h4>
          <p class="card-subtitle text-muted fs-7">Please enter your username and password</p>

          <hr/>

          <div class="alert alert-danger fs-7" role="alert" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">
              <i class="bi bi-exclamation-diamond-fill"></i> {{error}}
			</p>
            
          </div>
      
          <form method="POST" class="mt-4 mb-5" @submit.prevent="submitForm">
			<div class="form-floating mb-2">
				<input id="username" name="username" type="text" class="form-control floating-input" placeholder="Username" v-model="username" required>
				<label for="username">Username</label>
			</div>
			
			<div class="form-floating">
				<input id="password" name="password" type="password" class="form-control floating-input" placeholder="Password" v-model="password" required>
				<label for="password">Password</label>
			</div>
            <div class="d-grid mt-3">
              <button class="btn btn-primary">Log In</button>
            </div>
          </form>

          <hr />

          <h6 class="card-subtitles mt-2 text-muted">Don't have account? How about <router-link to="/register">Sign up</router-link>?</h6>
        </div>
      </div>
    </div>
    
    <div class="mobile col-12 col-sm-6">
      <h1><strong>Hey! Let's Think Together For a Secs!</strong></h1>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import axios from 'axios';
import {toast} from 'bulma-toast';

export default {
  name: 'Login',
  data(){
    return {
      username: '',
      password: '',
      errors: [],
    }
  },
  components: {
  },
  mounted() {
    document.title = 'Wlog'
  },
  methods: {
    async submitForm(){
	  // Initialize the array once again to prevent it being stacked
	  // This essentially refresh the array for each request
	  this.errors = []
	  
      axios.defaults.headers.common['Authorization'] = ''
	  localStorage.removeItem('token')
	  
	  const formData = {
		username: this.username,
		password: this.password,
	  }
	  
	  await axios
	  .post('/backdoor/token/', formData)
	  .then(response => {
		const token = response.data.access
		this.$store.commit('setToken', token)
		
		axios.defaults.headers.common['Authorization'] = 'Bearer ' + token
		localStorage.setItem('token', token)
		
		toast({
			message: 'Welcome home! Enjoy your time here!',
			type: 'is-success',
			dismissable: true,
			pauseOnHover: true,
			duration: 5000,
			position: 'top-center',
			animate: {in: 'fadeIn', out: 'fadeOut'},
		})
		
		const toPath = this.$route.query.to || '/dashboard'
		this.$router.push(toPath)
	  })
	  .catch(error => {
		if(error.response){
			for (const property in error.response.data){
				// This is using backquote (`), you need a backquote to initialize Vue's components inside a string.
				this.errors.push(`${property}: ${error.response.data[property]}`)
			}
		} else {
			this.errors.push('Something went wrong, please try again!')
			console.log(JSON.stringify(error))
		}
	  })
    }
  }
};
</script>

<style scoped>
  .h-80vh {
    height: 80vh;
  }
  
  .fs-7 {
	font-size: 0.9rem !important;
  }

  .row {
    padding: 100px 15px 50px 15px;
  }

  .card {
    box-shadow: 0 0 5px 1px #ccc;
  }

  @media (max-width: 576px) {
    .mobile {
      padding-top: 150px;
      padding-bottom: 150px;
    }
  }
</style>
