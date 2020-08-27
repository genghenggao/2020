# Vue

[TOC]

## 一、Promise

- ES6可以通过Promise解决网络请求的回调问题

- 什么情况下会使用到Promise？
  - 一般情况下有异步操作，使用Promise对这个异步操作进行封装
  - new -> 构造函数(1.保存一些状态信息 2.导入传入的函数)
  - 再执行传入的回调函数时，会传入两个参数，resolve，reject。本身又是函数

#### 1、Promise的基本使用

新建文件夹，新建01-Promise的使用.html

```html
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-20 10:39:38
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-20 11:32:41
 -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <script>
        // 1、使用sertTimeout
        // setTimeout(() => {
        //     console.log("Hello World");
        // }, 1000);

        // 参数 -> 函数(resolve,reject)
        // resolve，reject本身也是函数
        // 链式编程
        new Promise((resolve, reject) => {
            // 第一次网络请求的代码
            setTimeout(() => {
                resolve()
            }, 1000);
        }).then(() => {
            // 第一次拿到结果的处理代码
            console.log("Hello World");
            console.log("Hello World");
            console.log("Hello World");
            console.log("Hello World");

            return new Promise((resolve, reject) => {
                //第二次网络请求的代码  
                setTimeout(() => {
                    resolve()
                }, 1000);
            })
        }).then(() => {
            // 第二次拿到结果的处理代码
            console.log('Hello Vuejs');
            console.log('Hello Vuejs');
            console.log('Hello Vuejs');
            console.log('Hello Vuejs');

            return new Promise((resolve, reject) => {
                // 第三次网络请求的代码
                setTimeout(() => {
                    resolve()
                }, 1000);
            })
        }).then(() => {
            // 第三次拿到结果的处理代码
            console.log('Hello Python');
            console.log('Hello Python');
            console.log('Hello Python');
            console.log('Hello Python');
        })


        new Promise((resolve, reject) => {
            setTimeout(() => {
                // 成功的时候调用resolve
                // resolve('Hello World')
                // 失败的时候调用reject
                reject('error message')
            }, 1000);
        }).then((data) => {
            console.log(data);
            console.log(data);
            console.log(data);
            console.log(data);
        }).catch((err) => {
            console.log(err);
        })
    </script>
</body>

</html>
```

#### 2、Promise的另一种使用

新建02-Promise的另一种使用.html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <script>
        new Promise((resolve, reject) => {
            setTimeout(() => {
                // resolve('Hello Vuejs')
                reject('error message')
            }, 1000)
        }).then(data => {
            console.log(data);

        }, err => {
            console.log(err);
        })
    </script>
</body>

</html>

```

#### 3、Promise的链式调用

3.1、新建03-Promise的链式调用(一).html

```html
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <script>
        // 参数 -> 函数(resolve,reject)
        // resolve，reject本身也是函数
        // 链式编程
        new Promise((resolve, reject) => {
            // 第一次网络请求的代码
            setTimeout(() => {
                resolve()
            }, 1000);
        }).then(() => {
            // 第一次拿到结果的处理代码
            console.log("Hello World");
            console.log("Hello World");
            console.log("Hello World");
            console.log("Hello World");

            return new Promise((resolve, reject) => {
                //第二次网络请求的代码  
                setTimeout(() => {
                    resolve()
                }, 1000);
            })
        }).then(() => {
            // 第二次拿到结果的处理代码
            console.log('Hello Vuejs');
            console.log('Hello Vuejs');
            console.log('Hello Vuejs');
            console.log('Hello Vuejs');

            return new Promise((resolve, reject) => {
                // 第三次网络请求的代码
                setTimeout(() => {
                    resolve()
                }, 1000);
            })
        }).then(() => {
            // 第三次拿到结果的处理代码
            console.log('Hello Python');
            console.log('Hello Python');
            console.log('Hello Python');
            console.log('Hello Python');
        })
    </script>
</body>

</html>
```

3.2、新建03-Promise的链式调用(二).html

```html
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-20 14:42:05
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-20 15:14:15
 -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <script>
        // 1、
        // new Promise((resolve, reject) => {
        //     setTimeout(() => {
        //         resolve('aaa')
        //     }, 1000);
        // }).then(res => {
        //     // 1.自己处理10行代码
        //     console.log(res, '第一层的10行处理代码');

        //     // 2.
        //     return new Promise((resolve) => {
        //         resolve(res + '111')
        //     })
        // }).then(res => {
        //     console.log(res, '第二层的10行处理代码');
        //     return new Promise(resolve => {
        //         resolve(res + '222')
        //     })
        // }).then(res => {
        //     console.log(res, '第三层的10行处理代码');
        // })

        // 2、new Promise(resolve => resolve(结果))简写 
        // new Promise((resolve, reject) => {
        //     setTimeout(() => {
        //         resolve('aaa')
        //     }, 1000);
        // }).then(res => {
        //     // 1.自己处理10行代码
        //     console.log(res, '第一层的10行处理代码');

        //     // 2.对结果进行第一次处理
        //     return  Promise.resolve(res + '111')
        // }).then(res => {
        //     console.log(res, '第二层的10行处理代码');
        //     return  Promise.resolve(res + '222')
        // }).then(res => {
        //     console.log(res, '第三层的10行处理代码');
        // })

        // 3、省略掉Promise.resolve
        // new Promise((resolve, reject) => {
        //     setTimeout(() => {
        //         resolve('aaa')
        //     }, 1000);
        // }).then(res => {
        //     // 1.自己处理10行代码
        //     console.log(res, '第一层的10行处理代码');

        //     // 2.对结果进行第一次处理
        //     return res + '111'
        // }).then(res => {
        //     console.log(res, '第二层的10行处理代码');
        //     return res + '222'
        // }).then(res => {
        //     console.log(res, '第三层的10行处理代码');
        // })


        // 4、省略掉Promise.resolve
        new Promise((resolve, reject) => {
            setTimeout(() => {
                resolve('aaa')
            }, 1000);
        }).then(res => {
            // 1.自己处理10行代码
            console.log(res, '第一层的10行处理代码');

            // 2.对结果进行第一次处理
            return Promise.reject('err message')
        }).then(res => {
            console.log(res, '第二层的10行处理代码');
            return res + '222'
        }).then(res => {
            console.log(res, '第三层的10行处理代码');
        }).catch(err => {
            console.log(err);
        })
    </script>
</body>

</html>
```

#### 4、Promsie的all方法使用

```html
<!--
 * @Description: henggao_learning
 * @version: v1.0.0
 * @Author: henggao
 * @Date: 2019-10-20 15:22:09
 * @LastEditors: henggao
 * @LastEditTime: 2019-10-20 15:30:33
 -->
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
</head>

<body>
    <script>
        Promise.all([
            // new Promise((resolve,reject) =>{
            //     $ajax({
            //         url:'url1',
            //         success:function(data){
            //             resolve(data)
            //         }
            //     })
            // }),
            // new Promise((resolve,reject) =>{
            //     $ajax({
            //         url:'url2',
            //         success:function(data){
            //             resolve(data)
            //         }
            //     })
            // })
            new Promise((resolve, reject) => {
                setTimeout(() => {
                    resolve({
                        name: 'hengga',
                        age: 18
                    })
                }, 2000);
            }),
            new Promise((resolve, reject) => {
                setTimeout(() => {
                    resolve({
                        name: 'Kobe',
                        age: 19
                    })

                }, 1000);
            })
        ]).then(results => {
            console.log(results)
        })
    </script>
</body>

</html>
```

