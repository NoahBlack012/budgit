<template>
  <div class="stats">
    <Nav />
    <h1>Statistics</h1>
    <div class="graphs">
      <pie-chart v-if="loaded" :chartdata="chartdata" :options="options" id="expense_category" />
    </div>
  </div>
</template>

<script>
import Nav from "../components/Nav";
import PieChart from "../components/charts/PieChart";
import axios from "axios";
export default {
  name: "Stats",
  components: {
    Nav,
    PieChart,
  },
  data: () => {
    return {
      loaded: false, 
      chartdata: null, 
      options: {
        responsive: true,
        maintainAspectRatio: false
      }
    };
  },
  async mounted () {
    this.loaded = false
    try {
      const data = await axios.post(`${process.env.VUE_APP_BASE}/get_pie_totals`, {
        userid: process.env.VUE_APP_USERID, // Replace with state var
        api_key: process.env.VUE_APP_API_KEY,
      })
      this.chartdata = data.data.totals_datasets
      this.loaded = true
    } catch (e) {
      console.error(e)
    }
  }
}
        // var res = await axios.post(
        //   `${process.env.VUE_APP_BASE}/get_pie_totals`,
        //   {
        //     userid: process.env.VUE_APP_USERID, // Replace with state var
        //     api_key: process.env.VUE_APP_API_KEY,
        //   }
        // );
// axios.post(`${process.env.VUE_APP_BASE}/get_pie_totals`, {
//         "userid": process.env.VUE_APP_USERID, // Replace with state var
//         "api_key": process.env.VUE_APP_API_KEY
//     }
// )
// .then(res => {
//     this.category_datasets = res.data.totals_datasets
//     this.category_datasets = JSON.parse(this.category_datasets)
//     console.log(this.category_datasets);
// })
// .catch(err => console.error(err))
// console.log(this.category_datasets);
</script>

<style scoped>
.graphs {
  display: grid;
  grid-template-columns: 33% 33% 33%;
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