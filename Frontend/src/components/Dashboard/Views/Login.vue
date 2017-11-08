<template>
  <div id="Login" class="wrapper">
    <div class="col-lg-4 col-md-5">
      <!--Section List-->
      <div class="card">
        <div class="header">
          <h4 class="title">Login Panel</h4>
        </div>
        <div class="content">
          <!--form-->
          <form>

            <div class="row">
              <div class="col-md-12">
                <fg-input type="text"
                          label="User"
                          placeholder="Section Name"
                          v-model="user"
                          id="sectionName">
                </fg-input>
              </div>
            </div>

            <div class="row">
              <div class="col-md-12">
                <fg-input type="password"
                          label="Password"
                          placeholder="Password"
                          v-model="password"
                          id="sectionName">
                </fg-input>
              </div>
            </div>

            <div class="text-center">
              <button type="submit" class="btn btn-info btn-fill btn-wd" @click.prevent="submit">
                Login
              </button>
            </div>
            <div class="clearfix"></div>
          </form>
        </div>
      </div>
      <!--end-->
    </div>
    <div class="col-lg-8 col-md-7">
    </div>
  </div>
</template>

<script>

</script>

<style scoped>
  .demo-card-square.mdl-card {
    width: 320px;
    height: 320px;
  }
  .demo-card-square > .mdl-card__title {
    color: #fff;
  }
  #Login{
    margin-top: 10%;
    margin-left: 38%;
  }
</style>
