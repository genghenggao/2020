# Cesium使用



```vue
<template>
  <!-- <div id="cesiumContainer"></div>
   -->
  <div>
    <div id="cesiumContainer" class="fullSize"></div>
    <div id="loadingOverlay"><h1>Loading...</h1></div>
    <div id="toolbar">
      <div id="zoomButtons"></div>
    </div>
  </div>
</template>

<script>
import * as Cesium from "cesium/Cesium";
import * as widgets from "cesium/Widgets/widgets.css";

export default {
  name: "Cesium",
  mounted() {
    var cesiumAsset =
      "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJqdGkiOiIxZDE0MWI4OS1jYjYxLTRmMDEtYWI5Yy1hZjBiNDAwZjc2NzEiLCJpZCI6MTgzMDEsImlhdCI6MTYwOTMyNjMxNH0.5H4EA7TyeUBhRmOI6IoRFXjyLtEJAjFZKJORBhGK2uc";
    var tiandituTk = "	9c117468801c8405aaddff93da98c1e6";
    // var tiandituTk = "	ebf64362215c081f8317203220f133eb";
    // 服务域名
    var tdtUrl = "https://t{s}.tianditu.gov.cn/";
    var subdomains = ["0", "1", "2", "3", "4", "5", "6", "7"];
    Cesium.Ion.defaultAccessToken = cesiumAsset; //设置你的seisum asset，不添加则使用默认，下方会有提示
    var viewer = new Cesium.Viewer("cesiumContainer", {
      animation: false, //是否显示动画控件
      baseLayerPicker: false, //是否显示图层选择控件
      geocoder: true, //是否显示地名查找控件
      timeline: false, //是否显示时间线控件
      sceneModePicker: true, //是否显示投影方式控件
      navigationHelpButton: false, //是否显示帮助信息控件
      infoBox: true, //是否显示点击要素之后显示的信息
    });
    //加载影像底图
    var layer = new Cesium.WebMapTileServiceImageryProvider({
      url:
        "http://t0.tianditu.gov.cn/img_w/wmts?tk=9c117468801c8405aaddff93da98c1e6",
      layer: "img",
      style: "default",
      tileMatrixSetID: "w",
      format: "tiles",
      maximumLevel: 18,
    });
    viewer.imageryLayers.addImageryProvider(layer);
    viewer._cesiumWidget._creditContainer.style.display = "none"; // 隐藏cesium ion
    //加载影像注记
    var layer1 = new Cesium.WebMapTileServiceImageryProvider({
      url:
        "http://t0.tianditu.gov.cn/cia_w/wmts?tk=9c117468801c8405aaddff93da98c1e6",
      layer: "cia",
      style: "default",
      tileMatrixSetID: "w",
      format: "tiles",
      maximumLevel: 18,
    });
    viewer.imageryLayers.addImageryProvider(layer1);
    // 将三维球定位到中国
    viewer.camera.flyTo({
      destination: Cesium.Cartesian3.fromDegrees(103.84, 31.15, 17850000),
      orientation: {
        heading: Cesium.Math.toRadians(348.4202942851978),
        pitch: Cesium.Math.toRadians(-89.74026687972041),
        roll: Cesium.Math.toRadians(0),
      },
      complete: function callback() {
        // 定位完成之后的回调函数
      },
    });
  },
};
</script>

<style scoped>
@import url(https://sandcastle.cesium.com/templates/bucket.css);
</style>


```

