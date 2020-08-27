# Notes

[TOC]

## 一、spring boot各层之间的关系

 **spring boot 中分为为 controller层、service层、dao层、entity层。** 

- entity层：entity层和model层一样，存放的是实体类，属性值与数据库中的属性值保持一致。 实现set和get方法。

- dao层：即mapper层，对数据库进行持久化操作，他的方法是针对数据库操作的，基本用到的就是增删改查。它只是个接口，只有方法名字，具体实现在mapper.xml中。

- service层：业务层，存放业务逻辑处理，不直接对数据库进行操作，有接口和接口实现类，提供controller层调用的方法。

- controller层：控制器层，导入service层，调用service方法，controller通过接收前端传过来的参数进行业务操作，在返回一个指定的路径或者数据表。 

- 根目录：src.main.java

  -  工程启动类(Application.java) 
  -  实体类(domain) 
  -  数据访问层(Dao) 
  -  数据服务层(Service) 
  -  数据服务接口的实现(serviceImpl) 
  -  前端控制器(Controller) 
  -  工具类(utils) 
  -  常量接口类(constant) 
  -  配置信息类(config) 

- 资源文件：src.main.resources

  -  页面以及js/css/image等置于static文件夹下的各自文件下 
  -  使用模版相关页面等置于templates文件夹下的各自文件下 

-  一个基本 [sb2-web](https://blog.csdn.net/ubuntu64fan/article/details/80555915) 的目录结构如下： 

  ```
  ├── clean-run.sh
  ├── logs/            日志文件目录
  │   ├── sb2-web_test_2018-06-02_0959.0.log
  │   └── sb2-web_test.log
  |               
  ├── mvnw
  ├── mvnw.cmd
  ├── pom.xml
  ├── pysrc/            python 脚本目录
  ├── README.md
  ├── src/              源文件目录
  │   ├── main
  │   │   ├── java
  │   │   │   └── com
  │   │   │       └── mydomain
  │   │   │           ├── guru/          工具包目录
  │   │   │           │   ├── AccountValidator.java
  │   │   │           │   ├── DateConverter.java
  │   │   │           │   ├── JsonBeanUtil.java
  │   │   │           │   ......
  │   │   │           └── webapi/        web 接口目录
  │   │   │               ├── Application.java
  │   │   │               ├── config/    sb2 app 配置文件目录
  │   │   │               │   ├── CORSFilter.java
  │   │   │               │   ├── JwtAuthenticationEntryPoint.java
  │   │   │               │   ├── JwtAuthenticationFilter.java
  │   │   │               │   ├── WebMvcConfig.java
  │   │   │               │   ├── WebSecurityConfig.java
  │   │   │               │   └── ......
  │   │   │               ├── controller/   控制器目录
  │   │   │               │   ├── AuthenticationController.java
  │   │   │               │   ├── KaptchaController.java
  │   │   │               │   └── UserController.java
  │   │   │               ├── dao/          DAO 目录 (或者称为：repository)
  │   │   │               │   ├── KaptchaTokenDao.java
  │   │   │               │   └── UserDao.java
  │   │   │               ├── model/        Model 目录 （绑定数据表）
  │   │   │               │   ├── AuthToken.java
  │   │   │               │   ├── Constants.java
  │   │   │               │   ├── dto/      DTO 数据传输组件目录
  │   │   │               │   │   ├── KaptchaTokenDto.java
  │   │   │               │   │   └── UserDto.java
  │   │   │               │   ├── KaptchaToken.java
  │   │   │               │   ├── LoginUser.java
  │   │   │               │   ├── Role.java
  │   │   │               │   └── User.java
  │   │   │               └── service/      服务接口目录     
  │   │   │                   ├── impl/     服务接口实现目录
  │   │   │                   │   ├── KaptchaTokenServiceImpl.java
  │   │   │                   │   └── UserServiceImpl.java
  │   │   │                   ├── KaptchaTokenService.java
  │   │   │                   └── UserService.java
  │   │   └── resources/          资源总目录
  │   │       ├── application-dev.properties         开发配置
  │   │       ├── application-prod.properties        产品配置
  │   │       ├── application.properties             当前配置
  │   │       ├── application-test.properties        测试配置
  │   │       ├── kaptcha.properties                 图片验证码配置
  │   │       ├── logback-spring.xml                 日志文件配置
  │   │       ├── mysql-webapi.cresql                数据库创建语句
  │   │       └── templates/                         web 模板目录
  │   │       │   ├── user/
  │   │       │   ├── login.html
  │   │       │   ......
  │   │       ├── static/                            静态资源目录
  │   │              ├── bootstrap-4.1.0/
  │   │              │   ├── css/
  │   │              │   │   ├── bootstrap.css
  │   │              │   │   ├── bootstrap.css.map
  │   │              │   │   ├── bootstrap-grid.css
  │   │              │   │   ├── bootstrap-grid.css.map
  │   │              │   │   ├── bootstrap-grid.min.css
  │   │              │   │   ├── bootstrap-grid.min.css.map
  │   │              │   │   ├── bootstrap.min.css
  │   │              │   │   ├── bootstrap.min.css.map
  │   │              │   │   ├── bootstrap-reboot.css
  │   │              │   │   ├── bootstrap-reboot.css.map
  │   │              │   │   ├── bootstrap-reboot.min.css
  │   │              │   │   └── bootstrap-reboot.min.css.map
  │   │              │   └── js
  │   │              │       ├── bootstrap.bundle.js
  │   │              │       ├── bootstrap.bundle.js.map
  │   │              │       ├── bootstrap.bundle.min.js
  │   │              │       ├── bootstrap.bundle.min.js.map
  │   │              │       ├── bootstrap.js
  │   │              │       ├── bootstrap.js.map
  │   │              │       ├── bootstrap.min.js
  │   │              │       └── bootstrap.min.js.map
  │   │              ├── css
  │   │              │   └── common.css
  │   │              └── js
  │   │                  └── jquery
  │   │                      ├── jquery-1.11.2.min.js
  │   │                      └── jquery.min.map
  │   └── test
  │       └── java
  │           └── com
  │               └── yourdomain
  │                   └── webapi/
  │                       ├── ApplicationTests.java
  │                       └── UserDocumentationTests.java        自动文档生成测试
  └── update-build.sh       源文件自动版本更新脚本
  ————————————————
  版权声明：本文为CSDN博主「车斗」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
  原文链接：https://blog.csdn.net/ubuntu64fan/article/details/80555915
  ```

  

## 二、参考

### 1、参考

0、[SpringBoot-MongoDB官网](https://docs.spring.io/spring-data/mongodb/docs/2.2.2.RELEASE/reference/html/#reference)

1、[SpringBoot+MongoDB 实现图片存取](https://blog.csdn.net/augustu1/article/details/89519163)

2、[SpringBoot中使用GridFS](https://blog.csdn.net/weixin_43794897/article/details/85146318)

3、[SpringBoot操作MongoDB Gridfs](https://www.jianshu.com/p/0595c0e26995)

4、[SpringBoot整合MongoDB JPA,测试MongoRepository与MongoTemplate用法,简单增删改查+高级聚合](https://blog.csdn.net/a1697752105/article/details/101777749)

5、[springboot集成mongodb使用mongoTemplate和MongoRepository](https://blog.csdn.net/lr131425/article/details/77648900)

6、[SpringBoot | 第三十一章：MongoDB的集成和使用](https://blog.lqdev.cn/2018/11/01/springboot/chapter-thirty-one/)

7、[如何在Springboot中使用slf4j记录日志](https://blog.csdn.net/zhuzhezhuzhe1/article/details/80557251)

8、[MongoDB + GridFS实现大文件的存储 +工具类](https://blog.csdn.net/Appleyk/article/details/79815894)



### 2、参考

[SpringBoot中使用GridFS](https://blog.csdn.net/weixin_43794897/article/details/85146318)

[springboot中使用GridFS上传文件、查询文件、删除文件](https://blog.csdn.net/weixin_44446298/article/details/88056161)

[SpringBoot使用mongoDB的GridFs进行上传文件，下载文件，删除文件等操作](https://blog.csdn.net/qq_40389276/article/details/101050250)

[Spring Boot使用GridFS实现文件的上传和下载](https://blog.csdn.net/qq_44693282/article/details/97916541)

[SpringBoot操作MongoDB Gridfs](https://www.jianshu.com/p/0595c0e26995)

[springBoot学习之mongoDB gridfs文件操作](https://blog.csdn.net/qw12312312/article/details/82288438)

[spring配置mongodb使用gridfs](https://blog.csdn.net/fuck487/article/details/78920003)

[使用mongodb对文件(图片、音频、视频)的存储、读取操作](https://blog.csdn.net/wang_zhi_peng2007/article/details/84915969)

[预览存储在mongoDB的文件（excel、word、PDF、图片）](https://blog.csdn.net/qq_25320187/article/details/78468387)

[spring boot 2.1.2 实现mongodb GridFSFile文件预览](https://blog.csdn.net/Amy126/article/details/88842746)

[mongodb存储图片和文件实践](https://blog.csdn.net/javahongxi/article/details/74131117)

[springboot2.0x集成mongodb提供GridFsTemplate类实现文件上传下载](https://blog.csdn.net/qq_42972094/article/details/82785441)

[Spring项目使用Mongodb中GridFS实现文件上传下载查找（附效果图）](https://blog.csdn.net/qq_39525799/article/details/86506182)

[MongodbGFS结合SpringBoot 实现大文件的简单上传与下载](https://blog.csdn.net/Cher1sh_zhaotong/article/details/79275956) +++++

[SpringBoot 集成 MongoDB 实现文件上传下载](https://blog.csdn.net/W3Chhhhhh/article/details/89479865) ++++

[微服务笔记之Spring Cloud 中使用MongoDB GridFS实现文件存储服务(Finchley)](https://blog.csdn.net/liuchunlin2008/article/details/84672362)

 

### 3、分类参考

- MongodbGFS结合SpringBoot 实现大文件的简单上传与下载

https://blog.csdn.net/Cher1sh_zhaotong/article/details/79275956

- 添加MongoDB配置类

https://blog.csdn.net/qq_44693282/article/details/97916541

https://blog.csdn.net/weixin_44446298/article/details/88056161

https://blog.csdn.net/qq_40389276/article/details/101050250

https://blog.csdn.net/qw12312312/article/details/82288438





### 4、登录

[springboot 整合 MongoDB 实现登录注册，html 页面获取后台参数的方法](https://www.cnblogs.com/ainyi/p/8605802.html)

[基于 MongoDB 及 Spring Boot 的文件服务器的实现](https://www.imooc.com/article/18443)   --分页查询

[基于vue-simple-uploader封装文件分片上传、秒传及断点续传的全局上传插件](https://www.cnblogs.com/xiahj/p/vue-simple-uploader.html)

[Java Spring boot + Mongodb + Vue +阿里云OSS 实现的电子相册](https://www.jianshu.com/p/6a9f0564f550)

### 5、

## 三、注意点

### 1、GridFSDBFile改为GridFSFile

1.1、 **注意**：springboot2.x时代，文件下载的时候使用的gridFsTemplate.findOne(query)返回类型由GridFSDBFile改为GridFSFile，所以下面这种方式不能用了 

```java
GridFSDBFile gridFSDBFile = gridFsTemplate.findOne(new Query().addCriteria(Criteria.where("_id").is(id)));
gridFSDBFile.writeTo(response.getOutputStream());

```

1.2、 **解决方案**：把GridFSFile 转成 GridFsResource 

-  做成一个bean配置 

  

参考：

 https://blog.csdn.net/han_chuang/article/details/91439516 

 https://blog.csdn.net/zhang_Red/article/details/81633535 





## 四、进一步开发

[SpringCloud + MongoDB 实现订单缓存](https://blog.csdn.net/zzg19950824/article/details/79426972)





## 五、案例

[Vue+SpringBoot项目实战](https://learner.blog.csdn.net/)



## 六、概念

- 前后端分离的意思是前后端之间通过 RESTful API 传递 JSON 数据进行交流。不同于 JSP 之类，后端是不涉及页面本身的内容的。 

- 在开发的时候，前端用前端的服务器（Ngix），后端用后端的服务器（Tomcat），当我开发前端内容的时候，可以把前端的请求通过前端服务器转发给后端（称为**反向代理**），这样就能实时观察结果，并且不需要知道后端怎么实现，而只需要知道接口提供的功能 。

- **正向代理**与**反向代理**



## 七、Vue知识点

### 1、Login不需要导航栏

登录页是不需要导航栏和侧边栏的，那么就需要规避掉登录页。

这时，就可以采用keep-alive结合$route.meta来实现这个功能。keep-alive 是 Vue 内置的一个组件，可以使被包含的组件保留状态，或避免重新渲染。$route.meta则可以选择让需要的页面才展示。

参考：https://blog.csdn.net/Mr_EvanChen/article/details/80847724

### 2、动态改变左侧导航显示内容

点击顶部导航栏动态改变左侧导航显示内容

https://blog.csdn.net/qq_42589862/article/details/90732617

### 3、views与components

虽然都是按组件方式写，但是作用功能区别很明显啊，`views`跟`components`怎么会区分不了呢。
你写个首页`Index.vue`这肯定是个 **页面views**
你写个首页头`IndexHeader.vue`这就是个 **组件components**

如果项目中是否引入了`vue-router`，简单理解成`vue-router`使用的组件是`views`就行了。



## 八、学习

- 八叉树

- ECharts

- 三维地震数据segy数据显示（java使用VTK）：https://blog.csdn.net/yanfeng1022/article/details/89553935

