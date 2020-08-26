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
      items: [
        {
          id: 1,
          income: false,
          title: "Item 1",
          value: 200
        },
      ],
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
  }
}
</script>

<style scoped>
</style>