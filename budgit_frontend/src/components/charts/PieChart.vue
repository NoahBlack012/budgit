<script>
import { Pie } from 'vue-chartjs'
import axios from 'axios'
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
            totals_datacollection: {}
        }
    },
    mounted () {
        async function get_totals_data() {
                try {
                var res = await axios.post(
                    `${process.env.VUE_APP_BASE}/get_pie_totals`,
                    {
                    userid: process.env.VUE_APP_USERID, // Replace with state var
                    api_key: process.env.VUE_APP_API_KEY,
                    }
                );
                setTimeout(() => {
                    var category_datasets = res.data.totals_datasets;
                    category_datasets = JSON.parse(this.category_datasets);
                    this.totals_datacollection = {
                        type: "Pie",
                        labels: category_datasets.labels,
                        datasets: [
                            {
                            label: category_datasets.datasets.label,
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
                            data: category_datasets.datasets.data,
                            },
                        ],
                    };
                    console.log(this.totals_datacollection)
                }, 3000);
                } catch (e) {
                    console.error(e);
                }
                return
            }
        get_totals_data()
        const options = {
            legend: {
                display: true,
            },
            responsive: true,
            maintainAspectRatio: false
        }
        console.log(this.totals_datacollection);
        this.renderChart(this.totals_datacollection, options)
    }
}   
</script>