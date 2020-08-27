# MongoDB

[TOC]



## 一、MongoDBGidFS实现上传

- FileUploadController.java

```java
/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-11-26 14:23:41
 * @LastEditors: henggao
 * @LastEditTime: 2019-11-26 16:06:51
 */
package com.henggao.mongeostore_v1.controller;

import java.io.IOException;
import java.io.InputStream;
import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import org.bson.types.ObjectId;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.gridfs.GridFsTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import com.mongodb.gridfs.GridFS;
import com.mongodb.gridfs.GridFSDBFile;
import com.mongodb.gridfs.GridFSFile;

@Controller
@EnableAutoConfiguration
public class FileUploadController {

    // 获得SpringBoot提供的mongodb的GridFS对象
    @Autowired
    private GridFsTemplate gridFsTemplate;

    @Autowired
    private GridFS gridFS;

    // 工程主页
    @RequestMapping(value = "/", method = RequestMethod.GET)
    String home(Model model) {
        return "uploadForm";
    }

    // 上传文件控制器
    @RequestMapping(value = "/uploadfile", method = RequestMethod.POST)
    @ResponseBody
    String uploadfile(HttpServletRequest request) {
        String result = "error";
        try {
            /**
             * Servlet3.0新增了request.getParts()/getPart(String filename) api，
             * 用于获取使用multipart/form-data格式传递的http请求的请求体， 通常用于获取上传文件。
             */
            Part part = request.getPart("file");

            // 获得提交的文件名
            String filename = part.getSubmittedFileName();
            // 获得文件输入流
            InputStream ins = part.getInputStream();
            // 获得文件类型
            String contenttype = part.getContentType();
            // 将文件存储到mongodb中,mongodb 将会返回这个文件的具体信息
            ObjectId gfs = gridFsTemplate.store(ins, filename, contenttype);
 
			result = gfs.toString();
 
		} catch (IOException e) {
		} catch (ServletException e) {
			e.printStackTrace();
		}
		return result;
	}
 
	// 下载文件控制器
	@RequestMapping(value = "/downloadfile", method = RequestMethod.POST)
	@ResponseBody
	String downloadfile(@RequestParam(name = "fname", required = true) String filename, HttpServletResponse response) {
 
		/**
		 * 关于Query的具体用发下面的链接给的很清楚了，这里就不多说了。
		 * 
		 * @link{http://www.baeldung.com/queries-in-spring-data-mongodb}
		 */
		Query query = Query.query(Criteria.where("filename").is(filename));
 
		// 查询单个文件
        // GridFSDBFile gfsfile = gridFsTemplate.findOne(query);
        GridFSFile gfsfile = gridFsTemplate.findOne(query);
		// 通知浏览器进行文件下载
		response.setContentType(gfsfile.getContentType());
		response.setHeader("Content-Disposition", "attachment;filename=" + gfsfile.getFilename());
 
		try {
			gfsfile.writeTo(response.getOutputStream());
		} catch (IOException e) {
			e.printStackTrace();
		}
 
		return "success";
	}
 
}
```

- uploadForm.html

  ```html
  <!--
   * @Description: henggao_learning
   * @version: v1.0.0
   * @Author: henggao
   * @Date: 2019-11-26 14:18:21
   * @LastEditors: henggao
   * @LastEditTime: 2019-11-26 14:18:25
   -->
  <!DOCTYPE html>
   
  <html xmlns="http://www.w3.org/1999/xhtml"
        xmlns:th="http://www.thymeleaf.org">
  <head>
      <title>uploadForm</title>
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
  </head>
  <body>
  	<div>
  		<form method="POST" enctype="multipart/form-data" action="/uploadfile">
  				<input type="file" name="file" />
                  <input type="submit" value="上传" />
  		</form>
  		<form method="POST" action="/downloadfile">
  			<p>输入文件名<input type="text" name="fname" /></p>
  			 <input type="submit" value="下载" />
  		</form>
  	</div>
  </body>
  </html>
  ```

  

- application.yml

  ```yml
  spring:
    thymeleaf:
      mode: HTML5
      encoding: UTF-8
      servlet:
        content-type: text/html; charset=utf-8
      cache: false
    data:
      mongodb:
        uri: mongodb://192.168.55.110:20000/gridfs,192.168.55.111:20000/gridfs,192.168.55.112:20000/gridfs
        database: gridfs
    servlet:
    #uploadfile
      multipart:
        max-file-size:
          1024000KB
        max-request-size:
          2048000KB
  
  ```

  

```JAVA
/*
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-11-26 14:23:41
 * @LastEditors: henggao
 * @LastEditTime: 2019-11-27 10:51:11
 */
package com.henggao.mongeostore_v1.controller;

import java.io.IOException;
import java.io.InputStream;
import java.io.OutputStream;
import java.net.URLEncoder;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.Part;

import com.mongodb.client.gridfs.GridFSBucket;
import com.mongodb.client.gridfs.GridFSBuckets;
import com.mongodb.client.gridfs.GridFSDownloadStream;
import com.mongodb.client.gridfs.model.GridFSFile;
import org.apache.commons.io.IOUtils;
import org.bson.types.ObjectId;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.data.mongodb.MongoDbFactory;
import org.springframework.data.mongodb.core.query.Criteria;
import org.springframework.data.mongodb.core.query.Query;
import org.springframework.data.mongodb.gridfs.GridFsResource;
import org.springframework.data.mongodb.gridfs.GridFsTemplate;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

@Controller
@EnableAutoConfiguration
public class FileUploadController {

    Logger logger = LoggerFactory.getLogger(FileUploadController.class);
    // 获得SpringBoot提供的mongodb的GridFS对象
    @Autowired
    private GridFsTemplate gridFsTemplate;

    @Autowired
    private GridFSBucket gridFSBucket;

    @Autowired
    private MongoDbFactory mongoDbFactory;

    /**
     * 主页
     * 
     * @param model
     * @return
     */
    @RequestMapping(value = "/", method = RequestMethod.GET)
    String home(Model model) {
        return "uploadForm";
    }

    /**
     * 上传文件
     * 
     * @param request
     * @return
     */
    @RequestMapping(value = "/uploadfile", method = RequestMethod.POST)
    @ResponseBody
    String uploadFile(HttpServletRequest request) {
        String result = "error";
        try {
            /**
             * Servlet3.0新增了request.getParts()/getPart(String filename) api，
             * 用于获取使用multipart/form-data格式传递的http请求的请求体， 通常用于获取上传文件。
             */
            Part part = request.getPart("file");
            // 获得提交的文件名
            String filename = part.getSubmittedFileName();
            logger.info("Save File..." + filename);
            // 获得文件输入流
            InputStream ins = part.getInputStream();
            // 获得文件类型
            String contenttype = part.getContentType();
            // 将文件存储到mongodb中,mongodb 将会返回这个文件的具体信息
            ObjectId gfs = gridFsTemplate.store(ins, filename, contenttype);

            result = gfs.toString();

        } catch (IOException e) {
        } catch (ServletException e) {
            e.printStackTrace();
        }
        return result;
    }

    // 根据id查看文件
    @RequestMapping(value = "/queryfile")
    @ResponseBody
    public void queryFile(HttpServletResponse response, HttpServletRequest request) throws IOException {
        // 根据文件id查询文件
        GridFSFile gridFSFile = gridFsTemplate
                .findOne(Query.query(Criteria.where("_id").is("5ddccad1617c6e0d2168b7ba")));
        // 使用GridFsBucket打开一个下载流对象
        GridFSDownloadStream gridFSDownloadStream = gridFSBucket.openDownloadStream(gridFSFile.getObjectId());
        // 创建GridFsResource对象，获取流
        GridFsResource gridFsResource = new GridFsResource(gridFSFile, gridFSDownloadStream);
        // 从流中取数据
        String s = IOUtils.toString(gridFsResource.getInputStream(), "UTF-8");
        // System.out.println(s);
        logger.info("query" + s);
    }

    // 查询，预览文件（图片、PDF），下载
    @RequestMapping(value = "/queryfile1")
    @ResponseBody
    public void show(@RequestParam(name = "file_id") String fileId, String type, HttpServletResponse response,
            HttpServletRequest request) throws IOException {
        // GridFSFile gridFSFile = this.getById(fileId);
        Query query = Query.query(Criteria.where("_id").is(fileId));
        GridFSFile gfsFile = gridFsTemplate.findOne(query);
        if (gfsFile != null) {
            // mongo-java-driver3.x以上的版本就变成了这种方式获取
            GridFSBucket bucket = GridFSBuckets.create(mongoDbFactory.getDb());
            GridFSDownloadStream gridFSDownloadStream = bucket.openDownloadStream(gfsFile.getObjectId());
            GridFsResource gridFsResource = new GridFsResource(gfsFile, gridFSDownloadStream);
            String fileName = gfsFile.getFilename().replace(",", "");
            // 处理中文文件名乱码
            if (request.getHeader("User-Agent").toUpperCase().contains("MSIE")
                    || request.getHeader("User-Agent").toUpperCase().contains("TRIDENT")
                    || request.getHeader("User-Agent").toUpperCase().contains("EDGE")) {
                fileName = java.net.URLEncoder.encode(fileName, "UTF-8");
            } else {
                // 非IE浏览器的处理：
                fileName = new String(fileName.getBytes("UTF-8"), "ISO-8859-1");
            }

            response.setHeader("Content-Disposition", "inline;filename=\"" + fileName + "\"");

            IOUtils.copy(gridFsResource.getInputStream(), response.getOutputStream());
        }
    }

    // 下载文件
    // @RequestMapping(value = "/downloadfile", method = RequestMethod.POST)
    // @ResponseBody
    // String downloadfile(@RequestParam(name = "fname", required = true) String
    // filename, HttpServletResponse response) {
    @RequestMapping(value = "/downloadfile", method = RequestMethod.POST)
    @ResponseBody
    public void downloadfile(@RequestParam(name = "fname", required = true) String filename, HttpServletRequest request,
            HttpServletResponse response) throws IOException {
        logger.info("Get File..." + filename);
        Query query = Query.query(Criteria.where("filename").is(filename));
        // 查询单个文件
        GridFSFile gridFSFile = gridFsTemplate.findOne(query);
        if (gridFSFile == null) {
            return;
        }

        String fileName = gridFSFile.getFilename().replace(",", "");
        String contentType = gridFSFile.getMetadata().get("_contentType").toString();

        // 通知浏览器进行文件下载
        response.setContentType(contentType);
        response.setHeader("Content-Disposition",
                "attachment;filename=\"" + URLEncoder.encode(fileName, "UTF-8") + "\"");
        GridFSDownloadStream gridFSDownloadStream = gridFSBucket.openDownloadStream(gridFSFile.getObjectId());
        GridFsResource resource = new GridFsResource(gridFSFile, gridFSDownloadStream);

        OutputStream outputStream = response.getOutputStream();
        InputStream inputStream = resource.getInputStream();
        IOUtils.copy(inputStream, outputStream);
        outputStream.flush();
        outputStream.close();
        inputStream.close();
    }

    // 删除文件
    @RequestMapping(value = "/deleteFile")
    @ResponseBody
    public void deleteFile() throws IOException {
        // 根据文件id删除fs.files和fs.chunks中的记录
        gridFsTemplate.delete(Query.query(Criteria.where("_id").is("5ddccad1617c6e0d2168b7ba")));
        System.out.println("success");
    }

    // 删除文件
    @RequestMapping(value = "/deleteFile1")
    @ResponseBody
    public void deleteFiles(@RequestParam(value = "fileId") String fileId) throws IOException {
        // 根据文件id删除fs.files和fs.chunks中的记录
        Query query = Query.query(Criteria.where("_id").is(fileId));
        // 查询单个文件
        GridFSFile gfsfile = gridFsTemplate.findOne(query);
        if (gfsfile != null) {
            gridFsTemplate.delete(Query.query(Criteria.where("_id").is(fileId)));
            System.out.println("success");
        }
    }

}
```

