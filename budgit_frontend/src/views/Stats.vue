<template>
    <div class="stats">
        <Nav />
        <h1>Statistics</h1>
        <div class="graphs">
            <pie-chart :chartlabel="totals_label" :datapoints="totals_datapoints" :labels="totals_category_labels" id="expense_category" />
            <pie-chart :chartlabel="totals_label" :datapoints="totals_datapoints" :labels="totals_category_labels" id="expense_category2" />
            <pie-chart :chartlabel="totals_label" :datapoints="totals_datapoints" :labels="totals_category_labels" id="expense_category3" />
        </div>
    </div>
</template>

<script>
import Nav from "../components/Nav"
import PieChart from "../components/charts/PieChart"
export default {
    name: "Stats",
    components: {
        Nav,
        PieChart
    }, 
    data(){
        return{
            totals_label: "Chart",
            totals_datapoints: [20, 30, 40, 10], //Api call to get users values
            totals_category_labels: ["A", "B", "C", "D"], //Api call to get users categoies
        }
    }
}
</script>

<style scoped>
    .graphs{
        display: grid;
        grid-template-columns: 33% 33% 33%;
    }

    #expense_category{
        grid-column: 1;
    }
    #expense_category2{
        grid-column: 2;
    }
    #expense_category3{
        grid-column: 3;
    }
</style>