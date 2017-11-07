<template>
  <div class="android-more-section">
  <div class="RegisterTable">
    <!--mdl card-->
    <div class="demo-card-square mdl-card mdl-shadow--2dp">
      <div class="mdl-card__title mdl-card--expand">
        <h2 class="mdl-card__title-text">Register Table</h2>
      </div>
      <div class="mdl-card__supporting-text">
        <h1>{{msg}}</h1>
          <label for="Qrcode">TableId</label>
          <input type="text" id="Qrcode" v-model="tableId">
        <video autoplay id="webcam" width="250" height="250" ></video>
      </div>
      <div class="mdl-card__actions mdl-card--border">
        <input type="submit" id="register" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" value="Register" v-on:click="register()">
      </div>
    </div>
  </div>
  </div>
</template>

<script>
  import axios from 'axios'
  import cookie from 'vue-cookie'
  export default {
    name: 'RegisterTable',
    code: '',
    data () {
      return {
        msg: '',
        errors: [],
        registered: false,
        tableList: [],
        tableId: '',
        api_table_url:'http://127.0.0.1:8000/api/food/table/',
        table_id:'',
        customerList:[]
      }
    },
    mounted () {
      this.isCustomerRegistered()
    },
    methods: {
      Qrscan: function () {
        var vm = this
        require('../../static/js/qrscan/qrscan.js')
//        console.log(this.tableId)
        QRReader.init('#webcam', '../../static/js/qrscan/')
        function scan () {
          QRReader.scan(function (result) {
            vm.tableId = result
//          register
            vm.register()
            console.log(result)
            return
//            setTimeout(scan, 200)
          })
        }
        scan()
      },
      setTableId: function () {
        this.tableId = document.getElementById("Qrcode").value
      },
      getTableList: function () {
        axios.get('http://127.0.0.1:8000/api/food/table')
          .then(response => {
            console.log(response.data)
            this.tableList = response.data
          }).catch(e => {
            this.errors.push(e)
            console.error(e)
          })
      },
      getCustomerList: function () {
        axios.get('http://127.0.0.1:8000/api/customer/')
          .then(response => {
            console.log(response.data)
            this.customerList = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      setNewCustomerList: function () {
        axios.post('http://127.0.0.1:8000/api/customer/create', {
          table_id: this.table_id,
        })
          .then(response => {
            console.log(response.data)
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      register: function () {
        console.log('called')
        for (var i = 0; i < this.tableList.length; i++) {
          if (this.tableId === this.tableList[i].table_id) {
            this.table_id = this.tableList[i].id;
            cookie.set('customerTableId',this.tableId, 1);
            cookie.set('customerRegistered','true', 1);
            this.$parent.reloadMenu = true;
            this.updateTableRegistered();
            this.setNewCustomerList()
            this.$router.push('menu/')
          }else{
            this.msg = 'Invalid  !!!'
            location.reload();
          }
        }
      },
      isCustomerRegistered: function () {
        if (cookie.get('customerRegistered') === 'true'){
          this.$router.push('menu/')
        }else {
          this.Qrscan()
          this.getTableList()
        }
      },
      updateTableRegistered: function () {
        axios.patch(this.api_table_url + this.table_id +  '/edit/', {
          registered: true,
        })
          .then(response => {
            console.log(response)
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      }
    }
  }
</script>

<style scoped>
  .demo-card-square.mdl-card {
    width: 320px;
    height: auto;
    margin-left: 20px;
    margin-top: 140px;
  }

  .demo-card-square > .mdl-card__title {
    /*color: #fff;*/
    background: url('../assets/icon/icon_drinks.png') bottom right 15% no-repeat #46B6AC;
  }
</style>
