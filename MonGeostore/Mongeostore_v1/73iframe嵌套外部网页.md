# 嵌套外部网页

[TOC]

## 1. 前言

### 1.1 需求分析

- 有时候项目需要嵌入第三方监控界面，又需要在自己的项目中进行跳转，这时候就需要使用iframe

### 1.2 实现原理

1. 给菜单URL添加嵌套网页前缀，如果是服务端网页，除内部URL外，以iframe:前缀开头，外部网页直接以http[s]完整路径开头。

2. 路由导航守卫在动态加载路由时，检测到如果是外部嵌套网页，则绑定IFrame嵌套组件，最后用IFrame来渲染嵌套页面。

3. 菜单点击跳转的时候，根据路由类型生成不同的路由路径，载入特定的页面内容渲染到步骤二绑定的特定组件上。



## 2. 实现

### 2.1 确定菜单URL

### 2.2 绑定嵌套组件

### 2.3



- [ref](https://cloud.tencent.com/developer/article/1448305)





## 3. 直接使用

```vue
<template>
  <div>
    <iframe
      src="https://echarts.apache.org/examples/en/index.html"
      id="map"
      scrolling="no"
      frameborder="0"
      style="
        position: absolute;
        top: 4px;
        left: 210px;
        right: 0px;
        bottom: 10px;
      "
    ></iframe>
  </div>
</template>
 
 
<script>
export default {
  data() {
    return {};
  },
  mounted() {
    /**
     * iframe-宽高自适应显示
     */
    function changeMapIframe() {
      const map = document.getElementById("map");
      const deviceWidth = document.body.clientWidth;
      const deviceHeight = document.body.clientHeight;
      map.style.width = Number(deviceWidth) - 240 + "px"; //数字是页面布局宽度差值
      map.style.height = Number(deviceHeight) + 764 + "px"; //数字是页面布局高度差
    }

    changeMapIframe();

    window.onresize = function () {
      changeMapIframe();
    };
  },
};
</script>

```





```

```



