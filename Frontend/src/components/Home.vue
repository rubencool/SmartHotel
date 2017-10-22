<template>
  <div class="home">
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">

      <div class="android-header mdl-layout__header mdl-layout__header--waterfall">
        <div class="mdl-layout__header-row">
          <span class="android-title mdl-layout-title" style="color: #757575">
            SmartHotel
          </span>
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
              <a class="mdl-navigation__link mdl-typography--text-uppercase" href="">Contact</a>
            </nav>
          </div>
        </div>
      </div>
      <!--drawer-->
      <div class="android-drawer mdl-layout__drawer">
        <span class="mdl-layout-title">
          SmartHotel
        </span>
        <nav class="mdl-navigation">
          <a class="mdl-navigation__link" href="">
            <i class="material-icons">home</i>
            Home
          </a>
          <a class="mdl-navigation__link" href="">
            <i class="material-icons">restaurant menu</i>
            Menu
          </a>
          <a class="mdl-navigation__link" href="">
            <img class="nav-icon" src="../assets/icon/icon_checkout.png">
            Checkout
          </a>
          <a class="mdl-navigation__link" href="">
            <img class="nav-icon" src="../assets/icon/icon_about.png">
            About
          </a>
          <a class="mdl-navigation__link" href="">
            <img class="nav-icon" src="../assets/icon/icon_contact.png">
            Contact
          </a>
        </nav>
      </div>

      <!--content-->
      <div class="android-content mdl-layout__content">
        <div class="android-more-section">
          <div class="android-card-container mdl-grid">

            <!--order-->
            <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp">
              <div class="mdl-card__media">
                <img src="../assets/icon/icon_menu.png">
              </div>
              <div class="mdl-card__title">
                <h4 class="mdl-card__title-text">
                  Menu
                </h4>
              </div>
              <div class="mdl-card__supporting-text">
              <span class="mdl-typography--font-light mdl-typography--subhead">
                Order Food !
              </span>
              </div>
              <div class="mdl-card__actions">
                <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" href="#/menu">
                  Order
                  <i class="material-icons">
                    chevron_right
                  </i>
                </a>
              </div>
            </div>

            <!--checkout-->
            <div class="mdl-cell mdl-cell--2-col mdl-cell--2-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp">
              <div class="mdl-card__media">
                <img src="../assets/icon/icon_checkout.png">
              </div>
              <div class="mdl-card__title">
                <h4 class="mdl-card__title-text">
                  Checkout
                </h4>
              </div>
              <div class="mdl-card__supporting-text">
              <span class="mdl-typography--font-light mdl-typography--subhead">
                Billing & Stuff
              </span>
              </div>
              <div class="mdl-card__actions">
                <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" href="">
                  Checkout
                  <i class="material-icons">chevron_right</i>
                </a>
              </div>
            </div>

            <!--contact us-->
            <div class="mdl-cell mdl-cell--2-col mdl-cell--2-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp">
              <div class="mdl-card__media">
                <img src="../assets/icon/icon_contact.png">
              </div>
              <div class="mdl-card__title">
                <h4 class="mdl-card__title-text">Talk to us !</h4>
              </div>
              <div class="mdl-card__supporting-text">
              <span class="mdl-typography--font-light mdl-typography--subhead">
                Contact us !
              </span>
              </div>
              <div class="mdl-card__actions">
                <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" href="">
                  Contact
                  <i class="material-icons">chevron_right</i>
                </a>
              </div>
            </div>

            <!--contact-->
            <div class="mdl-cell mdl-cell--2-col mdl-cell--2-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp">
              <div class="mdl-card__media">
                <img src="../assets/icon/icon_contact.png">
              </div>
              <div class="mdl-card__title">
                <h4 class="mdl-card__title-text">Contact</h4>
              </div>
              <div class="mdl-card__supporting-text">
              <span class="mdl-typography--font-light mdl-typography--subhead">
                Talk to us !
              </span>
              </div>
              <div class="mdl-card__actions">
                <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" href="">
                  Contact
                  <i class="material-icons">chevron_right</i>
                </a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
    export default {
      name: 'Home',
      data () {
        return {
          msg: 'Welcome to Your Vue.js App'
        }
      }
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .my-login-card-size {
    max-width: 320px;
    height: auto;
  }

  /*.mdl-layout__header {*/
    /*background-color: white;*/
  /*}*/

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



  #view-source {
    position: fixed;
    display: block;
    right: 0;
    bottom: 0;
    margin-right: 40px;
    margin-bottom: 40px;
    z-index: 900;
  }
</style>
