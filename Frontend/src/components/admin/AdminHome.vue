<template>
  <div class="mdl-layout mdl-js-layout mdl-layout--fixed-drawer
            mdl-layout--fixed-header">
    <header class="mdl-layout__header">
      <div class="mdl-layout__header-row">
        <div class="mdl-layout-spacer"></div>
        <div class="mdl-textfield mdl-js-textfield mdl-textfield--expandable
                  mdl-textfield--floating-label mdl-textfield--align-right">
          <label class="mdl-button mdl-js-button mdl-button--icon"
                 for="fixed-header-drawer-exp">
            <i class="material-icons">search</i>
          </label>
          <div class="mdl-textfield__expandable-holder">
            <input class="mdl-textfield__input" type="text" name="sample"
                   id="fixed-header-drawer-exp">
          </div>
        </div>
      </div>
    </header>
    <div class="mdl-layout__drawer">
      <span class="mdl-layout-title">Admin Panel</span>
      <nav class="mdl-navigation">
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
        <a class="mdl-navigation__link" href="">Link</a>
      </nav>
    </div>
    <main class="mdl-layout__content">
      <div class="android-card-container mdl-grid">
        <!-- Your content goes here -->
        <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp">
          <div class="mdl-card__media">
          </div>
          <div class="mdl-card__supporting-text">
              <h2 class="mdl-typography--font-light mdl-typography--subhead">
                {{registeredTable.length}}
              </h2>
          </div>
          <div class="mdl-card__actions">
            <h3>In Service Tables</h3>

          </div>
        </div>

        <div class="mdl-cell mdl-cell--2-col mdl-cell--4-col-tablet mdl-cell--2-col-phone mdl-card mdl-shadow--3dp">
          <div class="mdl-card__media">
          </div>
          <div class="mdl-card__supporting-text">
              <span class="mdl-typography--font-light mdl-typography--subhead">
                {{unRegisteredTable.length}}
              </span>
          </div>
          <div class="mdl-card__actions">
              <h3>Empty Tables</h3>
          </div>
        </div>
      </div>
    </main>
  </div>
</template>

<script>
  import axios from 'axios'
//  this.$parent.load = 'admin'
      export default {
    name: 'home',
    data () {
      return {
        msg: 'welcome to admin home page',
        errors: [],
        load: 'admin',
        unRegisteredTable: [],
        registeredTable: []
      }
    },
    mounted () {
//      this.$parent.load = 'admin'
      this.getInServiceTable();
      this.getUnServiceTable();

    },
    methods: {
//      methods
      reload: function (){
      },
      getInServiceTable: function () {
        axios.get('http://localhost:8000/api/food/table/registered')
          .then(response => {
            console.log(response.data)
            this.registeredTable = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      getUnServiceTable: function () {
        axios.get('http://localhost:8000/api/food/table/unregistered')
          .then(response => {
            console.log(response.data)
            this.unRegisteredTable = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
    }
  }
</script>

<style scoped>
  .box{

  }
  #cardRegisteredTable.demo-card-event.mdl-card {
    width: 256px;
    height: 256px;
    background: #3E4EB8;
    margin-left: 100px;
    margin-top: 60px;
  }
  #cardUnRegisteredTable.demo-card-event.mdl-card {
    width: 256px;
    height: 256px;
    background: #3E4EB8;
    margin-left: 500px;
    margin-top: 60px;
  }
  .demo-card-event > .mdl-card__actions {
    border-color: rgba(255, 255, 255, 0.2);
  }
  .demo-card-event > .mdl-card__title {
    align-items: flex-start;
  }
  .demo-card-event > .mdl-card__title > h4 {
    margin-top: 0;
  }
  .demo-card-event > .mdl-card__actions {
    display: flex;
    box-sizing:border-box;
    align-items: center;
  }
  .demo-card-event > .mdl-card__actions > .material-icons {
    padding-right: 10px;
  }
  .demo-card-event > .mdl-card__title,
  .demo-card-event > .mdl-card__actions,
  .demo-card-event > .mdl-card__actions > .mdl-button {
    color: #fff;
  }

</style>
