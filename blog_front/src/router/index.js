import Vue from 'vue'
import VueRouter from 'vue-router'
import index from '@/views/index'
import Details from '@/views/Details'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: index
  },
  {
    path: '/detail',
    name: 'detail',
    component: Details
  }
]

const router = new VueRouter({
  mode: 'hash',
  base: process.env.BASE_URL,
  routes
})

export default router
