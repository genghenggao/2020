# YSCB测试MongoDB

- Centos7



## 0.前言

### 1.Java安装

- 此前装过java环境

- 验证

  ```
  java -version
  ```

  ![](IMG/微信截图_20210326211357.png)



### 2.Maven安装

#### 1.下载

- 到国内开源镜像下载Maven, 推荐使用[TUNA-清华开源镜像站](https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/)

  ![](IMG/微信截图_20210326210139.png)

  ```
  wget https://mirrors.tuna.tsinghua.edu.cn/apache/maven/maven-3/3.6.3/binaries/apache-maven-3.6.3-bin.tar.gz
  ```

  

- 补充一个概念🍎

  ```
  bin.tar.gz是适用于linux、MacOsX系统的二进制文件
  
  bin.zip是适用于windows的二进制文件
  
  src.tar.gz是linux下的源码
  
  src.zip是windows的源码
  ```

#### 2.配置Maven

##### 2.1 解压

```
tar -zxvf apache-maven-3.6.3-bin.tar.gz -C /usr/local
```

##### 2.2 MAVEN_HOME

```
sudo vim /etc/profile
```

添加内容

```
#Maven_home
export MAVEN_HOME=/usr/local/apache-maven-3.6.3
export PATH=${MAVEN_HOME}/bin:$PATH
```

![](IMG/微信截图_20210326211001.png)

#### 2.3 Source

```
source /etc/profile
```

- 注销或重启后生效( 不重启在当前Shell 下生效)

#### 2.4 验证

```
mvn -version
```

![](IMG/微信截图_20210326211307.png)



## 1.下载

```shell
curl -O --location https://github.com/brianfrankcooper/YCSB/releases/download/0.17.0/ycsb-0.17.0.tar.gz
```

- 下载了一个多小时，中间还断过几次，十分难受，所以当你遇到同样的情况的时候，不要慌~😂

## 2. 解压

```
tar xfvz ycsb-0.17.0.tar.gz
```

## 3.切到目录、可以查看信息

```
cd ycsb-0.17.0

./bin/ycsb
```

![](IMG/微信截图_20210326201519.png)

- 可以开始测试了，美滋滋~

- 查看workloads目录下的文件

```
cd workloads
```

![](IMG/微信截图_20210326201409.png)

- 在ycsb/workloads/目录下建立名为mongotest_in_only的文件，写入一下内容

```
#插入100万条文档数据

recordcount=1000000

operationcount=1000000

workload=com.yahoo.ycsb.workloads.CoreWorkload

readallfields=true

readproportion=0

updateproportion=0

scanproportion=0

#只有插入的操作,1就是100%

insertproportion=1

requestdistribution=uniform

insertorder=hashed

fieldlength=250

fieldcount=8

mongodb.url=mongodb://127.0.0.1:20000/ycsb?w=0

mongodb.writeConcern=acknowledged

threadcount=100
```



### 运行YCSB

- 命令在ycsb-0.17.0目录下🎈

现在你已经准备好运行了！首先，使用异步驱动程序来加载数据：

```
./bin/ycsb load mongodb-async -s -P workloads/workloada > outputLoad.txt
```

然后，运行工作负载：

```
./bin/ycsb run mongodb-async -s -P workloads/workloada > outputRun.txt
```



同样，要使用来自MongoDB Inc.的同步驱动程序，我们加载数据：

```
./bin/ycsb load mongodb -s -P workloads/workloada > outputLoad.txt
```

然后，运行工作负载：

```
./bin/ycsb run mongodb -s -P workloads/workloada > outputRun.txt
```



例如：

```
./bin/ycsb load mongodb-async -s -P workloads/workloada -p mongodb.url=mongodb://localhost:27017/ycsb?w=0
```

![](IMG/微信截图_20210326204631.png)

使用MongoDB公司的同步驱动程序运行：

```
./bin/ycsb load mongodb -s -P workloads/workloada -p mongodb.url=mongodb://localhost:27017/ycsb?w=0
```

![](IMG/微信截图_20210326204716.png)



```
bin/ycsb.sh load basic -P workloads/workloada
bin/ycsb.sh run basic -P workloads/workloada
```



下面有问题：

```
./bin/ycsb load mongodb -P workloads/mongotest_in_only -s >mongo_20210326.txt

./bin/ycsb run mongodb -P workloads/mongotest_read_only -s >mongo_20210326.txt

```



## YCSB进行MongoDB分片压力测试

- 可以制定mongodb连接（覆盖workloads/mongotest_in_only设置？）

```
./bin/ycsb load mongodb -threads 100 -s -P workloads/mongotest_in_only -p mongodb.url=mongodb://127.0.0.1:20000/ycsb?w=0 > outputLoad_shard.txt
```





## 问题

- 出现如下问题

![](IMG/微信截图_20210326214831.png)

- 初步分析是没有安装maven，重启服务

