<template>
    <div >
        <paginate
        :page-count="endIndex"
        :click-handler="goPage"
        :prev-text="'Prev'"
        :next-text="'Next'"
        :container-class="'pagination'"
        :page-class="'page-item'"
        :page-link-class="'page-link'"
        :prev-class="'page-item'"
        :prev-link-class="'page-link'"
        :next-class="'page-item'"
        :next-link-class="'page-link'"
        >    
        </paginate>
    </div> 
</template>

<script>
export default {
    props:{
        endIndex: Number,
        onDarkmode: Boolean,
    },
    data(){
        return{
        }
    },
    methods:{
        goPage(p){
    
            this.$emit('go-page',p)
        },
        
    },
    created: function(){
    },
}
</script>

<style scoped>
    .page-link{
        cursor: pointer;
    }
</style>