<template>
  <div class="page">
    <div class = "form">
      <form @submit.prevent="login">
        <h1 id="signintitle">Sign In</h1>
        <input type="text" id="username" v-model="username" placeholder="Username" autocomplete="off"><br>
        <input type="password" id="password" v-model="password" placeholder="Password"><br>
        <input type="submit" value="SIGNIN" id = "button">
      </form>
    </div>
    <div class="signup">
      <div class="signupcontent">
        <h1 id="signuptitle">Sign Up</h1>
        <button id = "button">
          <router-link to="/signup" id="link">Signup</router-link>
        </button>
      </div>
    </div>
  </div>
</template>

<style>
  #signintitle{
    color: black;
  }

  #signuptitle{
    color: #fff;
  }

  .page{
    display: grid;
    border-radius: 10px;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
    0 10px 10px rgba(0,0,0,0.22);
    width: 50%;
    min-height: 50%;
    grid-template-columns: 50% 50%;
  }

  .form{
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    grid-column: 1;
    min-height: 100%;
  }

  input, #input{
    background-color: #eee;
    border: none;
    padding: 5%;
    margin: 1%;
    text-align: center;
  }

  input, input::placeholder{
    font-size: 12pt;
    color: black;
  }

  #button{
    border-radius: 20px;
    border: 1px solid #FF4B2B;
    background-color: #FF4B2B;
    color: #FFFFFF;
    font-size: 12px;
    font-weight: bold;
    padding: 12px 45px;
    letter-spacing: 1px;
    text-transform: uppercase;
  }

  #button:hover{
    cursor: pointer;
  }

  .signup, .login{
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100%;
    background-color: #FF416C;
    grid-column: 2;
  }

  h1, p{
    color: #fff;
    text-transform: uppercase;
    font-weight: bold;
  }

  #link{
    text-decoration: none;
    color: white
  }
</style>

<script>

import { mapActions, mapGetters } from 'vuex'
import axios from 'axios'

export default {
  name: 'Login',
  data(){
    return {
      username: '',
      password: '',
    }
  }, 
  methods: {
    ...mapActions(['loginUser']),
    async login(){
      const res = await axios.post(`${process.env.VUE_APP_BASE}/login`, {
            api_key: process.env.VUE_APP_API_KEY,
            username: this.username, 
            password: this.password
        })
      
      if (res.data.login){
        this.loginUser(res.data.userid)
        this.$router.push("/")
      }
    }
  }, 
  computed: mapGetters(['userid'])
}
</script>


