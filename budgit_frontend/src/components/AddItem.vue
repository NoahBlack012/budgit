<template>
    <form @submit.prevent="additem" autocomplete="off">
        <input type="text" name="title" v-model="title" placeholder="Item">
        <input type="number" name="value" v-model="value" placeholder="Amount">
        <input type="submit" value="Create Item">
    </form>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
export default {
    name: "AddItem", 
    data(){
        return{
            title: '',
            value: ''
        }
    },
    methods: {
        additem(){
            const newitem = {
                id: uuidv4(),
                title: this.title,
                value: this.value,
                income: false
            }
            this.title = ''; 
            this.value = '';
            this.$emit('add-item', newitem);
        }
    }
}
</script>