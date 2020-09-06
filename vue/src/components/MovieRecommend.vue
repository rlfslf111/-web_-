<template>
  <div>
    <strong>
      <h2>Recommend Movie List</h2>
    </strong>
    <div class="ml-auto mr-auto row d-flex justify-content-center">
      <div
        class="card col col-xl-3 col-lg-3 col-md-4 col-sm-6 col-12"
        :class="{'bg-secondary':onDarkmode}"
        style="width: 16rem;"
        v-for="movie in recommendMovie"
        :key="movie.id"
      >
        <div class="card-body">
          <img
            v-if="movie.poster_path"
            :src="`https://image.tmdb.org/t/p/w500` + movie.poster_path"
            class="card-img-top mb-2 mobile-disable cursor"
            alt="moviePoster mobile-disable"
            data-toggle="modal"
            :data-target="'#movie' + movie.id"
          />
          <img
            v-else
            :src="'https://www.ira-sme.net/wp-content/themes/consultix/images/no-image-found-360x260.png'"
            class="card-img-top mb-2 mobile-disable cursor"
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
            class="btn btn-info mobile-disable"            
            data-toggle="modal"
            :data-target="'#movie' + movie.id"
          >영화 정보 상세보기</button>
          <MovieDetail :movie="movie" :isLoggedIn="isLoggedIn" />
        </div>
      </div>
    </div>
    <hr class="mb-5" />
  </div>
</template>

<script>
import axios from "axios";
import MovieDetail from "./MovieDetail.vue";

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "MovieRecommend",
  data: function() {
    return {
      recommendMovie: []
    };
  },
  props: {
    onDarkmode: Boolean,
    isLoggedIn: Boolean,
  },
  components: {
    MovieDetail
  },
  methods: {
    fetchRecommend: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(BACK_URL + `/movies/recommend/`, config)
        .then(response => {
          console.log(response.data);
          this.recommendMovie = response.data;
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  },
  created: function() {
    this.fetchRecommend();
  }
};
</script>

<style scoped>
</style>