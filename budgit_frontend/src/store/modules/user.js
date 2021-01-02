//import axios from 'axios';

const state = {
    userid: null,
}
const getters = {
    userid: (state) => state.userid 
}
const actions = {
    async loginUser( {commit}, userid ) {
        commit('setUserid', userid)
    }
}
const mutations = {
    setUserid: (state, userid) => { state.userid = userid }
}

export default {
    state,
    getters,
    actions,
    mutations
}