# 网站ico图标设置

[TOC]

## 一、设置

1. 将自己的ico图标，存储到public下，并命名favicon.ico替换原有的ico文件。
2. 新建vue.config.js文件，并作以下配置。

```js
module.exports = {
  // ico图标设置
  pwa: {
    iconPaths: {
      favicon32: 'favicon.ico',
      favicon16: 'favicon.ico',
      appleTouchIcon: 'favicon.ico',
      maskIcon: 'favicon.ico',
      msTileImage: 'favicon.ico'
    }
  },
}
```

