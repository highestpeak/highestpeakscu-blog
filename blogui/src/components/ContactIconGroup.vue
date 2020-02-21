<template>
  <div id="ContactIconGroup">
    <div class="header-icons">
      <a :href="'mailto:'+contact.email">
        <i class="icon fa fa-envelope"></i>
      </a>
      <a :href="contact.github" target="_blank">
        <i class="icon fa fa-github-alt"></i>
      </a>
      <a :href="'tencent://AddContact/?fromId=50&fromSubId=1&subcmd=all&uin='+contact.qq" target="_blank">
        <i class="icon fa fa-qq"></i>
      </a>
      <a :href="'https://steamcommunity.com/id/'+contact.steam+'/'" target="_blank">
        <i class="icon fa fa-steam"></i>
      </a>
    </div>
  </div>
</template>

<script>
// import {
//     contact
// } from "@/setting"
import {getSetting} from "@/utils/request"
export default {
  name: "ContactIconGroup",
  data() {
    return {
      // contact_:contact,
      contact:{
        "email":null,
        "qq":null,
        "github":null,
        "steam":null,
      }
    };
  },
  async created() {
    if(this.$store.state.setting.setting==null){
      var settingJson = await getSetting();
      this.$store.commit('setting/setSetting',settingJson); 
    }
    this.contact.email=this.$store.state.setting.setting.get("contact")["email"]; 
    this.contact.qq=this.$store.state.setting.setting.get("contact")["qq"]; 
    this.contact.github=this.$store.state.setting.setting.get("contact")["github"]; 
    this.contact.steam=this.$store.state.setting.setting.get("contact")["steam"];  
  },
  methods:{
  }
};
</script>

<style scoped>
* a:hover{
  border-bottom: none !important;
}
/* header icons */

.header-icons {
  display: flex;
  justify-content: center;
  text-align: center;
}

.header-icons a {
  background-color: transparent;
  -webkit-text-decoration-skip: objects;
}

.header-icons a:-webkit-any-link {
  color: -webkit-link;
  cursor: pointer;
  text-decoration: underline;
}

@media only screen and (min-width: 550px) {
  .header-icons .icon {
    width: 35px;
    height: 35px;
    font-size: 35px;
  }
}

.header-icons .icon:active,
.header-icons .icon:hover {
  color: #ffd4e5;
  background: #6e5773;
}

.header-icons .icon {
  height: 20px;
  padding: 10px;
  border-radius: 50%;
  border: 2px solid #6e5773;
  transition: all 0.7s;
  width: 20px;
  font-size: 20px;
  margin: 5px;
}
.header-icons .icon {
  color: #1aa3a3;
  text-align: center;
}
.fa {
  display: inline-block;
  font: 14px/1 FontAwesome;
  font-size: inherit;
  text-rendering: auto;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}
</style>