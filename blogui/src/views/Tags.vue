<template>
  <div id="tag-page">
    <!-- <h1 style="text-align:center">This is an Tags page</h1> -->
    <div class="tag-cloud">
      <a v-for="(tag,index) in taglist" :key="index" style="background: #9cb2e1;" href="#" v-on:click="tagClick(index)">{{tag}}</a>
    </div>
    
    <div v-if="showPreview!=-1" class="tag-list" >
      <h3 class="tag-name">{{ tagPreviewList[showPreview].tag }}</h3>
      <ul v-for="(item,index) in tagPreviewList[showPreview].previews" :key="index" class="tag-preview">
        <li>
          <router-link :to="'/article/'+item.id">{{ item.title }}</router-link>
        </li>
      </ul>
    </div>
    
  </div>
</template>

<script>
import {getTagList} from "@/utils/request"
export default {
  name: 'Tags',
  props: ['name'],
  components:{
  },
  data(){
    return{
      showPreview:-1,
      taglist:[],
      tagPreviewList:[],
        // taglist:["python","java","后端","闲谈4","闲谈5","闲谈6","闲谈7","闲谈8","闲谈9"],
        // tagPreviewList:[
        //   {
        //     tag:"闲谈1",
        //     previews:[
        //       {"href":"#","title":"1搭建一个舒服的hexo博客"},
        //       {"href":"#","title":"1开始写博客"},
        //       {"href":"#","title":"1仅仅是测试"},
        //     ],
        //   },
        //   {
        //     tag:"闲谈2",
        //     previews:[
        //       {"href":"#","title":"2搭建一个舒服的hexo博客"},
        //       {"href":"#","title":"2开始写博客"},
        //       {"href":"#","title":"2仅仅是测试"},
        //     ],
        //   },{
        //     tag:"闲谈3",
        //     previews:[
        //       {"href":"#","title":"3搭建一个舒服的hexo博客"},
        //       {"href":"#","title":"3开始写博客"},
        //       {"href":"#","title":"3仅仅是测试"},
        //     ],
        //   },{
        //     tag:"闲谈4",
        //     previews:[
        //       {"href":"#","title":"4搭建一个舒服的hexo博客"},
        //       {"href":"#","title":"4开始写博客"},
        //       {"href":"#","title":"4仅仅是测试"},
        //     ],
        //   },
        // ]
    }
  },
  created(){
    this.$store.commit('banner/showBanner'); 
    this.$store.commit('banner/setContent',{
      title:"Tags",
      desc:"标签检索",
    }); 
    this.initShowIndex();
    this.initTag();
  },
  methods:{
    tagClick(index){
      this.showPreview=index;
    },
    initShowIndex(){
      if (this.taglist.length<=0) {
        this.showPreview= -1;
      }else{
        var targetIndex = this.taglist.indexOf(this.name);
        this.showPreview= targetIndex == -1? 0:targetIndex;
      }
    },
    async initTag(){
      var tags = await getTagList();
      // console.log(tags);
      for (let index = 0; index < tags.length; index++) {
        const tagElment = tags[index];
        this.taglist.push(tagElment[0]);
        console.log(tagElment[0]);
        var newPreviewElment = {
          tag:tagElment[0],
          previews:[],
        };
        for (let iter = 0; iter < tagElment[1].length; iter++) {
          const article = tagElment[1][iter];
          newPreviewElment.previews.push({
              "id":article.id,
              "title":article.title,
          });
        }
        this.tagPreviewList.push(newPreviewElment);
      }
      this.initShowIndex();
      // console.log(this.tagPreviewList);
    }
  }

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
*{
  text-align: initial;
}
.tag-cloud{
    margin: 30px 0;
    text-align: center;
}
.tag-cloud a {
    border: none;
    line-height: 28px;
    margin: 0 4px;
    margin-bottom: 8px;
    background: #63a35c;
    display: inline-block;
    border-radius: 4px;
    padding: 0 10px;
    color: #fff !important;
    transition: background 0.5s;
}
.tag-cloud a:hover{
  background: #0085a1 !important;
  border-bottom: none !important;
  padding-bottom: 0px !important;
}
.tag-list{
  margin-left: 1em;
  margin-right: 1em;
}
.tag-name{
  font-size: 1.4em;
  position: relative;
}
.tag-name::before{
    content: "#";
    color: #42b983;
    position: absolute;
    left: -0.7em;
    top: -2px;
    font-size: 1.2em;
    font-weight: 700;
}
.tag-preview {
  font-size: 1.1em;
  padding-left: 1em;
}
.tag-preview li {
  cursor: pointer;
  margin: 10px 0;
}
.tag-preview a {
    text-decoration: none !important;
    color: #42b983 !important;
    cursor: pointer !important;
}
</style>
