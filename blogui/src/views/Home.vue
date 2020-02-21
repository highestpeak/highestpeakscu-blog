<template>
  <div class="home">
    <!-- 文章列表 -->
    <div>
      <ArticleCard 
        v-for="article in articleList"
        :key="article.id"
        :id="article.id"
        :title="article.title"
        :date="article.create_time"
        :tags="article.tags"
        :description="article.description"/>
    </div>
    <!-- 分页 -->
    <div class="block pagination">
        <el-pagination
        @current-change="handleCurrentChange"
        :current-page.sync="currentPage"
        :page-size="pageSize"
        :total="articleTotal"
        :hide-on-single-page="true"
        layout="prev, pager, next"
        background />
        <!-- </el-pagination> -->
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import ArticleCard from '@/components/articleCard.vue'
import {getArticleList,getArticleNum} from "@/utils/request"
// import {
//     setting
// } from "@/setting"
import {getSetting} from "@/utils/request"
export default {
  name: 'Home',
  components: {
    ArticleCard,
  },
  data(){
    return{
      currentPage:1, // 当前页数
      articleTotal:0, // 所有的博文数量
      pageSize:5, // 每页博文数量
      articleList:[], // 博文简要信息列表
    }
  },
  async created(){
    this.$store.commit('banner/closeBanner'); 
    if(this.$store.state.setting.setting==null){
      var settingJson = await getSetting();
      this.$store.commit('setting/setSetting',settingJson); 
    }
    this.pageSize=parseInt(this.$store.state.setting.setting.get("setting")["pagesize"],10); 
    this.articleTotal=await getArticleNum();
    this.handleCurrentChange();
  },
  methods:{
    async handleCurrentChange() {
      var detail=await getArticleList(this.currentPage,this.pageSize,{"tags":["a","b","c"],"time":"2018"});
      this.articleList=detail.articleList;
    },
  }
}
</script>
<style scoped>
.pagination{
  text-align: center;
}
</style>