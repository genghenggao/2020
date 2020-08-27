# Vue

[TOC]

## 一、TabBar

### 1、新建项目

#### 1.1、新建tabbar

```shell
vue init webpack tabbar
```

#### 1.2、删除默认元素

- 删除components文件里的默认HelloWorld.vue

#### 1.3、修改App.vue

```vue
<template>
  <div id="app">
  </div>
</template>

<script>
export default {
  name: 'App',
  components: {
  }
}
</script>

<style>
</style>
```

#### 1.4、添加内容

- App.vue

  ![](IMG/微信截图_20191018145952.png)

#### 1.5、引入样式

1.5.1、在src/assets创建css文件夹、img文件夹。

- 在css中创建base.css,设置一些通用样式。

  ![](IMG/微信截图_20191018150408.png)

1.5.2、引用样式

- 第一种：可以在main.js中引用样式

![](IMG/微信截图_20191018150047.png)

- 第二种：在App.vue中引用样式（（推荐这里引用样式））

  ![](IMG/微信截图_20191018150251.png)

- 设置样式参数

![](IMG/微信截图_20191018150619.png)



#### 1.6、Tabbar组件封装

上述1.5中这种方式没有复用性，可以封装成独立的组件。

##### 1.6.1、抽离组件

在components下新建tabbar/TabBar.vue，将App.vue中设置抽离到TabBar.vue

![](IMG/微信截图_20191018151634.png)

##### 1.6.2、修改App.vue

![](IMG/微信截图_20191018152137.png)

##### 1.6.3、查看

![](IMG/微信截图_20191018152225.png)

##### 1.6.4、TabBarItem组件封装

- 新建src/assets/img/tabbar,放入相应的svg图片（官方网址：http://www.iconfont.cn/ 找到需要的icon ）

- 在components/tabbar新建TabBarItem.vue

  ![](IMG/微信截图_20191018162613.png)

- 修改App.vue

  ![](IMG/微信截图_20191018162743.png)

- 查看

  ![](IMG/微信截图_20191018162843.png)

##### 1.6.5、TabBarItem传入active图片

- 设置TabBarItem.vue

  ![](IMG/微信截图_20191018170007.png)

- 修改App.vue

  ![](IMG/微信截图_20191018170121.png)

##### 1.6.6、TabBarItem和路由结合

- 手动安装router路由，创建项目时没有安装路由，手动安装。

```
 npm install vue-router --save
```

- 新建src/router/index.js

  ```js
  import Vue from 'vue'
  import VueRouter from 'vue-router'
  
  // 1、安装插件
  Vue.use(VueRouter)
  
  // 2、创建路由对象
  const routes =[
  
  ]
  
  const router = new VueRouter({
      routes
  })
  
  // 3、导出router
  export default router
  
  ```

- main.js

  ![](IMG/微信截图_20191018183432.png)

- 在src下新建views文件夹，存放视图。views下新建home、cart、category、cart等文件夹。

  - home文件下新建Home.vue

    ```vue
    <template>
      <h2>首页</h2>
    </template>
    
    <script>
    export default {
    
    }
    </script>
    
    <style>
    
    </style>
    ```

  - cart文件下新建Cart.vue

  - profile文件下新建Profile.vue

  - category文件下新建Category.vue

- 路由配置

  - index.js

  ![](IMG/微信截图_20191018185113.png)

- 监听item点击，跳转

![](IMG/微信截图_20191018190208.png)

- App.vue

  ![](IMG/微信截图_20191018191142.png)

- 查看

![](IMG/微信截图_20191018191220.png)

##### 1.6.7、TabBarItem和颜色动态控制

- 通过计算属性设置判断活跃状态

- TabBarItem.vue

  ![](IMG/微信截图_20191018192256.png)

- 查看

  ![](IMG/微信截图_20191018192330.png)

- 动态决定颜色

  - 修改TabBarItem.vue

  ![](IMG/微信截图_20191018200311.png)

  ![](IMG/微信截图_20191018200435.png)

  ![](IMG/微信截图_20191018200506.png)

  - 完整的TabBarItem.vue

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-18 15:52:25
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-18 19:57:22
 -->
<template>
  <div class="tab-bar-item" @click="itemClick">
    <!-- 使用具名插槽，动态设置内容 -->
    <div v-if="!isActive">
      <slot name="item-icon"></slot>
    </div>
    <div v-else>
      <slot name="item-icon-active"></slot>
    </div>
    <!-- <div :class="{active:isActive}">
      <div>
        <slot name="item-text"></slot>
      </div>
    </div>-->
    <!-- 动态绑定样式 -->
    <div :style="activeStyle">
      <div>
        <slot name="item-text"></slot>
      </div>
    </div>
    <!-- <img src="../../assets/img/tabbar/like_filled.svg" alt />
    <div>首页</div>-->
  </div>
</template>

<script>
export default {
  name: "TabBarItem",
  props: {
    path: String,
    activeColor: {
      type: String,
      default: "#d4237a"
    }
  },
  data() {
    return {
      // isActive: true
    };
  },
  computed: {
    isActive() {
      //  /home ->item1(/home) =true
      //  /home ->item1(/category) = false
      //  /home ->item1(/cart) = false
      //  /home ->item1(/profile) = false
      // indexOf =-1找到了true;  ！=-1没找到为false
      return this.$route.path.indexOf(this.path) !== -1;
    },
    activeStyle() {
      return this.isActive ? { color: this.activeColor } : {};
    }
  },
  methods: {
    itemClick() {
      // console.log('itemClick');
      this.$router.push(this.path);
    }
  }
};
</script>

<style>
.tab-bar-item {
  /* 均等分 */
  flex: 1;
  /* 据中 */
  text-align: center;
  /* tab-bar高度设置 */
  height: 49px;
  /* 文字大小 */
  font-size: 14px;
}
.tab-bar-item img {
  width: 24px;
  height: 24px;
  /* svg图片上边距 */
  margin-top: 3px;
  /* 去掉图片与文字距离默认3个像素 */
  vertical-align: middle;
  /* 图片与文字之间设置2个像素 */
  margin-bottom: 2px;
}

/* .active {
  color: #d4237a;
} */
</style>
```

- 查看

  ![](IMG/微信截图_20191018200623.png)

这样就封装好了，可以在App.vue中通过`activeColor`任意自定义字体颜色。

![](IMG/微信截图_20191018200824.png)

![](IMG/微信截图_20191018200748.png)

##### 1.6.8、对App.vue进行抽取

- 在components下新建MainTabBar.vue,注意一下修改对应路径

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-18 20:12:52
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-18 20:22:17
 -->
<template>
  <tab-bar>
    <tab-bar-item path="/home" activeColor="blue">
      <img slot="item-icon" src="../assets/img/tabbar/home.svg" alt />
      <img slot="item-icon-active" src="../assets/img/tabbar/home_active.svg" alt />
      <div slot="item-text">首页</div>
    </tab-bar-item>
    <tab-bar-item path="/category">
      <img slot="item-icon" src="../assets/img/tabbar/categories.svg" alt />
      <img slot="item-icon-active" src="../assets/img/tabbar//categories_active.svg" alt />
      <div slot="item-text">分类</div>
    </tab-bar-item>
    <tab-bar-item path="/cart">
      <img slot="item-icon" src="../assets/img/tabbar/shopcart.svg" alt />
      <img slot="item-icon-active" src="../assets/img/tabbar/shopcart_active.svg" alt />
      <div slot="item-text">购物车</div>
    </tab-bar-item>
    <tab-bar-item path="/profile">
      <img slot="item-icon" src="../assets/img/tabbar/profile.svg" alt />
      <img slot="item-icon-active" src="../assets/img/tabbar/profile_active.svg" alt />
      <div slot="item-text">我的</div>
    </tab-bar-item>
  </tab-bar>
</template>

<script>
// 1.导入组建
import TabBar from "./tabbar/TabBar";
import TabBarItem from "./tabbar/TabBarItem";
export default {
  name: "MainTabBar",
  components: {
    // 2.注册组件
    TabBar,
    TabBarItem
  }
};
</script>

<style>
</style>
```

- App.vue

  ```vue
  <!--
   * @Description: henggao_learning
   * @version: v1.0.0
   * @Author: henggao
   * @Date: 2019-10-18 14:22:29
   * @LastEditors: henggao
   * @LastEditTime: 2019-10-18 20:15:50
   -->
  <template>
    <div id="app">
      <!-- 3.使用组件 -->
      <router-view></router-view>
      <main-tab-bar></main-tab-bar>
    </div>
  </template>
  
  <script>
  import MainTabBar from "./components/MainTabBar";
  
  export default {
    name: "App",
    components: {
      MainTabBar
    }
  };
  </script>
  
  <style>
  /* 引用样式 */
  @import "./assets/css/base.css";
  </style>
  
  ```

查看即可。

##### 1.6.9、文件路径别名

![](IMG/微信截图_20191019081220.png)

- 对于文件路径使用`../xxx/xxx`这种模式可能会出现路径错误，在build/webpack.base.conf.js进行路径别名设置。

![](IMG/微信截图_20191019081505.png)

- 在文件中引用路径，@对应src路径
  - src时，需要使用`~/xxx/xxx`
  - import时，需要使用`@/xxx/xxx`

![](IMG/微信截图_20191019082103.png)

