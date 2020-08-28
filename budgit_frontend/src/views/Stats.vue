<template>
    <div class="stats">
        <Nav />
        <h1>Stats</h1>
        <pie-chart :chartlabel="label" :datapoints="datapoints" id="chart" />
    </div>
</template>

<script>
import Nav from "../components/Nav"
import PieChart from "../components/PieChart"
export default {
    name: "Stats",
    components: {
        Nav,
        PieChart
    }, 
    data(){
        return{
            label: "Chart",
            datapoints: [20, 30, 40, 10]
        }
    }
}
</script>

<style scoped>
    #chart{
        float: left;
    }
</style>