<template>
  <div class="page">
    <h1 id = "title">Login</h1>
    <div class = "form">
      <form @submit.prevent="login">
        <input type="text" id="username" v-model="username" placeholder="Username" autocomplete="off"><br>
        <input type="password" id="password" v-model="password" placeholder="Password"><br>
        <input type="submit" value="Log In" id = "button">
      </form>
      <div class="signup" id = "button">
        <router-link to="/signup" id="link">Signup</router-link>
      </div>
    </div>
  </div>
</template>

<style>
  #title{
    font-size: 30pt;
    color: white;
  }

  .page{
    width: 50%;
    min-height: 40vh;
    background: #2F1D85;
    grid-template-rows: 40% 60%;
    grid-template-columns: 100%;
  }

  .form{
    overflow: auto;
    display: grid;
    place-items: center;
    grid-row: 2;
  }

  input{
    background-color: #91B1EB;
    border: none;
    margin: 1px;
    padding: 10px;
    text-align: center;
  }

  input:focus{
    background-color: #6F5FB8;
  }

  input, input::placeholder{
    font-size: 12pt;
    color: white;
  }

  #button{
    background-color: #91B1EB;
    padding: 3px;
    margin: 5px;
  }

  #button:hover{
    background-color: #6F5FB8
  }

  .signup{
    width: fit-content;
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


