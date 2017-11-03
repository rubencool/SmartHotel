// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

require('../node_modules/material-design-lite/material.min.css')
require('../node_modules/material-design-lite/material.min.js')
Vue.config.productionTip = false


//use vue-cookie
// Require dependencies
// cookie = require('vue-cookie');
// // Tell Vue to use the plugin
// Vue.use(cookie);


/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})
