<template>
  <div>
    <!-- <h1>This is an TimeLine page</h1> -->
    <div class="time-body" v-loading="loading">
      <section v-for="(activity,index) in activities" :key="index" class="time-section">
          <h1 class="section-year">
          {{activity.section}}
          </h1>
          <div v-for="(item,iter) in activity.list" :key="iter" class="section-list">
            <div class="section-list-item">
              <router-link :to="'/article/'+item.id" class="archive-title">{{item.title}}</router-link>
              <p class="archive-date">{{item.date}}</p>
            </div>
          </div>
      </section>
    </div>
  </div>
</template>

<script>
import {timeLineGet} from "@/utils/request"
export default {
  name: 'TimeLine',
  props: {},
  data(){
    return{
      loading:false,
      activities:[
        {
          section:"2018",
          list:[
            {"title":"权限管理","id":123,"date":"12-3"},
            {"title":"权限管理","id":123,"date":"12-3"},
            {"title":"权限管理","id":123,"date":"12-3"},
          ]
        },{
          section:"2017",
          list:[
            {"title":"权限管理","id":123,"date":"12-3"},
            {"title":"权限管理","id":123,"date":"12-3"},
            {"title":"权限管理","id":123,"date":"12-3"},
          ]
        },{
          section:"2016",
          list:[
            {"title":"权限管理","id":123,"date":"12-3"},
            {"title":"权限管理","id":123,"date":"12-3"},
            {"title":"权限管理","id":123,"date":"12-3"},
          ]
        }
      ]
    }
  },
  created(){
    this.$store.commit('banner/showBanner'); 
    this.$store.commit('banner/setContent',{
      title:"Timeline",
      desc:"时间线",
    }); 
    this.loading=true;
    this.initTimeLine();
  },methods:{
    async initTimeLine(){
      this.activities=await timeLineGet();
      this.loading=false;
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  text-align: initial;
}
.time-body{
  padding: 2em 1em;
    margin: 0 auto;
    height: 100%;
    max-width: 980px;
    position: relative;
    transform: translateY(-20px);
    transition: all 0.4s;
}
.time-body::before{
  position: absolute;
  top: 2em;
  bottom: 1em;
  left: 30px;
  height: auto;
  content: '';
  background-color: #42b983;
  width: 4px;
}
.time-section {
    padding-left: 30px;
    position: relative;
}
.time-section .section-year {
    cursor: pointer;
    font-size: 1.8em;
    margin-left: 10px;
}
.time-section .section-year:before {
    position: absolute;
    left: 8px;
    top: 11px;
    content: '';
    background-color: #fff;
    width: 12px;
    height: 12px;
    border: 2px solid #42b983;
    border-radius: 50%;
}
.time-section .section-list .section-list-item {
    margin: 20px 0 20px 10px;
    position: relative;
}
.time-section .section-list .section-list-item:before {
    position: absolute;
    left: -29px;
    top: 7px;
    content: '';
    background-color: #42b983;
    width: 10px;
    height: 10px;
    border-radius: 50%;
}
.time-section .section-list .section-list-item .archive-title {
    color: #34495e;
    transition: all 0.3s ease;
    font-size: 1.1em;
    font-weight: initial !important;
}
.time-section .section-list .section-list-item .archive-title:hover {
    color: #42b983 !important;
    padding-left: 10px;
    padding-bottom: 0px !important;
    border-bottom: none !important;
}
.time-section .section-list .section-list-item .archive-date {
    color: #7f8c8d;
    font-size: 0.9em;
    margin: 5px 0;
}
</style>
