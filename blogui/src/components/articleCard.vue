<template>
  <article class="article-card">
      <h2 class="article-title"><router-link :to="'/article/'+id">{{title}}</router-link></h2>
      <p class="article-date">{{date}}</p>
      <router-link v-for="(tag,index) in tags" :key="index" :to="'/tags/'+tag">
          <span class="tag-code" 
          :style="'background-color:'+color[index%color.length][0]+
                  ';color:'+color[index%color.length][1]">
            {{tag}}
          </span>
      </router-link>
      <div class="article-content">
            {{description}}
      </div>
      <router-link :to="'/article/'+id" class="readmore">
          Read more
      </router-link>
  </article>
</template>

<script>
import {articleCardTagColor} from "@/style/color"
export default {
  name: 'ArticleCard',
  props: ["id","title","date","tags","description"],
  data(){
    return{
        color:articleCardTagColor,
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
    text-align: initial;
}
* a{
  color:#2c3e50;
}
.article-card{
    margin:10px auto;
    display: block;
    padding-bottom: 10px;
}
.article-card:first-child {
    margin-top: 60px;
}
.article-title{
    font-size: 1.6em;
    margin-bottom: 0;
}
.article-date{
    color: #7f8c8d;
    margin: 10px 0;
    font-size: 0.9em;
}
.tag-code {
    font-family: 'Roboto Mono', Monaco, courier, monospace;
    font-size: 0.8em;
    display: inline-block;
    background-color: #f8f8f8;
    color: #e96900;
    padding: 3px 5px;
    margin: 0 2px 5px 0;
    border-radius: 2px;
    white-space: nowrap;
}
.article-content{
    margin: 10px 0;
    color: #34495e;

    overflow : hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 3; 
    word-wrap:break-word;
    word-break:break-all;
}
.readmore{
    text-decoration: none !important;
    color: #42b983 !important;
    cursor: pointer;
    font-weight: 600 !important;
    display: inline-block;
    transition: all 0.3s !important;
    border-bottom: none !important;
}
.readmore:hover{
    transform: translateX(10px);
}
</style>
