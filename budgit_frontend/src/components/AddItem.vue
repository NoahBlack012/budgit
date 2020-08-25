<template>
    <form @submit.prevent="additem" autocomplete="off">
        <input type="text" name="title" v-model="title">
        <input type="number" name="value" v-model="value">
        <input type="submit" value="Create Item">
    </form>
</template>

<script>
import { v4 as uuidv4 } from 'uuid'
export default {
    name: "AddItem", 
    methods: {
        additem(){
            const newitem = {
                id: uuidv4(),
                title: this.title,
                value: this.value,
                income: false
            }
            this.$emit('add-item', newitem);
            this.title = ''; 
        }
    }
}
</script>