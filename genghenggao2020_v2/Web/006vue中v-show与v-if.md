# v-if与v-show区别

- 在使用Echarts是报错：`Cannot read property 'getAttribute' of null`问题，我在div中使用了v-if，换为v-show报错消失

- v-if 是动态添加，当值为false 时，是完全移除该元素，即dom 树中不存在该元素。 v-show 仅是隐藏/ 显示，值为false 时，该元素依旧存在于dom 树中。

