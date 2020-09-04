//import axios from 'axios';

const state = {
    items: {
        id: 1,
        title: "Item 1",
        value: 200,
        category: "food"
    },
}
const getters = {
    items: (state) => state.budget_items
}
const actions = {}
const mutations = {}

export default {
    state,
    getters,
    actions,
    mutations
}