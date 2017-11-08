<template>
  <div class="row">
    <div class="col-lg-8 col-md-7">
      <!--Form-->
      <span class="mdl-chip mdl-chip--contact">
          <span class="mdl-chip__contact mdl-color--teal mdl-color-text--white">A</span>
          <span class="mdl-chip__text">{{error}}</span>
          </span>
      <div class="card">
        <div class="header">
          <h4 class="title">Edit Category</h4>
        </div>
        <div class="content">
          <form>

            <div class="row">
              <div class="col-md-12">
                <fg-input type="text"
                          label="Table Name"
                          placeholder="Section Name"
                          v-model="sectionName"
                          id="sectionName">
                </fg-input>
              </div>
            </div>

            <div class="text-center">
              <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="submit(tableId)">
                Update
              </button>
            </div>
            <div class="clearfix"></div>
          </form>
          <div class="col-xs-3 text-right">

          </div>
          <!--end-->
        </div>
      </div>
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
        tableId:this.$route.params.id ,
        sectionList:[],
        sectionName:'',
        error:''
      }
    },
    mounted() {
      this.getSectionList()
    },
    methods: {
      getSectionList: function () {
        axios.get('http://localhost:8000/api/food/category/'+this.tableId +'/')
          .then(response => {
            console.log(response.data)
            this.sectionList = response.data
            this.sectionName = this.sectionList.cat_name
          }).catch(e => {
//          this.errors.push(e)
          console.error(e)
        })
      },
      getCheckoutTable: function () {
        axios.get('http://localhost:8000/api/food/table/checkout')
          .then(response => {
            console.log(response.data)
            this.checkoutTable = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      submit (id) {
        if (this.sectionName === ""){
          this.error = "Fill the field"
        }else {
          axios.put('http://localhost:8000/api/food/table/'+id +'/edit/', {
            table_id: this.sectionName,
            section: this.sectionList.section
          })
            .then(response => {
              console.log(response.data)
            }).catch(e => {
            console.error(e)
          })
          this.sectionName= ''
          this.$router.go(-1)
        }
      },
      ready: function() {
        // watch for file input on bootstrap
//        this.watchFileInput();
      },
    }
  }

</script>
<style>

</style>
