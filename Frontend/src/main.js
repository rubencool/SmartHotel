// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
// import Quagga from 'quagga'
// import jsqrcode from 'jsqrcode'

require('../node_modules/material-design-lite/material.min.css')
require('../node_modules/material-design-lite/material.min.js')
require('../node_modules/quagga/dist/quagga.min.js')

Vue.config.productionTip = false

// const Quagga = require('quagga').default

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  template: '<App/>',
  components: {App}
})
