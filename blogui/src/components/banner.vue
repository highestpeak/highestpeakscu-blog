<template>
  <div class="article-banner" :style="'background-color:#'+color[0]+';background-image:url('+image[0]+color[1]+image[1]+');' ">
      <h2 style="transform: translateY(0px); opacity: 1;" :style="'color:'+color[2]">{{title}}</h2>
      <p class="post-date" style="transform: translateY(0px); opacity: 1;" :style="'color:'+color[2]">{{desc}}</p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {
  name: 'Banner',
  props: {
  },
  computed:{
    ...mapGetters({
        title: "banner/bannerTitle",
        desc: "banner/bannerDesc",
        color:"banner/bannerColor", // get text color from color[2],Foreground from color[0],background from color[1]
        image:"banner/bannerImage",
      })
  },
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.article-banner {
    width: 100%;
    box-sizing: border-box;
    top: 0;
    left: 0;
    padding: 100px 20px 25px 20px;
    text-align: center;
    position: relative;
    background-repeat: repeat;
    background-position: center;
    /* background-size: cover; */
    /* background-color: #d292a1;
background-image: url("data:image/svg+xml,%3Csvg width='100' height='100' viewBox='0 0 100 100' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath d='M11 18c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm48 25c3.866 0 7-3.134 7-7s-3.134-7-7-7-7 3.134-7 7 3.134 7 7 7zm-43-7c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm63 31c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM34 90c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zm56-76c1.657 0 3-1.343 3-3s-1.343-3-3-3-3 1.343-3 3 1.343 3 3 3zM12 86c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm28-65c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm23-11c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-6 60c2.21 0 4-1.79 4-4s-1.79-4-4-4-4 1.79-4 4 1.79 4 4 4zm29 22c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zM32 63c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm57-13c2.76 0 5-2.24 5-5s-2.24-5-5-5-5 2.24-5 5 2.24 5 5 5zm-9-21c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM60 91c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM35 41c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2zM12 60c1.105 0 2-.895 2-2s-.895-2-2-2-2 .895-2 2 .895 2 2 2z' fill='%239d3f55' fill-opacity='0.4' fill-rule='evenodd'/%3E%3C/svg%3E"); */
}
.article-banner h2 {
    margin: 0.4em 0;
    font-size: 2.2em;
    color: #fff;
    text-shadow: 0 0 40px #34495e;
    opacity: 0;
    transform: translateY(-20px);
    transition: all 0.4s;
}
.article-banner .post-date {
    margin: 10px 0 20px 0;
    color: #fff;
    opacity: 0;
    transform: translateY(-20px);
    transition: all 0.4s;
    transition-delay: 0.05s;
}
</style>
