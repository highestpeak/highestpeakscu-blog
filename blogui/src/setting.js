import {getSetting} from "@/utils/request"
// var json=require('./setting.json');
var settingJson = getSetting();
var info=settingJson.info
var contact=settingJson.contact
var money=settingJson.money
var setting=settingJson.setting

// alipay png in assets dir
// wechat png in assets dir
// page logo png in assets dir
// api in api.js
// colors set in style dir
export{
    info,
    contact,
    money,
    setting
}