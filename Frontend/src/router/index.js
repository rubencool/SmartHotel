import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import MenuRoute from '@/components/MenuRoute'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },
    {
      path: '/menu',
      name: 'MeuRoute',
      component: MenuRoute
    }
  ]
})
