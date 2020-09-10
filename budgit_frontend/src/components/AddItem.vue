<template>
    <form @submit.prevent="formsubmit" autocomplete="off">
        <input type="text" name="title" v-model="title" placeholder="Item"><br>
        <input type="text" name="value" v-model="value" placeholder="Amount"><br>
        <select name="category" id="category" v-model="category">
            <option  v-bind:key="cat" v-for="cat in categories" :value="cat">{{ cat }}</option>
        </select>
        <AddCategory v-on:add-category="new_category" />
        <br>
        <input type="submit" value="Create Item">
        <div class="errors" v-if="formsubmited">
            <div class="error" v-if="!$v.value.numeric">Amount Must Be a Number</div>
            <div class="error" v-if="!$v.value.required">Please Enter an Amount</div>
            <div class="error" v-if="!$v.title.required">Please Enter a Title</div>
        </div>
    </form>
</template>

<script>
import { required, numeric } from 'vuelidate/lib/validators'
import AddCategory from "./AddCategory"
// import { v4 as uuidv4 } from 'uuid'
import axios from "axios"
export default {
    name: "AddItem", 
    components: {
        AddCategory,
    },
    data(){
        return{
            title: '',
            value: '',
            formsubmited: false,
            categories: [],
        }
    },
    validations:{
        title:{
            required
        },
        value:{
            required,
            numeric
        },
    },
    methods: {
        new_category(new_categories){
            this.categories = new_categories
        },
        formsubmit(){
            this.formsubmited = true;
            this.$v.$touch()
            if (!this.$v.$invalid) {
                this.additem();
            }
        },
        additem(){
            let item_category = ''
            if (this.category === "additem"){
                this.categoray.appendChild(this.newitem)
                item_category = this.newitem
            }else{
                item_category = this.category
            }
            const new_item = {
                title: this.title,
                value: this.value,
                category: item_category,
            }
            axios.post(`${process.env.VUE_APP_BASE}/add_item`, {
                    "userid": process.env.USERID, //Replace with state var
                    "api_key": process.env.VUE_APP_API_KEY,
                    "new_item": new_item
                }
            )
            .then(res => new_item.id = res.id)
            .catch(err => console.error(err))
            this.title = ''; 
            this.value = '';
            this.category = '';
            this.formsubmited = false;
            this.$emit('add-item', new_item);
        }
    }, 
    created(){
        axios.post(`${process.env.VUE_APP_BASE}/get_categories`, {
            "userid": process.env.VUE_APP_USERID, // Replace with state var
            "api_key": process.env.VUE_APP_API_KEY
        })
        .then(res => {
            for (let i of res.data.categories){
                this.categories.push(i)
            }
            console.log(this.categories);
        })
        .catch(err => console.error(err))
    },
}
</script>

<style scoped>
    .error{
        color: red;
    }
</style>