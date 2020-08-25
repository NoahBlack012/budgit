<template>
    <div>
        <div class="items" v-bind:key='item.id' v-for="item in items">
            <BudgetItem v-bind:item="item" />
        </div>      
    </div>
</template>

<script>
import BudgetItem from './BudgetItem'
export default {
    name: 'BudgetItems',
    components: {
        BudgetItem,
    },
    props: [
        'items'
    ]
}
</script>

<style scoped>

</style>