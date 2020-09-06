<template>
    <div>
        <div class="modal fade" :id="'movie' + movie.id" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
            <div class="modal-dialog" style="max-width:750px;">
                <div class="modal-content">
                    <div class="modal-header">
                        <h5 class="modal-title my-auto" id="exampleModalLabel">{{movie.title}}</h5><div class="btn btn-success ml-3 my-auto" >평점 : {{movieInfo.vote_average}}</div>
                        <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true">&times;</span>
                        </button>
                    </div>
                    <div class="modal-body">
                        <img v-if="movieInfo.backdrop_path" :src="`https://image.tmdb.org/t/p/w500` + movieInfo.backdrop_path" :alt="movie.title" height="500px" width="700px" class="w-100">
                        <img v-else :src="'https://www.ira-sme.net/wp-content/themes/consultix/images/no-image-found-360x260.png'" class="card-img-top mb-2" alt="moviePoster" />
                        <hr>
                        <p v-if="movieInfo.overview">{{movieInfo.overview}}</p>
                        <p v-else class="my-auto">해당 영화의 줄거리가 제공되지 않습니다.</p>
                    </div>
                    <div class="modal-footer">

                    <!-- 평점 부여하기 -->
                    <div class="input-group">
                        <MovieRating :movie="movie" @rate-delete="rateDelete" :isLoggedIn="isLoggedIn"/>  
                    </div>

                    <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'

import MovieRating from './MovieRating.vue'

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "MovieDetail",
  props: {
    movie: Object,
    isLoggedIn: Boolean
  },
  components: {
      MovieRating,
  },
  data: function() {
      return {
          movieInfo:{
              title: null,
              poster_path: null,
              backdrop_path:null,
              overview:null,
              release_data: null,
              vote_average: null,
          },
      }
  },
  methods: {
      fetchDetailMovie: function() {
            axios.get(BACK_URL + `/movies/${this.movie.id}`)
                .then((response) => {
                    console.log(response.data)
                    this.movieInfo.title = response.data.title
                    this.movieInfo.poster_path = response.data.poster_path
                    this.movieInfo.backdrop_path = response.data.backdrop_path
                    this.movieInfo.overview = response.data.overview
                    this.movieInfo.release_data = response.data.release_data
                    this.movieInfo.vote_average = response.data.vote_average
                }).catch((error) => {
                    console.log(error.response.data);
                })
        },
        rateDelete: function() {
            const config = {
                headers: {
                Authorization: `Token ${this.$cookies.get("auth-token")}`
                }
            };
            axios.delete(BACK_URL + `/movies/${this.movie.id}/rate/`,config)
                .then((response) => {
                    if (response.data.status == "OK") {
                        console.log(response.data)
                    } else {
                        alert('삭제할 수 없습니다.')
                    }
                }).catch((error) => {
                    console.log(error.response.data)
                })
        },
  },
  created: function () {
      this.fetchDetailMovie()
  },

};
</script>

<style>
</style>