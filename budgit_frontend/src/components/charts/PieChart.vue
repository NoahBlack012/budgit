<script>
import { Pie } from 'vue-chartjs'
export default {
    extends: Pie,
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
                    fontColor: 'white', 
                }
            }
        })
    }
}   
</script>