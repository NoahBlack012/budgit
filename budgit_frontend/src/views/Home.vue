<template>
  <div class="home">
    <Nav />
    <img alt="Vue logo" src="../assets/logo.png">
    <h1>Home</h1>
  </div>
</template>

<script>
// @ is an alias to /src
//import HelloWorld from '@/components/HelloWorld.vue'
import Nav from "../components/Nav"

export default {
  name: 'Home',
  components: {
    Nav,
  }
}
</script>
