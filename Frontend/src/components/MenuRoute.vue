<template>
  <div class="Menu">
    <div class="mdl-layout mdl-js-layout mdl-layout--fixed-header">

      <!--content-->
      <div class="android-content mdl-layout__content">
        <div class="android-more-section">
          <div class="android-card-container mdl-grid" v-if="category && category.length">

            <!--order-->
            <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp" v-for="cat in category">
              <div class="mdl-card__media">
                <!--<img :src="getImgUrl(cat.icon)"/>-->
            <!--TODO dynamic img url-->
                <img src="../assets/icon/icon_maindish.png"/>
              </div>
              <div class="mdl-card__supporting-text">
              <span class="mdl-typography--font-light mdl-typography--subhead">
                Order Food !
              </span>
              </div>
              <div class="mdl-card__actions">
              <a class="android-link mdl-button mdl-js-button mdl-typography--text-uppercase" v-bind:style="{fontSize: 14+'px'}" v-bind:href="'#/menu/'+cat.cat_name.toLowerCase()" >
                {{cat.cat_name}}
                <i class="material-icons">
                  chevron_right
                </i>
              </a>
            </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--end-->
    <ul v-if="errors && errors.length">
      <li v-for="error in errors">
        {{error.message}}
      </li>
    </ul>
        <router-view/>
  </div>
</template>

<script>
  import axios from 'axios'
  export default {
    name: 'MenuRoute',
    data () {
      return {
        category: [],
        errors: [],
        url: '../assets/icon/icon_drinks.png',
        msg: 'MenuRoute'
      }
    },
    created () {
      this.loadCategory()
    },
    methods: {
      loadCategory: function () {
        axios.get('http://18cb5d26.ngrok.io/api/food/category')
          .then(response => {
            console.log(response.data)
            this.category = response.data
//          ready url
//            this.category.forEach(this.url = +this.category.icon)
          }).catch(e => {
            this.errors.push(e)
            console.error(e)
          })
      },
      getImgUrl: function (image) {
        var images = require.context('../assets/icon', false, /\.png$/)
        return images('./' + image)
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  h1, h2 {
    font-weight: normal;
  }

  ul {
    list-style-type: none;
    padding: 0;
  }

  li {
    display: inline-block;
    margin: 0 10px;
  }

  a {
    color: #42b983;
  }

  .nav-icon {
    height: 30px;
    width: 30px;
  }

  .mdl-layout__header {
    background-color: white;
  }

  .mdl-layout__header-row .mdl-navigation__link {
    color: #757575;
  }
</style>

