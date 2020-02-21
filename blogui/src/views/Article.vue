<template>
  <div class="app-body flex-box" style="transition-delay: 0.15s; transform: translateY(0px); opacity: 1;">
      <article>
        <mavon-editor
          ref="mavon"
          defaultOpen="preview"
          v-model="articleContent"
          :navigation="false"
          :toolbarsFlag="false"
          :subfield="false"
          :preview="true"
          :transition="true"
          codeStyle="github" 
          v-loading="articleloading"
          style="position:initial;"
        />
        <!-- code style: dracula github hopscotch idea mono-blue qtcreator_light-->
      </article>
      
      <div style="width: 100%;height:auto;">
        <div style="margin:15px 0;width: 100%;">
          <el-rate
          v-model="stars"
          :colors="starColors"
          style="float:left;"
          :disabled="disabledRate"
          @change="handleStarChange"
          />
        </div>

        <money style="float:right;"/>
        <br/><br/>
        
        <div style="margin:20px 0;width: 100%;">
          <h2 style="float:left;">TAGS:</h2>
          <CardTags 
          :tagList="articleTag"
          style="float:left;margin:25px 0;margin-left:10px;"
          />
        </div><br/><br/><br/><br/>

        <Vssue
        v-if="articleTitle!=null"
        :title="'test2-'+articleTitle"
        />
        <!-- :options="options" -->
      </div>
      
      <aside class="catalog-container" style="margin-top:0px;" :style="'top:'+catalogtop+'px'">
        <strong class="toc-title">Catalog</strong>
        <div id="navigation" class="wx_navigation"  style="margin-top:10px;"/>
      </aside>
  </div>
</template>

<script>
// Local Registration
import { mavonEditor } from "mavon-editor";
import "mavon-editor/dist/css/index.css";
import {getArticle,sendStar,getArticleContent} from "@/utils/request"
import CardTags from "@/components/articleCardTags"
import money from "@/components/money"

export default {
  name: "Article",
  props:['id'],
  components: {
    mavonEditor,
    CardTags,
    money
  },
  data() {
    return {
      catalogtop:0,
      t1 : 0,
      t2 : 0,
      timer : null,

      articleTitle:null,
      articleTag:'',
      articleURL:'',
      articleContent:'',
      articleDate:'',
      stars:0,
      disabledRate:false,
      articleloading:false,
      starColors: ['#99A9BF', '#F7BA2A', '#FF9900'] 
    };
  },
  created() {
    this.$store.commit('banner/showBanner'); 
    this.$store.commit('banner/setContent',{
      title:"文章标题",
      desc:"发布日期",
    }); 
    this.articleInit();
    window.addEventListener('scroll', this.handleScroll);
    if(localStorage.getItem("~blog"+this.id+"-star-set~")=="true"){
      this.disabledRate=true;
    }
  },
  destroyed(){
    window.removeEventListener('scroll', this.handleScroll);
  },
  mounted(){
    
  },
  updated(){
    var page=this;
    page.buildNavigation();
  },
  methods: {
    async articleInit(){
        this.disabledRate=true;
        var article = await getArticle(this.id);
        this.articleTitle=article.articleTitle;
        this.articleDate=article.articleDate;
        this.articleURL=article.articleContent;
        this.stars=article.articleStars;
        this.articleTag=article.articleTag;
        this.$store.commit('banner/setContent',{
          title:this.articleTitle,
          desc:this.articleDate,
        }); 
        this.articleloading=true;
        this.articleContent=await getArticleContent(this.articleURL);
        this.articleloading=false;
        if(localStorage.getItem("~blog"+this.id+"-star-set~")=="true"){
          this.disabledRate=true;
        }else{
          this.disabledRate=false;
        }
    },

    buildNavigation() {
      var a = document.getElementById('navigation')
      a.innerHTML = this.$refs.mavon.d_render // mavmon根据marodown内容生成的dom
      const nodes = a.children
      var newDoms = []
      if (nodes.length) {
          for (let i = 0; i < nodes.length; i++) {
              const id = (nodes[i].children && nodes[i].children.length) ? nodes[i].children[0].id : ''
              judageH(nodes[i], i, nodes, id)
          }
      }
      function judageH(node, i, nodes, domId) {
          const reg = /^H[1-6]{1}$/
          if (!reg.exec(node.tagName)) { // 把不是h标签的都过滤掉
              node.style.display = 'none'
          } else {
              node.classList.add('navigator-item')
              const nodeArr = node.innerHTML.split('</a>')
              const id = domId
              const content = nodeArr[1]
              var childs = node.childNodes
              for (var index = childs.length - 1; index >= 0; index--) {
                  node.removeChild(childs[index])
              }
              const a = document.createElement('a')
              a.style.color="#41b883";
              a.style.fontWeight = "normal";
              a.id = id
              a.innerHTML = content
              node.appendChild(a)
              node.onclick = function () {
                  window.location.replace('#' + this.children[0].id)
              }
              newDoms.push(node)
          }
      }
      const sliceDoms = [] // 归类好的节点树
      newDoms.forEach((dom, i) => { // 把标题归类 每部分的标题组合到一起
          const level = dom.tagName.substr(1)
          const upLevel = newDoms[i - 1] ? newDoms[i - 1].tagName.substr(1) : ''
          if (upLevel) {
              if (level > upLevel) {
                  sliceDoms[sliceDoms.length - 1].push(dom)
              } else if (level > sliceDoms[sliceDoms.length - 1][0].tagName.substr(1)) {
                  sliceDoms[sliceDoms.length - 1].push(dom)
              } else {
                  sliceDoms.push([dom])
              }
          } else {
              sliceDoms.push([dom])
          }
      })
      sliceDoms.forEach(doms => {
          const thisTitleMaxId = doms[0].tagName.substr(1)
          doms.forEach(dom => {
              const domHeadingLevel = dom.tagName.substr(1) - thisTitleMaxId + 1
              dom.classList.add('heading_' + domHeadingLevel);
              dom.style.color="#41b883";
              dom.style.textAlign = "left";
              dom.style.fontSize = "17px";
              dom.style.marginBlockStart = "3px";
              dom.style.marginBlockEnd = "0px";
              dom.style.fontWeight = "normal";
              dom.style.marginLeft = (domHeadingLevel-1)*15+"px";
              // console.log(dom.style);
          })
      })
    },// buildNavigation

    handleScroll(){
      clearTimeout(this.timer);
      this.timer = setTimeout(this.isScrollEnd, 100);
      this.t1 = document.documentElement.scrollTop || document.body.scrollTop;
      
    },
    isScrollEnd() {
      this.t2 = document.documentElement.scrollTop || document.body.scrollTop;
      if(this.t2 == this.t1){
        var scrollTop=this.t1;
        var nextTop=scrollTop-150;
        this.catalogtop=nextTop<0?0:nextTop;
      }
    },

    handleStarChange(value){
        console.log("star: "+value);
        if(localStorage.getItem("~blog"+this.id+"-star-set~")!="true"){
          sendStar(this.id,value);
          localStorage.setItem("~blog"+this.id+"-star-set~",true);
          this.disabledRate=true;
        }
    }
  }
};
</script>

<style scoped>
.post-article {
    margin-top: 0;
    width: 100%;
}
article {
    display: block;
}
.catalog-container{
  width:250px;
  margin-right:-260px;
  max-height: 500px;
  overflow: hidden;
  overflow-y:auto;
  text-overflow: ellipsis;
  position:fixed;
  z-index:999;
  top:0%;
  right:0;
  text-align: initial;
}

.catalog-container .toc-title {
    font-size: 1.2em;
    position: relative;
    padding-left: 28px;
}
.catalog-container .toc-title:before {
    content: '';
    position: absolute;
    width: 22px;
    height: 22px;
    left: 0;
    top: 2px;
    background: url(../assets/catalog.png) no-repeat;
    background-size: contain;
}
.catalog-container .toc-nav {
    padding: 0;
    margin-top: 1em;
    max-height: 480px;
}
.catalog-container li {
    list-style-type: none;
    line-height: 1.5;
}
.catalog-container li a {
    text-decoration: none;
    color: #42b983 !important;
    cursor: pointer;
    font-weight: initial !important;
}
</style>

<style>
.el-rate__icon {
  font-size: 38px !important;
  margin: 10px auto;
}
</style>

<style>
/* markdown style */
.markdown-body blockquote {
  border-left: 4px solid #42b983 !important;
}

.markdown-body blockquote *{
  margin-bottom: 0 !important;
}
</style>