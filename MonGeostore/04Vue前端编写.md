# Vue前端页面

[TOC]

## 前言

- 在样式组件上我们使用了饿了么团队推出的**element-ui**，这是一套专门匹配Vue.js框架的功能样式组件。



## 1.需要的配置

### 安装Element

```
 npm install element-ui
```



### 安装vue-resource

- 要调用后台、数据，需引入vue-resource，此处可使用npm工具，进行安装，

```
npm install vue-resource
```



### 安装打包工具webpack

```
npm install webpack
```



### 安装axios

```
npm install axios
```



## 2.导入项目

在main.js中引入Element、VueResource

![](IMG/微信截图_20200828170826.png)

## 3.编写页面内容Segy.vue

- 在src/views文件夹下新建一个名为Segy.vue的组件，通过调用之前在Django上写好的api，实现添加segy和显示segy数据的功能。

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-08-28 08:36:26
 * @LastEditors: henggao
 * @LastEditTime: 2020-08-28 17:19:32
-->
<template>
  <div class="home">
    <el-row display="margin-top:10px">
      <el-input
        v-model="input"
        placeholder="请输入测线号"
        style="display:inline-table; width: 30%; float:left"
      ></el-input>
      <el-button type="primary" @click="addSegy()" style="float:left; margin: 2px;">新增</el-button>
    </el-row>
    <el-row>
      <el-table :data="segyList" style="width: 100%" border>
        <el-table-column prop="id" label="编号" min-width="100">
          <template slot-scope="scope">{{ scope.row.pk }}</template>
        </el-table-column>
        <el-table-column prop="num_id" label="测线号" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.num_id }}</template>
        </el-table-column>
        <el-table-column prop="x_line" label="x_line" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.x_line }}</template>
        </el-table-column>
        <el-table-column prop="y_line" label="y_line" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.y_line }}</template>
        </el-table-column>
        <el-table-column prop="value" label="value" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.value }}</template>
        </el-table-column>
        <el-table-column prop="author" label="采集人员" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.author }}</template>
        </el-table-column>
        <el-table-column prop="creat_time" label="添加时间" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.create_time }}</template>
        </el-table-column>
        <el-table-column prop="update_time" label="更新时间" min-width="100">
          <template slot-scope="scope">{{ scope.row.fields.update_time }}</template>
        </el-table-column>
      </el-table>
    </el-row>
  </div>
</template>

<script>
export default {
  name: "segy",
  data() {
    return {
      input: "",
      segyList: []
    };
  },
  mounted: function() {
    this.showSegys();
  },
  methods: {
    addSegy() {
      this.$http
        .get("http://127.0.0.1:8000/api/add_segy?num_id=" + this.input)
        .then(response => {
          var res = JSON.parse(response.bodyText);
          if (res.error_num === 0) {
            this.showSegys();
          } else {
            this.$message.error("新增数据失败，请重试");
            console.log(res["msg"]);
          }
        });
    },
    showSegys() {
      this.$http.get("http://127.0.0.1:8000/api/show_segys").then(response => {
        var res = JSON.parse(response.bodyText);
        console.log(res);
        if (res.error_num === 0) {
          this.segyList = res["list"];
        } else {
          this.$message.error("查询数据失败");
          console.log(res["msg"]);
        }
      });
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1,
h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>



```

## 4.运行前端程序

切换到前端目录mongeostore_ui，运行程序，查看浏览器

```
npm run serve
```

- 如果发现列表抓取不到数据，可能是出现了跨域问题，打开浏览器console确认

  ![](IMG/微信截图_20200828171105.png)

- 这时候我们须要在Django层注入header，用Django的第三方包`django-cors-headers`来解决跨域问题：

```
 pip install django-cors-headers
```

- **settings.py 修改：**

  ![](IMG/微信截图_20200828171611.png)

```
'corsheaders.middleware.CorsMiddleware',

CORS_ORIGIN_ALLOW_ALL = True
```

 

- 后端接口记得启动

  ```
  #激活虚拟环境,先切换到目录
  cd mongeostore_env
  
  .\Scripts\activate
  
  python manage.py runserver
  ```

  

- **在前端工程目录下，输入**`npm run serve`**启动node自带的服务器，浏览器会自动打开， 我们能看到页面：**

![](IMG/微信截图_20200828171711.png)

- **新增数据，新增的信息会实时反映到页面的列表中，这得益于Vue.js的数据双向绑定特性。**

- 在前端工程目录下，输入`npm run build`，如果项目没有错误的话，就能够看到所有的组件、css、图片等都被webpack自动打包到dist目录下了：

```
npm run build
```

![](IMG/微信截图_20200828210430.png)