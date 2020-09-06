<template>
  <div>
    <h1>Article List</h1>
    <div class="d-flex justify-content-end"><button class="btn btn-info" @click="newArticle"><h6 class="my-auto">NEW</h6></button></div>
    <table class="table mt-2">
      <thead :class="{'thead-dark':onDarkmode}">
        <tr>
          <th scope="col">ID</th>
          <th scope="col">TITLE</th>
          <th scope="col">MOVIE</th>
          <th scope="col">USER</th>
          <th scope="col">MAKE_TIME</th>
          <th scope="col">MODIFY_TIME</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="article in articles" :key="`article_${article.id}`" @click="articleDetail(article.id)">
          <th scope="row">{{article.id}}</th>
          <td>{{article.title}}</td>
          <td>{{article.movie.title}}</td>
          <td>{{article.user.username}}</td>
          <td>{{article.created_at}}</td>
          <td>{{article.updated_at}}</td>
        </tr>
      </tbody>
    </table>
    <Pagination :onDarkmode="onDarkmode" :endIndex="endIndex" @go-page="goPage" class="d-flex justify-content-center"/>
  </div>
</template>

<script>
import axios from "axios";
import Pagination from "../../components/Pagination"

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "ArticleListView",
  data() {
    return {
      articles: [],
      endIndex:null
    };
  },
  props:{
    onDarkmode:Boolean
  
  },
  components: {
    Pagination,
  },
  methods: {
    fetchArticles() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(BACK_URL + "/articles/", config)
        .then(res => this.articles = res.data)
        .catch(() => this.$router.push('/accounts/login'))
    },
    articleDetail: function(id) {
      this.$router.push(`/articles/${id}`)
    },
    goPage(p){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(BACK_URL + `/articles/?page=${p}`, config)
        .then(res => this.articles = res.data)
        .catch(err => console.error(err))
    },
    getEndIndex(){
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(BACK_URL + "/articles/count/", config)
        .then(res => {
          this.endIndex = res.data.end_index
          })
        .catch(err => console.error(err))
    },
    newArticle: function() {
      this.$router.push(`/articles/create/`)
    },
  },
  created() {
    this.fetchArticles()
    this.getEndIndex()
  }
};
</script>

<style>
td {
  cursor: pointer;
}
tr:hover {
  background-color: #eee;
}
</style>
