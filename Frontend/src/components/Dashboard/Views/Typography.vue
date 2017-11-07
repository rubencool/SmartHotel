<template>
  <div class="row">
    <div class="col-lg-4 col-md-5">
        <span class="mdl-chip mdl-chip--contact">
          <span class="mdl-chip__contact mdl-color--teal mdl-color-text--white">A</span>
          <span class="mdl-chip__text">{{error}}</span>
          </span>
      <!--Section List-->
      <div class="card">
        <a href="#/admin/table/form">
          <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab">
            <i class="material-icons">add</i>
          </button>
        </a>
        <div class="header">
          <h4 class="title">Section List</h4>
        </div>
        <div class="content">
          <ul class="list-unstyled team-members">
            <li>
              <div class="row" v-for="table in tableList">
                <div class="col-xs-3">
                  <div class="avatar">
                    <img :src="'static/img/section/section.png'" alt="Circle Image" class="img-circle img-no-padding img-responsive">
                  </div>
                </div>
                <div class="col-xs-6">
                  <div class="card">
                    {{table.table_id}}

                  </div>
                </div>


                <div class="row-xs-3 text-left">
                  <a @click.prevent="dlt(section.id)"><i id="icon" class="material-icons">delete</i></a>
                  <a :href="'http://localhost:8080/#/admin/table/edit/' +table.id"><i id="icon" class="material-icons">update</i></a>
                </div>
                <div class="stats" slot="footer"></div>
              </div>
            </li>
          </ul>
        </div>
      </div>
      <!--end-->
    </div>
    <div class="col-lg-8 col-md-7">
      <router-view></router-view>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'

  export default {
    components: {

    },
    data () {
      return {
        tableList:[],
        sectionTableList:[],
        error:''
      }
    },
    mounted() {
      this.getTableList()

    },
    methods: {
      getTableList: function () {
        axios.get('http://localhost:8000/api/food/table')
          .then(response => {
            console.log(response.data)
            this.tableList = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      getSectionTable: function (id) {
        axios.get('http://localhost:8000/api/food/table/section/' + id +'/')
          .then(response => {
            console.log(response.data)
            this.sectionTableList = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      dlt: function (id) {
          axios.delete('http://localhost:8000/api/food/table/' + id + "/delete/")
            .then(response => {
            }).catch(e => {
            this.errors.push(e)
            console.error(e)
          })
          this.$router.go(this.$router.currentRoute)
      }
    }
  }

</script>
<style>
  #icon{
    /*margin-left:150px;*/
  }

  .icon{

  }

</style>
