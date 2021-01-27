<template>
  <div class="budget">
      <Nav />
      <h1>Budget</h1>
      <div class="container">
        <div class="new-item">
          <AddItem v-on:add-item="additem" id="form" :categories="categories" />
          <AddCategory id="addcategory" v-on:add-category="add_category" />
        </div>
        
        <div class="items">
          <BudgetItems v-bind:items="items" v-on:del-item="deleteitem" />
          <h3>Total: ${{total}}</h3>
        </div>
      </div>
  </div>
</template>

<script>
import Nav from "../components/Nav"
import BudgetItems from "../components/BudgetItems"
import AddItem from "../components/AddItem"
import AddCategory from "../components/AddCategory"
import axios from "axios"
import { mapGetters } from "vuex"

export default {
  name: 'Budget',
  components: {
    Nav,
    BudgetItems,
    AddItem,
    AddCategory, 
  },
  data(){
    return{
      items: [],
      total: null,
      categories: [], 
    }
  },
  computed: mapGetters(['userid']),
  methods: {
    additem(newitem){
      // Api call is made from AddItem component
      this.all_items = [...this.all_items, newitem];
      this.items = this.all_items.slice(this.all_items.length - 5, this.all_items.length)
      this.getTotal();
    },
    deleteitem(id){
      // Make api call to delete item from db
      this.all_items = this.all_items.filter(item => item.id !== id); //Remove deleted item from list
      this.items = this.all_items.slice(this.all_items.length - 5, this.all_items.length)
      axios.post(`${process.env.VUE_APP_BASE}/delete_item`, {
        "userid": this.userid, 
        "api_key": process.env.VUE_APP_API_KEY,
        "deleted_id": id
      })
      .then()
      .catch(err => console.error(err))
      this.getTotal();
    }, 
    getTotal(){
      this.total = 0
      for (let item of this.all_items){
        let value = item.value;
        this.total += parseInt(value);
      }
    }, 
    add_category(new_categories){
      this.categories = new_categories;
    }
  },
  mounted(){
    this.getTotal();
  },
  async created(){
    if (! this.userid){
      this.$router.push("/login")
    }
    const res = await axios.post(`${process.env.VUE_APP_BASE}/get_items`, {
      "userid": this.userid,
      "api_key": process.env.VUE_APP_API_KEY
    })
    this.all_items = res.data.items; 
    this.items = this.all_items.slice(this.all_items.length - 5, this.all_items.length);
    this.getTotal();

    const category_res = await axios.post(`${process.env.VUE_APP_BASE}/get_categories`, {
        "userid": this.userid,
        "api_key": process.env.VUE_APP_API_KEY
    })

    for (let i of category_res.data.categories){
      this.categories.push(i)
    }
  }
}
</script>


<style scoped>
  .new-item #form{
    min-width: 100%;
    min-height: 100%;
  }


  .budget{
    min-width: 100%;
    min-height: 100%;
  }

  .container{
    min-width: 100%;
    min-height: 100%;
    display: grid;
    grid-template-columns: 50% 50%;
    box-shadow: 0 14px 28px rgba(0,0,0,0.25), 
    0 10px 10px rgba(0,0,0,0.22);
  }

  .new-item{
    min-height: 100%;
    grid-column: 1;
    background-color: #fff;
    display: grid;
    padding-top: 5%;
    padding-bottom: 5%;
  }

  .items{
    min-height: 100%;
    grid-column: 2;
    background-color: #FF4B2B;
    padding-top: 5%;
    padding-bottom: 5%;
  }

</style>

