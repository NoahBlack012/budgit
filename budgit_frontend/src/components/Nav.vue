<template>
    <div id="nav">
        <div class="navbar">
            <router-link to="/">Home</router-link>
            <router-link to="/budget">Budget</router-link>
            <router-link to="/stats">Statistics</router-link>
            <router-link to="/login" @click="logout">Logout</router-link>
        </div>
    </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
    name: "Nav",
    methods: {
        ...mapActions(['loginUser']),
        logout(){
            this.loginUser(0)
            this.$router.push("/login")
        }
    }
}
</script>

<style>
    #nav {
        min-width: 100%;
        top: 0%;
        left: 0%;
        height: fit-content;
    }

    .navbar{
        height: fit-content;
        min-width: 100%;
        background-color: #fff;
        padding: 20px;
    }

    a{
        border-radius: 20px;
        border: 1px solid #FF4B2B;
        background-color: #FF4B2B;
        color: #FFFFFF;
        font-size: 12px;
        font-weight: bold;
        padding: 12px 45px;
        letter-spacing: 1px;
        text-transform: uppercase;
        text-decoration: none;
        margin: 7%;
    }

    a.router-link-exact-active{
        background-color: #a82710;
        border: 1px solid #a82710;
    }

</style>