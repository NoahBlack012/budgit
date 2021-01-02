<template>
    <div id = "add_category">
        <form @submit.prevent="add_category" autocomplete="off">
            <input type="text" v-model="new_category">
            <input type="submit" value="+" id="btn">
            <div v-if="formsubmited">
                <div class="error" v-if="!$v.new_category.required">Enter a Category</div>
            </div>
        </form>
    </div>
</template>

<script>
import axios from "axios"
import { required } from "vuelidate/lib/validators"
import { mapGetters } from 'vuex'

export default {
    name: "AddCategory", 
    data(){
        return{
            formsubmited: false,
        }
    },
    validations: {
        new_category: {
            required
        }
    },
    computed: mapGetters(['userid']),

    methods: {
        add_category(){
            this.$v.$touch()
            this.formsubmited = true
            if (!this.$v.$invalid){
                axios.post(`${process.env.VUE_APP_BASE}/add_category`, {
                    "new_category": this.new_category, 
                    "api_key": process.env.VUE_APP_API_KEY,
                    "userid": this.userid 
                })
                .then(res => {
                    let new_categories = res.data.categories
                    this.$emit('add-category', new_categories)
                })
                .catch(err => console.error(err))
                this.new_category = ""
            }
        }
    }
}
</script>

<style scoped>
    #btn{
        border-radius: 50%;
        background: aqua;
        color: black;
        border: 1px solid aqua;
    }
    
    #btn:hover {
        cursor: pointer;
    }
    .error{
        color: red;
    }
</style>