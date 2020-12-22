# Django＋Vue实现dwebsocket通信

[TOC]

## 0. 前言

- Django实现websocket大致上有两种方式，一种channels，一种是dwebsocket。channels依赖于redis，twisted等，相比之下使用dwebsocket要更为方便一些



## 1. Django

### 1.1  Python环境下安装

```
pip install dwebsocket
```



### 1.2 配置Django下的setttings.py文件

```
MIDDLEWARE = [
	...
	# 'dwebsocket.middleware.WebSocketMiddleware',# 为所有的URL提供websocket，如果只是单独的视图需要可以不选
]

WEBSOCKET_ACCEPT_ALL = True  # 可以允许每一个单独的视图实用websockets
```



### 1.3 views.py

```python
# 地震数据解析，下载云端数据
# @require_http_methods(['GET'])
@accept_websocket
def AnalysisCloudDown(request):

    if request.is_websocket():  # 如果请求是websocket请求：

        WebSocket = request.websocket
        print(WebSocket)
        i = 0  # 设置发送至前端的次数
        messages = {}

        while True:
            i += 1  # 递增次数 i
            time.sleep(1)  # 休眠1秒

            # 判断是否通过websocket接收到数据
            if WebSocket.has_messages():

                # 存在Websocket客户端发送过来的消息
                client_msg = WebSocket.read().decode()
                print(client_msg)
                # # 从数据库拿到数据
                seismic_obj = SeismicInfo.objects(id=client_msg).first()
                filename = seismic_obj.seismic_filename
                seismic_file = seismic_obj.filedata.read  # 注意这个地方不用加（）
                seismic_filensize = seismic_obj.filedata.length
                content_type = seismic_obj.filedata.content_type
                filename = filename + '.' + content_type
                # 数据写入服务器
                RECORD_SIZE = 1024*40  # 单位是B
                with open("../mongeostore_env/pic/%s" % filename, 'wb') as f:
                    # f.write(seismic_file)
                    # print(f.tell())
                    # print('save success')
                    records = iter(partial(seismic_file, RECORD_SIZE), b'')
                    for r in records:
                        f.write(r)
                        percent = int(f.tell()*100/seismic_filensize)
                        # print(percent)
                        # print(percent)
                        # print(f.tell())
                        # return HttpResponse(percent)

                        # 设置发送前端的数据
                        messages = {
                            # 'time': time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())),
                            # 'server_msg': 'send %d times!' % i,
                            'client_msg': client_msg,
                            'percent': percent
                        }
                        request.websocket.send(json.dumps(messages))
            # else:
            #     # 设置发送前端的数据
            #     messages = {
            #         'time': time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())),
            #         'server_msg': 'send %d times!' % i,
            #     }

            #     # 设置发送数据为json格式
            #     request.websocket.send(json.dumps(messages))
    else:
        try:#如果是普通的http方法
            message = request.GET['message']
            return HttpResponse(message)
        except:
            # return render(request,'index.html')
            return HttpResponse('test123')

```





- [ref](https://blog.csdn.net/u012887259/article/details/102804701?utm_medium=distribute.pc_relevant.none-task-blog-baidujs_title-11&spm=1001.2101.3001.4242)

- [ref](https://www.cnblogs.com/polly-ling/p/10173388.html)

- [ref](https://blog.csdn.net/weixin_47073925/article/details/106503752?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-4.control)

