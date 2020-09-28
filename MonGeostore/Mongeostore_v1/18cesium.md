# vue地图可视化 Cesium篇

[TOC]

## 一、cesium 安装

```
npm install cesium --save 
```

## 二、配置文件 vue.config.js

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