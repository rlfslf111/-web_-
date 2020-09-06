<template>
  <div>
    <div class="row form-group mb-0 d-flex align-items-center">
      <label for="exampleInputEmail1" class="col-2 font-weight-bolder my-auto">ID:</label>
      <input
        type="text"
        class="form-control col-10"
        id="exampleInputEmail1"
        aria-describedby="emailHelp"
        v-model="signupData.username"
      />
    </div>
    <small id="emailHelp" class="form-text text-muted d-flex justify-content-end">Please Input your ID</small>

    <div class="row form-group mb-0 d-flex align-items-center mt-3">
      <label for="exampleInputPassword1" class="col-2 font-weight-bolder my-auto">PW:</label>
      <input
        type="password"
        class="form-control col-10"
        id="exampleInputPassword1"
        v-model="signupData.password1"
      />
    </div>
    <small id="emailHelp" class="form-text text-muted d-flex justify-content-end">Please Input your PASSWORD</small>

    <div class="row form-group mb-0 d-flex align-items-center mt-3">
      <label for="exampleInputPassword1" class="col-2 font-weight-bolder my-auto">Confirm:</label>
      <input
        type="password"
        class="form-control col-10"
        id="exampleInputPassword1"
        v-model="signupData.password2"
        @keypress.enter="signup"
      />
    </div>
    <small id="emailHelp" class="form-text text-muted d-flex justify-content-end">Please Check your PASSWORD</small>
    <button @click="signup" class="my-3 btn btn-success">Submit</button>
  </div>
</template>

<script>
export default {
  name: "SignupView",
  data: function() {
    return {
      signupData: {
        username: "",
        password1: "",
        password2: "",
      }
    };
  },
  methods: {
    signup: function() {
      this.$emit("submit-signup-data", this.signupData);
      
    }
  }
};
</script>

<style>
</style>