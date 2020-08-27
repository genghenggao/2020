# Spring Boot

[参考文档](https://docs.spring.io/spring-boot/docs/2.1.4.RELEASE/reference/htmlsingle/#boot-features-spring-mvc-auto-configuration)

@**import**（）

​	给容器导入组件

1. **resources文件夹中目录结构**
- static：保存所有的静态资源
   - tempates：保存所有的模板页面；（Spring Boot默认jar包使用嵌入式的Tomcat，不支持JSP页面）；可以使用模板引擎（freemarket、thymeleaf）；
   - application.properties：Spring Boot应用的配置文件；可以修改一些默认参数;
   

------

**SpringBoot底层使用<u>slf4j + logback</u>进行日志记录**

------

## 模板引擎

- JSP
- Velocity
- Freemarker
- [Thymeleaf](https://www.thymeleaf.org/doc/tutorials/3.0/usingthymeleaf.html#literals)（SpringBoot推荐）

## 错误处理机制

### 1）、错误的定制页面

1. 有模板引擎的情乱下；**error/状态码**;

   页面能获取的信息：

   - timestamp：时间戳
   - status：状态码
   - error：错误提示
   - exception：异常对象
   - message：异常信息
   - errors：JSR303数据校验的错误				

2. 没有模板引擎（模板引擎下找不到这个错误页面），静态资源文件夹下找；

3. 以上都没有错误页面，就是默认来到SpringBoot默认的错误提示页面；

### 2）、如何定制JSON数据

1. 自定义;
2. 转发到/error进行自适应相应效果处理;
3. 将我们的定制数据携带出去;

## 配置嵌入式Servlet容器

### 1）、如何定制和修改Servlet容器

### 2）、注册三大组件【Servlet、Filter、Listener】



## 替换为其他的嵌入式Servlet容器

1. Tomcat
2. Jetty（长连接）
3. Undertow（不支持JSP）

## 外置Servlet容器

1）、必须创建一个war项目 ；

2）、将嵌入式Tomcat指定为provided ；

3）、必须SpringBootServletInitializer

4）、启动服务器就可以使用 ；



------

## SpringBoot与数据访问

效果 ：

​		默认用的是org.apache.tomcat.jdbc.pool.DataSource作为数据源 ；

​		数据源的相关配置在DataSourceProperties里面 ；

自动配置原理 ：

​	org.Springframework.boot.autoconfigure.jdbc  ；



## SpringBoot+Gradle测试



## JDBC测试



```properties
spring:
    datasource:
        username: root
        password: 123456
        url: jdbc:mysql://192.168.0.100:3307/jdbc
        driver-class-name: com.mysql.jdbc.Driver
```

## 整合基本JDBC与数据源

druid（阿里、成套的数据安全、监控） 、hikari（性能好）