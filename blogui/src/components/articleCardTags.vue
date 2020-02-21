<template>
  <div>
    <router-link v-for="(tag,index) in tagList" :key="index" :to="'/tags/'+tag">
        <span class="tag-code" 
        :style="'background-color:'+tagColor[index%tagColor.length][0]+
                ';color:'+tagColor[index%tagColor.length][1]">
        {{tag}}
        </span>
    </router-link>
  </div>
</template>

<script>
import {articleCardTagColor} from "@/style/color"
export default {
  name: 'CardTags',
  props:['tagList'],
  data(){
    return{
        tagColor:articleCardTagColor,
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
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
</style>
