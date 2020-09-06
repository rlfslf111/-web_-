<template>
  <div>
      <div>
      <div class="form-check form-check-inline">
        <p class="my-auto mr-2">수정할 평점을 입력해주세요 :</p>
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
      <button class="btn btn-success" @click="rateModify">수정</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

const BACK_URL = "https://inmin.herokuapp.com";

export default {
    name:'MovieRatingUpdate',
    props: {
        movie:Object,
        rateMovie:Object,
    },
    data: function () {
        return {
            tempPoint: null,
        }
    },
    methods: {
        rateModify: function() {
            console.log(this.rateMovie.point)
            const config = {
            headers: {
              Authorization: `Token ${this.$cookies.get("auth-token")}`
            }
          };
          axios.post(BACK_URL + `/movies/${this.movie.id}/rate/`,this.rateMovie,config)
            .then((response) => {
                this.tempPoint = response.data.point
                this.$emit('rate-update',this.tempPoint)
            }).catch((error) => {
                console.log(error.response.data)
            })
        },
    },
}
</script>

<style>

</style>