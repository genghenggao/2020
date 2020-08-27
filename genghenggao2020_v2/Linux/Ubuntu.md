## 常用命令操作

```shell
1、检查内核版本，必须是3.10及以上
uname -r
2、Ubuntu彻底清除history命令历史记录
# 第一步： 删除 .bash_history 文件
root@master:~# rm -rf ~/.bash_history
# 第二步： 清空命令历史记录
root@master:~# history -c
3、清理加速
#清理旧版本的软件缓存
hduser@master:~$ sudo apt-get autoclean
#清理所有软件缓存
hduser@master:~$ sudo apt-get clean
#删除系统不再使用的孤立软件
hduser@master:~$ sudo apt-get autoremove
```

## 安装Docker

（1）更新系统包索引

```shell
hduser@master:~$ sudo apt-get update
```

（2）添加HTTPS协议，允许apt从HTTPS安装软件包

```shell
hduser@master:~$ sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
```

（3）添加Docker 公共密钥

```shell
#Docker中科大源
hduser@master:~$ curl -fsSL https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
```

4）设置版本库类型（Ubuntu18.04对应版本**“bionic“”**），软件版本包括三种：** stable、edge、test**

```shell
#Docker中科大源
hduser@master:~$ sudo add-apt-repository "deb [arch=amd64] https://mirrors.ustc.edu.cn/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
```

安装Docker CE

（1）更新系统包索引

```shell
hduser@master:~$ sudo apt-get update
```

（2）安装最新版Docker CE

```shell
hduser@master:~$ sudo apt-get install docker-ce
```

使用的时候需要切换到root下。

## Ubuntu清理硬盘空间的8个技巧

前四个已经测试使用：

[参考链接]([https://www.linuxdashen.com/debianubuntu%E6%B8%85%E7%90%86%E7%A1%AC%E7%9B%98%E7%A9%BA%E9%97%B4%E7%9A%848%E4%B8%AA%E6%8A%80%E5%B7%A7](https://www.linuxdashen.com/debianubuntu清理硬盘空间的8个技巧))：

https://www.linuxdashen.com/debianubuntu%E6%B8%85%E7%90%86%E7%A1%AC%E7%9B%98%E7%A9%BA%E9%97%B4%E7%9A%848%E4%B8%AA%E6%8A%80%E5%B7%A7](https://www.linuxdashen.com/debianubuntu清理硬盘空间的8个技巧)



## Ubuntu遇到的问题

Ubuntu 18.04，开机后一直出现下列语句，一直卡在emergency mode 模式

```shell
welcome to emergency mode！after logging in ，type “journalctl -xb” to view system logs，“systemctl reboot” to reboot ，“systemctl
 default” to try again to boot into default mode。
give root password for maintenance（？？ Control-D？？？）：
```

原因解决方法： 

输入密码，回车~

之前修改过/etc/fstab 文件，新加了自动挂载的磁盘，但是自动挂载并未成功导致出现了此问题。

```shell
vi /etc/fstab
```

解决方法：先输入root密码，登陆root账户，然后打开/etc/fstab, 将之前自动挂载的内容注释掉，然后保存重启，就可以正常启动了