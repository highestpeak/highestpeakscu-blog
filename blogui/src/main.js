import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import 'font-awesome/css/font-awesome.css'

import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
Vue.use(ElementUI);

// 引入 vssue
import Vssue from 'vssue'
// 引入对应平台的 api 包
import GithubV4 from '@vssue/api-github-v4'
// 引入 vssue 的样式文件
import 'vssue/dist/vssue.css'
Vue.use(Vssue, {
  // 设置要使用的平台 api
  api: GithubV4,

  // 在这里设置你使用的平台的 OAuth App 配置
  owner: 'xxxx',
  repo: 'xxxx',
  prefix:'评论',
  autoCreateIssue:true,
  clientId: 'xxxxx',
  clientSecret: 'xxxxx', // 只有在使用某些平台时需要
})

Vue.config.productionTip = false

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
