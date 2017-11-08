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
          <h4 class="title">Add Food</h4>
        </div>
        <div class="content">

          <form>

            <div class="row">
              <div class="col-md-12">
                <fg-input type="text"
                          label="Food Name"
                          placeholder="Food Name"
                          v-model="sectionName"
                          id="sectionName">
                </fg-input>
              </div>
            </div>

            <div class="row">
              <div class="col-md-12">
                <fg-input type="number"
                          label="Rate"
                          placeholder=" Rate"
                          v-model="itemRate"
                          id="sectionName">
                </fg-input>
              </div>
            </div>

            <div class="row">
              <div class="col-md-12">
                <fg-input type="text"
                          label="Details"
                          placeholder="Details"
                          v-model="itemDetails"
                          id="sectionName">
                </fg-input>
              </div>
            </div>

            <div class="row">
              <div class="col-md-12">
                <input type="file"
                          id="fileItem"
                          label="Image Url"
                          placeholder="File"/>
              </div>

              <div class="row">
                <div class="col-md-12">
                  <label>Category</label>
                  <select>
                    <option v-for="cat in category" v-bind:value="cat.id">{{cat.cat_name}}</option>
                  </select>
                </div>
              </div>
            </div>

            <div class="text-center">
              <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="submit">
                Create
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
        sectionName:'',
        error:'',
        itemRate:'',
        itemDetails:'',
        itemImg:'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAPoAAAD6CAIAAAAHjs1qAAAABmJLR0QA/wD/AP+gvaeTAAAD+0lEQVR4nO3d0W3cMBBAQStI/y1fGrCA6EAeyXszBdiC8bAfK5q6Xq/XDzT8Wf0A8DlyJ0TuhMidELkTIndC5E6I3AmROyFyJ0TuhMidELkTIndC5E6I3AmROyFyJ0TuhMidELkTIndC5E6I3AmROyFyJ0TuhMidELkTIndC5E6I3AmROyFyJ0TuhMidELkTIndC5E6I3An5u/B3X9e18Lf/v7svLT99/qdfbL77+aOeZ5WFX6423QmROyFyJ0TuhMidELkTIndCVu7d76zay47ao++2/z7l7/kBpjshcidE7oTInRC5EyJ3QuROyI579zuj9rij9tCjzqOfvhdfeH79KdOdELkTIndC5E6I3AmROyFyJ+SkvfvpTtnHfzHTnRC5EyJ3QuROiNwJkTshcifE3n282fe+8zbTnRC5EyJ3QuROiNwJkTshcifkpL37bvvp3Z7nqdOf/w2mOyFyJ0TuhMidELkTIndC5E7Ijnv3Db/H+avZ97uPun/mlL/nB5juhMidELkTIndC5E6I3AmROyFX8NDzbO6Z2ZbpTojcCZE7IXInRO6EyJ0QuROy8rz77HPYo86Fzz6//tRu5+AP+l6s6U6I3AmROyFyJ0TuhMidELkTsnLvPnv/+nTvO/t5Zr8HGGX2e4OFTHdC5E6I3AmROyFyJ0TuhMidkJPumVl1vnyU3c6jj3LQvTqmOyFyJ0TuhMidELkTIndC5E7IjvfM7HY/zFN3P3/27539/uHp/wns9t7jx3QnRe6EyJ0QuRMid0LkTojcCdnxnplV56dH7cVr98lseI/7HdOdELkTIndC5E6I3AmROyFyJ+Ske2Z2s+qc/arz+l+QiulOiNwJkTshcidE7oTInRC5E7Jy777hPSS/OmUvPsqq+3k+wHQnRO6EyJ0QuRMid0LkTojcCVl5z8ydVXvcVe8Bdnv/sNvzDGS6EyJ3QuROiNwJkTshcidE7oTsuHe/M/v7oKOsurf+i/flo5juhMidELkTIndC5E6I3AmROyEn7d138/TelVPuX191b/0HmO6EyJ0QuRMid0LkTojcCZE7Ifbu452+tz7lOd9guhMid0LkTojcCZE7IXInRO6EnLR3P2W/O+qemVH7+ztP/567fV/2DaY7IXInRO6EyJ0QuRMid0LkTsiOe3f3lL/n6T5+9rn8Dd+TmO6EyJ0QuRMid0LkTojcCZE7IdeGy1GYxHQnRO6EyJ0QuRMid0LkTojcCZE7IXInRO6EyJ0QuRMid0LkTojcCZE7IXInRO6EyJ0QuRMid0LkTojcCZE7IXInRO6EyJ0QuRMid0LkTojcCZE7IXInRO6EyJ0QuRMid0LkTojcCZE7If8AeFUJ9t+fKqkAAAAASUVORK5CYII=',
        itemCategory:'',
        category:[]
      }
    },
    mounted() {
      this.getCategory()
    },
    methods: {
      getSectionList: function () {
        axios.get('http://localhost:8000/api/food/table')
          .then(response => {
            console.log(response.data)
            this.sectionList = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      getCategory: function () {
        axios.get('http://localhost:8000/api/food/category')
          .then(response => {
            console.log(response.data)
            this.category = response.data
          }).catch(e => {
          this.errors.push(e)
          console.error(e)
        })
      },
      submit () {
        var files = document.getElementById('fileItem').files;
//          this.itemImg = this.getBase64(files[0]);
        if (this.sectionName === ""){
          this.error = "Fill the field"
        }else {
          var formData = new FormData()
          formData.append('itm_name', this.sectionName);
          formData.append('rate', this.itemRate);
          formData.append('details', this.itemDetails);
          formData.append('in_category', this.itemCategory);
          formData.append('img', files[0], files[0].name);
          axios.post('http://localhost:8000/api/food/item/create', formData
          ,{ headers: { 'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW' } })
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
      getBase64:function (file) {
        var reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = function () {
        console.log(reader.result);
        return reader.result
      };
        reader.onerror = function (error) {
        console.log('Error: ', error);
      };
      }
    }
  }

</script>
<style>

</style>
