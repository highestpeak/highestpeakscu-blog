(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["about"],{"06d1":function(t,e,n){},8323:function(t,e,n){"use strict";var a=n("06d1"),s=n.n(a);s.a},"85fe":function(t,e,n){},c8a1:function(t,e,n){"use strict";var a=n("85fe"),s=n.n(a);s.a},f820:function(t,e,n){"use strict";n.r(e);var a=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{staticClass:"about"},[n("div",{staticClass:"block"},[n("el-avatar",{attrs:{size:100,src:t.info_.avator}})],1),n("h1",[t._v(t._s(t.info_.blogname))]),n("p"),n("div",{staticStyle:{"font-weight":"bold"},domProps:{innerHTML:t._s(t.info_.introduction)}}),n("p"),n("ContactIconGroup"),n("money")],1)},s=[],c=(n("96cf"),n("1da1")),o=function(){var t=this,e=t.$createElement,n=t._self._c||e;return n("div",{attrs:{id:"ContactIconGroup"}},[n("div",{staticClass:"header-icons"},[n("a",{attrs:{href:"mailto:"+t.contact.email}},[n("i",{staticClass:"icon fa fa-envelope"})]),n("a",{attrs:{href:t.contact.github,target:"_blank"}},[n("i",{staticClass:"icon fa fa-github-alt"})]),n("a",{attrs:{href:"tencent://AddContact/?fromId=50&fromSubId=1&subcmd=all&uin="+t.contact.qq,target:"_blank"}},[n("i",{staticClass:"icon fa fa-qq"})]),n("a",{attrs:{href:"https://steamcommunity.com/id/"+t.contact.steam+"/",target:"_blank"}},[n("i",{staticClass:"icon fa fa-steam"})])])])},i=[],r=n("b775"),u={name:"ContactIconGroup",data:function(){return{contact:{email:null,qq:null,github:null,steam:null}}},created:function(){var t=this;return Object(c["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(null!=t.$store.state.setting.setting){e.next=5;break}return e.next=3,Object(r["g"])();case 3:n=e.sent,t.$store.commit("setting/setSetting",n);case 5:t.contact.email=t.$store.state.setting.setting.get("contact")["email"],t.contact.qq=t.$store.state.setting.setting.get("contact")["qq"],t.contact.github=t.$store.state.setting.setting.get("contact")["github"],t.contact.steam=t.$store.state.setting.setting.get("contact")["steam"];case 9:case"end":return e.stop()}}),e)})))()},methods:{}},l=u,f=(n("8323"),n("2877")),m=Object(f["a"])(l,o,i,!1,null,"2e4588be",null),g=m.exports,b=n("baf3"),d={name:"About",data:function(){return{info_:null}},created:function(){var t=this;return Object(c["a"])(regeneratorRuntime.mark((function e(){var n;return regeneratorRuntime.wrap((function(e){while(1)switch(e.prev=e.next){case 0:if(t.$store.commit("banner/showBanner"),t.$store.commit("banner/setContent",{title:"About",desc:"关于"}),null!=t.$store.state.setting.setting){e.next=7;break}return e.next=5,Object(r["g"])();case 5:n=e.sent,t.$store.commit("setting/setSetting",n);case 7:t.info_=t.$store.state.setting.setting.get("info");case 8:case"end":return e.stop()}}),e)})))()},components:{ContactIconGroup:g,money:b["a"]}},h=d,p=(n("c8a1"),Object(f["a"])(h,a,s,!1,null,"2ab1b4b9",null));e["default"]=p.exports}}]);
//# sourceMappingURL=about.6af48e47.js.map