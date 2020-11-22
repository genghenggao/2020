百度API使用



## 1、申请AK

访问：https://lbsyun.baidu.com/apiconsole/key#/home

![](IMG/微信截图_20201006171422.png)



选择使用了类型。我这里使用的式浏览器，按提示申请即可。

![](IMG/微信截图_20201006171550.png)

## 2、通过模块化引入的方法

参考：https://github.com/Dafrok/vue-baidu-map

### 2.1 安装

```
npm i vue-baidu-map --save
```

### 2.2 初始化

在main.js中添加配置

```
import Vue from 'vue'
import BaiduMap from 'vue-baidu-map'

Vue.use(BaiduMap, {
  /* Visit http://lbsyun.baidu.com/apiconsole/key for details about app key. */
  ak: 'YOUR_APP_KEY'
})
```

### 2.3 使用

新建一个MapView.vue，测试。

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-06 17:05:32
 * @LastEditors: henggao
 * @LastEditTime: 2020-10-06 18:45:25
-->
<template>
  <div>
    <el-card class="card-back-color card1">
      <div class="baidu-title">
        <h4>百度地图API</h4>
      </div>
      <baidu-map :center="center" :zoom="zoom" @ready="handler" class="map">
        <bm-scale anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-scale>
        <bm-navigation anchor="BMAP_ANCHOR_TOP_RIGHT"></bm-navigation>
        <bm-map-type
          :map-types="['BMAP_NORMAL_MAP', 'BMAP_HYBRID_MAP']"
          anchor="BMAP_ANCHOR_TOP_LEFT"
        ></bm-map-type>
      </baidu-map>
    </el-card>
  </div>
</template>

<script>
export default {
  name: "mapview",
  data() {
    return {
      center: { lng: 0, lat: 0 },
      zoom: 3
    };
  },

  mounted() {
    this.addPoints();
  },
  methods: {
    handler({ BMap, map }) {
      map.enableScrollWheelZoom(true); //开启鼠标滚轮缩放
      console.log(BMap, map);
      this.center.lng = 121.62;
      this.center.lat = 38.92;
      this.zoom = 11.5;
    }
  }
};
</script>

<style>
/* The container of BaiduMap must be set width & height. */
.map {
  width: 100%;
  height: 500px;
}
</style>

```

![](IMG/微信截图_20201006215022.png)





官方文档功能很全：https://dafrok.github.io/vue-baidu-map/#/zh/start/installation