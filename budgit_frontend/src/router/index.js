import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Budget from '../views/Budget.vue'
import Stats from '../views/Stats.vue'

Vue.use(VueRouter)

  const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/login',
    name: 'Login',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/Login.vue')
  },
  {
    path: '/budget',
    name: "Budget",
    component: Budget
  },
  {
    path: '/stats',
    name: 'Stats',
    component: Stats
  }
]

const router = new VueRouter({
  mode: "history",
  routes: routes
})

export default router
