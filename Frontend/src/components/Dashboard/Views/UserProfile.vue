<template>
    <div id="print" class="row">
      <div class="col-lg-4 col-md-5">
        <!--Checkout Tables-->
        <div class="card">
          <div class="header">
            <h4 class="title">{{title1}}</h4>
          </div>
          <div class="content">
            <ul class="list-unstyled team-members">
              <li>
                <div class="row" v-for="table in checkoutTable">
                  <div class="col-xs-3">
                    <div class="avatar">
                      <img :src="image" alt="Circle Image" class="img-circle img-no-padding img-responsive">
                    </div>
                  </div>
                  <div class="col-xs-6">
                    <a v-bind:href="url +table.table_id +'/' + table.cust_id">
                      {{table.table_id}}
                    </a>
                  </div>

                  <div class="col-xs-3 text-right">
                    <button class="btn btn-sm btn-success btn-icon">
                      <i class="fa fa-envelope"></i>
                    </button>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <!--end-->

        <!--In service Tables-->
        <div class="card">
          <div class="header">
            <h4 class="title">{{title2}}</h4>
          </div>
          <div class="content">
            <ul class="list-unstyled team-members">
              <li>
                <div class="row" v-for="table in inServiceTable">
                  <div class="col-xs-3">
                    <div class="avatar">
                      <img :src="image" alt="Circle Image" class="img-circle img-no-padding img-responsive">
                    </div>
                  </div>
                  <div class="col-xs-6">
                    <a v-bind:href="url +table.table_id +'/' + table.cust_id">
                      {{table.table_id}}
                    </a>
                  </div>

                  <div class="col-xs-3 text-right">
                    <button class="btn btn-sm btn-success btn-icon active">
                      <i class="fa fa-envelope"></i>
                    </button>
                  </div>
                </div>
              </li>
            </ul>
          </div>
        </div>
        <!--end-->
      </div>
      <div class="col-lg-8 col-md-7">
        <router-view></router-view>
        <!--<edit-profile-form v-if="">-->

        <!--</edit-profile-form>-->
      </div>
    </div>
</template>
<script>
  import EditProfileForm from './UserProfile/EditProfileForm.vue'
  import axios from 'axios'

  export default {
    data() {
      return {
        title1: 'Checkout Tables',
        title2: 'In Service Tables',
        image: 'static/img/faces/face-1.jpg',
        inServiceTable: [],
        checkoutTable: [],
        url: '#/admin/stats/bill/'
      }
    },
    components: {
      EditProfileForm,
    },
    mounted() {
      this.getInServiceTable()
      this.getCheckoutTable()

    },
    methods: {
      getInServiceTable: function () {
        axios.get('http://localhost:8000/api/food/table/uncheckout')
          .then(response => {
            console.log(response.data)
            this.inServiceTable = response.data
          }).catch(e => {
          this.errors.push(e)
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
    }
  }

</script>
<style>


</style>
