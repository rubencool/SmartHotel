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
        <input type="submit" id="register" class="mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect mdl-button--accent" value="Register">
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
        tableId: ''
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
//        MediaStreamTrack.stop()
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
      register: function () {
        console.log('called')
        for (var i = 0; i < this.tableList.length; i++) {
          if (this.tableId === this.tableList[i].tabel_Id) {
            cookie.set('customerTableId',this.tableId, 1);
//            if(cookie.get('customerRegistered') === 'false') {
//              cookie.delete('customerRegistered');
              cookie.set('customerRegistered','true', 1);
//            }else{
//              cookie.set('customerRegistered','true',1);
//            }
//            this.$parent.CustomerTableId = this.tableId;
//            this.$parent.CustomerRegistered = true;
            this.$parent.reloadMenu = true;
            this.$router.push('menu/')
//            this.router.go('/');
//            window.location.href = "http://localhost:8080/#/menu/true/gardenA1";
//            location.replace('http://localhost:8080/#/menu/true/gardenA1')
          }else{
            this.msg = 'Invalid  !!!'
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
