<template>
  <div>
    <div class="card mt-4">
      <div class="card-header d-flex">
        <strong class="mr-auto">{{comment.user.username}}</strong>
        <small class="my-auto ml-auto">{{comment.created_at}}</small>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item d-flex">
          <CommentUpdate v-if="isUpdated" :comment="comment" @update-comment="commentModify" />
          <span v-else>{{comment.content}}</span>
        </li>
      </ul>
    </div>
    <div v-if="isValidatedUser" class="d-flex">
    <small
        class="ml-auto mr-2 badge commentModify btn btn-outline-success"
        @click="commentModify"
    >
        <span v-if="isUpdated">취소</span>
        <span v-else>수정</span>
    </small>
    <small class="badge commentDelete btn btn-outline-danger" @click="commentDelete">삭제</small>
    </div>
  </div>
</template>

<script>
import CommentUpdate from "../components/CommentUpdate";
import axios from "axios";
const BACK_URL = "https://inmin.herokuapp.com";
export default {
  name: "CommentList",
  props: {
    comment: Object
  },
  data: function() {
    return {
      bringId: {
        articleId: this.comment.article.id,
        commentId: this.comment.id
      },
      isUpdated: false,
      isValidatedUser: false
    };
  },
  components: {
    CommentUpdate
  },
  methods: {
    commentModify: function() {
      this.isUpdated = !this.isUpdated;
    },
    commentDelete: function() {
      if ( confirm('댓글을 삭제하시겠습니다?')){
        this.$emit("comment-delete", this.comment);

      }
    },
    validUser: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(
          BACK_URL +
            `/articles/${this.$route.params.id}/comments/${this.comment.id}/user`,
          config
        )
        .then(response => {
          if (response.data.status === "OK") {
            this.isValidatedUser = true;
          }
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  },
  created() {
    this.validUser();
  }
};
</script>

<style>
.commentModify {
  cursor: pointer;
}
.commentDelete {
  cursor: pointer;
}
</style>