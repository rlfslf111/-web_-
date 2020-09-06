<template>
  <div>
    <div v-if="!isRating">
      <div class="form-check form-check-inline">
        <p class="my-auto mr-2">평점을 입력해주세요 :</p>
        <input
          class="form-check-input"
          v-model="rateMovie.point"
          type="radio"
          name="inlineRadioOptions"
          id="inlineRadio1"
          value="0"
        />
        <label class="form-check-label" for="inlineRadio1">0</label>
      </div>
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          v-model="rateMovie.point"
          type="radio"
          name="inlineRadioOptions"
          id="inlineRadio2"
          value="2"
        />
        <label class="form-check-label" for="inlineRadio2">2</label>
      </div>
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          v-model="rateMovie.point"
          type="radio"
          name="inlineRadioOptions"
          id="inlineRadio2"
          value="4"
        />
        <label class="form-check-label" for="inlineRadio2">4</label>
      </div>
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          v-model="rateMovie.point"
          type="radio"
          name="inlineRadioOptions"
          id="inlineRadio2"
          value="6"
        />
        <label class="form-check-label" for="inlineRadio2">6</label>
      </div>
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          v-model="rateMovie.point"
          type="radio"
          name="inlineRadioOptions"
          id="inlineRadio2"
          value="8"
        />
        <label class="form-check-label" for="inlineRadio2">8</label>
      </div>
      <div class="form-check form-check-inline">
        <input
          class="form-check-input"
          v-model="rateMovie.point"
          type="radio"
          name="inlineRadioOptions"
          id="inlineRadio2"
          value="10"
        />
        <label class="form-check-label" for="inlineRadio2">10</label>
      </div>
      <button class="btn btn-success" @click="ratingMovie">평가</button>
    </div>
    
    <MovieRatingUpdate v-if="isUpdated" :movie="movie" :rateMovie="rateMovie" @rate-update="updateRate"/>
    
    <div v-if="isRating">
      <div class="ml-3 my-auto btn btn-warning">내 평점 : {{point}}</div>
      <small
        class="ml-2 mr-2 badge commentModify btn btn-outline-success"
        @click="rateModify"
      >
        <span v-if="isUpdated">취소</span>
        <span v-else>수정</span>
      </small>
      <small class="badge commentDelete btn btn-outline-danger" @click="rateDelete">삭제</small>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import MovieRatingUpdate from './MovieRatingUpdate.vue'

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "MovieRating",
  components: {
      MovieRatingUpdate,
  },
  data: function() {
    return {
      rateMovie: {
        point: null
      },
      isRating: false,
      point: null,
      isUpdated:false,
    };
  },
  props: {
    movie: Object,
    isLoggedIn: Boolean
  },
  methods: {
    CheckRatingUser: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(BACK_URL + `/movies/${this.movie.id}/rate/`, config)
        .then(response => {
          if (response.data.status == "FAIL") {
            this.isRating = false;
          } else {
            this.isRating = true;
            this.point = response.data.point;
            console.log(this.point)
            console(this.isRating);
          }
        })
        .catch(error => {
          console.log(error.response);
        });
    },
    ratingMovie: function() {
      if (this.isLoggedIn){

        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(
          BACK_URL + `/movies/${this.movie.id}/rate/`,
          this.rateMovie,
          config
        )
        .then(response => {
          if (response.data.status == 'OK') {
            this.isRating = !this.isRating
            this.point = response.data.point
          }
          console.log(this.isRating)
        })
        .catch(error => {
          console.log(error.response.data);
        });
      }else{
        console.log(this.isLoggedIn)
        alert('로그인이 필요합니다.')
      }
    },
    rateDelete: function() {
      this.$emit('rate-delete',this.movie)
        this.isRating = false
        this.isUpdated = false
        this.rateMovie.point = null
    },
    rateModify: function() {
        this.isUpdated = !this.isUpdated
    },
    updateRate: function(point) {
        this.point = point
        this.isUpdated = !this.isUpdated
    },
  },
  created: function() {
    this.CheckRatingUser();
  }
};
</script>

<style>
</style>