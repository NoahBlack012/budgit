<template>
  <div class="budget">
      <Nav />
      <h1>Budget</h1>
      <AddItem v-on:add-item="additem" />
      <BudgetItems v-bind:items="items" v-on:del-item="deleteitem" />
      <ExpenseTotal v-bind:total="total" />
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from "../components/Nav"
import BudgetItems from "../components/BudgetItems"
import AddItem from "../components/AddItem"
import ExpenseTotal from "../components/ExpenseTotal"
import axios from "axios"
export default {
  name: 'Budget',
  components: {
    Nav,
    BudgetItems,
    AddItem,
    ExpenseTotal
  },
  data(){
    return{
      // Make api call and get user's budget
      items: [],
      total: 0
    }
  },
  methods: {
    additem(newitem){
      // Make api call to save item to db
      this.items = [...this.items, newitem];
      this.getTotal();
    },
    deleteitem(id){
      // Make api call to delete item from db
      this.items = this.items.filter(item => item.id !== id); //Remove deleted item from list
      this.getTotal();
    }, 
    getTotal(){
      this.total = 0
      for (let item of this.items){
        let value = parseInt(item.value, 10);
        this.total = this.total + value;
      }
    }
  },
  beforeMount(){
    this.getTotal();
  },
  created(){
    console.log(process.env.VUE_APP_API_KEY);
    // fetch(`${process.env.VUE_APP_BASE}/get_items`, {
    //   method: 'POST',
    //   content: 'application/json',
    //   body: JSON.stringify({
    //     "userid": 1, 
    //     "api_key": process.env.VUE_APP_API_KEY
    //     }),
    //   }
    // )
    axios.post(`${process.env.VUE_APP_BASE}/get_items`, {
      "userid": 1, 
      "api_key": process.env.VUE_APP_API_KEY
    })
    .then((res) => {
      console.log(res.data);
      this.items = res.data.items;
      })
    .catch(err => console.error(err))
  }
}
</script>

<style scoped>
</style>