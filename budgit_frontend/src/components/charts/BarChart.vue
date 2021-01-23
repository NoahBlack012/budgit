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
                        fontColor: 'white'
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