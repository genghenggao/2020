# 登录页面开发

[TOC]

## 一、前后端结合

- 在开发的时候，前端用前端的服务器（Nginx），后端用后端的服务器（Tomcat），开发前端内容的时候，可以把前端的请求通过前端服务器转发给后端（称为反向代理），这样就能实时观察结果，并且不需要知道后端怎么实现，而只需要知道接口提供的功能，两边的开发人员（两个我）就可以各司其职啦。

## 二、前端页面

在views下新建Login.vue

- **Login.vue**

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-11-28 14:35:59
 * @LastEditors: henggao
 * @LastEditTime: 2019-11-29 19:26:25
 -->
<template>
  <div>
    用户名:
    <input type="text" v-model="loginForm.username" placeholder="请输入用户名" />
    <br />
    <br />密码：
    <input type="password" v-model="loginForm.password" placeholder="请输入密码" />
    <br />
    <br />
    <button v-on:click="login">登录</button>
  </div>
</template>

<script>
export default {
  name: "Login",
  data() {
    return {
      loginForm: {
        username: "",
        password: ""
      },
      responseResult: []
    };
  },
  methods: {
    login() {
      this.$axios
        .post("/login", {
          username: this.loginForm.username,
          password: this.loginForm.password
        })
        .then(successResponse => {
          if (successResponse.data.code === 200) {
            this.$router.replace({ path: "/index" });
          }
        })
        .catch(failResponse => {});
    }
  }
};
</script>

```



## 附录

- 项目目录结构

```
│  .browserslistrc
│  .eslintrc.js
│  .gitignore
│  babel.config.js
│  package-lock.json
│  package.json						npm包配置文件，定义了项目的npm脚本，依赖包等信息
│  README.md						项目说明
│  tree.txt
│  vue.config.js					 项目配置
│  
├─public
│      favicon.ico					网站图标
│      index.html					入口页面
│      
└─src
    │  App.vue						根组件
    │  main.js						入口js文件
    │  
    ├─assets						资源目录，这里的资源会被wabpack构建
    │  ├─css
    │  └─img
    │          logo.png
    │          
    ├─components					公共组件目录
    │  │  HelloWorld.vue
    │  │  Login.vue
    │  │  
    │  └─home
    │          AppIndex.vue
    │          
    ├─router						前端路由
    │      index.js
    │      
    ├─store							应用级数据（state）
    │      index.js
    │      
    └─views							页面目录
            About.vue
            Home.vue
            Mongeostore.vue
            
```



参考：https://learner.blog.csdn.net/article/details/88925013

