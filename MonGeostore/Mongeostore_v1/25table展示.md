# 将GridFS添加到Table展示

[TOC]

## 一、读取GridFS中信息



- `views.py`

```python
@require_http_methods(['GET'])
def FileShow(request):
    """
    docstring
    """
    client = MongoClient("192.168.55.110", 20000)  # 连接MongoDB数据库
    db = client.segyfile  # 选定数据库，设定数据库名称为segyfile
    fs = GridFS(db, collection='mysegy')  # 连接GridFS集合，名称为mysegy
    gf = fs.find_one()
    # print(gf.filename)
    # print(gf.length)
    # print(dir(gf.md5))
    # print(dir(gf.md5))

    response = {}
    data = []
    for grid_out in fs.find({"$where": "this._id.match(/.*o/)"}):
        # print(grid_out._file)
        # response = {}
        # response = grid_out._file
        response['uploadDate'] = str(grid_out.upload_date)
        # print(response)
        # print(type(response))
        # print(json.dumps(response))
        
        data.append(grid_out._file)
        print(data)
        response['list'] = data
        response['msg'] = 'success'
        response['error_num'] = 0
   

    return JsonResponse(response,safe=False) #不加safe=False的话必须返回dic
    # return JsonResponse(json.loads(response)) #不加safe=False的话必须返回dict
    # return HttpResponse(json.dumps(response), content_type="application/json")

```



## 二、vue

- SeiTable.vue

```vue
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2020-10-06 21:09:44
 * @LastEditors: henggao
 * @LastEditTime: 2020-11-02 20:57:26
-->
<template>
  <div class="seismictable" style="overflow: scroll;max-height: 750px;">
    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">_id</th>
          <th scope="col">filename</th>
          <th scope="col">contentType</th>
          <th scope="col">length</th>
          <th scope="col">uploadDate</th>
          <th scope="col">publisher</th>
          <th scope="col">aliases</th>
          <th scope="col">metadata</th>
          <th scope="col">md5</th>
          <th scope="col">chunkSize</th>
        </tr>
      </thead>
      <tbody id="list"></tbody>
      <!-- <tbody>
        <tr v-for="file in files">
          <td v-text="file._id"></td>
          <td v-text="file.filename"></td>
          <td v-text="file.contentType"></td>
          <td v-text="file.length"></td>
          <td v-text="file.uploadDate"></td>
          <td v-text="file.publisher"></td>
          <td v-text="file.aliases"></td>
          <td v-text="file.metadata"></td>
          <td v-text="file.md5"></td>
          <td v-text="file.chunkSize"></td>
        </tr>
      </tbody> -->
      <!-- <tbody>
        <tr>
          <th scope="row">1</th>
          <td>Mark</td>
          <td>Otto</td>
          <td>@mdo</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
        </tr>
        <tr>
          <th scope="row">2</th>
          <td>Jacob</td>
          <td>Thornton</td>
          <td>@fat</td>
          <td>{{files.filename}}</td>
        </tr>
        <tr>
          <th scope="row">3</th>
          <td colspan="2">Larry the Bird</td>
          <td>@twitter</td>
        </tr>
      </tbody> -->
    </table>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "SeiTable",
  data() {
    return {
      files: []
    };
  },
  created() {
    this.showFile();
  },
  mounted() {
    // this.showFile();
  },
  methods: {
    showFile() {
      const url = "http://127.0.0.1:8000/load/fileshow/";
      axios.get(url).then(response => {
        // var res = JSON.parse(response.bodyText);
        console.log(response);
        console.log(response.data.filename);
        var result = response.data.list;
        this.files = result;
        $(response.data.list).each(function(i, values) {
          $("#list").append(
            "<tr><td>" +
              values._id +
              "</td>" +
              "<td><a href='getBookByname?name='>" +
              values.filename +
              "</ta></td>" +
              "<td>" +
              values.contentType +
              "</td>" +
              "<td>" +
              values.length +
              "</td>" +
              "<td>" +
              values.uploadDate +
              "</td>" +
              "<td>" +
              values.publisher +
              "</td>" +
              "<td>" +
              values.aliases +
              "</td>" +
              "<td>" +
              values.metadata +
              "</td>" +
              "<td>" +
              values.md5 +
              "</td>" +
              "<td>" +
              values.chunkSize +
              "</td></tr>"
          );
        });
        // table
      });
    }
  }
};
</script>

<style>
.seismictable {
  border: 0;
  padding: 0;
}
</style>
```





- [ref](https://blog.csdn.net/weixin_40570675/article/details/81774942?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-2.edu_weight)

