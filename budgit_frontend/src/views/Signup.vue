<template>
    <div class="signup">
        <h1>Signup</h1>
        <form @submit.prevent="signup">
            <input type="text" name="username" id="username" v-model="username" placeholder="username">
            <input type="password" name="password" id="password" v-model="password" placeholder="password">
            <input type="password" name="confirm_password" id="confirm_password" v-model="confirm_password" placeholder="Confirm Password">
            <input type="submit" value="Create User">
        </form>
        <div v-if="non_password_match">The passwords entered do not match</div>
        <div v-if="username_taken">That username is already taken</div>
    </div>
</template>

<script>
import axios from 'axios'
import { mapActions } from 'vuex'

export default {
    name: "Signup", 
    data(){
        return{
            username: '',
            password: '',
            confirm_password: '',
            non_password_match: false,
            username_taken: false,
        }
    },

    methods: {
        ...mapActions(['loginUser']), 

        async signup(){
            this.username_taken = false
            this.non_password_match = false
            if (this.password !== this.password){
                this.non_password_match = true
            }else{
                const res = await axios.post(`${process.env.VUE_APP_BASE}/signup`, {
                    api_key: process.env.VUE_APP_API_KEY,
                    username: this.username, 
                    password: this.password
                })
                if (res.data.user_created){
                    this.loginUser(res.data.userid)
                    this.$router.push('/')
                }else{
                     this.username_taken = true
                }
            }
        }
    }

}
</script>