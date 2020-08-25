<template>
    <div class="budgetitem" v-bind:class="{'income': item.income}">
        <h1>{{item.title}}</h1>
        <h1>${{item.value}}</h1>
    </div>
</template>

<script>
export default {
    name: 'BudgetItem',
    props: [
        'item'
    ]
}
</script>

<style scoped>
    .budgetitem{
        color: red;
    }
    .income{
        color: green;
    }
</style>