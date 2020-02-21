<template>
  <div class="header">
    <div v-if="showbanner && !isActive" class="header-container">
      <a class="home-link" href="/" :style="'color:'+color[2]+' !important'">
        <div class="logo"><el-avatar  :src="info_.avator"></el-avatar></div>
        <span>{{blogname}}</span>
      </a>
      <ul class="right-list">
        <li v-for="(item,index) in menu" :key="index" class="list-item">
          <router-link :to="item.link" class="item-link" :style="'color:'+ color[2]+' !important'">{{ item.name }}</router-link>
        </li>
      </ul>
    </div>
    <div v-else class="header-container">
      <a class="home-link" href="/">
        <div class="logo"><el-avatar  :src="info_.avator"></el-avatar></div>
        <span>{{blogname}}</span>
      </a>
      <ul class="right-list">
        <li v-for="(item,index) in menu" :key="index" class="list-item">
          <router-link :to="item.link" class="item-link">{{ item.name }}</router-link>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
import { mapGetters } from 'vuex'
// import {
//     info
// } from "@/setting"
import {getSetting} from "@/utils/request"
export default {
  name: "Head",
  data(){
      return{
        menu:[
            {"link":"/","name":"HOME"},
            {"link":"/tags","name":"TAGS"},
            {"link":"/repos","name":"REPOS"},
            {"link":"/timeline","name":"TIME LINE"},
            {"link":"/about","name":"ABOUT"},
        ],
        blogname:{},
        info_:{},
      }
  },
  computed:{
    ...mapGetters({
        color: "banner/bannerColor", // get text color from color[2]
        showbanner: "banner/bannerShow",
        isActive:"banner/fixedActive",
      }),
  },
  async created(){
    if(this.$store.state.setting.setting==null){
      var settingJson = await getSetting();
      this.$store.commit('setting/setSetting',settingJson); 
    }
    this.info_=this.$store.state.setting.setting.get("info"); 
    this.blogname=this.info_.blogname;
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
    font-weight: initial;
    font-family: 'Source Sans Pro', 'Helvetica Neue', Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
}
ol, ul, form, p {
    margin: 0;
}
.header {
  background: none;
  border: none;
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  z-index: 200;
  transition: background 0.5s;
}
.fixed-header {
    position: fixed;
    background-color: rgba(255,255,255,0.98);
    box-shadow: 0 0 3px rgba(14,14,14,0.26);
}
.header-container {
  max-width: 1200px;
  height: 40px;
  margin: 0 auto;
  padding: 10px 40px;
  position: relative;
}
.home-link {
    display: flex;
    align-items: center;
    float: left;
    /* font-weight: 500 !important; */
    font-size: 1.5em;
    line-height: 40px;
}
.home-link span{
  font-weight: 600 !important;
}
.home-link:hover {
    padding-bottom: none !important;
    border-bottom: none !important;
}
.logo {
    /* background: url(images/logo.png); */
    background-size: contain;
    width: 40px;
    height: 40px;
    margin-right: 10px;
}
.right-list *{
    list-style: none;
    float: right;
    padding: 0;
    font-weight: initial !important;
}
.list-item {
    display: inline-block;
    margin: 0 8px;
    float: left;
}
.item-link {
    height: 40px;
    line-height: 40px;
    text-decoration: none;
    color: #fff;
    padding-bottom: 3px;
}
.menu {
    display: none;
    float: right;
    width: 24px;
    height: 24px;
    margin-top: 10px;
}
.menu .icon-bar {
    display: block;
    width: 24px;
    height: 2px;
    border-radius: 1px;
    margin-top: 4px;
    background-color: #fff;
}
.menu-mask {
    display: none;
    position: fixed;
    left: 0;
    top: 52px;
    z-index: 99;
    width: 100%;
    overflow: hidden;
    max-height: 0;
    background: rgba(255,255,255,0.98);
    -webkit-transition: max-height 0.2s ease;
    transition: max-height 0.2s ease;
}
.menu-list {
    padding: 0;
}
.menu-item {
    position: relative;
    list-style: none;
    text-align: center;
    padding: 10px 0;
}
.menu-link {
    text-decoration: none;
    color: #7f8c8d;
}
.right-list {
    list-style: none;
    float: right;
    padding: 0;
}

/*  */
.header .home-link{
  color: #fff !important;
}
.fixed-header .home-link{
  color: #42b983  !important;
}
.header .right-list .list-item .item-link{
  color: #fff !important;
}
.fixed-header .right-list .list-item .item-link{
  color: #000  !important;
}
</style>
