<template>
	<div class="drinksContainer">
		<div class="mdl-tabs__panel" id="drink">
			<ul class="demo-list-two mdl-list"  >
			  <li class="mdl-list__item mdl-list__item--two-line" v-for= "item in itemlist" v-if="item.in_category===1">
			    <span class="mdl-list__item-primary-content">
			      <i class="material-icons mdl-list__item-avatar">person</i>
			      <span>{{item.itm_name}}</span>
			      <span class="mdl-list__item-sub-title">{{item.details}}</span>
			    </span>
			    <span class="mdl-list__item-secondary-content">
			      <a class="mdl-list__item-secondary-action" href="#"><i class="material-icons">chevron_right</i></a>
			    </span>
			  </li>
			</ul>
		</div>
	</div>
</template>
<script>
import axios from 'axios'
export default {
	name: 'drinks',
	data () {
		return{
			itemlist: [],
			errors: [],
		}
	},
	created () {
		this.loadItemList()
	},
	methods: {
		loadItemList: function() {
			axios.get('http://127.0.0.1:8000/api/food/item')
          .then(response => {
            console.log(response.data)
            this.itemlist = response.data
			}).catch(e => {
	            this.errors.push(e)
	            console.error(e)
	        })
		}
	}
}
</script>
<style scoped>
.demo-list-two {
  width: 300px;
}
.android-more-section{
	padding-left: 30px;
}
</style>