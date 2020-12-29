# vue地图可视化 Cesium篇

[TOC]

## 方法一（未配置成功）

### 一、cesium 安装

```
npm install cesium --save 
```

### 二、配置文件 vue.config.js

在项目根目录新增配置文件 vue.config.js,如下

```

```







四、Hello World!

App.vue 中输入以下代码

```
<template>
  <div id="app">
    <div id="cesiumContainer"></div>
  </div>
</template>

<script>
import Cesium from 'cesium/Cesium'
import 'cesium/Widgets/widgets.css'
export default {
  name: 'App',
  mounted () {
    this.$nextTick(() => {
      const viewer = new Cesium.Viewer('cesiumContainer')
      console.log('viewer: ', viewer)
    })
  }
}
</script>
<style>
html,
body {
  width: 100%;
  height: 100%;
  padding: 0;
  margin: 0;
}
#app,#cesiumContainer {
  font-family: "Avenir", Helvetica, Arial, sans-serif;
  width: 100%;
  height: 100%;
  overflow: hidden;
}
</style>

```

五、运行

```
npm run serve

```

根据官网的说明，浏览器运行结果如下



## 方法二（推荐）

### 一、安装

```
npm install vue-cesium --save
```



### 二、使用

```vue
<template>
  <div class="viewer">
    <vc-viewer>
      <vc-layer-imagery></vc-layer-imagery>
    </vc-viewer>
  </div>
</template>

<script>
import Vue from "vue";
import VueCesium from "vue-cesium";
// VueCesium 默认使用 `https://unpkg.com/cesium/Build/Cesium/Cesium.js`
Vue.use(VueCesium, {
  // cesiumPath 是指引用的Cesium.js路径，如
  // 项目本地的Cesium Build包，vue项目需要将Cesium Build包放static目录：
  // cesiumPath: /static/Cesium/Cesium.js
  // 个人在线Cesium Build包：
  // cesiumPath: 'https://zouyaoji.top/vue-cesium/statics/Cesium/Cesium.js'
  // 个人在线SuperMap Cesium Build包（在官方基础上二次开发出来的）：
  // cesiumPath: 'https://zouyaoji.top/vue-cesium/statics/SuperMapCesium/Cesium.js'
  // 官方在线Cesium Build包，有CDN加速，推荐用这个：
  cesiumPath: "https://unpkg.com/cesium/Build/Cesium/Cesium.js",
  // 指定Cesium.Ion.defaultAccessToken，使用Cesium ion的数据源需要到https://cesium.com/ion/申请一个账户，获取Access Token。不指定的话可能导致 Cesium 在线影像加载不了
  accessToken:
    "你的token",
});
export default {};
</script>

<style>
.viewer {
  width: 100%;
  height: 400px;
}
</style>
```



- [api](https://zouyaoji.top/vue-cesium/#/zh/start/usage)