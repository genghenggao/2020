# 目录
[TOC]

## Base64

- **Base64**是一种基于64个可打印字符来表示[二进制数据](https://zh.wikipedia.org/wiki/二进制)的表示方法。由于{\displaystyle \log _{2}64=6}![{\displaystyle \log _{2}64=6}](https://wikimedia.org/api/rest_v1/media/math/render/svg/9c986fbdc6c036a937e0647d7a6ec5ad745bccab)，所以每6个[比特](https://zh.wikipedia.org/wiki/位元)为一个单元，对应某个可打印字符。3个[字节](https://zh.wikipedia.org/wiki/字节)相当于24个比特，对应于4个Base64单元，即3个字节可由4个可打印字符来表示。它可用来作为[电子邮件](https://zh.wikipedia.org/wiki/电子邮件)的传输[编码](https://zh.wikipedia.org/wiki/字符编码)。

- 图片转Base64：https://www.coder.work/imagebase64



## wxPython			 					 					 					

-  wxPython是一个Python包装wxWidgets（这是用 C++ 编写），一个流行的跨平台GUI工具包。



## three.js

- VUE项目中使用THREE.js加载obj、vtk模型

- 如今浏览器的功能越来越强大，而且这些功能可能通过JavaScript直接调用。你可以用HTML5标签轻松地添加音频和视频，而且可以在HTML5画布上创建各种交互组件。现在这个功能集合里又有了一个新成员，即支持webGL。通过webgl可以直接使用显卡的计算资源，创建高性能的二维和三维计算机图形，然后在JavaScript里直接使用webGL编程，创建三维场景并生成动画，这个过程非常复杂，而且容易出错。three.js库可以简化这个过程。

  ----摘自《Three.js开发指南》

  看了上面的摘文，我想大概能够明白three.js和webgl的关系，webgl是大部分浏览器直接支持的一种3D绘图标准。three.js在它的基础上进行了进一步的封装和简化开发开发过程，个人认为类似于jQuery对原生js的关系。

## OpenGL

## webgl

- WebGL是一种基于OpenGL的浏览器内置3D渲染器，它可以让你在HTML5页面中直接显示3维内容。 



## 可视化

- 可视化领域主要用到的工具主要有OpenGL、VTK、Direct3D和OSG（Open Scene Graph）四种，它们各自有各自的特点。



在三维显示领域，OpenGL 是神一样的存在，其地位就像编程语言里面的 C 一样。基于 OpenGL 衍生出来的分支、派系，林林总总。Python 旗下，影响较大的三维库有 **pyOpenGl / VTK / Mayavi / Vispy** 等，它们各自拥有庞大的用户体。



## 三维技术

- 常见的三维技术包括Cult3D、Java3D、Flash3D、Silverlight、unity3D、Sun3D、VRP系列、viewport、converse3D等，而最新发展的Html5和webGL等技术，由于不需要插件依赖，而且具备硬件加速能力，因此具有更大发展前景。

- 目前主流的WebGL框架主要有：Three.js、Babylon.js、SceneJS、PhiloGL、vtkJS等。



## 概念：

- 数据库系统
  - 由数据库、DBMS(及其开发工具)、应用系统和数据库管理员组成
- 数据库管理系统（DBMS）
  - 是一种重要的程序设计系统，它由一个相互关联的数据集合(这个数据集合称为数据库)和一组访问这些数据的  程序组成。DBMS是位于用户和计算机操作系统之间的数据管理软件。
  -  功能：
    - 1.数据定义  
    - 2.数据操纵  
    - 3.事务管理和运行管理 
    - 4.数据存储和查询处理 
    - 5.数据库的建立和维护
    -  6.其他功能：包括DBMS与其他软件通信、异构数据库之间数据转换和互相操作等
- 数据管理系统
  - 数据管理系统是用户用以[计算机的数据库进行控制、更新、扩充、传送和其他操作的软件系统。
  - 数据管理系统的基本功能是按照用户的要求，从大量的数据资源中提取有[信息价值](https://baike.baidu.com/item/信息价值)的数据。例如可以通过检索、排序、合并、转换、汇总等方法获得这些数据。数据管理系统要解决两个主要的问题，一是定义各种数据的要求形式，二是如何由系统来处理这些要求。
- 可视化
- 三维建模



## Python地震数据处理包

### segyio

- segyio库试图易于有效地用于原型设计以及与可能较大的segy文件的交互。文件读取和写入是流式传输，开箱即用即可提供大文件支持，而且没有麻烦。

### obspy

- [ obspy](http://docs.obspy.org/)是一个针对地震领域开发的python库。
- [obspy中文教程（一）](https://blog.csdn.net/dodwind/article/details/81085749)

### APASVO

- 一种图形工具，用于在地震道中执行事件检测/拾取。




