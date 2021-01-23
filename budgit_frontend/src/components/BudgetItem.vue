<template>
    <div class="budgetitem">
        <p>
            {{item.title}}
            <span style="color:green">${{item.value}} </span>
            <span id = "cat">{{item.category}}</span>
            <button @click="$emit('del-item', item.id)" class = "delete">X</button>
        </p>
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
        color: black;
    }
    .income{
        color: green;
    }
    .delete {
        background: #ff0000;
        color: #fff;
        border: none;
        padding: 5px 9px;
        border-radius: 50%;
        cursor: pointer;
    }
    #cat{
        color: blue;
    }
</style>