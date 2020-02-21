import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Tags from '../views/Tags.vue'
import Repos from '../views/Repos.vue'
import TimeLine from '../views/TimeLine.vue'
import Article from '../views/Article.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/tags',
    name: 'Tags',
    component: Tags
  },
  {
    path: '/repos',
    name: 'Repos',
    component: Repos
  },
  {
    path: '/timeLine',
    name: 'TimeLine',
    component: TimeLine
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/article/:id',
    name: 'ArticlePage',
    component: Article,
    props: true
  },
  {
    path: '/tags/:name',
    name: 'Tags',
    component: Tags,
    props: true
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
