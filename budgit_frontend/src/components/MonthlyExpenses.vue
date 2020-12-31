<template>
    <div id="monthlyexpenses">
        <bar-chart v-if="loaded" :chartdata="chartdata" :options="options" />
    </div>
</template>

<script>
import BarChart from "./charts/BarChart";
import axios from "axios";
export default {
    name: "MonthlyExpenses", 
    components: {
        BarChart
    }, 
    data() {
        return{
            loaded: false,
            chartdata: null,
            options: null,
        }
    }, 

    async mounted() {
        this.loaded = false
        try{
            const res = await axios.post(`${process.env.VUE_APP_BASE}/get_monthly_bar_totals`, {
                    userid: process.env.VUE_APP_USERID, // Replace with state var
                    api_key: process.env.VUE_APP_API_KEY,
                }
            )
            this.chartdata = res.data.bar_data
            this.options = {
                scales: {
                    yAxes: [{
                        ticks: {
                            callback: function(value) {
                                return '$' + value;
                            }
                        }
                    }]
                },
                tooltips: {
                    enabled: true,
                    mode: 'single',
                    callbacks: {
                        label: function(tooltipItem) {
                            return '$' + tooltipItem.yLabel;
                        }
                    }
                }, 
                responsive: true,
                maintainAspectRatio: false,
            }
            this.loaded = true
        }catch(err) {console.error(err)}
    }
}
</script>