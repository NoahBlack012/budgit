<template>
    <div class="expensetotal">
        {{total}}
    </div>
</template>

<script>
export default {
    name: "ExpenseTotal", 
    props: [
        "total"
    ],
}
</script>

<style scoped>

</style>