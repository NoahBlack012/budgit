<template>
  <div class="login">
    <h1>Login</h1>
    <form @submit.prevent="login">
      <input type="text" id="username" v-model="username" placeholder="username">
      <input type="password" id="password" v-model="password" placeholder="password">
      <input type="submit" value="Login">
    </form>
    <router-link to="/signup">Signup</router-link>
  </div>
</template>

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

<style scoped>

</style>
