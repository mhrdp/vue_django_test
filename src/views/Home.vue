<template>
  <div class="row align-items-center h-80vh">
    <div class="col-12 col-sm-6">
      <div class="card text-start mx-auto" style="width:25rem">
        <div class="card-body">
          <h4 class="card-title"><strong>Log In</strong></h4>
          <p class="card-subtitle mt-2 text-muted">Please enter your username and password</p>

          <hr/>

          <div class="alert alert-danger fs-6" role="alert" v-if="errors.length">
            <p v-for="error in errors" v-bind:key="error">
              <i class="bi bi-exclamation-diamond-fill"></i> {{error}}
			</p>
            
          </div>
      
          <form method="POST" class="mt-4 mb-5" @submit.prevent="submitForm">
            <label for="username">Username</label>
            <input id="username" name="username" type="text" class="form-control" placeholder="Username" v-model="username" required>

            <label for="password" class="mt-2">Password</label>
            <input id="password" name="password" type="password" class="form-control" placeholder="Password" v-model="password" required>
            <div class="d-grid mt-3">
              <button class="btn btn-primary">Log In</button>
            </div>
          </form>

          <hr />

          <h6 class="card-subtitles mt-2 text-muted">Don't have account? How about <a href="#">Sign up</a>?</h6>
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
import axios from 'axios'

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
		
		const toPath = this.$route.query.to || '/dashboard'
		this.$router.push(toPath)
	  })
	  .catch(error => {
		if(error.response){
			for (const property in error.response.data){
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

  .row {
    padding: 15px;
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
