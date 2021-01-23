<template>
  <div class="home">
    <Nav />
    <h1>Home</h1>
    <div class="content">
      <div class="items">
        <RecentItems id="items" />
      </div>
      <div class="links">
        <div id="links">
          <div class="budgetlink">
            <router-link to="/budget" id="link">View Your Budget</router-link>
          </div>
          <div class="statslink">
            <router-link to="/stats" id="link">View Insights About your Budget</router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import RecentItems from "../components/RecentItems"; 
import { mapGetters } from 'vuex';

export default {
  name: 'Home',
  components: {
    Nav,
    RecentItems,
  },
  computed: mapGetters(['userid']), 
  created() {
    if (! this.userid){
      this.$router.push("/login")
    }
  }
}
</script>

<style scoped>
  .home{
    min-width: 100%;
    min-height: 100%;
  }

  .content{
    display: grid;
    grid-template-columns: 50% 50%;
    min-width: 100%;
    min-height: 100%;
  }

  .items{
    background-color: #FF4B2B;
    grid-column: 1;
    min-width: 100%;
    min-height: 100%;
  }

  .links{
    grid-column: 2;
    min-width: 100%;
    min-height: 100%;
    background-color: #fff;
  }

  #links{
    min-width: 100%;
    min-height: 100%;
    margin: 30px;
    display: grid;
    grid-template-rows: 50% 50%;
  }

  .budgetlink{
    grid-row: 1;
  }

  .statslink{
    grid-row: 2;
  }
</style>
