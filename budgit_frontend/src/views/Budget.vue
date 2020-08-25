<template>
  <div class="budget">
      <Nav />
      <h1>Budget</h1>
      <BudgetItems v-bind:items="items" />
  </div>
</template>

<script>
// @ is an alias to /src
import Nav from "../components/Nav"
import BudgetItems from "../components/BudgetItems"
export default {
  name: 'Budget',
  components: {
    Nav,
    BudgetItems,
  },
  data(){
    return{
      items: [
        {
          id: 1,
          income: false,
          title: "Item 1",
          value: 200
        },
        {
          id: 2,
          income: true,
          title: "Item 2",
          value: 500
        },
        {
          id: 3,
          income: false,
          title: "Item 3",
          value: 10
        },
      ]
    }
  }
}
</script>

<style scoped>
</style>