import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Customer from '@/components/Customer'
import MenuRoute from '@/components/MenuRoute'
import RegisterTable from '@/components/RegisterTable'
import Contact from '@/components/Contact'
import AboutUs from '@/components/AboutUs'
import Drink from '@/components/Drink'
// import AdminHome from '@/components/admin/AdminHome'
import Overview from '@/components/Dashboard/Views/Overview.vue'
import UserProfile from '@/components/Dashboard/Views/UserProfile.vue'
import EditProfileForm from '@/components/Dashboard/Views/UserProfile/EditProfileForm.vue'
import Notifications from '@/components/Dashboard/Views/Notifications.vue'
import Icons from '@/components/Dashboard/Views/Icons.vue'
import Maps from '@/components/Dashboard/Views/Maps.vue'
import Typography from '@/components/Dashboard/Views/Typography.vue'
import TableForm from '@/components/Dashboard/Views/Table/TableForm.vue'
import Form from '@/components/Dashboard/Views/Section/Form.vue'
import TableEdit from '@/components/Dashboard/Views/Table/TableEdit.vue'
import Edit from '@/components/Dashboard/Views/Section/Edit.vue'
import TableList from '@/components/Dashboard/Views/TableList.vue'
import DashboardLayout from '@/components/Dashboard/Layout/DashboardLayout.vue'



Vue.use(Router)


export default new Router({
  routes: [
    {
      path: '/',
      name: 'header',
      redirect: '/home',
      component: Customer,

      children: [
        {
          path: '/home',
          name: 'Home',
          component: Home
        },

        {
          path: '/menu',
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

    },

  //  admin route
    {
      path: '/admin',
      component: DashboardLayout,
      redirect: '/admin/overview',
      children: [
        {
          path: 'overview',
          name: 'overview',
          component: Overview
        },
        {
          path: 'stats',
          name: 'stats',
          component: UserProfile,
          children: [
            {
              path: 'bill/:tableId/:custId',
              name: 'bill',
              component: EditProfileForm
            }
          ]
        },
        {
          path: 'notifications',
          name: 'notifications',
          component: Notifications
        },
        {
          path: 'icons',
          name: 'icons',
          component: Icons
        },
        {
          path: 'maps',
          name: 'maps',
          component: Maps
        },
        {
          path: 'table',
          name: 'table-list',
          component: Typography,
          children: [
            {
              path: 'form',
              name: 'tableform',
              component: TableForm
            },
            {
              path: 'edit/:id',
              name: 'tableedit',
              component: TableEdit
            }
          ]
        },
        {
          path: 'section',
          name: 'section-list',
          component: TableList,
          children: [
            {
              path: 'form',
              name: 'form',
              component: Form
            },
            {
              path: 'edit/:id',
              name: 'edit',
              component: Edit
            }
          ]
        }
      ]
    },
    // { path: '*', component: NotFound }
  ]
})
