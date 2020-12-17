# Segy数据

[TOC]

## 准备

- segyio
- mongoengine



## 一、数据读取

- 读取道到的数据时numpy.ndarray，需要转换为list

```python
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import FloatField, IntField, ListField, PointField, StringField
from mongoengine import *
from mongoengine.context_managers import switch_collection, switch_db

connect(alias='drill_system', db='钻孔数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='rs_system', db='遥感数据管理子系统', host='192.168.55.110', port=20000)


class SegyData(Document):
    name = StringField(required=True, max_length=200)
    age = IntField(required=True)
    location = ListField()
    meta = {'db_alias': 'rs_system'}


with switch_collection(SegyData, 'group2000') as SegyData:
    # Users(name='hello Group 2000 collection!').save()  # 将数据保存至 group2000 集合
    # Users(name='Ross').save()  # ===》 这时会将数据保存至 'archive-user-db'

    import segyio
    content = ".\mongeostore_env\mytest\LX_SEGY2.segy"
    with segyio.open(content, mode="r", strict=False, ignore_geometry=False, endian='big') as f:
        datatest = f.trace[0]  #拿到segy中数据
        datatest1 = f.trace[1]  #拿到segy中数据
        datalist = datatest.tolist() #将<class 'numpy.ndarray'>转为list
        datalist1 = datatest1.tolist() #将<class 'numpy.ndarray'>转为list

        user1 = SegyData(
            name='segy1',
            age=2001,
            location=[datalist,datalist1]
        )
        user1.save()
        print(user1.name)
        print(user1.location)
    # user1.name = 'zz11'
    # user1.save()
    # print(user1.name)
```



## 二、创建应用

### 1、虚拟目录下创建应用

```
python manage.py startapp mongeostore_seismic
```

### 2、settings.py

```
INSTALLED_APPS = [
	"mongeostore_seismic",
]
```

### 3、新建urls.py

- 3.1、新建mongoestore_seismic/urls.py

- 3.2、在工程目录mongeostore_v1/urls.py下注册

![](IMG/微信截图_20201216212949.png)



### 4、新建serializers.py

- 用于序列化



### 5、实例——地震数据上传

- 地震数据上传文件(mongoengine方式，对比一下pymongo方式，查看40、41小节)

#### 5.1 地震元数据上传

##### 5.1.0 SeisUpload.vue

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-16 22:18:57
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-17 22:09:03
-->
<template>
  <el-row :gutter="20">
    <el-col :span="10" :offset="6">
      <el-container style="min-width: 600px; overflow: hidden">
        <el-header><h2>地震元数据上传</h2></el-header>
        <el-main>
          <el-form
            ref="form"
            :model="form"
            label-width="100px"
            class="drillmetaupload"
          >
            <el-scrollbar style="height: 650px">
              <el-form-item label="文件名称">
                <el-input
                  v-model="form.seismic_filename"
                  placeholder="LX_SEGY001"
                ></el-input>
              </el-form-item>
              <el-form-item label="研究区域">
                <el-input
                  v-model="form.location"
                  placeholder="【吉林蛟河】"
                ></el-input>
              </el-form-item>

              <el-form-item label="项目名称">
                <el-input
                  v-model="form.project_name"
                  placeholder="【吉林蛟河】乌林精查补充地质报告及乌林水文地质"
                ></el-input>
              </el-form-item>
              <el-form-item label="单位名称">
                <el-input
                  v-model="form.company_name"
                  placeholder="中国矿业大学（北京）"
                ></el-input>
              </el-form-item>
              <el-form-item label="上传人员">
                <el-input
                  v-model="form.uploader"
                  placeholder="采集员"
                ></el-input>
              </el-form-item>
              <el-form-item label="上传时间">
                <el-date-picker
                  type="date"
                  placeholder="选择日期"
                  v-model="form.seismic_upload_date"
                  style="width: 100%"
                ></el-date-picker
              ></el-form-item>

              <el-form-item label="源文件">
                <el-row>
                  <el-button ref="VideoChose" id="VideoChose" size="medium "
                    >选择文件</el-button
                  >
                </el-row>
                <el-card style="margin-top: 20px">
                  <el-table :data="fileList" style="width: 100%">
                    <!-- <el-table-column prop="id" label="文件id"></el-table-column> -->
                    <el-table-column
                      prop="name"
                      label="文件名称"
                    ></el-table-column>
                    <el-table-column
                      prop="type"
                      label="文件类型"
                    ></el-table-column>
                    <el-table-column
                      prop="size"
                      label="文件大小"
                      v-slot="{ row }"
                    >
                      {{ row.size }}MB
                    </el-table-column>
                    <el-table-column label="进度" v-slot="{ row }">
                      <el-progress
                        :text-inside="true"
                        :stroke-width="16"
                        :percentage="row.percentage"
                      ></el-progress>
                    </el-table-column>
                    <el-table-column label="取消上传" v-slot="{ row }">
                      <el-button
                        type="danger"
                        icon="el-icon-delete"
                        size="mini"
                        circle
                        @click="removeFile(row.id)"
                      ></el-button>
                    </el-table-column>
                    <el-table-column label="上传状态" v-slot="{ row }">
                      <el-link
                        :type="
                          row.loadType == 0
                            ? 'info'
                            : row.loadType == 1
                            ? 'warning'
                            : row.loadType == 2
                            ? 'success'
                            : 'danger'
                        "
                        :underline="false"
                        >{{
                          row.loadType == 0
                            ? "等待上传"
                            : row.loadType == 1
                            ? "正在上传"
                            : row.loadType == 2
                            ? "上传成功"
                            : "上传失败"
                        }}</el-link
                      >
                    </el-table-column>
                  </el-table>
                </el-card>
              </el-form-item>
              <el-form-item>
                <el-button
                  ref="VideoChose"
                  type="primary"
                  size="medium  "
                  @click="onSubmit"
                  >提交</el-button
                >
                <el-button>取消</el-button>
              </el-form-item>
            </el-scrollbar>
          </el-form>
        </el-main>
      </el-container>
    </el-col>
  </el-row>
</template>

<script>
import plupload from "plupload";
import axios from "axios";
import { stringify } from "qs";
export default {
  name: "SeismicMetaUpload",
  data() {
    return {
      form: {
        seismic_filename: "",
        location: "",
        company_name: "",
        uploader: "",
        depth: "",
        project_name: "",
        seismic_upload_date: "",
      },
      show: false,
      fileList: [],
      fileOptions: {
        browse_button: "VideoChose",
        // url: "http://127.0.0.1:8000/load/uploadfile/",
        url: "http://127.0.0.1:8000/seismic/seismicinfo/",
        flash_swf_url: "script/Moxie.swf",
        silverlight_xap_url: "script/Moxie.xap",
        // chunk_size: "10mb", //分块大小  ,注销掉或者改chunk_size：'0mb'为解决文件大于10M存为blob问题
        max_retries: 3,
        unique_names: true,
        multi_selection: false, //是否允许选择多文件
        views: {
          list: true,
          thumbs: true, // Show thumbs
          active: "thumbs",
        },
        filters: {
          mime_types: [
            //文件格式
            {
              title: "files",
              extensions:
                // "png,jpg,svg,mp4,rmvb,mpg,mxf,avi,mpeg,wmv,flv,mov,ts,docx,doc,pdf,segy,xls,xlsx,csv", //文件格式
                "segy,sgy",
            },
          ],
          max_file_size: "10240mb", //最大上传的文件
          prevent_duplicates: true, //不允许选取重复文件
        },
        multipart_params: {
          uuid: "", //参数
          // testparams: "Must can see me",
          // "testparams2": "Must can see me2"
        },
      },
    };
  },

  mounted() {
    //实例化一个plupload上传对象
    this.uploader.init();
    //绑定进队列
    this.uploader.bind("FilesAdded", this.FilesAdded);
    //绑定进度
    this.uploader.bind("UploadProgress", this.UploadProgress);
    //上传之前
    this.uploader.bind("BeforeUpload", this.BeforeUpload);
    //上传成功监听
    this.uploader.bind("FileUploaded", this.FileUploaded);
    //获取uuid
    // let url = `http://127.0.0.1:8000/api/uploadinfo/`;
    let url = `http://127.0.0.1:8000/seismic/seismicinfo/`;
    axios.get(url).then(({ data }) => {
      this.fileOptions.multipart_params.uuid = data;
    });
  },
  computed: {
    //实例化一个plupload上传对象
    uploader() {
      return new plupload.Uploader(this.fileOptions);
    },
  },
  methods: {
    //绑定进队列
    FilesAdded(uploader, files) {
      console.log(this.form);
      let data = this.form;
      if (files[0].name.length > 25) {
        // $.messager.show("提示", "文件名称太长！", "info");
        this.$message({
          type: "error",
          message: "文件名称太长！",
        });
        return;
      }
      if (uploader.files.length > 1) {
        // 最多上传3张图
        // $.messager.show("提示", "只能上传一个文件，请删除多余文件！", "info");
        this.$message({
          type: "error",
          message: "只能上传一个文件,请先删除！",
        });
        uploader.removeFile(files[0]);
        return;
      }
      let objarr = files.map((val, ind) => {
        let obj = {};
        obj.id = val.id;
        obj.name = val.name;
        obj.type = val.type;
        // obj.upload_date = val.upload_date;
        obj.upload_date = new Date().toLocaleString(); //获取日期与时间
        // obj.publiser = val.publiser;
        obj.publisher = "publisher"; //获取当前登录用户信息
        obj.size = parseInt((val.origSize / 1024 / 1024) * 100) / 100;
        obj.percentage = 0;
        obj.loadType = 0;
        console.log(obj);
        return obj;
      });
      this.fileList.push(...objarr);
    },
    //上传之前回调
    BeforeUpload(uploader, file) {
      this.fileList = this.fileList.map((val, ind) => {
        if (val.id == file.id) {
          val.loadType = 1;
        }

        //设置参数
        console.log(val.name);
        if (
          this.form["seismic_filename"] == "" ||
          this.form["location"] == "" ||
          this.form["project_name"] == "" ||
          this.form["company_name"] == "" ||
          this.form["uploader"] == "" ||
          this.form["seismic_upload_date"] == ""
        ) {
          console.log("信息有误！");
        } else {
          uploader.setOption("multipart_params", {
            // form: this.form, //设置表单擦不能输
            seismic_filename: this.form["seismic_filename"],
            location: this.form["location"],
            project_name: this.form["project_name"],
            company_name: this.form["company_name"],
            uploader: this.form["uploader"],
            seismic_upload_date: this.form["seismic_upload_date"].getTime(),
            filename: val.name,
            publisher: val.publisher,
            type: val.type,
            upload_date: new Date().toLocaleString(),
            // size:val.size
          });
        }
        uploader.settings.multipart_params.size = val.size;
        uploader.settings.multipart_params.id = val.id;
        return val;
      });
    },
    //上传进度回调
    UploadProgress(uploader, file) {
      this.fileList = this.fileList.map((val, ind) => {
        if (val.id == file.id) {
          val.percentage = file.percent;
        }
        return val;
      });
    },
    // 上传成功回调
    FileUploaded(uploader, file, responseObject) {
      this.fileList = this.fileList.map((val, ind) => {
        if (val.id == file.id) {
          // if (JSON.parse(responseObject.response).status == 0) {
          if (status == 0) {
            val.loadType = 2;
          } else {
            val.loadType = 3;
          }
        }
        return val;
      });
    },
    //取消上传回调
    removeFile(id) {
      this.uploader.removeFile(id);
      this.fileList = this.fileList.filter((val, ind) => {
        if (val.id == id) {
          return false;
        } else {
          return true;
        }
      });
    },
    //开始上传
    // FileUplodeOn() {
    //   this.uploader.start();
    // },
    onSubmit() {
      if (
        this.form["seismic_filename"] == "" ||
        this.form["location"] == "" ||
        this.form["project_name"] == "" ||
        this.form["company_name"] == "" ||
        this.form["uploader"] == "" ||
        this.form["seismic_upload_date"] == ""
      ) {
        console.log("请检查输入信息！");
         this.$message.error('缺少相关信息，请重新输入！');
      } else {
        this.uploader.start();
      }
    },
  },
};
</script>

<style lang="scss">
.drillmetaupload .el-form-item {
  width: 560px; //这里设置为了和右边滚动条有一定的距离
}
.el-scrollbar__wrap {
  overflow-x: hidden; //设置滚动条隐藏
}
</style>
```



##### 5.1.1 models.py

```python
'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 21:36:57
LastEditors: henggao
LastEditTime: 2020-12-17 09:54:39
'''
from datetime import datetime
from django.db import models
from mongoengine import connect
from mongoengine.document import Document
from mongoengine.fields import DateTimeField, FileField, StringField

# Create your models here.
# 设置数据库
connect(alias='default', db='地震数据管理子系统',
        host='192.168.55.110', port=20000)
connect(alias='seismic_system', db='地震数据管理子系统',
        host='192.168.55.110', port=20000)


class SeismicInfo(Document):
    '''钻孔定位表'''
    filename = StringField(required=True)
    location = StringField(required=True)
    company_name = StringField(required=True)
    uploader = StringField(required=True)
    upload_date = DateTimeField(default=datetime.now(), required=True)
    project_name = StringField(required=True)
    filedata = FileField()

    meta = {'db_alias': 'seismic_system',
            # 'collection': '地震数据Demo1', 'indexes': ['filename']}
            'collection': '地震数据', 'indexes': ['filename']}

    def __str__(self) -> str:
        """
        docstring
        """
        return self.filename

```

- 需要注意的是，设置一个default，否则上传文件时会报错

##### 5.1.2 serializers.py

```python
from .models import SeismicInfo
from rest_framework_mongoengine.serializers import DocumentSerializer
class SeismicInfoSerializer(DocumentSerializer):
    '''钻孔数据管理子系统定位表数据'''
    class Meta:
        model = SeismicInfo
        fields = "__all__"
```

##### 5.1.3 views.py

```python
import os
from .models import SeismicInfo
import time
from django.http.response import HttpResponse
from mongoengine.context_managers import switch_collection
from rest_framework.views import APIView
# Create your views here.


class SeismicInfoView(APIView):
    def get(self, request, *args, **kwargs):
        """
        docstring
        """
        seismic_obj = SeismicInfo.objects.all().order_by('_id')  # 一定要排序
        print(seismic_obj)
        # 创建分页对象
        page = MyPagination()
        # 实例化查询，获取分页的数据
        page_chapter = page.paginate_queryset(
            queryset=seismic_obj, request=request, view=self)
        # 序列化及结果返回，将分页后返回的数据, 进行序列化
        ser = SeismicInfoSerializer(instance=page_chapter, many=True)
        data = {'list': ser.data}
        return page.get_paginated_response(data)

    def post(self, request, *args, **kwargs):
        """
        docstring
        """
        fileio = request.FILES.get("file", None)  # 注意比较

        print(request.data['upload_date'])  # DRF才有request.data
        print(request.POST)  # Django只有request.POST、request.GET
        print(request.data)
        # _id = self.request.POST.get('id')
        seismic_filename = request.data['seismic_filename'],  # 取出来竟是个元组，QAQ
        location = request.data['location'],
        company_name = request.data['company_name'],
        uploader = request.data['uploader'],
        project_name = request.data['project_name'],
        seismic_upload_date = request.data['seismic_upload_date'],
        # 上传到GriDFS中
        filename = request.data['filename'],

        temp_time2 = int(seismic_upload_date[0])/1000
        # 转换成localtime
        time_local2 = time.localtime(temp_time2)
        # 转换成新的时间格式(2016-05-05 20:28:54)

        dt2 = time.strftime("%Y-%m-%d", time_local2)

        # 保存到本地
        if not os.path.exists('upload/'):
            os.mkdir('upload/')
        with open("./upload/%s" % fileio.name, 'wb+') as f:
            for chunk in fileio.chunks():
                f.write(chunk)
            f.close()
        # 写入数据
        write_data = SeismicInfo(
            seismic_filename=seismic_filename[0],
            location=location[0],
            project_name=project_name[0], company_name=company_name[0], uploader=uploader[0],
            seismic_upload_date=dt2)

        with open("./upload/%s" % fileio.name, 'rb') as fd:
            # 写入GridFS
            write_data.filedata.put(
                fd, content_type='segy', filename=seismic_filename[0], aliases=[filename[0]])
            # writedata.filedata.put(SeismicInfo, content_type='segy')
        write_data.save()

        return HttpResponse('success')
```



##### 5.1.4 urls.py

```python
from django.urls import include, path

from . import views
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'drillmeta', DrillMetaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('seismicinfo/', SeismicInfoView.as_view(),
         name='seismicinfo'),  # 地震数据查询、上传
]
```



#### 5.2 地震数据——增、删、改、查



##### 5.2.0  SeismicData.vue

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-12-16 15:08:04
 * @LastEditors: henggao
 * @LastEditTime: 2020-12-17 21:49:58
-->
<template>
  <div class="DataShow">
    <div>
      <h2
        style="
          font-size: 30px;
          padding-top: 10px;
          color: #870000;
          min-width: 1100px;
          overflow: hidden;
          text-align: left;
        "
      >
        <i class="el-icon-caret-right" /> 地震元数据信息
      </h2>
    </div>
    <el-container>
      <el-header class="data_search">
        <!--搜索头 开始-->
        <section id="search-title" style="min-width: 500px">
          <el-form
            :inline="true"
            :model="searchCondition"
            class="demo-form-inline"
            @submit.native.prevent
          >
            <el-form-item label="关键字:">
              <el-input
                v-model="searchCondition.filter_key"
                suffix-icon="el-icon-view"
                placeholder="请输入关键字"
                @keyup.enter.native="onSearchSubmit"
              ></el-input>
            </el-form-item>
            <el-form-item id="submit-item">
              <el-button
                type="info"
                plain
                icon="el-icon-search"
                @click="onSearchSubmit"
                >查询</el-button
              >
            </el-form-item>
            <el-form-item id="submit-reset">
              <el-button
                type="info"
                plain
                icon="el-icon-refresh"
                @click="resetData"
                >重置</el-button
              >
            </el-form-item>
            <el-form-item id="addNew-item">
              <el-button
                type="info"
                plain
                icon="el-icon-upload"
                @click="uploadSeismicData"
                >上传</el-button
              >
            </el-form-item>
            <!-- <el-form-item id="addNew-item">
              <el-button
                type="info"
                plain
                icon="el-icon-edit"
                @click="dialogVisible = true"
                >新增</el-button
              >
            </el-form-item> -->
          </el-form>
        </section>
        <!--搜索头 结束-->
        <!-- <SearchData /> -->
      </el-header>
      <el-main class="data_content">
        <div class="data_table" style="overflow: hidden">
          <!-- 注意里面max-height字段设置高度  tableData放列表数据 -->
          <el-table
            class="tb-edit"
            highlight-current-row
            :data="tableData"
            style="width: 100%"
            max-height="650px"
            @selection-change="handleSelectionChange"
            lazy
          >
            <!-- 选择框设置 -->
            <el-table-column type="selection" width="55"> </el-table-column>
            <template v-for="col in cols">
              <!-- 设置排序字段 -->
              <el-table-column
                :key="col._id"
                :prop="col.prop"
                sortable
                :label="col.label"
                align="center"
              >
                <!-- 每一行数据 -->
                <template slot-scope="scope">
                  <div v-if="!scope.row.isEdit">{{ scope.row[col.prop] }}</div>
                  <div v-else>
                    <el-input v-model="scope.row[col.prop]"></el-input>
                  </div>
                </template>
              </el-table-column>
            </template>
            <el-table-column
              label="下载文件"
              class="details"
              width="100"
              style="text-align: center"
            >
              <template slot-scope="scope">
                <el-button
                  type="primary"
                  plain
                  size="mini"
                  @click="
                    downloadfile(scope.row.seismic_filename, scope.row.id)
                  "
                  >下载文件</el-button
                >
              </template>
            </el-table-column>
            <el-table-column fixed="right" label="操作" width="160">
              <h2>防止按钮消失</h2>
              <!--加入这一行，防止按钮消失-->
              <template slot-scope="scope">
                <el-button
                  type="primary"
                  plain
                  size="mini"
                  @click="handleEdit(scope.$index, scope.row)"
                  >{{ scope.row.isEdit ? "保存" : "编辑" }}</el-button
                >
                <el-button
                  @click.native.prevent="
                    deleteRow(scope.$index, tableData, scope.row)
                  "
                  type="danger"
                  plain
                  size="mini"
                >
                  删除
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
        <!-- 分页 -->
        <div class="block" style="overflow: hidden">
          <el-pagination
            small
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page.sync="currentPage"
            :page-sizes="pageSizes"
            :page-size="PageSize"
            layout="total, sizes, prev, pager, next, jumper"
            :total="totalCount"
          >
          </el-pagination>
        </div>
        <!-- 下面这个用来设置点击添加按钮的弹出框，里面可以进行嵌套表格来展示弹出的表格信息,使用下面的:visible.sync来控制显示与否。里面绑定的是我们新设置的值，填写完成后，将我们这个新值塞到页面中所有的数据当中去  -->
        <!-- 添加数据的对话框 -->
        <el-dialog
          title="添加数据"
          :visible.sync="dialogVisible"
          width="30%"
          @close="addDialogClosed"
        >
          <!-- 内容的主体区域 -->
          <!--去掉:rules="addFormRules" -->
          <el-form
            ref="addFormRef"
            :model="add_to_data"
            :rules="addFormRules"
            label-width="120px"
          >
            <template v-for="(item, key) of addForm">
              <!-- <el-form-item
                v-if="key == '_id'"
                :label="key"
                :prop="key"
                :key="key"
              >
                <el-input v-model="addForm[key]"></el-input>
              </el-form-item> -->
              <el-form-item
                v-if="key !== 'id' && key !== 'location'"
                :label="key"
                :prop="key"
                :key="key"
              >
                <el-input v-model="add_to_data[key]"></el-input>
              </el-form-item>
            </template>
          </el-form>
          <!-- 底部区域 -->
          <span slot="footer" class="dialog-footer">
            <el-button @click="dialogVisible = false">取 消</el-button>
            <el-button
              type="primary"
              :disabled="true"
              v-if="!add_button_state"
              @click="addData"
              >确 定</el-button
            >
            <el-button
              type="primary"
              v-else-if="add_button_state"
              @click="addData"
              >确 定</el-button
            >
          </span>
        </el-dialog>
      </el-main>
    </el-container>
  </div>
</template>

<script>
import axios from "axios";
import qs from "qs";

// import SearchData from "@/components/SearchData.vue";
export default {
  name: "SeismicData",
  components: {
    // SearchData
  },
  data() {
    // 校验添加信息
    let checkZk_name = (rule, value, callback) => {
      const regZk_name = /^ZK[0-9]{1,6}/;
      // const regKey_word = /^[A-Za-z0-9\u4e00-\u9fa5]{3,}$/;
      if (regZk_name.test(value)) {
        // 验证通过，合法
        return callback();
      }
      // 验证不通过，不合法
      callback(new Error("请输入正确的孔号"));
    };
    // 校验添加信息
    let checkCoordinate_E = (rule, value, callback) => {
      var re = /^[0-9]+.?[0-9]*/; //判断字符串是否为数字
      if (re.test(value)) {
        // 验证通过，合法
        return callback();
      }
      // 验证不通过，不合法
      callback(new Error("请输入正确的参数"));
    };
    // 校验添加信息
    let checkCoordinate_N = (rule, value, callback) => {
      var re = /^[0-9]+.?[0-9]*/; //判断字符串是否为数字
      if (re.test(value)) {
        // 验证通过，合法
        return callback();
      }
      // 验证不通过，不合法
      callback(new Error("请输入正确的参数"));
    };
    // 校验添加信息
    let checkCoordinate_R = (rule, value, callback) => {
      var re = /^[0-9]+.?[0-9]*/; //判断字符串是否为数字
      if (re.test(value)) {
        // 验证通过，合法
        return callback();
      }
      // 验证不通过，不合法
      callback(new Error("请输入正确的参数"));
    };
    // 校验添加信息
    let checkMax_depth = (rule, value, callback) => {
      var re = /^[0-9]+.?[0-9]*/; //判断字符串是否为数字
      if (re.test(value)) {
        // 验证通过，合法
        return callback();
      }
      // 验证不通过，不合法
      callback(new Error("请输入正确的参数"));
    };
    // 校验添加信息
    let checkLocation = (rule, value, callback) => {
      var re = /^[0-9]+.?[0-9]*/; //判断字符串是否为数字
      if (re.test(value)) {
        // 验证通过，合法
        return callback();
      }
      // 验证不通过，不合法
      callback(new Error("请输入正确的参数"));
    };

    return {
      // cols prop属性值都是作为 tableData的属性
      cols: [
        { label: "节点编号_id", prop: "_id.$oid", nickname: "normal" },
        { label: "名称nickname", prop: "nickname", nickname: "sort" },
        { label: "类型combat", prop: "combat", nickname: "normal" },
        { label: "状态level", prop: "level", nickname: "normal" },
        { label: "坐标rid", prop: "rid", nickname: "normal" },
      ],
      //   表格数据
      tableData: [
        {
          node: "0051",
          name: " 机库顶",
          type: "UWB",
          status: "正常",
          coordinate: "12.21,34.45,34.6",
        },
        {
          node: "0061",
          name: "机库门",
          type: "GPS",
          status: "低电",
          coordinate: "45.41,67.45,78.6",
        },
        {
          node: "0061",
          name: "机库门",
          type: "GPS",
          status: "低电",
          coordinate: "45.41,67.45,78.6",
        },
      ],
      // 筛选字段
      filter_data: [
        { text: "ZK1", value: "ZK1" },
        { text: "ZK2", value: "ZK2" },
        { text: "ZK3", value: "ZK3" },
        { text: "ZK4", value: "ZK4" },
      ],
      // 分页数据，默认第几页
      currentPage: 1,
      // 总条数，根据接口获取数据长度(注意：这里不能为空)
      totalCount: 400,
      // 个数选择器（可修改）
      pageSizes: [10, 20, 50, 100],
      // 默认每页显示的条数（可修改)
      PageSize: 10,
      // 控制添加用户对话框的显示与隐藏，默认为隐藏
      dialogVisible: false,
      // 添加对象表格的字段名
      addForm: {
        zk_name: "",
        coordinate_E: "",
        coordinate_N: "",
        coordinate_R: "",
        max_depth: "",
        track_type: "曲",
        coordinate_lng: "",
        coordinate_lat: "",
        // location: {
        //   type: "Point",
        //   coordinates: [],
        // },
      },
      // 添加数据框的字段,用来判断是否为空，确定按钮
      add_to_data: {
        zk_name: "",
        coordinate_E: "",
        coordinate_N: "",
        coordinate_R: "",
        max_depth: "",
        track_type: "曲",
        coordinate_lng: "",
        coordinate_lat: "",
        // location: {
        //   type: "Point",
        //   coordinates: [],
        // },
      },
      // 通过add_button_state值判断确定按钮是否激活
      add_button_state: false,
      // // 添加表单的验证规则对象
      addFormRules: {
        zk_name: [
          { required: true, message: "请输入钻孔号", trigger: "blur" },
          { min: 3, max: 10, message: "数据格式为'ZK1'", trigger: "blur" },
          { validator: checkZk_name, trigger: "blur" },
        ],
        coordinate_E: [
          { required: true, message: "请输入参数", trigger: "blur" },
          { validator: checkCoordinate_E, trigger: "blur" },
        ],
        coordinate_N: [
          { required: true, message: "请输入参数", trigger: "blur" },
          { validator: checkCoordinate_N, trigger: "blur" },
        ],
        coordinate_R: [
          { required: true, message: "请输入参数", trigger: "blur" },
          { validator: checkCoordinate_R, trigger: "blur" },
        ],
        max_depth: [
          { required: true, message: "请输入参数", trigger: "blur" },
          { validator: checkMax_depth, trigger: "blur" },
        ],
        track_type: [
          { required: true, message: "请输入参数", trigger: "blur" },
        ],
        coordinate_lng: [
          { required: true, message: "请输入参数", trigger: "blur" },
          { validator: checkMax_depth, trigger: "blur" },
        ],
        coordinate_lat: [
          { required: true, message: "请输入参数", trigger: "blur" },
          { validator: checkMax_depth, trigger: "blur" },
        ],
        location: [{ required: true, message: "请输入参数", trigger: "blur" }],
      },
      // 搜索对象
      searchCondition: {
        filter_key: "",
        Depth: "",
        _id: "",
      },
      // 用于判断是否点击过搜索按钮
      flag: false,
    };
  },
  watch: {
    add_to_data: {
      handler(curval, oldval) {
        // console.log(Object.keys(curval)[0]);
        let regZk_name = /^ZK[0-9]{1,6}/;
        let re = /^[0-9]+.?[0-9]*/; //判断字符串是否为数字
        if (
          regZk_name.test(curval.zk_name) &&
          re.test(curval.coordinate_E) &&
          re.test(curval.coordinate_N) &&
          re.test(curval.coordinate_R) &&
          re.test(curval.max_depth) &&
          curval.track_type != "" &&
          re.test(curval.coordinate_lng) &&
          re.test(curval.coordinate_lat)
        ) {
          this.add_button_state = true;
        } else {
          this.add_button_state = false;
        }
      },
      deep: true,
    },
  },
  created() {
    this.showData(this.PageSize, this.currentPage); //展示Collection表格数据
    // this.onSearchSubmit(this.PageSize, this.currentPage); //展示Collection表格数据
  },
  mounted() {},
  methods: {
    // 展示数据,将页码及每页显示的条数以参数传递提交给后台
    showData(n1, n2) {
      const url = "http://127.0.0.1:8000/seismic/seismicinfo/";
      axios
        .get(url, {
          params: {
            // 每页显示的条数
            PageSize: n1,
            // 显示第几页
            currentPage: n2,
          },
        })
        .then((response) => {
          // var res = JSON.parse(response.bodyText);
          // console.log(response);
          console.log(response.data);
          console.log(response.data.data);

          this.tableData = response.data.data.list;
          console.log(response.data.data.list);

          this.totalCount = response.data.data.count; //分页总数

          let tmp = this.tableData[0];
          // console.log(tmp);
          // var listcol = [];

          // cols prop属性值都是作为 tableData的属性
          var newcols = [
            { label: "文件名称", prop: "seismic_filename" },
            { label: "研究区域", prop: "location" },
            { label: "项目名称", prop: "project_name" },
            { label: "单位名称", prop: "company_name" },
            { label: "上传人员", prop: "uploader" },
            { label: "上传时间", prop: "seismic_upload_date" },
            // { label: "钻孔柱状图", prop: "zk_histogram" },
          ];

          this.cols = newcols;
          let tem_list = [];
          for (let i = 0; i < 55; i++) {
            // const element = array[i];
            let ZK = "ZK";
            let ZKX = ZK + i;
            // {text:"ZKX",value;"ZKX"}
            let json_data = { text: ZKX, value: ZKX };
            tem_list.push(json_data);
          }
          // console.log(tem_list);
          this.filter_data = tem_list;
        });
    },

    // 重置Collection表格数据
    resetData() {
      (this.flag = false), this.showData(10, 1);
    },
    // 选择框
    handleSelectionChange(val) {
      this.multipleSelection = val;
    },
    // 排序
    filterHandler(value, row, column) {
      const property = column["property"];
      return row[property] === value;
    },

    // 点击按钮，添加数据
    addData() {
      // this.addForm.visible = true;
      // 发送添加数据的网络请求
      const url = "http://127.0.0.1:8000/load/adddrilllocation/";
      let tmp_data = this.add_to_data;
      console.log(tmp_data); //这个取得值是undefined，但可以成功发送到后端
      axios
        .post(url, {
          tmp_data,
          // 设置上传到后端的数据库和集合名称
          // colname: this.$store.state.title_message,
          // dbname: this.$store.state.temp_database,
        })
        .then((res) => {
          console.log("Success");
        })
        .catch((err) => {
          console.log("错误");
          this.$message.warning("输入数据存在错误！");
        });

      // 隐藏添加用户的对话框
      this.dialogVisible = false;
      // 重新获取用户列表数据
      // this.showData();
      //通过flag判断,刷新数据
      if (!this.flag) {
        this.showData();
      } else {
        this.onSearchSubmit();
      }
    },
    // 监听添加对话框的关闭事件
    addDialogClosed() {
      this.$refs.addFormRef.resetFields();
    },
    // 上传
    uploadSeismicData() {
      this.$router.push({ path: "/mongeostore/seismicupload" });
    },
    // 下载
    downloadfile(seismic_filename, id) {
      console.log(id);
      const url = "http://127.0.0.1:8000/seismic/seismicfiledownload/";
      axios
        .get(url, {
          params: {
            file_id: id,
          },
          responseType: "blob",
        })
        .then((response) => {
          if (response.data.size === 0) {
            console.log("下载失败");
          } else {
            console.log(response);
            let blob = new Blob([response.data], {
              type: "application/octet-stream",
            });
            let url = window.URL.createObjectURL(blob);
            const link = document.createElement("a"); // 创建a标签
            link.href = url;
            // link.download = "下载文件.segy"; // 重命名文件
            link.download = seismic_filename + ".segy"; // 重命名文件
            link.click();
            URL.revokeObjectURL(url); // 释放内存
          }
        })
        .catch((err) => {
          console.log("err");
        });
    },
    // 编辑（修改）按钮
    handleEdit(index, row) {
      // console.log(index, row);
      // 动态设置数据并通过这个数据判断显示方式
      if (row.isEdit) {
        // 点击保存的
        this.$delete(row, "isEdit");
        // console.log("开始delete");
        // console.log(index, row); //把row发送给后端
        // console.log(row["_id"]["$oid"]); //把row发送给后端
        // row["id"] = row["_id"]["$oid"];
        // row["help_param"] = "help_param"; //用于解决后端smscode参数为3019"}多了"}问题
        // let postData = qs.stringify(row); // w为了解决后端拿不到数据问题
        // postData["_id"] = row["_id"]["$oid"];
        // console.log(typeof postData);
        // console.log(row["id"]);
        let json_data = JSON.stringify(row);

        const url = "http://127.0.0.1:8000/seismic/editseismicinfo/";
        axios
          .post(
            url,
            {
              // data: JSON.stringify(row) //data用于post请求
              json_data,
              // 设置上传到后端的数据库和集合名称
              colname: this.$store.state.title_message,
              dbname: this.$store.state.temp_database,
            },
            {
              headers: { "Content-Type": "application/x-www-form-urlencoded" },
            }
            // console.log(postData)
          )
          .then((res) => {
            console.log("编辑成功");
            console.log(res.data);
            if (res.data == 412) {
              // 输入有误,后端返回状态码,进行提示
              this.$message.error("输入时间有误,请重新编辑!");
            }
          })
          .catch((err) => {
            console.log("输入有误");
          });
      } else {
        // 点击编辑
        this.$set(row, "isEdit", true);
        // console.log("开始set");
        // console.log(index, row);
      }
      // console.log(this.tableData);s
    },
    // 删除按钮
    deleteRow(index, rows, row) {
      // 添加确认删除框
      this.$confirm("永久删除，是否继续？", "提示", {
        confirmButtonText: "确定",
        cancelButtonText: "取消",
        type: "warning",
      })
        .then(() => {
          // 删除操作
          rows.splice(index, 1);
          let json_data = JSON.stringify(row);
          console.log(json_data);
          const url = "http://127.0.0.1:8000/seismic/deleteseismicinfo/";
          axios
            .post(
              url,
              {
                json_data,
                // 设置上传到后端的数据库和集合名称
                colname: this.$store.state.title_message,
                dbname: this.$store.state.temp_database,
              },
              {
                headers: {
                  "Content-Type": "application/x-www-form-urlencoded",
                },
              }
            )
            .then((res) => {
              console.log("删除成功");
              // 重新获取用户列表数据
              // this.showData();
              //通过flag判断,刷新数据
              if (!this.flag) {
                this.showData(this.PageSize, this.currentPage);
              } else {
                this.onSearchSubmit(this.PageSize, this.currentPage);
              }
            });
        })
        .catch(() => {
          this.$message({
            type: "info",
            message: "取消删除",
          });
        });
    },
    // 开始搜索
    onSearchSubmit(n1, n2) {
      this.currentPage = n2;
      // this.initAdminList(1);
      if (this.searchCondition.filter_key == "") {
        this.$message.warning("查询条件不能为空！");
        return;
      } else {
        // console.log(this.searchCondition.filter_key);
        // console.log(this.$store.state.temp_database);
        let filter_key_data = this.searchCondition.filter_key;
        const url = "http://127.0.0.1:8000/seismic/seismicinfosearch/";
        axios
          .get(url, {
            params: {
              // 每页显示的条数
              PageSize: n1,
              // 显示第几页
              currentPage: n2,
              // 搜索字段
              search_key: filter_key_data,
            },
          })
          .then((response) => {
            if (response.data.data.list) {
              this.tableData = response.data.data.list; //返回查询的数据

              this.totalCount = response.data.data.count; //搜索后分页总数;
            } else {
              // alert("输入有误或数据不存在");
              this.$message.warning("输入有误或数据不存在");
              return;
            }
            //页面初始化数据需要判断是否检索过
            this.flag = true;
          });
      }
    },

    handleDelete(index, row) {
      console.log(index, row);
    },
    // 分页
    // 每页显示的条数
    handleSizeChange(val) {
      console.log(`每页 ${val} 条`);
      // 改变每页显示的条数
      this.PageSize = val;
      // 点击每页显示的条数时，显示第一页
      // this.showData(val, 1);
      if (!this.flag) {
        this.showData(val, 1); // this.pageSize是undefined，使用选定的或默认值
      } else {
        this.onSearchSubmit(val, 1);
      }
      // 注意：在改变每页显示的条数时，要将页码显示到第一页
      this.currentPage = 1;
      // this.handleCurrentChange(this.currentPage);
    },
    // 监听 pageSize 改变的事件，显示第几页
    handleCurrentChange(val) {
      console.log(`当前页: ${val}`);
      // 改变默认的页数
      this.currentPage = val;

      if (!this.flag) {
        this.showData(this.PageSize, val); // this.pageSize是undefined，使用选定的或默认值
      } else {
        this.onSearchSubmit(this.pageSize, val);
      }
    },
  },
};
</script>

<style>
/* 全局样式 */
</style>
<style lang="scss" scoped>
/* 本地样式 */
// 设置真个数据内容的大小
// .DataShow {
//   // height: 775px;
//   // height: 810px;
// }
// 设置搜索框的大小
.data_search {
  height: 45px !important;
}
// 设置表格数据大小，表格+分页
// .data_content {
//   // height: 680px !important;
//   // overflow: auto;
// }
// 设置表格数据大小
.data_table {
  height: 650px !important; //注意这个高度和table中max-height="620px"对应,避免部分内容展示不出来
  // overflow: auto;
}
// 搜索设置
#search-title {
  padding-top: 2px;
  height: 45px;
  float: right;
}
// 设置搜索关键字段字体
.demo-form-inline ::v-deep .el-form-item__label {
  font-size: 18px !important;
  color: rgb(73, 76, 80);
  font-family: "Arial Narrow";
  font-weight: bold;
}
// 设置表格数据滚动条,这里还是留着比较好
.block {
  padding-top: 15px;
}
// .el-scrollbar__wrap {
//   overflow-x: hidden; //设置滚动条隐藏
// }
</style>
```



##### 5.2.1 增

- 这里使用上传，跳转到上传页面即可

  ```js
      // 上传
      uploadSeismicData() {
        this.$router.push({ path: "/mongeostore/seismicupload" });
      },
  ```

  

##### 5.2.2 删

- 删除数据，对比pymongo，可以直接删除文件

- views.py

  ```python
  # 删除地震数据
  def DeleteSeismicInfo(request):
      """
      docstring
      """
      if request.method == "POST":
          body_data = request.body
          # print(body_data)
          data_json = json.loads(body_data)
          # print(data_json)
          query_data_json = data_json['json_data']
          # print(query_data_json)
          dict_data = json.loads(query_data_json)
          print(dict_data)
          front_query_oid = dict_data['id']   
  
          query_obj = SeismicInfo.objects.get(
                  id=front_query_oid)
          print(query_obj)
          query_obj.delete()
          return HttpResponse("Delete Success")
  ```

  

##### 5.2.2 改

- 每条数据内容的编辑，
  - 这里需要删除掉文件字段： `dict_data.pop('filedata')`
  - 对于时间编辑错误，提供返回状态码，友好提示

- views.py

  ```python
  def EditSeismicInfo(request):
      if request.method == "POST":
  
          body_data = request.body
          data_json = json.loads(body_data)
          # print(data_json)
  
          query_data_json = data_json['json_data']
          dict_data = json.loads(query_data_json)
          dict_data.pop('filedata') #去掉文件字段
          front_query_oid = dict_data['id']
  
          query_obj = SeismicInfo.objects.get(
              id=front_query_oid)
          print(query_obj)
          try:
              query_obj.update(**dict_data)
              query_obj.save()
              return HttpResponse('success')
          except:
              print('输入有误')
              status_code = 412
              return HttpResponse(status_code)
  ```

  

##### 5.2.2 查

- 搜索框

- views.py

- 使用一般方法查询，接下来构建索引查询

  ```python
  class SeismicInfoSearch(APIView):
      def get(self, request, *args, **kwargs):
        """
          docstring
          """
          print('success')
          search_key = request.GET['search_key']  # 根据字段搜索
          print(search_key)
          seismic_obj = SeismicInfo.objects.filter(
              seismic_filename=search_key).all().order_by('_id')  # 一定要排序
          # seismic_obj = SeismicInfo.objects.search_text(search_key).first()
  
          # 创建分页对象
          page = MyPagination()
          # 实例化查询，获取分页的数据
          page_chapter = page.paginate_queryset(
              queryset=seismic_obj, request=request, view=self)
          # 序列化及结果返回，将分页后返回的数据, 进行序列化
          ser = SeismicInfoSerializer(instance=page_chapter, many=True)
          data = {'list': ser.data}
          return page.get_paginated_response(data)
  ```
  
  

##### 5.3 下载

- 数据库-->下载到服务器-->下载到浏览器
- 设计下载格式设置

- views.py

```python
@require_http_methods(['GET'])
def SeismicFileDownload(request):

    search_key = request.GET['file_id']  # 根据字段搜索
    print(search_key)

    # 从数据库拿到数据
    seismic_obj = SeismicInfo.objects(id=search_key).first()
    print(seismic_obj)
    print(seismic_obj.seismic_filename)
    filename = seismic_obj.seismic_filename
    seismic_file = seismic_obj.filedata.read()
    content_type = seismic_obj.filedata.content_type
    # print(type(seismic_file)) #<class 'bytes'>
    # print(type(content_type)) #<class 'str'>

    # 数据写入服务器
    with open("../mongeostore_env/upload/%s" % filename, 'wb') as f:
        f.write(seismic_file)
    print('save success')

    # # 拿到数据,返回前端
    with open("./upload/%s" % filename, "rb") as f:
        res = HttpResponse(f)
        res["Content-Type"] = "application/octet-stream"  # 注意格式
        res["Content-Disposition"] = 'filename="{}"'.format(filename)
    return res
```



- [ref](https://blog.csdn.net/qq_42345108/article/details/102842492?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.control)

- [ref](https://gitee.com/jingchu/python_mongo/blob/master/python_monogo/mngadmin/views.py)