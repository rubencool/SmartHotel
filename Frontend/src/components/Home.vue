<template>
  <div class="home">
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
              <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" href="#/contact">
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
              <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" href="#/contact">
                Contact
                <i class="material-icons">chevron_right</i>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import cookie from 'vue-cookie'
  export default {
      name: 'Home',
      data () {
        return {
          msg: 'Welcome to Your Vue.js App'
        }
      }
    }
//  cookie.set('customerRegistered', false, 1);
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .my-login-card-size {
    max-width: 320px;
    height: auto;
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
