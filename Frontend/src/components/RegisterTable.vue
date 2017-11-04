<template>
  <div class="RegisterTable">
    <div class="android-more-section">
      <!--mdl card-->
      <div class="demo-card-square mdl-card mdl-shadow--2dp">
        <div class="mdl-card__title mdl-card--expand">
          <h2 class="mdl-card__title-text">Register Table</h2>
        </div>
        <div class="mdl-card__supporting-text">
            <h1> {{tableId}}</h1>
            <label for="Qrcode">TableId</label>
            <input type="text" id="Qrcode" v-model="tableId">
          <video autoplay id="webcam" width=320 ></video>
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
  export default {
    name: 'RegisterTable',
    code: '',
    data () {
      return {
        msg: 'RegisterTable',
        errors: [],
        registered: false,
        tableList: [],
        tableId: 'hello'
      }
    },
    mounted () {
      this.Qrscan()
      this.getTableList()
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
//            setTimeout(scan, 1)
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
      register: function () {
        console.log('called')
        for (var i = 0; i < this.tableList.length; i++) {
          if (this.tableId === this.tableList[i].tabel_Id) {
            this.registered = true
            this.$router.push('menu/' + this.registered + '/' + this.tableId)
          }
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
