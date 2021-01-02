<template>
    <div id="pietotals">
        <pie-chart v-if="loaded" :chartdata="chartdata" :options="options" id="expense_category" />
    </div>
</template>

<script>
import PieChart from "./charts/PieChart";
import axios from "axios";
import { mapGetters } from 'vuex'; 

export default {
    name: "PieTotals", 
    components: {
        PieChart
    },
    computed: mapGetters(['userid']),
    data: () => {
        return {
        loaded: false, 
        chartdata: null, 
        options: null,
        };
    },
    async mounted () {
        this.loaded = false
        try {
        const data = await axios.post(`${process.env.VUE_APP_BASE}/get_pie_totals`, {
            userid: this.userid,
            api_key: process.env.VUE_APP_API_KEY,
        })
        this.chartdata = data.data.totals_datasets
        this.options = {
            tooltips: {
                enabled: true,
                mode: 'single',
                callbacks: {
                    title: function(tooltipItem, data) {
                        return data['labels'][tooltipItem[0]['index']];
                    },
                    label: function(tooltipItem, data) {
                        return "$" + data['datasets'][0]['data'][tooltipItem['index']];
                    },
                }
            }, 
            responsive: true,
            maintainAspectRatio: false,
        }
        this.loaded = true
        } catch (e) {
        console.error(e)
        }
    }
}
</script>