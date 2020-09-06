<template>
  <div>
    <MovieRecommend v-if="this.$cookies.isKey('auth-token')" :onDarkmode="onDarkmode" :isLoggedIn="isLoggedIn" />
    <strong>
      <h2>Movie List</h2>
    </strong>
    <div class="ml-auto mr-auto row d-flex justify-content-center">
      <div
        class="card col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-12"
        :class="{'bg-secondary':onDarkmode}"
        style="width: 16rem;"
        v-for="movie in movies"
        :key="movie.id"
      >
        <div class="card-body">
          <img
            v-if="movie.poster_path"
            :src="`https://image.tmdb.org/t/p/w500` + movie.poster_path"
            class="card-img-top mb-2 cursor"
            alt="moviePoster"
            data-toggle="modal"
            :data-target="'#movie' + movie.id"
          />
          <img
            v-else
            :src="'https://www.ira-sme.net/wp-content/themes/consultix/images/no-image-found-360x260.png'"
            class="card-img-top mb-2 cursor"
            alt="moviePoster"
            data-toggle="modal"
            :data-target="'#movie' + movie.id"
          />
          <h5
            class="card-title cursor"
            :class="{'text-white':onDarkmode}"
            data-toggle="modal"
            :data-target="'#movie' + movie.id"
          >{{movie.title}}</h5>
          <button
            type="button"
            class="btn btn-info"
            data-toggle="modal"
            :data-target="'#movie' + movie.id"
          >영화 정보 상세보기</button>
          <MovieDetail :movie="movie" :isLoggedIn="isLoggedIn" />
        </div>
      </div>
    </div>
    <Pagination
      :endIndex="endIndex"
      :onDarkmode="onDarkmode"
      @go-page="goPage"
      class="d-flex justify-content-center my-3"
      @click.native="scrollTop"
    />
    <button class="mobile-active fixed-btn btn " :class="{'btn-light':onDarkmode, 'btn-secondary':!onDarkmode}" @click="scrollTop">▲</button>
  </div>
</template>

<script>
import axios from "axios";

import MovieDetail from "../../components/MovieDetail.vue";
import MovieRecommend from "../../components/MovieRecommend.vue";
import Pagination from "../../components/Pagination";

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "MovieListView",
  data: function() {
    return {
      movies: []
    };
  },
  props: {
    isLoggedIn: Boolean,
    onDarkmode: Boolean,
  },
  components: {
    MovieDetail,
    MovieRecommend,
    Pagination
  },
  methods: {
    fetchMovies: function() {
      axios
        .get(BACK_URL + `/movies/?page=1`)
        .then(response => {
          this.movies = response.data;
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
    getEndIndex() {
      axios
        .get(BACK_URL + "/movies/count/")
        .then(res => {
          this.endIndex = res.data.end_index;
        })
        .catch(err => console.error(err));
    },
    goPage(p) {
      axios
        .get(BACK_URL + `/movies/?page=${p}`)
        .then(res => (this.movies = res.data))
        .catch(err => console.error(err));
    },
    scrollTop() {
      window.scrollTo(0, 0);
    }
    // movieDetail: function(id) {
    //     this.$router.push(`/movies/${id}`)
    // },
  },
  created: function() {
    this.fetchMovies();
    this.getEndIndex();
  }
};
</script>

<style>
@media (max-width: 575px) {
  .mobile-disable {
    display: none;
  }
}
@media (min-width: 575px) {
  .mobile-active {
    display: none;
  }
}
.cursor {
  cursor: pointer;
}
.fixed-btn {
  position: fixed;
  bottom: 10px;
  right: 10px;
}
</style>