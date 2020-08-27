# Bootstrap_Demo2

1）、需要用到的插件

- [JQuery.js](https://jquery.com/)
- [Bootstrap](https://v3.bootcss.com/getting-started/)
- [Chart.js](https://cdn.jsdelivr.net/npm/chart.js@2.8.0/dist/Chart.min.js)

2）、编写index.html

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
  <title>MongoGeoStore</title>

  <!-- Bootstrap -->
  <link href="../static/css/bootstrap.min.css" rel="stylesheet">
  <link href="../static/css/bootstrap-geostore.css" rel="stylesheet">

</head>

<body>
  <!-- 导航 -->
  <nav class="navbar navbar-default ">
    <div class="container">
      <div class="navbar-header">
        <!-- 小屏幕按钮和logo -->
        <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a href="index.html" class="navbar-brand">GeoStore Admin</a>
        <!-- 小屏幕按钮和logo -->
      </div>

      <!-- 导航 -->
      <div class="navbar-collapse collapse">
        <ul class="nav navbar-nav ">
          <li class="active"><a href="index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;后台首页</a>
          </li>
          <li><a href="user_list.html"><span class="glyphicon glyphicon-user"></span>&nbsp;&nbsp;用户管理</a></li>
          <li><a href="content.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;内容管理</a></li>
          <li><a href="tag.html"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;标签管理</a></li>
        </ul>
        <ul class="nav navbar-nav navbar-right">
          <li class="dropdown">
            <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
              admin
              <span class="caret"></span>
            </a>
            <ul class="dropdown-menu" aria-labelledby="dLabel">
              <li><a href="index.html"><span class="glyphicon glyphicon-screenshot"></span> &nbsp;&nbsp;前台首页</a></li>
              <li><a href="index.html"><span class="glyphicon glyphicon-user"></span> &nbsp;&nbsp;个人主页</a></li>
              <li><a href="index.html"><span class="glyphicon glyphicon-cog"></span> &nbsp;&nbsp;个人设置</a></li>
              <li><a href="index.html"><span class="glyphicon glyphicon-credit-card"></span> &nbsp;&nbsp;账户中心</a></li>
              <li><a href="index.html"><span class="glyphicon glyphicon-heart"></span> &nbsp;&nbsp;我的收藏</a></li>
            </ul>
          </li>
          <li><a href="#bbs"><span class="glyphicon glyphicon-off"></span> &nbsp;&nbsp; 退出</a></li>
        </ul>
      </div>
      <!-- 导航 -->
    </div>
  </nav>
  <!-- 导航 -->

  <!-- 警告框 -->
  <div class="container">
    <div class="row">
      <div class="col-md-12">
        <div class="alert alert-danger alert-dismissible fade in" role="alert">
          <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
              aria-hidden="true">×</span></button>
          <h4>网站程序有漏洞，急需修护！</h4>
          <p>当前版本程序(V1.01)存在严重安全问题，容易造成攻击，请即刻修护！</p>
          <p>
            <button type="button" class="btn btn-danger">立即修护</button>
            <button type="button" class="btn btn-default" data-dismiss="alert">稍后处理</button>
          </p>
        </div>
      </div>
      <div class="col-md-6">
        <div class="panel panel-default">
          <div class="panel-heading">网站数据统计</div>
          <div class="panel-body">
            <table class="table table-hover">
              <thead>
                <tr>
                  <th>统计项目</th>
                  <th>今日</th>
                  <th>昨日</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <th scope="row">注册会员</th>
                  <td>2200</td>
                  <td>4400</td>
                <tr>
                  <th scope="row">登陆会员</th>
                  <td>11200</td>
                  <td>11400</td>
                <tr>
                  <th scope="row">今日发帖</th>
                  <td>2200</td>
                  <td>2400</td>
                </tr>
                <tr>
                  <th scope="row">转载次数</th>
                  <td>3200</td>
                  <td>5400</td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="panel panel-default">
          <div class="panel-heading">网站热点</div>
          <ul class="list-group">
            <li class="list-group-item">
              <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;地学数据的研究意思及其价值 <small
                  class="pull-right">2015/08/08</small></a>
            </li>
            <li class="list-group-item">
              <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;地学数据的研究意思及其价值 <small
                  class="pull-right">2015/08/08</small></a>
            </li>
            <li class="list-group-item">
              <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;地学数据的研究意思及其价值 <small
                  class="pull-right">2015/08/08</small></a>
            </li>
            <li class="list-group-item">
              <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;地学数据的研究意思及其价值 <small
                  class="pull-right">2015/08/08</small></a>
            </li>
            <li class="list-group-item">
              <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;地学数据的研究意思及其价值 <small
                  class="pull-right">2015/08/08</small></a>
            </li>
            <li class="list-group-item">
              <a href="index.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;地学数据的研究意思及其价值 <small
                  class="pull-right">2015/08/08</small></a>
            </li>
          </ul>
        </div>
      </div>
      <div class="col-md-6">
        <div class="panel panel-default">
          <div class="panel-heading">本周访客统计</div>
          <div class="panel-body">
            <canvas id="canvas" class="col-md-12"></canvas>
          </div>
        </div>
      </div>
      <div class="col-md-6">
        <div class="panel panel-default">
          <div class="panel-heading">服务器状态</div>
          <div class="panel-body">
            <p>内存使用率： 40%</p>
            <div class="progress">
              <div class="progress-bar progress-bar-success progress-bar-striped" role="progressbar" aria-valuenow="40"
                aria-valuemin="0" aria-valuemax="100" style="width: 40%">
                <span class="sr-only">40% Complete (success)</span>
              </div>
            </div>
            <p>数据库使用率： 20%</p>
            <div class="progress">
              <div class="progress-bar progress-bar-info progress-bar-striped" role="progressbar" aria-valuenow="20"
                aria-valuemin="0" aria-valuemax="100" style="width: 20%">
                <span class="sr-only">20% Complete</span>
              </div>
            </div>
            <p>磁盘使用率： 60%</p>
            <div class="progress">
              <div class="progress-bar progress-bar-warning progress-bar-striped" role="progressbar" aria-valuenow="60"
                aria-valuemin="0" aria-valuemax="100" style="width: 60%">
                <span class="sr-only">60% Complete (warning)</span>
              </div>
            </div>
            <p>CPU使用率： 80%</p>
            <div class="progress">
              <div class="progress-bar progress-bar-danger progress-bar-striped" role="progressbar" aria-valuenow="80"
                aria-valuemin="0" aria-valuemax="100" style="width: 80%">
                <span class="sr-only">80% Complete (danger)</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="col-md-12">
        <div class="panel panel-default">
          <div class="panel-heading">团队留言板</div>
          <div class="panel-body">
            <div class="col-md-7">
              <div class="media well">
                <div class="media-left">
                  <a href="#">
                    <img class="media-object wh64" src="../static/img/a.jpeg" alt="学士">
                  </a>
                </div>
                <div class="media-body">
                  <h4 class="media-heading">学士</h4>
                  地学数据的研究意思及其价值，需要我们深入思考。
                </div>
              </div>
              <div class="media well">
                <div class="media-body text-right">
                  <h4 class="media-heading">学弟</h4>
                  是呀，地学数据具有大数据的特点外，还具有自身的特点。
                </div>
                <div class="media-right">
                  <a href="#">
                    <img class="media-object wh64" src="../static/img/b.jpeg" alt="学弟">
                  </a>
                </div>
              </div>
              <div class="media well">
                <div class="media-body text-right">
                  <h4 class="media-heading">学弟</h4>
                  是呀，地学数据具有大数据的特点外，还具有自身的特点。
                </div>
                <div class="media-right">
                  <a href="#">
                    <img class="media-object wh64" src="../static/img/b.jpeg" alt="学弟">
                  </a>
                </div>
              </div>
              <div class="media well">
                <div class="media-left">
                  <a href="#">
                    <img class="media-object wh64" src="../static/img/a.jpeg" alt="学士">
                  </a>
                </div>
                <div class="media-body">
                  <h4 class="media-heading">学士</h4>
                  地学数据的研究意思及其价值，需要我们深入思考。
                </div>
              </div>
            </div>
            <div class="col-md-5">
              <form action="#">
                <div class="form-group">
                  <label for="text1">输入留言内容</label>
                  <textarea class="form-control" id="text1" cols="10" rows="5" placeholder="请输入留言内容"></textarea>
                  <button type="submit" class="btn btn-default mar_t15">留言</button>
                </div>
              </form>
              <div class="panel panel-default">
                <div class="panel-heading">团队联系手册</div>
                <div class="panel-body">
                  <ul class="list-group">
                    <li class="list-group-item">站长(张先生): <span
                        class="glyphicon glyphicon-phone"></span>&nbsp;15518501828</li>
                    <li class="list-group-item">技术(李女士): <span
                        class="glyphicon glyphicon-phone"></span>&nbsp;15518501828</li>
                    <li class="list-group-item">合作(王先生): <span
                        class="glyphicon glyphicon-phone"></span>&nbsp;15518501828</li>
                    <li class="list-group-item">客服(宋先生): <span
                        class="glyphicon glyphicon-phone"></span>&nbsp;15518501828 &nbsp;&nbsp;<span
                        class="glyphicon glyphicon-phone-alt"></span>&nbsp;&nbsp;010-88888888</li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>




  <!-- footer -->
  <footer>
    <div class="container">
      <div class="row">
        <div class="col=-md-12">
          <p>
            Copyright &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp; 京公网安备：110402430067号
          </p>
        </div>
      </div>
    </div>
  </footer>
  <!-- footer -->

  <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
  <script src="../static/js/jquery-3.4.1.min.js"></script>
  <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
  <script src="../static/js/bootstrap.min.js"></script>
  <script src="../static/js/Chart.min.js"></script>
  <script src="../static/js/script.js"></script>

</body>

</html>
```

3）、编写user_list.html

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>MongoGeoStore</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">
    <link href="../static/css/bootstrap-geostore.css" rel="stylesheet">

</head>

<body>
    <!-- 导航 -->
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <!-- 小屏幕按钮和logo -->
                <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="index.html" class="navbar-brand">GeoStore Admin</a>
                <!-- 小屏幕按钮和logo -->
            </div>

            <!-- 导航 -->
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav ">
                    <li><a href="index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;后台首页</a></li>
                    <li class="active"><a href="#user_list.html"><span
                                class="glyphicon glyphicon-user"></span>&nbsp;&nbsp;用户管理</a></li>
                    <li><a href="content.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;内容管理</a>
                    </li>
                    <li><a href="tag.html"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;标签管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            admin
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="dLabel">
                            <li><a href="index.html"><span class="glyphicon glyphicon-screenshot"></span>
                                    &nbsp;&nbsp;前台首页</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-user"></span> &nbsp;&nbsp;个人主页</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-cog"></span> &nbsp;&nbsp;个人设置</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-credit-card"></span>
                                    &nbsp;&nbsp;账户中心</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-heart"></span>
                                    &nbsp;&nbsp;我的收藏</a></li>
                        </ul>
                    </li>
                    <li><a href="#bbs"><span class="glyphicon glyphicon-off"></span> &nbsp;&nbsp; 退出</a></li>
                </ul>
            </div>
            <!-- 导航 -->
        </div>
    </nav>
    <!-- 导航 -->

    <div class="container">
        <div class="row">
            <div class="col-md-2">
                <div class="list-group">
                    <a href="user_list.html" class="list-group-item active">用户管理</a>
                    <a href="user_search.html" class="list-group-item">用户搜索</a>
                    <a href="" role="button" class="list-group-item" data-toggle="modal" data-target="#myModal">添加用户</a>
                </div>
            </div>
            <div class="col-md-10">
                <div class="page-header">
                    <h1>用户管理</h1>
                </div>
                <ul class="nav nav-tabs">
                    <li class="active">
                        <a href="user_list.html">用户列表</a>
                    </li>
                    <li>
                        <a href="user_search.html">用户搜索</a>
                    </li>
                    <!-- Button trigger modal -->
                    <li>
                        <a href="" role="button" data-toggle="modal" data-target="#myModal">添加用户</a>
                    </li>
                </ul>
                <table class="table">
                    <thead>
                        <tr>
                            <th>ID</th>
                            <th>用户名</th>
                            <th>邮箱</th>
                            <th>操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">1</th>
                            <td>李先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                    <tbody>
                        <tr>
                            <th scope="row">2</th>
                            <td>张先生</td>
                            <td>12345678@qq.com</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">锁定</a></li>
                                        <li><a href="#">修改密码</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>
                </table>
                <nav class="pull-right">
                    <ul class="pagination">
                        <li class="disabled"><a href="#" aria-label="Previous"><span
                                    aria-hidden="true">&laquo;</span></a></li>
                        <li class="active"><a href="#">1 </a></li>
                        <li><a href="#">2 </a></li>
                        <li><a href="#">3 </a></li>
                        <li><a href="#">4 </a></li>
                        <li><a href="#">5 </a></li>
                        <li><a href="#">6 </a></li>
                        <li><a href="#"><span aria-hidden="true">&raquo;</span></a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
        <div class="modal-dialog" role="document">
            <div class="modal-content">
                <div class="modal-header">
                    <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                            aria-hidden="true">&times;</span></button>
                    <h4 class="modal-title" id="myModalLabel">添加用户</h4>
                </div>
                <div class="modal-body">
                    <form action="#">
                        <div class="form-group">
                            <label for="addname">用户名</label>
                            <input type="text" id="addname" class="form-control" placeholder="用户名">
                        </div>
                        <div class="form-group">
                            <label for="addpassword">用户密码</label>
                            <input type="text" id="addpassword" class="form-control" placeholder="请输入用户密码">
                        </div>
                        <div class="form-group">
                            <label for="addpassword">确认用户密码</label>
                            <input type="text" id="addpassword" class="form-control" placeholder="请确认输入用户密码">
                        </div>
                        <div class="form-group">
                            <label for="addemail">请输入用户邮箱</label>
                            <input type="email" id="addemail" class="form-control" placeholder="请输入用户邮箱">
                        </div>
                        <div class="form-group">
                            <label for="addyonghuzu">所属用户组</label>
                            <select id="addyonghuzu" class="form-control">
                                <option>限制会员</option>
                                <option>新手上路</option>
                                <option>注册会员</option>
                                <option>中级会员</option>
                                <option>高级会员</option>
                            </select>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                    <button type="button" class="btn btn-primary">提交</button>
                </div>
            </div>
        </div>
    </div>
    <!-- footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col=-md-12">
                    <p>
                        Copyright &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp;
                        京公网安备：110402430067号
                    </p>
                </div>
            </div>
        </div>
    </footer>
    <!-- footer -->

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="../static/js/jquery-3.4.1.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="../static/js/bootstrap.min.js"></script>

</body>

</html>
```

4）、编写user_search.html

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>MongoGeoStore</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">
    <link href="../static/css/bootstrap-geostore.css" rel="stylesheet">

</head>

<body>
    <!-- 导航 -->
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <!-- 小屏幕按钮和logo -->
                <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="index.html" class="navbar-brand">GeoStore Admin</a>
                <!-- 小屏幕按钮和logo -->
            </div>

            <!-- 导航 -->
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav ">
                    <li><a href="index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;后台首页</a></li>
                    <li class="active"><a href="#user_list.html"><span
                                class="glyphicon glyphicon-user"></span>&nbsp;&nbsp;用户管理</a></li>
                    <li><a href="content.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;内容管理</a>
                    </li>
                    <li><a href="tag.html"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;标签管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            admin
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="dLabel">
                            <li><a href="index.html"><span class="glyphicon glyphicon-screenshot"></span>
                                    &nbsp;&nbsp;前台首页</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-user"></span> &nbsp;&nbsp;个人主页</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-cog"></span> &nbsp;&nbsp;个人设置</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-credit-card"></span>
                                    &nbsp;&nbsp;账户中心</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-heart"></span>
                                    &nbsp;&nbsp;我的收藏</a></li>
                        </ul>
                    </li>
                    <li><a href="#bbs"><span class="glyphicon glyphicon-off"></span> &nbsp;&nbsp; 退出</a></li>
                </ul>
            </div>
            <!-- 导航 -->
        </div>
    </nav>
    <!-- 导航 -->

    <div class="container">
        <div class="row">
            <div class="col-md-2">
                <div class="list-group">
                    <a href="user_list.html" class="list-group-item">用户管理</a>
                    <a href="user_search.html" class="list-group-item active">用户搜索</a>
                    <a href="" role="button" class="list-group-item" data-toggle="modal" data-target="#myModal">添加用户</a>
                </div>
            </div>
            <div class="col-md-10">
                <div class="page-header">
                    <h1>用户管理</h1>
                </div>
                <ul class="nav nav-tabs">
                    <li>
                        <a href="user_list.html">用户列表</a>
                    </li>
                    <li class="active">
                        <a href="user_search.html">用户搜索</a>
                    </li>
                    <!-- Button trigger modal -->
                    <li>
                        <a href="" role="button" data-toggle="modal" data-target="#myModal">添加用户</a>
                    </li>
                </ul>
                <form action="#" class="user_search">
                    <div class="alert alert-info" role="alert">
                        <strong>技巧提示： </strong>
                        支持模糊搜索和匹配搜索，匹配搜索使用*代替！
                    </div>
                    <div class="form-group">
                        <label for="name">用户名</label>
                        <input type="text" id="name" class="form-control" placeholder="请输入用户名">
                    </div>
                    <div class="form-group">
                        <label for="uid">UID</label>
                        <input type="text" id="uid" class="form-control" placeholder="输入用户UID">
                    </div>
                    <div class="form-group">
                        <label for="yonghuzu">选择用户组</label>
                        <select id="yonghuzu" class="form-control">
                            <option>限制会员</option>
                            <option>新手上路</option>
                            <option>注册会员</option>
                            <option>中级会员</option>
                            <option>高级会员</option>
                        </select>
                    </div>
                    <button type="submit" class="btn btn-default">提交</button>
                </form>
            </div>
            <!-- Modal -->
            <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close"><span
                                    aria-hidden="true">&times;</span></button>
                            <h4 class="modal-title" id="myModalLabel">添加用户</h4>
                        </div>
                        <div class="modal-body">
                            <form action="#">
                                <div class="form-group">
                                    <label for="addname">用户名</label>
                                    <input type="text" id="addname" class="form-control" placeholder="用户名">
                                </div>
                                <div class="form-group">
                                    <label for="addpassword">用户密码</label>
                                    <input type="text" id="addpassword" class="form-control" placeholder="请输入用户密码">
                                </div>
                                <div class="form-group">
                                    <label for="addpassword">确认用户密码</label>
                                    <input type="text" id="addpassword" class="form-control" placeholder="请确认输入用户密码">
                                </div>
                                <div class="form-group">
                                    <label for="addemail">请输入用户邮箱</label>
                                    <input type="email" id="addemail" class="form-control" placeholder="请输入用户邮箱">
                                </div>
                                <div class="form-group">
                                    <label for="addyonghuzu">所属用户组</label>
                                    <select id="addyonghuzu" class="form-control">
                                        <option>限制会员</option>
                                        <option>新手上路</option>
                                        <option>注册会员</option>
                                        <option>中级会员</option>
                                        <option>高级会员</option>
                                    </select>
                                </div>
                            </form>
                        </div>
                        <div class="modal-footer">
                            <button type="button" class="btn btn-default" data-dismiss="modal">关闭</button>
                            <button type="button" class="btn btn-primary">提交</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- footer -->
        <footer>
            <div class="container">
                <div class="row">
                    <div class="col=-md-12">
                        <p>
                            Copyright &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp;
                            京公网安备：110402430067号
                        </p>
                    </div>
                </div>
            </div>
        </footer>
        <!-- footer -->

        <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
        <script src="../static/js/jquery-3.4.1.min.js"></script>
        <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
        <script src="../static/js/bootstrap.min.js"></script>

</body>

</html>
```

5）、编写content.html

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>MongoGeoStore</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">
    <link href="../static/css/bootstrap-geostore.css" rel="stylesheet">

</head>

<body>
    <!-- 导航 -->
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <!-- 小屏幕按钮和logo -->
                <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="index.html" class="navbar-brand">GeoStore Admin</a>
                <!-- 小屏幕按钮和logo -->
            </div>

            <!-- 导航 -->
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav ">
                    <li><a href="index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;后台首页</a></li>
                    <li><a href="user_list.html"><span class="glyphicon glyphicon-user"></span>&nbsp;&nbsp;用户管理</a>
                    </li>
                    <li class="active"><a href="content.html"><span
                                class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;内容管理</a>
                    </li>
                    <li><a href="tag.html"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;标签管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            admin
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="dLabel">
                            <li><a href="index.html"><span class="glyphicon glyphicon-screenshot"></span>
                                    &nbsp;&nbsp;前台首页</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-user"></span> &nbsp;&nbsp;个人主页</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-cog"></span> &nbsp;&nbsp;个人设置</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-credit-card"></span>
                                    &nbsp;&nbsp;账户中心</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-heart"></span>
                                    &nbsp;&nbsp;我的收藏</a></li>
                        </ul>
                    </li>
                    <li><a href="#bbs"><span class="glyphicon glyphicon-off"></span> &nbsp;&nbsp; 退出</a></li>
                </ul>
            </div>
            <!-- 导航 -->
        </div>
    </nav>
    <!-- 导航 -->

    <div class="container">
        <div class="row">
            <div class="col-md-2">
                <div class="list-group">
                    <a href="content.html" class="list-group-item active">内容管理</a>
                    <a href="content_post.html" class="list-group-item">添加内容</a>
                </div>
            </div>
            <div class="col-md-10">
                <div class="page-header">
                    <h1>内容管理</h1>
                </div>
                <ul class="nav nav-tabs">
                    <li class="active">
                        <a href="content.html">内容管理</a>
                    </li>
                    <li>
                        <a href="content_post.html">添加内容</a>
                    </li>
                </ul>
                <table class="table">
                    <thead>
                        <tr>
                            <th>文章标题</th>
                            <th>作者</th>
                            <th>发布时间</th>
                            <th>操作</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row">地学数据的研究具有空间属性和时间属性的探讨</th>
                            <td>学士</td>
                            <td>2019/05/05</td>
                            <td>
                                <div role="presentation" class="dropdown">
                                    <button class="btn btn-default" data-toggle="dropdown" href="#" role="button"
                                        aria-haspopup="true" aria-expanded="false">
                                        操作 <span class="caret"></span>
                                    </button>
                                    <ul class="dropdown-menu">
                                        <li><a href="#">编辑</a></li>
                                        <li><a href="#">删除</a></li>
                                        <li><a href="#">全局置顶</a></li>
                                    </ul>
                                </div>
                            </td>
                        </tr>
                    </tbody>

                </table>
                <nav class="pull-right">
                    <ul class="pagination">
                        <li class="disabled"><a href="#" aria-label="Previous"><span
                                    aria-hidden="true">&laquo;</span></a></li>
                        <li class="active"><a href="#">1 </a></li>
                        <li><a href="#">2 </a></li>
                        <li><a href="#">3 </a></li>
                        <li><a href="#">4 </a></li>
                        <li><a href="#">5 </a></li>
                        <li><a href="#">6 </a></li>
                        <li><a href="#"><span aria-hidden="true">&raquo;</span></a></li>
                    </ul>
                </nav>
            </div>
        </div>
    </div>
    <!-- footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col=-md-12">
                    <p>
                        Copyright &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp;
                        京公网安备：110402430067号
                    </p>
                </div>
            </div>
        </div>
    </footer>
    <!-- footer -->

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="../static/js/jquery-3.4.1.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="../static/js/bootstrap.min.js"></script>

</body>

</html>
```

6）、编写content_post.html

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>MongoGeoStore</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">
    <link href="../static/css/bootstrap-geostore.css" rel="stylesheet">

</head>

<body>
    <!-- 导航 -->
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <!-- 小屏幕按钮和logo -->
                <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="index.html" class="navbar-brand">GeoStore Admin</a>
                <!-- 小屏幕按钮和logo -->
            </div>

            <!-- 导航 -->
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav ">
                    <li><a href="index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;后台首页</a></li>
                    <li><a href="#user_list.html"><span class="glyphicon glyphicon-user"></span>&nbsp;&nbsp;用户管理</a>
                    </li>
                    <li class="active"><a href="content.html"><span
                                class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;内容管理</a>
                    </li>
                    <li><a href="tag.html"><span class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;标签管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            admin
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="dLabel">
                            <li><a href="index.html"><span class="glyphicon glyphicon-screenshot"></span>
                                    &nbsp;&nbsp;前台首页</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-user"></span> &nbsp;&nbsp;个人主页</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-cog"></span> &nbsp;&nbsp;个人设置</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-credit-card"></span>
                                    &nbsp;&nbsp;账户中心</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-heart"></span>
                                    &nbsp;&nbsp;我的收藏</a></li>
                        </ul>
                    </li>
                    <li><a href="#bbs"><span class="glyphicon glyphicon-off"></span> &nbsp;&nbsp; 退出</a></li>
                </ul>
            </div>
            <!-- 导航 -->
        </div>
    </nav>
    <!-- 导航 -->

    <div class="container">
        <div class="row">
            <div class="col-md-2">
                <div class="list-group">
                    <a href="content.html" class="list-group-item">内容管理</a>
                    <a href="content_post.html" class="list-group-item active">添加内容</a>
                </div>
            </div>
            <div class="col-md-10">
                <div class="page-header">
                    <h1>内容管理</h1>
                </div>
                <ul class="nav nav-tabs">
                    <li>
                        <a href="content.html">内容管理</a>
                    </li>
                    <li class="active">
                        <a href="content_post.html">添加内容</a>
                    </li>
                </ul>
                <form action="#" class="mar_t15">
                    <div class="form-group">
                        <label for="title">标题</label>
                        <input type="text" id="title" class="form-control" placeholder="请输入文章标题">
                    </div>
                    <div class="form-group">
                        <label for="content">文章内容</label>
                        <textarea id="content" class="form-control" cols="10" rows="15"
                            placeholder="请输入文章正文部分"></textarea>
                    </div>
                    <div class="checkbox">
                        <label>
                            <input type="checkbox">全局置顶
                        </label>
                        <button type="submit" class="btn btn-default pull-right">发布文章</button>
                    </div>
                </form>

            </div>
        </div>
    </div>

    <!-- footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col=-md-12">
                    <p>
                        Copyright &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp;
                        京公网安备：110402430067号
                    </p>
                </div>
            </div>
        </div>
    </footer>
    <!-- footer -->

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="../static/js/jquery-3.4.1.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="../static/js/bootstrap.min.js"></script>

</body>

</html>
```

7）、编写tag.html

```html
<!DOCTYPE html>
<html lang="zh-CN">

<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <!-- 上述3个meta标签*必须*放在最前面，任何其他内容都*必须*跟随其后！ -->
    <title>MongoGeoStore</title>

    <!-- Bootstrap -->
    <link href="../static/css/bootstrap.min.css" rel="stylesheet">
    <link href="../static/css/bootstrap-geostore.css" rel="stylesheet">

</head>

<body>
    <!-- 导航 -->
    <nav class="navbar navbar-default">
        <div class="container">
            <div class="navbar-header">
                <!-- 小屏幕按钮和logo -->
                <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                    <span class="icon-bar"></span>
                </button>
                <a href="index.html" class="navbar-brand">GeoStore Admin</a>
                <!-- 小屏幕按钮和logo -->
            </div>

            <!-- 导航 -->
            <div class="navbar-collapse collapse">
                <ul class="nav navbar-nav ">
                    <li><a href="index.html"><span class="glyphicon glyphicon-home"></span>&nbsp;&nbsp;后台首页</a></li>
                    <li><a href="user_list.html"><span class="glyphicon glyphicon-user"></span>&nbsp;&nbsp;用户管理</a>
                    </li>
                    <li><a href="content.html"><span class="glyphicon glyphicon-list-alt"></span>&nbsp;&nbsp;内容管理</a>
                    </li>
                    <li class="active"><a href="tag.html"><span
                                class="glyphicon glyphicon-tags"></span>&nbsp;&nbsp;标签管理</a></li>
                </ul>
                <ul class="nav navbar-nav navbar-right">
                    <li class="dropdown">
                        <a id="dLabel" type="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                            admin
                            <span class="caret"></span>
                        </a>
                        <ul class="dropdown-menu" aria-labelledby="dLabel">
                            <li><a href="index.html"><span class="glyphicon glyphicon-screenshot"></span>
                                    &nbsp;&nbsp;前台首页</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-user"></span> &nbsp;&nbsp;个人主页</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-cog"></span> &nbsp;&nbsp;个人设置</a>
                            </li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-credit-card"></span>
                                    &nbsp;&nbsp;账户中心</a></li>
                            <li><a href="index.html"><span class="glyphicon glyphicon-heart"></span>
                                    &nbsp;&nbsp;我的收藏</a></li>
                        </ul>
                    </li>
                    <li><a href="#bbs"><span class="glyphicon glyphicon-off"></span> &nbsp;&nbsp; 退出</a></li>
                </ul>
            </div>
            <!-- 导航 -->
        </div>
    </nav>
    <!-- 导航 -->

    <div class="container">
        <div class="row">
            <div class="col-md-12">
                <div class="page-header">
                    <h1>TAG标签管理</h1>
                </div>
                <div class="col-md-12 pad0">
                    <form>
                        <div class="col-md-10">
                            <input class="form-control" placeholder="请输入要添加的标签">
                        </div>
                        <div class="col-md-2">
                            <button type="submit" class="btn btn-default">添加</button>
                        </div>
                    </form>
                </div>
                <div class="col-md-12 taglist">
                    <div class="alert alert-info alert-dismissible pull-left" role="alert">
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                                aria-hidden="true">&times;</span></button>
                        <strong>Bootstrap</strong>
                    </div>
                    <div class="alert alert-info alert-dismissible pull-left" role="alert">
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                                aria-hidden="true">&times;</span></button>
                        <strong>MongoDB</strong>
                    </div>
                    <div class="alert alert-info alert-dismissible pull-left" role="alert">
                        <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span
                                aria-hidden="true">&times;</span></button>
                        <strong>SpringBoot</strong>
                    </div>
                </div>
            </div>
        </div>
    </div>

    <!-- footer -->
    <footer>
        <div class="container">
            <div class="row">
                <div class="col=-md-12">
                    <p>
                        Copyright &nbsp;©&nbsp;2018-2022&nbsp;&nbsp;www.mongogeostore.com&nbsp;&nbsp;
                        京公网安备：110402430067号
                    </p>
                </div>
            </div>
        </div>
    </footer>
    <!-- footer -->

    <!-- jQuery (Bootstrap 的所有 JavaScript 插件都依赖 jQuery，所以必须放在前边) -->
    <script src="../static/js/jquery-3.4.1.min.js"></script>
    <!-- 加载 Bootstrap 的所有 JavaScript 插件。你也可以根据需要只加载单个插件。 -->
    <script src="../static/js/bootstrap.min.js"></script>

</body>

</html>
```

8）、编写bootstarp-geostore.css

```css
body {
    font-family: 'Microsoft YaHei', sans-serif;
}

/* 进度条下边距 */
.progress {
    margin-bottom: 9px;
}

/* 头像 */
.wh64 {
    width: 64px;
    height: 64px;
    border-radius: 50%;
}

/* 边距 */
.mar_t15 {
    margin-top: 15px;
}

/* padding */
.pad0 {
    padding: 0;
}

/*page-header  */
.page-header {
    margin-top: 0;
}

.page-header h1 {
    margin: 0;
    font-size: 16px;
}

/* .user_searc */
.user_search {
    padding: 10px;
    border: solid 1px #ddd;
    border-top: none;
}

/* tag */
.taglist {
    padding-top: 15px;
}

.taglist .alert {
    margin: 0 15px 15px 0;
}

/* footer */
footer {
    font-weight: 400px;
    text-align: center;
    padding: 20px;
}
```

