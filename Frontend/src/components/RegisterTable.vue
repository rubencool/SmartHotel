<template>
  <div class="RegisterTable">
      <h1>Register Table </h1>
      <!-- <ul id="list"></ul> -->
      <input id="Qrcode" v-model="code"/>
      <video autoplay id="webcam" width=320 ></video>
  </div>

  <!--form-->
</template>

<script>
  export default {
    name: 'RegisterTable',
    data () {
      return {
        msg: 'RegisterTable',
        code: '',
        errors: [],
        file: '',
        url: 'http://api.qrserver.com/v1/read-qr-code/',
        path: ''
      }
    },
    mounted () {
      this.Qrscan()
    },
    methods: {
      Qrscan: function () {
        var data = "";
        require('../../static/js/qrscan/qrscan.js')
        // require('../../static/js/qrscan/decoder.js')
        QRReader.init('#webcam','../../static/js/qrscan/')
        function scan () {
          QRReader.scan(function (result) {
              data = result
              var Qrcode = document.getElementById("Qrcode").value = "";
              var Qrcode = document.getElementById("Qrcode").value = data;


              // var list = document.getElementById("list");
              // var li = document.createElement("li");
              // li.appendChild(document.createTextNode(data));
              // list.appendChild(li);
              console.log(data);
              return
            setTimeout(scan, 1)
          })
        }
        scan()
      },
      setCode: function (data){
        this.code = data.data
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
