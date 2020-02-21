<template>
  <div style="position:fixed">
    <aside class="box" ref="test">
      <button id="btn" v-on:click="adjustArea">三</button>
      <ul>
        <li style="margin:10px auto">
          <h1 style="color:#42b983">Highestpeak</h1>
        </li>
        <li v-for="(item,index) in menu" :key="index">
          <router-link :to="item.link">{{item.name}}</router-link>
        </li>
      </ul>
    </aside>
  </div>
</template>

<script>
export default {
  name: "Aside",
  props: {
    msg: String
  },
  data(){
      return{
        menu:[
            {"link":"/","name":"HOME"},
            {"link":"/tags","name":"TAGS"},
            {"link":"/repos","name":"REPOS"},
            {"link":"/timeline","name":"TIME LINE"},
            {"link":"/about","name":"ABOUT"},
        ],
      }
  },
  methods:{
    adjustArea(){
        var box=this.$refs.test;
        if (box.offsetLeft == 0) {
            box.style['margin-left'] = -200 + "px"
            this.$emit('adjustContent', "0px")
        } else {
            box.style['margin-left'] = 0 + "px"
            this.$emit('adjustContent', "200px")
        }
    },
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
* {
  margin: 0;
  padding: 0;
}

#btn {
  position: absolute;
  top: 0px;;
  left: 200px;
  width: 50px;
  height: 50px;
  border: 0;
  border-left: 1px solid rgb(23, 32, 43, 0.2);
  background: #61d4b3;
  color: #fff;
  cursor: pointer;
}

.box {
  float: left;
  position: relative;
  left: 0;
  height: 1000px;
  width: 200px;
  margin-left: 0;
  display: block;
  background-color: rgba(255,255,255,0.98);
  border-right: 2px solid #e5e5e5;
  -moz-transition: margin-left 2s;
  transition: margin-left 0.5s;
}

aside ul li {
  height: 40px;
  line-height: 40px;
  border-top: 1px solid #fff;
  border-bottom: 1px solid #fff;
  list-style-type: none;
  text-align: center;
}

aside ul li a {
  width: 100%;
  height: 100%;
  text-decoration-line: none;
  color: #959595 !important;
  display: block;
}

aside ul li a:hover {
  color: #000 !important;
  text-decoration: underline !important;
  text-decoration-color: brown !important;
  text-decoration-skip: 10px;
  border-bottom: none !important;
}
</style>
