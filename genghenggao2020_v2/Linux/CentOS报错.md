# CentOS报错

[TOC]

## 报错一：因为断电出现错误

### 问题描述

```
generating “/run/initramfs/rdsosreport.txt”
entering emergencymode. exit the shell to continue
type “journalctl” to view system logs.
you might want to save “/run/initramfs/rdsosreport.txt” to a usb stick or /boot after mounting them and attach it to a bug report。
```



### 解决方法

操作步骤：
1、执行`xfs_repair /dev/mapper/centos-root` 或者`xfs_repair /dev/mapper/centos-root -L`

```
xfs_repair /dev/mapper/centos-root

#或者
xfs_repair /dev/mapper/centos-root -L
```

2、重启

```
reboot
```

