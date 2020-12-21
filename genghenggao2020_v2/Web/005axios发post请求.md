# Axios发POST请求参数

- 发送的数据格式问题

- 引入QS模块，进行格式化

```
import qs from "qs";

let data = { filename: row.filename };
axios({
        method: "POST",
        url: this_url,
        data: qs.stringify(data),
        headers: { "Content-Type": "application/x-www-form-urlencoded" },

      })
        .then((res) => {
          console.log("success");
        })
        .catch((err) => {
          console.log("err");
        });
```

- [ref](https://blog.csdn.net/csdn_yudong/article/details/79668655)

- 后端接收

  ```
  <QueryDict: {'filename': ['MongoDB数据库探讨.pptx']}>
  ```

  