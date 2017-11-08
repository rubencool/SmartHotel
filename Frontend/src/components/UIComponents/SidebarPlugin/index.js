import Sidebar from './SideBar.vue'

const SidebarStore = {
  showSidebar: false,
  sidebarLinks: [
    {
      name: 'Home',
      icon: 'ti-panel',
      path: '/admin/overview'
    },
    {
      name: 'Billing',
      icon: 'ti-user',
      path: '/admin/stats'
    },
    {
      name: 'Section',
      icon: 'ti-view-list-alt',
      path: '/admin/section'
    },
    {
      name: 'Table Management',
      icon: 'ti-text',
      path: '/admin/table'
    },
    {
      name: 'Items',
      icon: 'ti-pencil-alt2',
      path: '/admin/item'
    },
    {
      name: 'Foods',
      icon: 'ti-map',
      path: '/admin/food'
    },
    {
      name: 'Notifications',
      icon: 'ti-bell',
      path: '/admin/notifications'
    }
  ],
  displaySidebar (value) {
    this.showSidebar = value
  }
}

const SidebarPlugin = {

  install (Vue) {
    Vue.mixin({
      data () {
        return {
          sidebarStore: SidebarStore
        }
      }
    })

    Object.defineProperty(Vue.prototype, '$sidebar', {
      get () {
        return this.$root.sidebarStore
      }
    })
    Vue.component('side-bar', Sidebar)
  }
}

export default SidebarPlugin
