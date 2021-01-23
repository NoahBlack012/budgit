<template>
  <div class="stats">
    <Nav />
    <h1>Statistics</h1>
    <div class="graphs">
      <div class="pietotals">
        <PieTotals id="expense_category" class="chart" />
      </div>

      <div class="monthlyexpenses">
        <MonthlyExpenses id = "monthly-expenses" class="chart" />
      </div>
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
  }, 
}
</script>

<style scoped>
  .stats{
    min-width: 100%;
    min-height: 100%;
  }
  .graphs {
    min-width: 100%;
    min-height: 100%;
    display: grid;
    grid-template-columns: 50% 50%;
  }

  .chart{
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
    0 10px 10px rgba(0,0,0,0.22);
    margin: 10px;
    color: rgb(45, 34, 189);
  }


  .pietotals{
    grid-column: 1;
  }

  .monthlyexpenses{
    grid-column: 2;
  }
</style>