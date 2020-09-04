<script>
import { Pie } from 'vue-chartjs'

export default {
    extends: Pie,
    props: {
        chartlabel: {
            type: String
        },
        datapoints: {
            type: Array
        },
        labels: {
            type: Array
        }
    },
    data() {
        return {
            chartData: {
                type: 'pie',
                labels: this.labels,
                datasets: [{
                    label: this.chartlabel,
                    borderWidth: 1,
                    borderColor: [
                        'rgba(255,99,132,1)',
                        'rgba(54, 162, 235, 1)',
                        'rgba(255, 206, 86, 1)',
                        'rgba(75, 192, 192, 1)'            
                    ],
                    backgroundColor: [
                        'rgba(255, 99, 132, 0.2)',
                        'rgba(54, 162, 235, 0.2)',
                        'rgba(255, 206, 86, 0.2)',
                        'rgba(75, 192, 192, 0.2)',                
                    ],
                    data: this.datapoints
                }]
            }, 
            options: {
                legend: {
                    display: true
                },
                responsive: true,
                maintainAspectRatio: false
            }
        }
    },
    mounted () {
        this.renderChart(this.chartData, this.options)
    }
}   
</script>