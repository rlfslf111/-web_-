<template>
  <div>
    <!-- detail page -->
    <div class="card p-0">
      <div class="card-header" :class="{'bg-dark':onDarkmode}">
        <strong class="d-flex mt-4">
          <h4 :class="{'text-light':onDarkmode}">Title : {{detail.title}}</h4>
        </strong>
        <small class="d-flex justify-content-end" :class="{'text-light':onDarkmode}">작성자 : {{detail.user}}</small>
      </div>
      <ul class="list-group list-group-flush">
        <li class="list-group-item d-flex text-mute" :class="{'darkmode':onDarkmode}">{{detail.content}}</li>
        <li class="list-group-item d-flex text-mute flex-column align-items-end" :class="{'darkmode':onDarkmode}">
          <small>Created At : {{detail.created_at}}</small>
          <small>Updated At : {{detail.updated_at}}</small>  
        </li>
        <li class="list-group-item d-flex flex-column align-items-center" :class="{'darkmode':onDarkmode}">
          <h3 class="">{{detail.movie.title}}</h3>
          <img
            v-if="detail.movie.poster_path"
            :src="`https://image.tmdb.org/t/p/w500` + detail.movie.poster_path"
            class="card-img-top mb-2 w-50"
            alt="moviePoster"
          />
          <img
            v-else
            :src="'https://www.ira-sme.net/wp-content/themes/consultix/images/no-image-found-360x260.png'"
            class="card-img-top mb-2 w-50"
            alt="moviePoster"
          />
        </li>
      </ul>
    </div>
      <div v-if="isValidatedUser" class="d-flex justify-content-end">
          <small
            class="my-1 mx-2 badge modifybadge btn btn-outline-success"
            @click="articleUpdate(detail.id)"            
          >수정</small>
          <small
            class="my-1 mx-1 badge deletebadge btn btn-outline-danger"
            @click="articleDelete"
          >삭제</small>
      </div>
    <hr class="mt-4 mb-4" />
    <!-- comment Write section -->
    <CommentInput @create-comment="createComment" />
    <hr class="mt-4 mb-4" />
    <!-- comment view sections -->
    <div>
      <h5 class="d-flex">Comments {{receiveComment.length}}</h5>
    </div>
    <CommentList
      v-for="comment in receiveComment"
      :key="comment.id"
      :comment="comment"
      @comment-delete="commentDelete"
    />
  </div>
</template>

<script>
import axios from "axios";
import CommentList from "../../components/CommentList.vue";
import CommentInput from "../../components/CommentInput.vue";

const BACK_URL = "https://inmin.herokuapp.com";

export default {
  name: "ArticleDetailView",
  components: {
    CommentList,
    CommentInput
  },
  data: function() {
    return {
      detail: {
        id: null,
        user: null,
        title: null,
        content: null,
        created_at: null,
        updated_at: null,
        movie:null,
      },
      receiveComment: [],
      isValidatedUser: false
    };
  },
  props: {
    username: String,
    onDarkmode: Boolean
  },
  methods: {
    fetchDetail: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(BACK_URL + `/articles/${this.$route.params.id}/`, config)
        .then(response => {
          this.detail.id = response.data.id;
          this.detail.user = response.data.user.username;
          this.detail.title = response.data.title;
          this.detail.content = response.data.content;
          this.detail.created_at = response.data.created_at;
          this.detail.updated_at = response.data.updated_at;
          this.detail.movie = response.data.movie;
          
        })
        .catch(error => {
          console.log(error);
        });
    },
    articleDelete: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      if(confirm('삭제하시겠습니까?')){

        axios
          .delete(BACK_URL + `/articles/${this.$route.params.id}/`, config)
          .then(response => {
            if (response.data.status == "FAIL") {
              alert(response.data.user_error);
            } else {
              alert("게시글이 삭제 되었습니다.");
              this.$router.push("/articles/");
            }
          })
          .catch(error => {
            console.log(error.response.data);
          });
      }
    },
    articleUpdate: function(id) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(BACK_URL + `/articles/${this.$route.params.id}/user`, config)
        .then(response => {
          if (response.data.status == "FAIL") {
            alert('본인 글만 수정할 수 있습니다.');
          } else {
            this.$router.push(`/articles/${id}/update`)
          }
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
    validUser: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(BACK_URL + `/articles/${this.$route.params.id}/user`, config)
        .then(response => {
          if (response.data.status === "OK"){
            this.isValidatedUser=true
          }
          
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
    createComment: function(commentData) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .post(
          BACK_URL + `/articles/${this.$route.params.id}/comments/`,
          commentData,
          config
        )
        .then(response => {
          this.receiveComment.push(response.data);
          alert("댓글 작성 완료!");
          commentData.content = "";
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
    fetchComment: function() {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .get(BACK_URL + `/articles/${this.$route.params.id}/comments/`, config)
        .then(response => {
          this.receiveComment = response.data;
        })
        .catch(error => {
          console.log(error.response.data);
        });
    },
    commentDelete: function(comment) {
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get("auth-token")}`
        }
      };
      axios
        .delete(
          BACK_URL +
            `/articles/${this.$route.params.id}/comments/${comment.id}/`,
          config
        )
        .then(response => {
          if (response.data.status == "FAIL") {
            alert("본인이 작성한 댓글만 삭제할 수 있습니다.");
          } else {
            alert("댓글이 삭제되었습니다.");
            this.$router.push(`/articles/`);
          }
        })
        .catch(error => {
          console.log(error.response.data);
        });
    }
  },

  created: function() {
    this.fetchDetail();
    this.fetchComment();
    this.validUser()
  }
};
</script>

<style>
.modifybadge {
  cursor: pointer;
}
.deletebadge {
  cursor: pointer;
}
.buttonComment {
  cursor: pointer;
}
.darkmode{
  background-color: #eee
  ;
}
</style>