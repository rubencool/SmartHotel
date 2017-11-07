import Vue from 'vue'
import Router from 'vue-router'

import Home from '@/components/Home'
import MenuRoute from '@/components/MenuRoute'
import RegisterTable from '@/components/RegisterTable'
import Contact from '@/components/Contact'
import AboutUs from '@/components/AboutUs'

import ItemList from '@/components/ItemList'
import Drink from '@/components/Drink'
import Breakfast from '@/components/Breakfast'
import Dessert from '@/components/Dessert'
import MainDish from '@/components/MainDish'


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
    },
    {
      path: '/items',
      name: 'Items',
      component: ItemList,
      children: [
        {
          path: 'drinks',
          component: Drink,
        },
        {
          path: 'breakfast',
          component: Breakfast,
        },
        {
          path: 'desserts',
          component: Dessert,
        },
        {
          path: 'maindish',
          component: MainDish,
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
