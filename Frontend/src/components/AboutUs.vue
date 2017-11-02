<template>
  <div class="contact">
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
              <a class="mdl-navigation__link mdl-typography--text-uppercase" href="#about">About</a>
              <a class="mdl-navigation__link mdl-typography--text-uppercase" href="#/contact">Contact</a>
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
          <a class="mdl-navigation__link" href="#/about">
            <img class="nav-icon" src="../assets/icon/icon_about.png">
            About
          </a>
          <a class="mdl-navigation__link" href="#/contact">
            <img class="nav-icon" src="../assets/icon/icon_contact.png">
            Contact
          </a>
        </nav>
      </div>

      <!--content-->
      <div class="android-content mdl-layout__content">
        <div class="android-more-section">
          <div class="android-card-container mdl-grid">
            <h2>Contact Us</h2> <br>

            <h3> <p>Utsha Tech Pvt. Ltd.<br>
              Newroad Pokhara<br>
              Phone: 061-4242196, 061-4102655, 9856078917 <br>
              Email: info@utshatech.com <br>
              : utshatech@gmail.com <br>
              URL: www.utshagroup.com</p> </h3>

          </div>
        </div>
      </div>
    </div>
  </div>

</template>

<script>

  export default {
    name: 'Contact',
    data () {
      return {
        msg: 'Welcome to Your Vue.js App'
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

  {
    box-sizing: border-box;
  }

  input[type=text], select, textarea{
    width: 100%;
    padding: 12px;
    border: 1px solid #ccc;
    border-radius: 4px;
    box-sizing: border-box;
    resize: vertical;
  }

  label {
    padding: 12px 12px 12px 0;
    display: inline-block;
  }

  input[type=submit] {
    background-color: #4CAF50;
    color: white;
    padding: 12px 20px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    float: right;
  }

  input[type=submit]:hover {
    background-color: #45a049;
  }

  .container {
    border-radius: 5px;
    background-color: #f2f2f2;
    padding: 20px;
  }

  .col-25 {
    float: left;
    width: 25%;
    margin-top: 6px;
  }

  .col-75 {
    float: left;
    width: 75%;
    margin-top: 6px;
  }

  /* Clear floats after the columns */
  .row:after {
    content: "";
    display: table;
    clear: both;
  }

  /* Responsive layout - when the screen is less than 600px wide, make the two columns stack on top of each other instead of next to each other */
  @media (max-width: 600px) {
    .col-25, .col-75, input[type=submit] {
      width: 100%;
      margin-top: 0;
    }
  }
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

  .mdl-layout__header {
    background-color: white;
  }

  .mdl-layout__header-row .mdl-navigation__link {
    color: #757575;
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
