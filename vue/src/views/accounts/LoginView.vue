<template>
  <div>
    <div class="row form-group mb-0 d-flex align-items-center">
      <label for="exampleInputEmail1" class="col-2 font-weight-bolder">ID: </label>
      <input type="text" class="form-control col-10" id="exampleInputEmail1" aria-describedby="emailHelp" v-model="loginData.username">
    </div>
    <small id="emailHelp" class="form-text text-muted d-flex justify-content-end">Please Input your ID</small>
    <div class="row form-group mb-0 d-flex align-items-center mt-3">
      <label for="exampleInputPassword1" class="col-2 font-weight-bolder">PW: </label>
      <input type="password" class="form-control col-10" id="exampleInputPassword1" v-model="loginData.password" @keypress.enter="login">
    </div>
    <small id="emailHelp" class="form-text text-muted d-flex justify-content-end">Please Input your PASSWORD</small>
    <button @click="login" class="my-3 btn btn-success">Submit</button>
  </div>

</template>

<script>
export default {
    name: 'LoginView',
    data: function () {
        return {
            loginData: {
                username:'',
                password:'',
            },
        }
    },
    methods: {
        login:function() {
            return this.$emit('submit-login-data',this.loginData)
        },
    },
}
</script>

<style>

</style>