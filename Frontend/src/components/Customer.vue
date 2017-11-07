<template>
  <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">
    <header class="mdl-layout__header">
      <div class="mdl-layout__header-row">
        <span class="android-title mdl-layout-title" style="color: #696969">SmartHotel</span>
        <!-- Add spacer, to align navigation to the right in desktop -->
        <div class="android-header-spacer mdl-layout-spacer"></div>
        <div class="android-search-box mdl-textfield mdl-js-textfield mdl-textfield--expandable mdl-textfield--floating-label mdl-textfield--align-right mdl-textfield--full-width">
          <label class="mdl-button mdl-js-button mdl-button--icon" for="search-field">
            <i class="material-icons">search</i>
          </label>
          <div class="mdl-textfield__expandable-holder">
            <input class="mdl-textfield__input" type="text" id="search-field">
          </div>
        </div>
        <!-- Navigation -->
        <div class="android-navigation-container">
          <nav class="android-navigation mdl-navigation">
            <a class="mdl-navigation__link mdl-typography--text-uppercase" href="">Home</a>
            <a class="mdl-navigation__link mdl-typography--text-uppercase" href="">Menu</a>
            <a class="mdl-navigation__link mdl-typography--text-uppercase" href="">Checkout</a>
            <a class="mdl-navigation__link mdl-typography--text-uppercase" href="">About</a>
            <a class="mdl-navigation__link mdl-typography--text-uppercase" href="#/contact">Contact</a>
          </nav>
        </div>
      </div>
    </header>
    <!--drawer-->
    <div class="android-drawer mdl-layout__drawer">
        	<span class="mdl-layout-title">SmartHotel
	        </span>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">
          <i class="material-icons">home</i>Home
        </a>
        <a class="mdl-navigation__link" href="">
          <i class="material-icons">restaurant menu</i>
          Menu
        </a>

        <!--todo -->
        <a class="mdl-navigation__link" href="">
          <img class="nav-icon" src="../assets/icon/icon_checkout.png">
          Checkout
        </a>
        <a class="mdl-navigation__link" href="">
          <img class="nav-icon" src="../assets/icon/icon_about.png">
          About Us
        </a>
        <a class="mdl-navigation__link" href="/contact">
          <img class="nav-icon" src="../assets/icon/icon_contact.png">
          Contact
        </a>
      </nav>
    </div>
    <router-view/>
  </div>
</template>

<script>
  export default {
    data () {
      return {
      }
    },
    name: 'app',
    code: '',
    components:{
    },
    mounted(){
    }

  }
</script>

<style>
  .nav-icon {
    height: 30px;
    width: 30px;
  }

  .nav-logo {
    height: 80px;
    width: auto;
    align-self: flex-start;
  }
  .mdl-navigation__link {
    text-align: left;
  }
  .mdl-layout__header {
    background-color:  	#3CB371;
  }

  .mdl-layout__header-row .mdl-navigation__link {
    color: white;
  }
</style>
