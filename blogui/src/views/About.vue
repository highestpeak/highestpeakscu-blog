<template>
  <div class="about">
    <div class="block"><el-avatar :size="100" :src="info_.avator"></el-avatar></div>
    <h1>{{info_.blogname}}</h1>
    <p></p>
      <div style="font-weight:bold" v-html="info_.introduction"></div>
    <p></p>
    <ContactIconGroup/>
    <money/>
  </div>
</template>
<script>
import ContactIconGroup from "@/components/ContactIconGroup.vue"
import money from "@/components/money"
// import {
//     info
// } from "@/setting"
import {getSetting} from "@/utils/request"
export default {
  name: 'About',
  data(){
    return{
      info_:null,
    }
  },
  async created(){
    this.$store.commit('banner/showBanner'); 
    this.$store.commit('banner/setContent',{
      title:"About",
      desc:"关于",
    }); 
    if(this.$store.state.setting.setting==null){
      var settingJson = await getSetting();
      this.$store.commit('setting/setSetting',settingJson); 
    }
    this.info_=this.$store.state.setting.setting.get("info"); 
  },
  components:{
    ContactIconGroup,money
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  text-align: center;
}
</style>
