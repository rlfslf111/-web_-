<template>
  <li class="list-group-item" @click="selectMovie">
      {{movie.title}}
  </li>
</template>

<script>
export default {
    name : "ArticleMovieSearch",
    props:{
        movie: Object,
    },
    methods:{
        selectMovie(){
            this.$emit('select-movie',this.movie)
        }
    }
}
</script>

<style scoped>
    .list-group-item{
        cursor: pointer;
    }
    .list-group-item:hover{
        background-color: lightblue;
    }
</style>