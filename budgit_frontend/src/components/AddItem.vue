<template>
    <div class="additem">
        <div class="addform">
            <form @submit.prevent="formsubmit" autocomplete="off">
                <input type="text" name="title" v-model="title" placeholder="Item"><br>
                <input type="text" name="value" v-model="value" placeholder="Amount"><br>
                <select name="category" id="input" v-model="category">
                    <option v-bind:key="cat" v-for="cat in categories" :value="cat">{{ cat }}</option>
                </select>
                <br>
                <input type="submit" value="Create" id="button">
                <div class="errors" v-if="formsubmited">
                    <div class="error" v-if="!$v.value.numeric">Amount Must Be a Number</div>
                    <div class="error" v-if="!$v.value.required">Please Enter an Amount</div>
                    <div class="error" v-if="!$v.title.required">Please Enter a Title</div>
                </div>
            </form>
        </div>
    </div>
</template>

<style scoped>
    .error{
        color: red;
    }

    input, #input{
        background-color: #eee;
        border: none;
        padding: 1vh;
        width: 20%;
        margin: 0.5%;
        text-align: center;
    }

    select{
        margin: 0.5%;
        width: 11%;
        background-color: #FF4B2B;
        font-weight: bold;
        text-transform: uppercase;
    }

    option{
        background-color: #FF4B2B;
        color: #fff;
        text-transform: uppercase;
    }

    input, input::placeholder{
        font-size: 12pt;
        color: black;
    }

    .additem{
        height: 1%;
    }


</style>


<script>
import { required, numeric } from 'vuelidate/lib/validators'
//import AddCategory from "./AddCategory"
import axios from "axios"
import { mapGetters } from "vuex"

export default {
    name: "AddItem", 
    components: {
       // AddCategory,
    },
    data(){
        return{
            title: '',
            value: '',
            formsubmited: false,
        }
    },
    props: {
        categories: Array, 
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

    computed: mapGetters(['userid']), 
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
            const new_item = {
                title: this.title,
                value: this.value,
                category: this.category,
            }
            axios.post(`${process.env.VUE_APP_BASE}/add_item`, {
                    "userid": this.userid, 
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
        
    },
}
</script>

