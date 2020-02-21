<template>
  <div>
    <el-tooltip placement="top" style="margin:15px 0;">
    <div slot="content">
        <img v-for="(item,index) in money_" :key="index" :src="item.src" style="margin:0 15px;width:150px;height:150px;"/>
    </div>
    <el-button type="danger" style="font-size:30px;" circle>赏</el-button>
    </el-tooltip>
  </div>
</template>

<script>
// import {
//     money
// } from "@/setting"
import {getSetting} from "@/utils/request"
export default {
  name: 'Money',
  props: {
    msg: String
  },
  data(){
    return{
      money_:null,
    }
  },
  async created(){
    if(this.$store.state.setting.setting==null){
      var settingJson = await getSetting();
      this.$store.commit('setting/setSetting',settingJson); 
    }
    this.money_=this.$store.state.setting.setting.get("money"); 
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
