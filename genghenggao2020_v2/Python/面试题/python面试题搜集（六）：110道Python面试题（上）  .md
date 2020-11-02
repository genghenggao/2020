python面试题搜集（六）：110道Python面试题（上）                                                    

**1、一行代码实现1--100之和**

利用sum()函数求和

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/40e8a9208b6444afbfed03f60b5d92b5.jpeg)

**2、如何在一个函数内部修改全局变量**

函数内部global声明 修改全局变量

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/a36301c0aecb498b84ef3a9f49b87b40.jpeg)

**3、列出5个python标准库**

os：提供了不少与操作系统相关联的函数

sys: 通常用于命令行参数

re: 正则匹配

math: 数学运算

datetime:处理日期时间

**4、字典如何删除键和合并两个字典**

del和update方法

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/ee574b10a7ce4a5aa2bfdc4a421039d4.jpeg)

**5、谈下python的GIL**

GIL  是python的全局解释器锁，同一进程中假如有多个线程运行，一个线程在运行python程序的时候会霸占python解释器（加了一把锁即GIL），使该进程内的其他线程无法运行，等该线程运行完后其他线程才能运行。如果线程运行过程中遇到耗时操作，则解释器锁解开，使其他线程运行。所以在多线程中，线程的运行仍是有先后顺序的，并不是同时进行。

多进程中因为每个进程都能被系统分配资源，相当于每个进程有了一个python解释器，所以多进程可以实现多个进程的同时运行，缺点是进程系统资源开销大

**6、python实现列表去重的方法**

先通过集合去重，在转列表

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/f49b686e64f340e3a7dc8bcab73e8a5a.jpeg)

**7、fun(\*args,\**kwargs)中的\*args,\**kwargs什么意思？**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/dd1a996b772d4bd4b7b23e1321518915.jpeg)

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/97f970c5dd9049369bbf3d8d51e27e7b.jpeg)

**8、python2和python3的range(100)的区别**

python2返回列表，python3返回迭代器，节约内存.

**9、一句话解释什么样的语言能够用装饰器?**

函数可以作为参数传递的语言，可以使用装饰器。

**10、python内建数据类型有哪些**

整型--int

布尔型--bool

字符串--str

列表--list

元组--tuple

字典--dict

**11、简述面向对象中__new__和__init__区别**

__init__是初始化方法，创建对象后，就立刻被默认调用了，可接收参数，如图

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/988372d37dee469f9f815e3f9702346f.jpeg)

1、__new__至少要有一个参数cls，代表当前类，此参数在实例化时由Python解释器自动识别。

2、__new__必须要有返回值，返回实例化出来的实例，这点在自己实现__new__时要特别注意，可以return父类（通过super(当前类名, cls)）__new__出来的实例，或者直接是object的__new__出来的实例。

3、__init__有一个参数self，就是这个__new__返回的实例，__init__在__new__的基础上可以完成一些其它初始化的动作，__init__不需要返回值。

4、如果__new__创建的是当前类的实例，会自动调用__init__函数，通过return语句里面调用的__new__函数的第一个参数是cls来保证是当前类实例，如果是其他类的类名，；那么实际创建返回的就是其他类的实例，其实就不会调用当前类的__init__函数，也不会调用其他类的__init__函数。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/70365bb075f34956addc33ed81d0e925.jpeg)

**12、简述with方法打开处理文件帮我我们做了什么？**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/0962ab0cef334ed7849f029f37e680e6.jpeg)

打开文件在进行读写的时候可能会出现一些异常状况，如果按照常规的f.open写法，我们需要try,except,finally，做异常判断，并且文件最终不管遇到什么情况，都要执行finally f.close()关闭文件，with方法帮我们实现了finally中f.close（当然还有其他自定义功能，有兴趣可以研究with方法源码）。

**13、列表[1,2,3,4,5]，请使用map()函数输出[1,4,9,16,25]，并使用列表推导式提取出大于10的数，最终输出[16,25]？**

map()函数第一个参数是fun，第二个参数是一般是list，第三个参数可以写list，也可以不写，根据需求。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/1e5dc8505a0c444cbc966b5dea9d8829.jpeg)

**14、python中生成随机整数、随机小数、0--1之间小数方法**

随机整数：random.randint(a,b),生成区间内的整数。

随机小数：习惯用numpy库，利用np.random.randn(5)生成5个随机小数。

0-1随机小数：random.random(),括号中不传参。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/66961832eee5488493be5ad27109589e.jpeg)

**15、避免转义给字符串加哪个字母表示原始字符串？**

r , 表示需要原始字符串，不转义特殊字符。

**16、中国，用正则匹配出标签里面的内容（“中国”），其中class的类名是不确定的。**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/5779faaf320a4eccbba47e3345d0f106.jpeg)

**17、python中断言方法举例**

assert（）方法，断言成功，则程序继续执行，断言失败，则程序报错。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/f3ad4e5b72154aa79c49a1ab66f7ce8b.jpeg)

**18、数据表student有id,name,score,city字段，其中name中的名字可有重复，需要消除重复行,请写sql语句**

select distinct name from student

**19、10个Linux常用命令**

ls pwd cd touch rm mkdir tree cp mv cat more grep echo

**20、python2和python3区别？列举5个**

1、Python3 使用 print 必须要以小括号包裹打印内容，比如 print('hi')

Python2 既可以使用带小括号的方式，也可以使用一个空格来分隔打印内容，比如 print 'hi'

2、python2 range(1,10)返回列表，python3中返回迭代器，节约内存

3、python2中使用ascii编码，python中使用utf-8编码

4、python2中unicode表示字符串序列，str表示字节序列

python3中str表示字符串序列，byte表示字节序列

5、python2中为正常显示中文，引入coding声明，python3中不需要

6、python2中是raw_input()函数，python3中是input()函数

**21、列出python中可变数据类型和不可变数据类型，并简述原理**

不可变数据类型：数值型、字符串型string和元组tuple不允许变量的值发生变化，如果改变了变量的值，相当于是新建了一个对象，而对于相同的值的对象，在内存中则只有一个对象（一个地址），如下图用id()方法可以打印对象的id。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/101d771d86d44ce7900138edde117929.jpeg)

可变数据类型：列表list和字典dict；允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，这里不存在引用计数，是实实在在的对象。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/6230573dcbd34690b48475d86f1839a5.jpeg)

**22、s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"**

set去重，去重转成list,利用sort方法排序，reeverse=False是从小到大排

list是不 变数据类型，s.sort时候没有返回值，所以注释的代码写法不正确。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/1892368a656e48f2842eb66bea8b78b6.jpeg)

**23、用lambda函数实现两个数相乘**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/10e7320ce74a4c74887b85e3fe8ea45b.jpeg)

**24、字典根据键从小到大排序**

dic={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/70604a718da047249b3d85ee2ea39eb8.jpeg)

**25、利用collections库的Counter方法统计字符串每个单词出现的次数"kjalfj;ldsjafl;hdsllfdhg;lahfbl;hl;ahlf;h"**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/efe2c795c0e643eabf525e2b68e28f1d.jpeg)

**26、字符串a = "not 404 found 张三 99 深圳"，每个词中间是空格，用正则过滤掉英文和数字，最终输出"张三 深圳"**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/e6b555253cd44fd8820257d548fc4a39.jpeg)

顺便贴上匹配小数的代码，虽然能匹配，但是健壮性有待进一步确认。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/2f1bf8a902c24c6fbce555b39bcb1516.jpeg)

**27、filter方法求出列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**

filter() 函数用于过滤序列，过滤掉不符合条件的元素，返回由符合条件元素组成的新列表。该接收两个参数，第一个为函数，第二个为序列，序列的每个元素作为参数传递给函数进行判，然后返回 True 或 False，最后将返回 True 的元素放到新列表。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/00a3cdddf8d54974a6d75f1a408fc242.jpeg)

**28、列表推导式求列表所有奇数并构造新列表，a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/d4f9b5f34b43420dbb8a343c53e0835c.jpeg)

**29、正则re.complie作用**

re.compile是将正则表达式编译成一个对象，加快速度，并重复使用。

30、a=（1，）b=(1)，c=("1") 分别是什么类型的数据？

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/b20516e6f3934c8185d1d697c6c8ab2e.jpeg)

**31、两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]**

extend可以将另一个集合中的元素逐一添加到列表中，区别于append整体添加。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/3abd424381d64af682b6ffaac7963700.jpeg)

**32、用python删除文件和用linux命令删除文件方法**

python：os.remove(文件名)

linux: rm 文件名

**33、log日志中，我们需要用时间戳记录error,warning等的发生时间，请用datetime模块打印当前时间戳 “2018-04-01 11:38:54”，顺便把星期的代码也贴上。**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/c876a8e14e5d40a5aec81c83bf74733e.jpeg)

**34、数据库优化查询方法**

外键、索引、联合查询、选择特定字段等等

**35、请列出你会的任意一种统计图（条形图、折线图等）绘制的开源库，第三方也行**

pychart、matplotlib

**36、写一段自定义异常代码**

自定义异常用raise抛出异常。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/b1da9d3d1cdd4496a4e98fa56d86de20.jpeg)

**37、正则表达式匹配中，（.\*）和（.\*?）匹配区别？**

（.*）是贪婪匹配，会把满足正则的尽可能多的往后匹配

（.*?）是非贪婪匹配，会把满足正则的尽可能少匹配

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/0ec2962c12a0452690b060da7a5e232d.jpeg)

**38、简述Django的orm**

ORM，全拼Object-Relation  Mapping，意为对象-关系映射。实现了数据模型与数据库的解耦，通过简单的配置就可以轻松更换数据库，而不需要修改代码只需要面向对象编程,orm操作本质上会根据对接的数据库引擎，翻译成对应的sql语句,所有使用Django开发的项目无需关心程序底层使用的是MySQL、Oracle、sqlite....，如果数据库迁移，只需要更换Django的数据库引擎即可。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/76a7b9cf0f054d288e51ea5d0487c7d5.jpeg)

**39、[[1,2],[3,4],[5,6]]一行代码展开该列表，得出[1,2,3,4,5,6]**

列表推导式的骚操作

运行过程：for i in a ,每个i是【1,2】，【3,4】，【5,6】，for j in i，每个j就是1,2,3,4,5,6,合并后就是结果。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/9f89f35c25744f588b899035f9a42cc5.jpeg)

还有更骚的方法，将列表转成numpy矩阵，通过numpy的flatten（）方法，代码永远是只有更骚，没有最骚

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/53e866ce06644f8da4d783ae997c7d9b.jpeg)

40、x="abc",y="def",z=["d","e","f"],分别求出x.join(y)和x.join(z)返回的结果

join()括号里面的是可迭代对象，x插入可迭代对象中间，形成字符串，结果一致，有没有突然感觉字符串的常见操作都不会玩了

顺便建议大家学下os.path.join()方法，拼接路径经常用到，也用到了join,和字符串操作中的join有什么区别，该问题大家可以查阅相关文档。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/b5b46c1eae954861ac56145c9b7285e4.jpeg)

**41、举例说明异常模块中try except else finally的相关意义**

try..except..else没有捕获到异常，执行else语句。

try..except..finally不管是否捕获到异常，都执行finally语句。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/0a0e0cb3225844cf813d80f101d3a4c2.jpeg)

**42、python中交换两个数值**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/ca3d3a00215948b4b4bd41289a206be4.jpeg)

**43、举例说明zip()函数用法**

zip()函数在运算时，会以一个或多个序列（可迭代对象）做为参数，返回一个元组的列表。同时将这些序列中并排的元素配对。

zip()参数可以接受任何类型的序列，同时也可以有两个以上的参数;当传入参数的长度不同时，zip能自动以最短序列长度为准进行截取，获得元组。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/58666e5c104c4738806b9b6a69baa1a5.jpeg)

**44、a="张明 98分"，用re.sub，将98替换为100**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/e73c0c2a4428426abec02e2b9b2f7b48.jpeg)

**45、写5条常用sql语句**

show databases;

show tables;

desc 表名;

select * from 表名;

delete from 表名 where id=5;

update students set gender=0,hometown="北京" where id=5

**46、a="hello"和b="你好"编码成bytes类型**

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/f436e86224a04a86adc1539c4f8adf57.jpeg)

**47、[1,2,3]+[4,5,6]的结果是多少？**

两个列表相加，等价于extend。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/7daad3163ae149908116395b0ec717fd.jpeg)

**48、提高python运行效率的方法**

1、使用生成器，因为可以节约大量内存

2、循环代码优化，避免过多重复代码的执行

3、核心模块用Cython PyPy等，提高效率

4、多进程、多线程、协程

5、多个if elif条件判断，可以把最有可能先发生的条件放到前面写，这样可以减少程序判断的次数，提高效率

**49、简述mysql和redis区别**

redis： 内存型非关系数据库，数据保存在内存中，速度快

mysql：关系型数据库，数据保存在磁盘中，检索的话，会有一定的Io操作，访问速度相对慢

**50、遇到bug如何处理**

1、细节上的错误，通过print（）打印，能执行到print（）说明一般上面的代码没有问题，分段检测程序是否有问题，如果是js的话可以alert或console.log。

2、如果涉及一些第三方框架，会去查官方文档或者一些技术博客。

3、对于bug的管理与归类总结，一般测试将测试出的bug用teambin等bug管理工具进行记录，然后我们会一条一条进行修改，修改的过程也是理解业务逻辑和提高自己编程逻辑缜密性的方法，我也都会收藏做一些笔记记录。

4、导包问题、城市定位多音字造成的显示错误问题。

**51、正则匹配，匹配日期2018-03-20**

url='https://sycm.taobao.com/bda/tradinganaly/overview/get_summary.json?dateRange=2018-03-20%7C2018-03-20&dateType=recent1&device=1&token=ff25b109b&_=1521595613462'

仍有同学问正则，其实匹配并不难，提取一段特征语句，用（.*?）匹配即可。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/890036117fac405ab1c4cfaf2cb47c69.jpeg)

**52、list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]**

利用min()方法求出最小值，原列表删除最小值，新列表加入最小值，递归调用获取最小值的函数，反复操作。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/87846fabee1741cca00fad04749d9aec.jpeg)

**53、写一个单列模式**

因为创建对象时__new__方法执行，并且必须return 返回实例化出来的对象所cls.__instance是否存在，不存在的话就创建对象，存在的话就返回该对象，来保证只有一个实例对象存在（单列），打印ID，值一样，说明对象同一个。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/dc4eb127b1d34707b621a41205824828.jpeg)

**54、保留两位小数**

题目本身只有a="%.03f"%1.3335,让计算a的结果，为了扩充保留小数的思路，提供round方法（数值，保留位数）。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/e3141adbfa104abfb310ecf60e6bdec5.jpeg)

**55、求三个方法打印结果**

fn("one",1）直接将键值对传给字典；

fn("two",2)因为字典在内存中是可变数据类型，所以指向同一个地址，传了新的额参数后，会相当于给字典增加键值对；

fn("three",3,{})因为传了一个新字典，所以不再是原先默认参数的字典。

![img](http://5b0988e595225.cdn.sohucs.com/images/20190328/31396b651c924d2292719b055669cbc2.jpeg)

来源网络，侵权删除[返回搜狐，查看更多](http://www.sohu.com/?strategyid=00001&spm=smpc.content.content.2.15783626202262BJK4jo)