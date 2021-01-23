<template>
    <div id = "add_category">
        <form @submit.prevent="add_cat" autocomplete="off">
            <input type="text" v-model="new_category" placeholder="Add Another Category"><br>
            <input type="submit" value="+" id="button">
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
        add_cat(){
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
            }
            this.new_category = ""
        }
    }
}
</script>

<style scoped>
    input{
        width: 25%;
    }

    input[type="text"]{
        padding: 5px 5px; line-height: 10px;
    }

    #button{
        width: 15%;
    }

    .error{
        color: red;
    }
</style>