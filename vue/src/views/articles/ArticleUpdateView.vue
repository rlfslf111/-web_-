<template>
  <div>
    <h1>Update Article</h1>
    <div class="form-group">
      <label for="title" class="font-weight-bolder mr-auto">title: </label>
      <input v-model="detailInfo.title" class="form-control" id="title" type="text" :placeholder="detailInfo.title"/>
    </div>
    <div class="form-group">
      <label for="content" class="font-weight-bolder">content: </label>
      <textarea class="form-control" id="content" rows="10" v-model="detailInfo.content" :placeholder="detailInfo.content"></textarea>
    </div>
    <div>
      <button @click="updateArticle" class="btn btn-success">Modify</button>
    </div>
  </div>

</template>

<script>
import axios from 'axios'

const BACK_URL = "https://inmin.herokuapp.com"

export default {
    name: 'ArticleUpdateView',
    data: function() {
        return {
            detailInfo: {
                title: null,
                content: null,
            }
        }
    },
    methods: {
        fetchUpdate: function() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.get(BACK_URL + `/articles/${this.$route.params.id}/`,config)
                .then((response) => {
                    this.detailInfo.title = response.data.title
                    this.detailInfo.content = response.data.content
                }).catch((error) => {
                    console.log(error.response.data);
                })
        },
        updateArticle: function() {
            const config = {
                headers: {
                    Authorization: `Token ${this.$cookies.get('auth-token')}`
                }
            }
            axios.put(BACK_URL + `/articles/${this.$route.params.id}/`,this.detailInfo,config)
                .then((response) => {
                    console.log(response.data)
                    this.$router.push(`/articles/${this.$route.params.id}`)
                }).catch((error) => {
                    console.log(error.response.data);
                })
        },
    },
    created: function() {
        this.fetchUpdate()
    },
}
</script>

<style>

</style>