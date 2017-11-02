import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import MenuRoute from '@/components/MenuRoute'
import RegisterTable from '@/components/RegisterTable'
import Contact from '@/components/Contact'
import AboutUs from '@/components/AboutUs'
import Drink from '@/components/Drink'



Vue.use(Router)

const router = new Router({
  routes: [],
  mode: 'history'
})

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    },

    {
      path: '/menu/:registered/:tableId',
      name: 'MeuRoute',
      component: MenuRoute,
      children: [
        {
          path: '/drinks',
          component: Drink
        }
      ]
    },
    {
      path: '/about',
      name: 'AboutUs',
      component: AboutUs
    },
    {
      path: '/contact',
      name: 'Contact',
      component: Contact
    },
    {
      path: '/register',
      name: 'RegisterTable',
      component: RegisterTable
    }
  ]
})
