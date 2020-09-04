<template>
    <form @submit.prevent="formsubmit" autocomplete="off">
        <input type="text" name="title" v-model="title" placeholder="Item"><br>
        <input type="text" name="value" v-model="value" placeholder="Amount"><br>
        <select name="category" id="category" v-model="category">
            <option value="food" selected>Food</option>
            <option value="transportation">Transportation</option>
            <option value="shopping">Shopping</option>
            <option value="rent">Rent</option>
        </select><br>
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
import { v4 as uuidv4 } from 'uuid'
export default {
    name: "AddItem", 
    data(){
        return{
            title: '',
            value: '',
            formsubmited: false,
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
            const newitem = {
                id: uuidv4(),
                title: this.title,
                value: this.value,
                category: item_category,
            }
            this.title = ''; 
            this.value = '';
            this.category = '';
            this.formsubmited = false;
            this.$emit('add-item', newitem);
        }
    }
}
</script>

<style scoped>
    .error{
        color: red;
    }
</style>