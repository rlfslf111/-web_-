<template>
  <div>
    <h1>New Article</h1>
    <div class="form-group">
      <label for="title" class="font-weight-bolder mr-auto">title: </label>
      <input v-model="articleData.title" class="form-control" id="title" type="text" />
    </div>
    <div class="form-group">
      <label for="movie" class="font-weight-bolder mr-auto">movie: </label>
      <input class="form-control" id="movie" type="text" v-on:input="typing" :value="searchWord" :searchActive="searchActive"/>
      <ul class="list-group">
        <ArticleMovieSearch v-for="selectedMovie in selectedMovies" :movie="selectedMovie" :key="selectedMovie.id" @select-movie="selectMovie"/>
      </ul>
    </div>
    <div class="form-group">
      <label for="content" class="font-weight-bolder">content: </label>
      <textarea class="form-control" id="content" rows="10" v-model="articleData.content"></textarea>
    </div>
    <div>
      <button @click="createArticle" class="btn btn-success">Submit</button>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ArticleMovieSearch from '../../components/ArticleMovieSearch'

const BACK_URL = 'https://inmin.herokuapp.com'

export default {
  name: "CreateView",
  components:{
    ArticleMovieSearch,
  },
  data() {
    return {
      articleData: {
        title: null,
        content: null,
        movie_id: null,
      },
      movies: [],
      searchWord:'',
      selectedMovies: [],
      searchActive: false,
    };
  },
  methods: {
    createArticle() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.post(BACK_URL + '/articles/', this.articleData, config)
        .then((response) => { 
          console.log(response.data) 
          this.$router.push('/articles/')
        })
        .catch((error) => {
            alert('내용을 다시 확인해주세요.')
            console.log(error.response.data)
        })
    },
    searchMovie() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(BACK_URL + '/movies/search/',config)
        .then((response) => { 
          this.movies=response.data
        })
        .catch((error) => {
            console.log(error.response.data)
        })

    },
    typing(e){
      const searchMovies=[]
      this.searchWord=e.target.value
      this.movies.forEach(
        movie => {
          if (movie.title.indexOf(this.searchWord)!==-1){
            searchMovies.push(movie)
          }
        }
      )
      this.selectedMovies=searchMovies
    },
    selectMovie(movie){
      this.articleData.movie_id=movie.id
      this.searchWord=movie.title
      this.selectedMovies=[]
    },
    
    checkLoggedIn() {
      if (!this.$cookies.isKey('auth-token')) {
        this.$router.push('/accounts/login')
      } 
    }
  },
  created() {
    this.checkLoggedIn()
    this.searchMovie()
  },
};
</script>

<style>
</style>