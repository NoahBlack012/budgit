<template>
  <div class="stats">
    <Nav />
    <h1>Statistics</h1>
    <div class="graphs">
      <PieTotals id="expense_category" class="chart" />
      <MonthlyExpenses id = "monthly-expenses" class="chart" />
    </div>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import PieTotals from "../components/PieTotals"
import MonthlyExpenses from "../components/MonthlyExpenses"
import { mapGetters } from 'vuex'

export default {
  name: "Stats",
  components: {
    Nav,
    PieTotals,
    MonthlyExpenses,
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
  .stats{
    min-width: 100%;
    min-height: 100%;
  }
  .graphs {
    min-width: 100%;
    display: grid;
    grid-template-columns: 33% 33% 33%;
  }

  .chart{
    background-color: #fff;
  }

  #expense_category {
    grid-column: 1;
  }
  #expense_category2 {
    grid-column: 2;
  }
  #expense_category3 {
    grid-column: 3;
  }
</style>