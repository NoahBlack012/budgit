<template>
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <!--<router-link to="/login">Login</router-link> |-->
      <router-link to="/budget">Budget</router-link> |
      <router-link to="/stats">Statistics</router-link>
    </div>
</template>

<script>
export default {
    name: "Nav",
}
</script>

<style scoped>
    #nav {
        width: 100%;
        background-color: #24292E;
        padding: 1em;
    }

    #nav a {
        font-weight: bold;
        color: #BABCB7;
    }

    #nav a.router-link-exact-active {
        color: #42b983;
    }
</style>