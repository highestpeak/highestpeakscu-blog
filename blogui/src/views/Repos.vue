<template>
  <div>
    <!-- <h1 style="text-align:center">This is an Repos page</h1> -->
    <div class="card-container">
      <section v-for="(repo,index) in repoDetailList" :key="index" class="project-card">
        <a :href="repo.repoURL" class="card-wrap" target="_blank">
        <div v-loading="repo.loading" class="card-header" data-name="off_render" 
            :style="'background-color:'+color[index%color.length]">
          </div>
          <h3 class="card-title">{{repo.repoName}}</h3>
          <p class="card-description">{{repo.description}}</p>
          <div class="card-footer">
            <span><i class="fa fa-star"></i>{{repo.stars}}</span>
            <span><i class="fa fa-code-fork"></i>{{repo.forks}}</span>
          </div>
        </a>
      </section>
    </div>
    <Vssue
      :title="'仓库页面'"
      />
  </div>
</template>

<script>
import {repoCardColor} from "@/style/color"
import {getAllReposURL,getAllReposDetail} from "@/utils/request"
export default {
  name: 'Repos',
  props: {
  },
  data(){
    return{
      repoApiList:[],
      repoDetailList:[],
      color:repoCardColor,
    }
  },
  created(){
    this.$store.commit('banner/showBanner'); 
    this.$store.commit('banner/setContent',{
      title:"Repo",
      desc:"项目仓库",
    });
    this.getAllRepos();
  },
  methods:{
    async getAllRepos(){
      var repo = await getAllReposURL();
      this.repoApiList=repo.repoApiList;
      this.repoDetailList=repo.repoDetailList;
      getAllReposDetail(this.repoApiList,this.repoDetailList);
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  text-align: initial;
  border-bottom: none;
}
.card-container{
  margin: 30px auto;
  display: -webkit-flex;
  display: flex;
  justify-content: space-between;
  flex-wrap: wrap;
}

.card-container .project-card {
    width: 320px;
    height: 160px;
    margin-bottom: 20px;
    position: relative;
}
.card-container .project-card .card-wrap:hover {
    border-color: rgba(0,0,0,0.1) rgba(0,0,0,0.1) rgba(0,0,0,0.15);
    box-shadow: 0 1px 3px rgba(0,0,0,0.05), 0 4px 12px rgba(0,0,0,0.1);
}
.card-container .project-card .card-wrap {
    box-sizing: border-box;
    height: 100%;
    display: block;
    padding: 20px;
    border: 1px solid #e5e5e5;
    border-radius: 4px;
    color: #34495e;
    transition: border-color 0.1s ease-in-out, box-shadow 0.1s ease-in-out;
}

.card-container .project-card .card-wrap .card-header {
    position: absolute;
    width: 100%;
    height: 20px;
    top: 0;
    left: 0;
    border-top-left-radius: 4px;
    border-top-right-radius: 4px;
    background-color: #42b983;
}

.card-container .project-card .card-wrap .card-title {
    margin-top: 10px;
    margin-bottom: 5px;
    font-size: 1.2em;

    overflow : hidden;
    text-overflow: ellipsis;
    display: -webkit-box;
    -webkit-box-orient: vertical;
    -webkit-line-clamp: 1; 
    word-wrap:break-word;
    word-break:break-all;
}
.card-container .project-card .card-wrap .card-footer {
    box-sizing: border-box;
    position: absolute;
    width: 100%;
    padding: 0 20px;
    bottom: 20px;
    left: 0;
}

.card-container .project-card .card-wrap .card-footer span:first-child {
    padding-right: 20px;
}
.card-container .project-card .card-wrap .card-footer span .fa {
    padding-right: 5px;
}

.card-description{
  font-weight: initial;

  overflow : hidden;
  text-overflow: ellipsis;
  display: -webkit-box;
  -webkit-box-orient: vertical;
  -webkit-line-clamp: 3; 
  word-wrap:break-word;
  word-break:break-all;
}
</style>
