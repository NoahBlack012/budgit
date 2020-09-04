import Vuex from "vuex";
import Vue from "vue";
// Import modules here
import app from "./modules/app"
//

// Load vuex
Vue.use(Vuex);

// Create Store

export default new Vuex.Store({
    modules: {
        app,
    }
})