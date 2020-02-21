<template>
  <div id="app" style="overflow-x: hidden;">
    <!-- <Aside @adjustContent="adjustContent" style="display:none;"></Aside> -->
    <Head ref="header" id="header" v-bind:class="{ 'fixed-header': isActive || !showbanner }"></Head>
    <transition name="el-fade-in-linear">
    <Banner v-if="showbanner"/>
    </transition>
    <section id="nav" ref="nav">
      <div class="main-body">
      <transition name="el-fade-in-linear">
      <router-view/>
      </transition>
      </div>
    </section>
    <div style="font-weight:bold" v-html="footerhtml"></div>
  </div>
</template>

<script>
// import Aside from '@/components/aside.vue'
import Head from '@/components/head.vue'
import Banner from '@/components/banner.vue'
import { mapGetters } from 'vuex'
import {getSetting} from "@/utils/request"
export default {
  components:{
    // Aside,
    Head,
    Banner
  },
  data(){
    return{
      footerhtml:"",
    }
  },
  computed:{
    ...mapGetters({
        showbanner: "banner/bannerShow",
        isActive:"banner/fixedActive",
      })
  },
  async created(){
    window.addEventListener('scroll', this.handleScroll);
    if(this.$store.state.setting.setting==null){
      var settingJson = await getSetting();
      this.$store.commit('setting/setSetting',settingJson); 
    }
    console.log(this.$store.state.setting.setting);
    this.footerhtml=this.$store.state.setting.setting.get("footer")["footerhtml"]; 
  },
  destroyed(){
    window.removeEventListener('scroll', this.handleScroll);
  },
  methods:{
    adjustContent(margin){
        var area = this.$refs.nav;
        area.style['margin-left'] = margin;
    },
    handleScroll () {
      var scrollTop = document.documentElement.scrollTop || document.body.scrollTop;
      if (scrollTop > 40) {
        // this.isActive=true;
        this.$store.commit('banner/fixedActive'); 
      } else if (scrollTop === 0) {
        // this.isActive=false;
        this.$store.commit('banner/fixedStop');
      }
      
    }
  },
}
</script>

<style>
body::-webkit-scrollbar {
    display:none;
}
/* app */
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  /* text-align: center; */
  /* color: #2c3e50; */
}

/* a */
#app a{
  /* color:#2c3e50; */
  text-decoration: none;
  font-weight: bold;
}

#app a:hover{
  padding-bottom: 2px;
  border-bottom: 2px solid #42b983;
}

/* contant */
#nav {
  padding: 15px;
  transition-duration: 0.5s;
  /* margin-left:300px; */
  margin-top: 30px;
}

.main-body{
  padding: 2em 1em;
  margin: 0 auto;
  height: 100%;
  max-width: 980px;
  position: relative;
  transform: translateY(-20px);
  transition: all 0.4s;
}

</style>
