<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
  import Header from './components/Header.vue'
export default {
  data () {
    return {
      reloadMenu : false,
      CustomerRegistered: true,
      CustomerTableId: '',
      load: ''
    }
  },
  name: 'app',
  code: '',
  components:{
    'app-header': Header
  },
  mounted(){
    this.load= document.URL;
  }

}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
</style>
