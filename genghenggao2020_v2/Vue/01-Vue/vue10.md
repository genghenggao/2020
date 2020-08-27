# Vue

[TOC]

## 一、Vuex

Vuex专门Vue.js应用程序开发的状态管理模式

Vuex放置一些共享

token：令牌

#### 1、安装Vuex

```shell
npm install vuex --save
```

#### 2、Vuex-devtools和mutations

##### 2.1、在components新建HelloVuex.vue

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-21 08:49:55
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-21 09:04:48
 -->
<template>
  <div>
      <!-- <h2>{{counter}}</h2> -->
      <h2>{{$store.state.counter}}</h2>
  </div>
</template>

<script>
export default {
    name:'HelloVuex',
}
</script>

<style>

</style>
```

##### 2.2、在src下新建store文件夹，新建index.js，用来设置vuex

```js
import Vue from 'vue'
import Vuex from 'vuex'

// 1.安装插件
Vue.use(Vuex)

// 2.创建对象
const store = new Vuex.Store({
    state:{
        counter:1000
    },
    mutations:{

    },
    actions:{

    },
    getters:{

    },
    modules:{
        
    }
})

// 3.导出store
export default store
```

##### 2.3、在main.js挂载

![](IMG/微信截图_20191021091054.png)

##### 2.4、在Chrome中安装deltools插件



![](IMG/微信截图_20191021094506.png)

![](IMG/微信截图_20191021094649.png)

##### 2.5、修改案例

###### 2.5.1、src/tore/1index.js

![](IMG/微信截图_20191021095847.png)

###### 2.5.2、src/APP.vue

![](IMG/微信截图_20191021100001.png)

###### 2.5.3、运行查看

![](IMG/微信截图_20191021100108.png)

### 3、Vuex核心概念

- State
  - Single Source of Truth 单一状态树（单一数据源）
- Getters
- Mutations
- Action
- Module

#### 3.1、getters

##### 3.1.1、getters的使用

- index.js

```js
/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-21 08:57:37
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-21 10:36:48
 */
import Vue from 'vue'
import Vuex from 'vuex'

// 1.安装插件
Vue.use(Vuex)

// 2.创建对象
const store = new Vuex.Store({
    state: {
        counter: 1000,
        students: [
            {
                id: 110,
                name: 'James',
                age: 23
            },
            {
                id: 111,
                name: 'Kobe',
                age: 24
            },
            {
                id: 112,
                name: "Curry",
                age: 30
            }
        ]
    },
    mutations: {
        // 方法
        increment(state) {
            state.counter++
        },
        decrement(state) {
            state.counter--
        }
    },
    actions: {

    },
    getters: {
        powerCounter(state) {
            return state.counter * state.counter
        },
        more20stu(state) {
            return state.students.filter(s => s.age > 24)
        }
    },
    modules: {

    }
})

// 3.导出store
export default store
```

- App.vue

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-21 08:35:25
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-21 10:37:31
 -->
<template>
  <div id="app">
    <h2>{{message}}</h2>
    <!-- <h2>{{counter}}</h2> -->
    <h2>{{$store.state.counter}}</h2>
    <!-- <button @click="counter++">+</button>
    <button @click="counter--">-</button>-->
    <button @click="addition">+</button>
    <button @click="subtraction">-</button>
    <h2>---App内容：getters相关信息---</h2>i
    <h2>{{$store.getters.powerCounter}}</h2>
    <h2>{{$store.getters.more20stu}}</h2>
    <h2>---HelloVuex内容---</h2>
    <hello-vuex :counter="counter"></hello-vuex>
  </div>
</template>

<script>
import HelloVuex from "./components/HelloVuex";

export default {
  name: "App",
  components: {
    HelloVuex
  },
  data() {
    return {
      message: "我是APP组件",
      counter: 0
    };
  },
  methods: {
    addition() {
      this.$store.commit("increment");
    },
    subtraction() {
      this.$store.commit("decrement");
    }
  }
};
</script>

<style>
</style>

```

- HelloVuex.vue

  ```vue
  <!--
   * @Description: henggao_learning
   * @version: v1.0.0
   * @Author: henggao
   * @Date: 2019-10-21 08:49:55
   * @LastEditors: henggao
   * @LastEditTime: 2019-10-21 10:37:42
   -->
  <template>
    <div>
      <!-- <h2>{{counter}}</h2> -->
      <h2>{{$store.state.counter}}</h2>
      <h2>{{$store.getters.powerCounter}}</h2>
      <h2>{{$store.getters.more20stu}}</h2>
    </div>
  </template>
  
  <script>
  export default {
    name: "HelloVuex"
  };
  </script>
  
  <style>
  </style>
  ```

- 查看

  ![](IMG/微信截图_20191021103827.png)

##### 3.1.2、动态获取

在index.js中中设置getters方法

- index.js

![](IMG/微信截图_20191021133949.png)

动态设置参数

- HelloVuex..vue

  ![](IMG/微信截图_20191021134031.png)

查看

![](IMG/微信截图_20191021134649.png)

#### 3.2、Mutation

Mutation方法必须是同步的。

##### 3.2.1、Mutationc传入参数

- App.vue

  ![](IMG/微信截图_20191021135632.png)

- index.js

  ![](IMG/微信截图_20191021135715.png)

##### 3.2.2、payload：负载

- App.vue

![](IMG/微信截图_20191021141241.png)

- index.js

  ![](IMG/微信截图_20191021141336.png)

查看

![](IMG/微信截图_20191021141450.png)



##### 3.2.3、提交风格

- App.vue

  ![](IMG/微信截图_20191021142316.png)

- index.js

  ![](IMG/微信截图_20191021142417.png)

##### 3.2.4、响应式

Vuex中store时响应式的

- App.vue

![](IMG/微信截图_20191021164325.png)

- index.js

  ![](IMG/微信截图_20191021164401.png)

点击修改信息按钮，查看。

![](IMG/微信截图_20191021164505.png)

响应式

![](IMG/微信截图_20191021165909.png)

查看

![](IMG/微信截图_20191021170004.png)



##### 3.2.5、类型常量

- 新建src/store/mutations-type.js

  ![](IMG/微信截图_20191021171150.png)

- App.vue

![](IMG/微信截图_20191021171106.png)

- index.js

  ![](IMG/微信截图_20191021171240.png)

查看

#### 3.3、action

- action异步操作

##### 3.3.1、action的使用(一)

- index.js

![](IMG/微信截图_20191021210748.png)

- App.vue

  ![](IMG/微信截图_20191021210911.png)

- 查看

  ![](IMG/微信截图_20191021210955.png)

##### 3.3.1、action的使用(二)

- index.js

  ![](IMG/微信截图_20191021212720.png)

- App.vue

  ![](IMG/微信截图_20191021212702.png)

- 查看

  ![](IMG/微信截图_20191021212754.png)



#### 3.4、modules

##### 3.4.1、modules的使用(一)

- index.js

  ![](IMG/微信截图_20191021214449.png)

- App.vue

  ![](IMG/微信截图_20191021214527.png)

  ![](IMG/微信截图_20191021214602.png)

##### 3.4.2、modules的使用(二)

- App.vue

  ![](IMG/微信截图_20191021215348.png)

- index.js

  ![](IMG/微信截图_20191021215420.png)

- 查看

  ![](IMG/微信截图_20191021215445.png)

##### 3.4.3、modules的使用(三)

- index.js

  ![](IMG/微信截图_20191021220125.png)

- App.vue

  ![](IMG/微信截图_20191021220216.png)

  ![](IMG/微信截图_20191021220235.png)

- 查看

  ![](IMG/微信截图_20191021220303.png)



### 4、Store文件夹的目录结构

- store
  - index.js    # 组装模块并导出store的地方
  - action.js    #根级别的action
  - mutations.js    #根级别的的mutation
  - modules
    - cart.js    #购物车
    - production.js   #产品模块	

#### 4.1、index.js进行抽取

对上述的store/index.js进行抽取，对index.js备份index_copy.js以便于比较

在store文件夹下分别新建mutations.js、actions.js、getters.js、modules/moduleA.js

- mutations.js

  ```js
  import { INCREMENT } from './mutations-type'
  export default {
      // 方法
      // increment(state) {
      //     state.counter++
      // },
      [INCREMENT](state) {
          state.counter++
      },
      decrement(state) {
          state.counter--
      },
      incrementCount(state, payload) {
          // console.log(count);
          // state.counter += count
          state.counter += payload.count
      },
      addStudent(state, stu) {
          state.students.push(stu)
      },
      updateInfo(state) {
          state.info.name = 'henggao'
  
          // state.info['address'] = '洛杉矶'  //该方式做不到响应式
          // Vue.set(state.info,'address','洛杉矶')
          // delete state.info.info.age //该方式做不到响应式
          // Vue.delete(state.info, 'age')
      }
  }
  ```

  

- actions.js

  ```js
  export default{
      // context：上下文
      // aUpdateInfo(context, payload) {
      //     setTimeout(() => {
      //         context.commit('updateInfo')
      //         console.log(payload.message);
      //         payload.success()
      //     }, 1000)
      // }
      aUpdateInfo(context, payload) {
          return new Promise((reslove, reject) => {
              setTimeout(() => {
                  context.commit('updateInfo')
                  console.log(payload);
                  reslove('1111111')
              }, 1000)
          })
      }
  }
  ```

  

- getters.js

  ```js
  export default {
      powerCounter(state) {
          return state.counter * state.counter
      },
      more20stu(state) {
          return state.students.filter(s => s.age > 24)
      },
      more20stuLength(state, getters) {
          return getters.more20stu.length
      },
      moreAgeStu(state) {
          // return function(age){
          //     return state.student.filter(s => s.age >age )
          // }
          return age => {
              return state.students.filter(s => s.age > age)
          }
      }
  }
  ```

  

- modules/moduleA.js

  ```js
  export default {
      state: {
          name: 'henggao'
      },
      mutations: {
          updateName(state, payload) {
              state.name = payload
          }
      },
      actions: {
          aUpdateName(context) {
              setTimeout(() => {
                  context.commit('updateName', 'James')
              }, 1000);
          }
      },
      getters: {
          fullName(state) {
              return state.name + '11111'
          },
          fullName2(state, getters) {
              return getters.fullName + '2222'
          },
          fullName3(state, getters, rooState) {
              return getters.fullName2 + rooState.counter
          }
      }
  }
  ```

  

- index.js

  ```js
  import Vue from 'vue'
  import Vuex from 'vuex'
  import mutations from './mutations'
  import actions from './actions'
  import getters from './getters'
  import moduleA from './modules/moduleA'
  // 1.安装插件
  Vue.use(Vuex)
  
  // 2.创建对象
  const state = {
      counter: 1000,
      students: [
          {
              id: 110, name: 'James', age: 23
          },
          {
              id: 111, name: 'Kobe', age: 24
          },
          {
              id: 112, name: "Curry", age: 30
          }
      ],
      info: {
          name: 'Kobe',
          age: 40,
          height: 1.98
      }
  }
  const store = new Vuex.Store({
      state,
      mutations,
      actions,
      getters,
      modules: {
          a: moduleA
      }
  })
  
  // 3.导出store
  export default store
  
  
  // 对象的结构
  const obj = {
      name: 'Wade',
      age: 18,
      height: 1.96
  }
  
  const { name, age, height } = obj
  console.log(obj);
  ```

  运行查看

