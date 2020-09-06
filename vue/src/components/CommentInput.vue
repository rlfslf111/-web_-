<template>
  <div class="input-group">
    <div class="input-group-prepend">
        <span class="input-group-text">Comment</span>
    </div>
    <textarea class="form-control" aria-label="With textarea" v-model="commentData.content"></textarea>
    <div class="input-group-prepend buttonComment">
        <span class="input-group-text" @click="createComment">작성</span>
    </div>
  </div> 
</template>

<script>
export default {
    name:'CommentInput',
    data: function () {
        return {
            commentData : {
                content: '',
            }
        }
    },
    methods: {
        createComment: function() {
            this.$emit('create-comment',this.commentData)
        }
    },
}
</script>

<style>

</style>