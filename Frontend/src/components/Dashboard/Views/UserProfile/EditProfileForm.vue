<template>
  <div id="section-to-print" class="row">
    <div class="col-md-12">
      <div class="card">
        <paper-table :title="table1.title" :sub-title="table1.subTitle" :data="table1.data" :columns="table1.columns">

        </paper-table>
      </div>
    </div>
  </div>
</template>
<script>
  import axios from 'axios'
  import PaperTable from '@/components/UIComponents/PaperTable.vue'
  const tableColumns = ['Item','Quantity','Rate', 'Total']
  var tableData = []
//    {
//    particular: 'Dakota Rice',
//    rate: '$36.738',
//    qty: 'Niger',
//    total: 'Oud-Turnhout'
//  },
//    {
//      particular: 'Dakota Rice',
//      rate: '$36.738',
//      qty: 'Niger',
//      total: 'Oud-Turnhout'
//    },
//    {
//      particular: 'Dakota Rice',
//      rate: '$36.738',
//      qty: 'Niger',
//      total: 'Oud-Turnhout'
//    },
//    {
//      particular: 'Dakota Rice',
//      rate: '$36.738',
//      qty: 'Niger',
//      total: 'Oud-Turnhout'
//    },
//    {
//      id: '',
//      particular: '',
//      rate: '',
//      qty: '',
//      total: 'Oud-Turnhout'
//    }]

  export default {
    components: {
      PaperTable
    },
    data () {
      return {
        table1: {
          title: this.$route.params.tableId,
          subTitle: 'Here is a Bill',
          columns: [...tableColumns],
//          columns:[],
//          data: [...tableData],
          data: [],
        },
        table_id: this.$route.params.tableId,
        cust_id: this.$route.params.custId,
        total: 0
      }
    },
    mounted() {
      this.getOrder()

    },
    methods: {
      getOrder: function () {
        var url = 'http://localhost:8000/api/customer/order/customer/' +this.cust_id
        var dis =''
        axios.get(url)
          .then(response => {
            console.log(response.data)
            this.table1.data = response.data
            for(var i=0; i<response.data.length; i++ ){
              this.total =this.total +response.data[0].total
              dis = (this.total *15)/100
            }
            this.table1.data.push({
              item: '',
              rate: 'Service 15%',
              quantity: '',
              total: dis
            })
            this.table1.data.push({
              item: '',
              rate: 'Total',
              quantity: '',
              total: this.total + dis
            })
          }).catch(e => {
//          this.errors.push(e)
          console.error(e)
        })
      },
    }
  }

</script>
<style>
  @media print {
    body * {
      visibility: hidden;
    }

    #section-to-print, #section-to-print * {
      visibility: visible;
    }

    #section-to-print {
      margin-top: 0;
      left: 0;
      top: 0;
    }
  }
</style>
