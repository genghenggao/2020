# Project

[TOC]

## 一、初始化项目

1、VScode使用SpringBoot构建maven

![](IMG/微信截图_20191118213238.png)

2、看一下初始化目录结构

![](IMG/微信截图_20191118213422.png)

## 二、SpringBoot+MongoDB 实现图片存取

1、在pom.xml添加MongoDB依赖（在初始化阶已经添加）

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-mongodb</artifactId>
</dependency>
```

![](IMG/微信截图_20191118101620.png)

2、创建application.yml配置文件（也可以在application.properties中配置）

```yml
spring:
    data:
        mongodb:
          uri: mongodb+srv://henggao:henggao@mongeostore-tgjjd.mongodb.net/test?retryWrites=true&w=majority
```

3、建立图片实体UploadFile.java

```java
/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-11-18 21:21:49
 * @LastEditors: henggao
 * @LastEditTime: 2019-11-18 21:31:44
 */
package com.henggao.mongeostore.domain;

import java.util.Date;

import org.bson.types.Binary;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import lombok.Data;

/**
 * geofiles 
 * 实现图片存取
 */
@Document
@Data
public class GeoFiles {

    @Id
    private String id;
    private String name;    //文件名
    private Date createdTime;   //上传时间
    private Binary content; //文件内容
    private String contentType; //文件类型
    private long size; //文件大小 
}
```

-  此处 id 的类型要设置为 String ，MongoDB 会自动分配 id ，设置为数值型会报错。 
-  [BSON](https://docs.mongodb.com/manual/reference/glossary/#term-bson) 是一个二进制序列化格式，在MongoDB里面被用来做文档存储和远程程序调用，我们使用 org.bson.types.Binary 类来封装文件内容。`new Binary(byte[] byte)` 

4、上传图片

```

```





## 三、Records

**注意：当使用`MongoRepositories`时，可能有些`MongoRepositories`类不在默认的包路径(启动类路径)下，可使用`@EnableMongoRepositories`的`basePackages`需要扫描的路径信息。若都在默认的包路径下，可以不加此注解的。** 