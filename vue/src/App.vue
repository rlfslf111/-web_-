<template>
  <div id="app" :class="{'dark-bg':onDarkmode}">
    <nav class="navbar navbar-expand-sm navbar-light bg-light mb-5" :class="{'bg-dark':onDarkmode}">
      <router-link class="navbar-brand" :class="{'text-white':onDarkmode}" to="/">Movie</router-link>
      <router-link class="navbar-brand" :class="{'text-white':onDarkmode}" to="/articles">Community</router-link>
      <button
        class="navbar-toggler"
        type="button"
        data-toggle="collapse"
        data-target="#navbarNavAltMarkup"
        aria-controls="navbarNavAltMarkup"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarNavAltMarkup">
        <div class="navbar-nav ml-auto">
          <router-link
            class="nav-item nav-link"
            :class="{'text-white':onDarkmode}"
            v-if="!isLoggedIn"
            to="/accounts/signup"
          >SignUp</router-link>
          <router-link
            class="nav-item nav-link"
            :class="{'text-white':onDarkmode}"
            v-if="!isLoggedIn"
            to="/accounts/login"
          >Login</router-link>
          <router-link
            class="nav-item nav-link"
            :class="{'text-white':onDarkmode}"
            v-if="isLoggedIn"
            to="/accounts/logout"
            @click.native="logout"
          >Logout</router-link>
        </div>
      </div>
    </nav>
    <button class="ml-auto mx-3 d-flex justify-content-end btn"
    @click="darkmode"
    :class="{'btn-light':onDarkmode, 'btn-secondary':!onDarkmode}">◐</button>
    <router-view
      class="container"
      @submit-login-data="login"
      @submit-signup-data="signup"
      :username="username"
      :isLoggedIn="isLoggedIn"
      :onDarkmode="onDarkmode"
    />
  </div>
</template>


<script>
import axios from "axios";

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "App",
  data: function() {
    return {
      isLoggedIn: false,
      username: "",
      onDarkmode: false,
    };
  },
  methods: {
    setCookiesAndLogin: function(key) {
      this.$cookies.set("auth-token", key);
      this.isLoggedIn = true;
      this.$router.push("/articles");
    },
    login: function(loginData) {
      this.username = loginData.username;
      axios
        .post(`${BACK_URL}/rest-auth/login/`, loginData)
        .then(response => {
          this.setCookiesAndLogin(response.data.key);
          console.log(this.username)
        })
        .catch(err => {
          alert("아이디와 비밀번호를 확인해주세요");
          console.log(err.response.data);
        });
    },
    logout: function() {
      const axiosConfig = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(`${BACK_URL}/rest-auth/logout/`, null, axiosConfig)
        .then(() => {
          alert("로그아웃 되었습니다.");
          this.$cookies.remove("auth-token");
          this.isLoggedIn = false;
          this.$router.push("/");
        })
        .catch(error => {
          console.log(error);
        });
    },
    signup: function(signupData) {
      axios
        .post(`${BACK_URL}/rest-auth/signup/`, signupData)
        .then(response => {
          this.setCookiesAndLogin(response.data.key);
          alert("회원가입이 완료되었습니다.");

        })
        .catch(error => {
          alert("입력 값을 다시 확인해주세요");
          console.log(error.response.data);
        });
    },
    darkmode(){
      this.onDarkmode=!this.onDarkmode
    }
  },
  created: function() {
    this.isLoggedIn = this.$cookies.isKey("auth-token");
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
.dark-bg{
  background-color: lightgray;
}
</style>
