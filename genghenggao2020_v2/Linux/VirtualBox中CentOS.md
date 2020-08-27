# VirtualBox中CentOS

[TOC]

## 一、新建虚拟机

1、创建虚拟机

![](IMG/微信截图_20190829170551.png)

2、输入名称

![](IMG/微信截图_20190829170655.png)

3、设置内存

![](IMG/微信截图_20190829170753.png)

4、创建虚拟磁盘

![**](IMG/微信截图_20190829170845.png)

![](IMG/微信截图_20190829170914.png)

![](IMG/微信截图_20190829170934.png)

![](IMG/微信截图_20190829171013.png)



## 二、安装`CentoOS7.6`

1、启动虚拟机

![](IMG/微信截图_20190829171216.png)

2、选择下载的ISO镜像

![](IMG/微信截图_20190829171306.png)

3、等待启动

![](IMG/微信截图_20190829171434.png)

4、选择语言

![](IMG/微信截图_20190829171630.png)

5、设置时间

![](IMG/微信截图_20190829171710.png)

![](IMG/微信截图_20190829171751.png)

6、设置界面

![](IMG/微信截图_20190829171819.png)

![](IMG/微信截图_20190829171955.png)

7、设置分区（可以默认，也可以自建分区，这里是自建分区）

![**](IMG/微信截图_20190829173836.png)

一、选择自动创建`Click here to create them automatically`。

![](IMG/微信截图_20190829201414.png)

二、点击`Accpet Changes`

![](IMG/微信截图_20190829201700.png)

以下是自己分配的，可以参考。

7.1 选择如何分区硬盘的方式“Standard Partition”，并点击下方“+”符号创建自定义磁盘空间

![](IMG/微信截图_20190829173049.png)

7.2第一步：创建/boot空间，大小设置为200，单位默认为MB，在实际的工作中可针对服务器的作用和性能调节此值的大小。

![](IMG/微信截图_20190829173251.png)

7.3第二步：创建swap的使用量，大小设置为2048，单位默认为MB，在实际的工作中可针对服务器的作用和性能调节此值的大小。

![](IMG/微信截图_20190829173359.png)

7.4第三步：创建`biosboot`空间，大小设置为1MB，此空间如果不创建在一些环境中系统将会出错。

![](IMG/微信截图_20190829173446.png)

7.5最后一步：创建/空间，大小设置为空，将划分余下的所有空间给/分区，在实际的工作中可针对服务器的作用和性能调节此值的大小。

![](IMG/微信截图_20190829173558.png)

7.6设置完成后可检查最后的设置情况，最后点击“Done”进入安装系统的下一步。

参考相应参数：

https://www.linuxidc.com/Linux/2019-04/158216.htm

![](IMG/微信截图_20190829173628.png)



![](IMG/微信截图_20190829173716.png)

分区参考：

https://jingyan.baidu.com/album/148a1921134d184d71c3b18d.html?picindex=3

https://www.cnblogs.com/set-config/p/9040407.html

8、开始安装

![](IMG/微信截图_20190829173934.png)

9、设置相关密码

![](IMG/微信截图_20190829174004.png)

9.1 设置root密码

![](IMG/微信截图_20190829174032.png)

9.2 设置用户密码

![](IMG/微信截图_20190829174112.png)

10、等待安装，重启。

![](IMG/微信截图_20190829175050.png)

11、授权

![](IMG/微信截图_20190829175349.png)

![](IMG/微信截图_20190829175414.png)

12、网络设置

![](IMG/微信截图_20190829175551.png)

![](IMG/微信截图_20190829175449.png)

12、完成

![](IMG/微信截图_20190829175627.png)

![](IMG/微信截图_20190829175720.png)

13、输入密码即可登录。



## 三、安装增强功能

`VirtualBox`安装一个`centos7.6`虚拟机，在安装增强功能的时候出现了，kernel headers not found for target kernel的错误。特记下我的解决方案。

1. update kernel

```shell
yum update kernel -y
```

2. Install the **kernel-headers, `kernel-devel`** and other required packages

```shell
yum install kernel-headers kernel-devel gcc make -y
```

3. Reboot the server to make sure it load to the new kernel

```shell
init 6
```

4.安装增强功能，重启即可。



## 四、设置网络

- 针对Windows宿主机防火墙（可以关闭，我这里是打开的），windows下`CMD`中`ipconfig`命令查看。

  ![](IMG/微信截图_20190827084253.png)

1、打开`VirtualBox`，设置。（先关闭CentOS`slave2`）

![](IMG/微信截图_20190829185808.png)

2、网卡1，使用NAT模式

![](IMG/微信截图_20190829185905.png)

3、添加一个网卡2，使用Host-Only模式

![](IMG/微信截图_20190829185905.png)

4、终端输入，`ip addr`，发现多了一张网卡`enp0s8`

![](IMG/微信截图_20190829190240.png)

5、切换到目录，查看。

```
cd /etc/sysconfig/network-scripts/

ls
```

![](IMG/微信截图_20190829190652.png)

6、使用root权限修改

```
vi ./ifcfg-enp0s3
```

![](IMG/微信截图_20190829191333.png)

7、保存，重启网络。

```
service  network restart
```

8、需要重启一下`slave2`，否则可能ping不通www.baidu.com

![](IMG/微信截图_20190829192015.png)

## 五、`Xshelll`远程连接`slave2`

1、输入相关信息

![](IMG/微信截图_20190829192435.png)

2、接受

![](IMG/微信截图_20190829192552.png)

3、输入用户名

![](IMG/微信截图_20190829192636.png)

4、输入密码

![](IMG/微信截图_20190829192740.png)

5、确定即可连接上。

## 六、修改用户名

1、将里面最下面的要改的用户名全部改成你想要改的。

```
vim /etc/passwd
```

![](IMG/微信截图_20190829193445.png)

2、将里面最下面的要改的用户名全部改成你想要改的。

```
vim /etc/passwd
```

![](IMG/微信截图_20190829193758.png)

3、将里面最下面的要改的用户名全部改成你想要改的。

```
vim /etc/shadow
```

![](IMG/微信截图_20190829194147.png)

4、替换旧的用户名

```shell
cd  /home  

mv huser hduser  #mv 旧用户名 新用户名
```

参考：

https://blog.csdn.net/low_down/article/details/85059696



## 七、`FinaShell`远程连接

- 和`XShell`不同，需要开启远程。

1、查看SSH是否安装：

```
[hduser@slave1 ~]$ rpm -qa | grep ssh
```

![](IMG/微信截图_20190829212803.png)

上图说明了 `centos 7` 默认安装了SSH包

2、安装缺失的包、并配置SSH。最后输入y。（切换到root权限）

```
[hduser@slave1 ~]$ su
Password: 
[root@slave1 hduser]# yum install openssh*
```

![](IMG/微信截图_20190829213126.png)

3、注册使用服务

```
[root@slave1 hduser]# systemctl enable sshd
```

4、配置`OpenSSH`服务（默认的就可以正常工作）

```
[root@slave1 hduser]# vim /etc/ssh/sshd_config 
```

5、重启`OpenSSH`服务

```
[root@slave1 hduser]# service sshd restart
```

6、打开`FinalShell`，输入信息连接。

![](IMG/微信截图_20190829213530.png)

`CentOS`启动SSH远程访问参考：

https://blog.csdn.net/ylanhds/article/details/80164006



## 八、`NotePad`++连接

1、先安装`NppFTP`插件

2、点击选择profile setting。

![](IMG/微信截图_20190829211028.png)

3、输入相关信息

![](IMG/微信截图_20190829210923.png)

4、点击选择连接。

![](IMG/微信截图_20190829211139.png)

5、查看如下

![](IMG/微信截图_20190829212626.png)

九、