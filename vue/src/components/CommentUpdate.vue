<template>
  <div class="input-group mb-3">
    <input
      type="text"
      class="form-control"
      placeholder="Recipient's username"
      aria-label="Recipient's username"
      aria-describedby="button-addon2"
      v-model="comment.content"
    />
    <div class="input-group-append">
      <button class="btn btn-outline-primary" type="button" id="button-addon2" @click="commentUpdate">작성</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "CommentUpdateView",
  data: function() {
    return {
      commentInfo: {
        article_id: null,
        id: null,
        content: null
      }
    };
  },
  props: {
    comment: Object
  },
  methods: {
    commentUpdate() {
      const BACK_URL = "https://inmin.herokuapp.com";
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      this.$emit("update-comment");
      axios
        .put(
          BACK_URL +
            `/articles/${this.comment.article.id}/comments/${this.comment.id}/`,
          this.comment,
          config
        )
        .then(response => {
          console.log(response.data);
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  }
};
</script>

<style>
</style>