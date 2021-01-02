<template>
  <div class="home">
    <Nav />
    <h1>Home</h1>
  </div>
</template>

<script>
import Nav from "../components/Nav"
import { mapGetters } from 'vuex';

export default {
  name: 'Home',
  components: {
    Nav,
  },
  computed: mapGetters(['userid']), 
  created() {
    if (! this.userid){
      this.$router.push("/login")
    }
  }
}
</script>
