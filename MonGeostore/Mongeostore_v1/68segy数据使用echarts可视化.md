# Segy数据使用Echarts可视化

[TOC]

## 1. 地震数据单道显示

- 显示一道数据图

- `SeismicAnalysis.vue`

```vue
 // 基于准备好的dom，初始化echarts实例
              let myChart = this.$echarts.init(
                document.getElementById("dataviews")
              );
              // let mychart = echarts.init(this.$refs.chart);
              // 指定图表的配置项和数据
              let data = [];
              seismicdata.forEach((element, i) => {
                data.push([i, element]);
              });
              let textname = "第" + this.val + "道数据展示图";
              let option = {
                title: {
                  // text: "当前道的频谱图",
                  text: textname,
                  subtext: "数据来自MonGeoStore解析",
                  left: "center",
                },
                animation: false,
                grid: {
                  top: 60,
                  left: 60,
                  right: 40,
                  bottom: 50,
                },
                xAxis: {
                  name: "",
                  minorTick: {
                    show: true,
                  },
                  splitLine: {
                    lineStyle: {
                      color: "#999",
                    },
                  },
                  minorSplitLine: {
                    show: true,
                    lineStyle: {
                      color: "#ddd",
                    },
                  },
                },
                yAxis: {
                  name: "y",
                  // min: -100,
                  // max: 100,
                  minorTick: {
                    show: true,
                  },
                  splitLine: {
                    lineStyle: {
                      color: "#999",
                    },
                  },
                  minorSplitLine: {
                    show: true,
                    lineStyle: {
                      color: "#ddd",
                    },
                  },
                },
                dataZoom: [
                  {
                    show: true,
                    type: "inside",
                    filterMode: "none",
                    xAxisIndex: [0],
                    // startValue: -20,
                    // endValue: 20,
                  },
                  {
                    show: true,
                    type: "inside",
                    filterMode: "none",
                    yAxisIndex: [0],
                    // startValue: -20,
                    // endValue: 20,
                  },
                ],
                series: [
                  {
                    type: "line",
                    showSymbol: false,
                    clip: true,
                    data: data,
                  },
                ],
              };
              // 使用刚指定的配置项和数据显示图表。
              myChart.setOption(option);
              // mychart.setOption(option);
```



## 2. 多道数据

- 尝试多道显示，使用懒加载

- 数据读取

  - 后端

    - f.trace[i]读出数组
    - 写成想要的list
    - 嵌套列表，[[],[]],使用追加append
    - 列表写入dict
    - dict转为字符串，str

  - 前端

    - json字符串转对象

      ```
       var datajson = eval("(" + res.data + ")");
      ```

- Echarts