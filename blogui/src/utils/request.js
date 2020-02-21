import axios from "axios";
// import qs from "qs";
import {
    articleListApi,
    articleNumApi,
    articleApi,
    tagListApi,
    repoListApi,
    timeLineApi,
    starSendApi,
    settingApi,
} from "@/api"

async function getArticleNum() {
    var num=0;
    await axios.get(articleNumApi)
    .then(response => {
        var data=response.data;
        num=parseInt(data.total,10)
    }).catch(error => {
        console.log(error)
    });
    return num;
}// getArticleList

async function getArticleList(currPage,num,requirement) {
    var page = {
        articleTotal:null,
        pageSize:null,
        articleList:null,
    };
    var start = (currPage-1)*num;
    await axios.get(articleListApi,{
        params:{
            'start':start,
            'num':num,
            'requirement':requirement,
        },
    })
    .then(response => {
        var data=response.data;
        page.articleTotal=data['total'];
        page.pageSize=data['per_page'];
        page.articleList=data['list'];
    }).catch(error => {
        console.log(error)
    });
    return page;
}// getArticleList

async function getArticle(id) {
    var page = {
        articleTitle:null,
        articleDate:null,
        articleContent:null,
        articleStars:null,
        articleTag:null,
    };
    await axios.get(articleApi,{
        params:{
            'id':id,
        },
    })
    .then(response => {
        var data=response.data;
        page.articleTitle=data['articleTitle'];
        page.articleDate=data['articleDate'];
        page.articleContent=data['articleContent'];
        page.articleStars=data['articleStars'];
        page.articleTag=data['articleTag'];
    }).catch(error => {
        console.log(error)
    });
    return page;
}//getArticle

async function getArticleContent(url){
    var content="";
    await axios.get(url)
    .then(response => {
        var data=response.data;
        content=decodeURIComponent(escape(window.atob(data.content)));
    }).catch(error => {
        console.log(error)
    });
    return content;
}

async function getTagList(){
    var tagList = [];
    await axios.get(tagListApi)
    .then(response => {
        var data = response.data;
        for (let index = 0; index < data.length; index++) {
            const element = data[index];
            tagList.push([
                element['name'],
                element['list']
            ]);
        }
    })
    .catch(error => {
        console.log(error);
    });
    return tagList;
}// getTagList

async function getAllReposURL(){
    var page = {
        repoApiList:[],
        repoDetailList:[],
    };
    // 请求被展示的repo url列表
    await axios.get(repoListApi)
        .then(response => {
            var data = response.data;
            for (let index = 0; index < data.length; index++) {
                const element = data[index];
                page.repoApiList.push(element['repoURL']);
            }
        })
        .catch(error => {
            console.log(error);
        });
    for (let index = 0; index < page.repoApiList.length; index++){
        page.repoDetailList.push({
            'repoName':'',
            'repoURL':'',
            'stars':'',
            'forks':'',
            'description':'',
            "loading":true
        })
    }
    return page;
}// getAllReposURL

// use github api to finish
function getAllReposDetail(repoURLList,repoDetailList){
    for (let index = 0; index < repoURLList.length; index++) {
        const repoURL = repoURLList[index];
        axios.get(repoURL)
        .then(response => {
            var data = response.data;
            repoDetailList[index]['repoName']=data['name'];
            repoDetailList[index]['repoURL']=data['html_url'];
            repoDetailList[index]['stars']=data['stargazers_count'];
            repoDetailList[index]['forks']=data['forks_count'];
            repoDetailList[index]['description']=data['description'];
            repoDetailList[index]["loading"]=false;
        })
        .catch(error => {
            console.log(error);
        });
    }// 请求repo
}//getAllReposDetail

async function timeLineGet(){
    var activities = [];
    // 请求被展示的repo url列表
    await axios.get(timeLineApi)
        .then(response => {
            var data = response.data;
            for (let index = 0; index < data.length; index++) {
                const element = data[index];
                var activity={
                    section:"",
                    list:[],
                }
                activity.section = element.section;
                for (let iter = 0; iter < element.list.length; iter++) {
                    const item = element.list[iter];
                    activity.list.push({
                        title:item.title,
                        id:item.id,
                        date:item.date,
                    })
                }
                activities.push(activity);
            }
        })
        .catch(error => {
            console.log(error);
        });
    return activities;
}

function sendStar(id,value){
    if(localStorage.getItem("~blog"+id+"-star-set~")){
        return;
    }
    axios.put(starSendApi,{
     
            'id':id,
            'star':value,

    })
    .then(response => {
        return response;
    })
    .catch(error => {
        console.log(error);
        return error;
    });
}

async function getSetting(){
    var settings = {};
    // 请求被展示的repo url列表
    await axios.get(settingApi)
        .then(response => {
            var data = response.data;
            settings = data;
        })
        .catch(error => {
            console.log(error);
        });
    return settings;
}

export{
    getArticleList,
    getArticleNum,
    getArticle,
    getTagList,
    getAllReposURL,
    getAllReposDetail,
    timeLineGet,
    sendStar,
    getArticleContent,
    getSetting
}