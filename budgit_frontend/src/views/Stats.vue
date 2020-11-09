<template>
  <div class="stats">
    <Nav />
    <h1>Statistics</h1>
    <div class="graphs">
      <pie-chart :chartlabel="label" :datapoints="datapoints" :labels="labels" id="expense_category" />
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
  data() {
    return {
      label: "Chart",
      labels: ["A", "B", "C", "D", "E"],
      datapoints: [1, 2, 3, 4, 5],
      totals_datacollection:  [],
      category_datasets: null,
    };
  },
  mounted() {
    this.get_totals_data();
  },
  methods: {
    get_totals_data() {
      async () => {
        try {
          var res = await axios.post(
            `${process.env.VUE_APP_BASE}/get_pie_totals`,
            {
              userid: process.env.VUE_APP_USERID, // Replace with state var
              api_key: process.env.VUE_APP_API_KEY,
            }
          );
          setTimeout(() => {
            this.category_datasets = res.data.totals_datasets;
            this.category_datasets = JSON.parse(this.category_datasets);
            this.totals_datacollection = {
              labels: this.category_datasets.labels,
              datasets: [
                {
                  label: this.category_datasets.datasets.label,
                  backgroundColor: this.category_datasets.datasets
                    .backgroundColor,
                  data: this.category_datasets.datasets.data,
                },
              ],
            };
          }, 3000);
        } catch (e) {
          console.error(e);
        }
      };
    },
  },
};
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