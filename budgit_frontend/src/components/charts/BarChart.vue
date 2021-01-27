<script>
import { Bar } from "vue-chartjs";
export default {
    extends: Bar, 
    name: "bar-chart",
    props: {
        chartdata: {
            type: Object,
            default: null
        },
    }, 

    mounted () {
        this.renderChart(this.chartdata, {
            responsive: true, 
            fontColor: 'white',
            legend: {
                labels: {
                    fontColor: 'white'
                }
            },
            scales: {
                yAxes: [{
                    ticks: {
                        fontColor: 'white', 
                        callback: function(value) {
                            return '$' + value.toFixed(2);
                        }, 
                    }
                }],
                xAxes: [{
                    ticks: {
                        fontColor: 'white',
                    }
                }]
            }
        }
        )
    }
}
</script>