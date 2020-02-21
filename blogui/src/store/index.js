import Vue from 'vue'
import Vuex from 'vuex'
import {
  svgColorList,
  svgImageList
} from "@/style/svgBackground"
Vue.use(Vuex)

const banner = {
  namespaced: true,
  state: {
      show:false,
      isActive:false,
      title:null,
      desc:null,

      colorIndex:Math.ceil(Math.random()*100),
      imageIndex:Math.ceil(Math.random()*100),
  },
  mutations: {
      showBanner(state){
        state.colorIndex++;
        state.imageIndex++;
        state.show = true;
      },
      closeBanner(state){
        state.show = false;
      },
      fixedActive(state){
        state.isActive = true;
      },
      fixedStop(state){
        state.isActive = false;
      },
      setContent(state,payload){
        state.title=payload.title;
        state.desc=payload.desc;
      },
  },
  actions: {},
  getters: {
      bannerShow(state){
        return state.show;
      },
      fixedActive(state){
        return state.isActive;
      },
      bannerTitle(state){
        return state.title;
      },
      bannerDesc(state){
        return state.desc;
      },
      bannerColor(state){
        var color = svgColorList[state.colorIndex%svgColorList.length].slice();
        if(!state.show){
          color[2]=null;
        }
        return color;
      },
      bannerImage(state){
        return svgImageList[state.imageIndex%svgImageList.length];
      },
  }
}

const setting = {
  namespaced:true,
  state:{
    setting:null,
  },
  mutations:{
    setSetting(state,settingJson){
      // console.log(settingJson);
      var info=settingJson.info
      var contact=settingJson.contact
      var money=settingJson.money
      var setting=settingJson.uisetting
      var footer=settingJson.footer
      if (state.setting==null) {
        state.setting=new Map();
      }
      state.setting.set("info",info);
      state.setting.set("contact",contact);
      state.setting.set("money",money);
      state.setting.set("setting",setting);
      state.setting.set("footer",footer);
    }
  }
}

export default new Vuex.Store({
  modules: {
    banner: banner,
    setting:setting,
  }
})
