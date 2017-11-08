<template>
  <div class="row">
    <div class="col-lg-4 col-md-5">
        <span class="mdl-chip mdl-chip--contact">
          <span class="mdl-chip__contact mdl-color--teal mdl-color-text--white">A</span>
          <span class="mdl-chip__text">{{error}}</span>
          </span>
      <!--Section List-->
      <div class="card">
        <a href="#/admin/food/form">
          <button class="mdl-button mdl-js-button mdl-button--fab mdl-button--mini-fab">
            <i class="material-icons">add</i>
          </button>
        </a>
        <div class="header">
          <h4 class="title">Food List</h4>
        </div>
        <div class="content">
          <ul class="list-unstyled team-members">
            <li>
              <div class="row" v-for="section in sectionList">
                <div class="col-xs-3">
                  <div class="avatar">
                    <img :src="section.img" alt="Circle Image" class="img-circle img-no-padding img-responsive">
                  </div>
                </div>
                <div class="col-xs-6">
                  <div class="card">
                    {{section.itm_name}}

                  </div>
                </div>


                <div class="row-xs-3 text-left">
                  <a @click.prevent="dlt(section.id)"><i id="icon" class="material-icons">delete</i></a>
                  <a :href="'http://localhost:8080/#/admin/food/edit/' +section.id"><i id="icon" class="material-icons">update</i></a>
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
  import PaperTable from '@/components/UIComponents/PaperTable.vue'
  const tableColumns = ['Id', 'Name', 'Salary', 'Country', 'City']
  const tableData = [{
    id: 1,
    name: 'Dakota Rice',
    salary: '$36.738',
    country: 'Niger',
    city: 'Oud-Turnhout'
  },
    {
      id: 2,
      name: 'Minerva Hooper',
      salary: '$23,789',
      country: 'Curaçao',
      city: 'Sinaai-Waas'
    },
    {
      id: 3,
      name: 'Sage Rodriguez',
      salary: '$56,142',
      country: 'Netherlands',
      city: 'Baileux'
    },
    {
      id: 4,
      name: 'Philip Chaney',
      salary: '$38,735',
      country: 'Korea, South',
      city: 'Overland Park'
    },
    {
      id: 5,
      name: 'Doris Greene',
      salary: '$63,542',
      country: 'Malawi',
      city: 'Feldkirchen in Kärnten'
    }]

  export default {
    components: {
      PaperTable
    },
    data () {
      return {
        table1: {
          title: 'Stripped Table',
          subTitle: 'Here is a subtitle for this table',
          columns: [...tableColumns],
          data: [...tableData]
        },
        table2: {
          title: 'Table on Plain Background',
          subTitle: 'Here is a subtitle for this table',
          columns: [...tableColumns],
          data: [...tableData]
        },
        sectionList:[],
        sectionTableList:[],
        error:''
      }
    },
    mounted() {
      this.getSectionList()

    },
    methods: {
      getSectionList: function () {
        axios.get('http://localhost:8000/api/food/item')
          .then(response => {
            console.log(response.data)
            this.sectionList = response.data
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
        this.getSectionTable(id)
        if (this.sectionTableList === []) {
          axios.delete('http://localhost:8000/api/food/category/' + id + "/delete/")
            .then(response => {
            }).catch(e => {
            this.errors.push(e)
            console.error(e)
          })
          this.$router.go(this.$router.currentRoute)
        }else{
          this.error = "Cant delete Category contain Food"
        }
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
