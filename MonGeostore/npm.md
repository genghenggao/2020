# NPM

[TOC]

#### npm install xxx

安装一个依赖到命令运行目录`node_modules`下。`node_modules`不存在会被创建。

#### npm install xxx -g

全局安装一个依赖,多用于安装一个全局命令，如'XXX-cli'

#### npm install xxx --save

安装一个依赖到命令运行目录`node_modules`下，并将依赖配置写入命令运行目录下的`package.json` `dependencies`节点下

#### npm install xxx --save-dev

安装一个依赖到命令运行目录`node_modules`下，并将依赖配置写入命令运行目录下的`package.json` `devDependencies`节点下

