### python面试题搜集（一）：2019 Python最新面试题及答案16道题吐血总结！50道Python面试题集锦（附答案）



Python是目前编程领域最受欢迎的语言。在本文中，我将总结Python面试中最常见的50个问题。每道题都提供参考答案，希望能够帮助你在2019年求职面试中脱颖而出，找到一份高薪工作。这些面试题涉及Python基础知识、Python编程、数据分析以及Python函数库等多个方面。

**Q1、Python中的列表和元组有什么区别？**

![img](https://upload-images.jianshu.io/upload_images/13717038-ed9cfb3318f3b043.jpg)

**Q2、Python的主要功能是什么？**

Python是一种解释型语言。与C语言等语言不同，Python不需要在运行之前进行编译。

Python是动态语言，当您声明变量或类似变量时，您不需要声明变量的类型。

<iframe scrolling="no" src="https://pos.baidu.com/s?hei=250&amp;wid=700&amp;di=u5677886&amp;ltu=https%3A%2F%2Fwww.lizenghai.com%2Farchives%2F19470.html&amp;psi=6491dccce6f1d3f6458137f687421622&amp;tcn=1578360715&amp;dri=1&amp;pis=-1x-1&amp;tlm=1578360714&amp;dis=0&amp;prot=2&amp;par=1846x1080&amp;ti=%E5%90%90%E8%A1%80%E6%80%BB%E7%BB%93%EF%BC%8150%E9%81%93Python%E9%9D%A2%E8%AF%95%E9%A2%98%E9%9B%86%E9%94%A6%EF%BC%88%E9%99%84%E7%AD%94%E6%A1%88%EF%BC%89%20%E2%80%93%20Python%E9%87%8F%E5%8C%96%E6%8A%95%E8%B5%84&amp;pcs=1829x972&amp;cfv=0&amp;ltr=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3D_VS-dxjBPrixBMFhdXXjaW6xQGcb7zKXm6MjTQypChDYMr3ILyrkLwPFzfx7K3ZsdFcgfYX1Qxci9kVPgIl1uq%26wd%3D%26eqid%3Dcc03f221000a7ab0000000055e13def3&amp;ant=0&amp;pss=1829x8942&amp;ccd=24&amp;cce=true&amp;ari=2&amp;dai=2&amp;drs=1&amp;exps=111000,110011&amp;chi=1&amp;dc=3&amp;cec=UTF-8&amp;col=zh-CN&amp;cmi=0&amp;cdo=-1&amp;tpr=1578360714793&amp;cja=false&amp;dtm=HTML_POST&amp;ps=894x364&amp;psr=1920x1080&amp;cpl=0" width="700" height="250" frameborder="0"></iframe>

Python适合面向对象的编程，因为它允许类的定义以及组合和继承。Python没有访问说明（如C ++的public，private）。

在Python中，函数是第一类对象。它们可以分配给变量。类也是第一类对象

编写Python代码很快，但运行比较慢。Python允许基于C的扩展，例如numpy函数库。

Python可用于许多领域。Web应用程序开发，自动化，数学建模，大数据应用程序等等。它也经常被用作“胶水”代码。

**Q3、Python是通用编程语言吗？**

Python能够编写脚本，但从一般意义上讲，它被认为是一种通用编程语言。

**Q4、Python是如何解释语言的？**

Python在运行之前不需要对程序进行解释。因此，Python是一种解释型语言。

**Q5、什么是pep？**

PEP代表Python Enhancement Proposal。它是一组规则，指定如何格式化Python代码以获得最大可读性。

**Q6、如何在Python中管理内存？**

python中的内存管理由Python私有堆空间管理。所有Python对象和数据结构都位于私有堆中。程序员无权访问此私有堆。python解释器负责处理这个问题。

Python对象的堆空间分配由Python的内存管理器完成。核心API提供了一些程序员编写代码的工具。

Python还有一个内置的垃圾收集器，它可以回收所有未使用的内存，并使其可用于堆空间。

**Q7、Python中的命名空间是什么？**

命名空间是一个命名系统，用于确保名称是唯一性，以避免命名冲突。

**Q8、什么是PYTHONPATH？**

它是导入模块时使用的环境变量。每当导入模块时，也会查找PYTHONPATH以检查各个目录中是否存在导入的模块。解释器使用它来确定要加载的模块。

**Q9、什么是python模块？Python中有哪些常用的内置模块？**

Python模块是包含Python代码的.py文件。此代码可以是函数类或变量。一些常用的内置模块包括：sys、math、random、data time、JSON。

**Q10、Python中的局部变量和全局变量是什么？**

全局变量：在函数外或全局空间中声明的变量称为全局变量。这些变量可以由程序中的任何函数访问。

局部变量：在函数内声明的任何变量都称为局部变量。此变量存在于局部空间中，而不是全局空间中。

**Q11、python是否区分大小写？**

是。Python是一种区分大小写的语言。

**Q12、什么是Python中的类型转换？**

类型转换是指将一种数据类型转换为另一种数据类型。

int（）  - 将任何数据类型转换为整数类型

float（）  - 将任何数据类型转换为float类型

ord（）  - 将字符转换为整数

hex（） – 将整数转换为十六进制

oct（）  - 将整数转换为八进制

tuple（） - 此函数用于转换为元组。

set（） - 此函数在转换为set后返回类型。

list（） - 此函数用于将任何数据类型转换为列表类型。

dict（） - 此函数用于将顺序元组（键，值）转换为字典。

str（） - 用于将整数转换为字符串。

complex（real，imag）  – 此函数将实数转换为复数（实数，图像）数。

**Q13、如何在Windows上安装Python并设置路径变量？**

要在Windows上安装Python，请按照以下步骤操作：

从以下链接安装python：https：//[http://www.python.org/downloads/](https://www.lizenghai.com/archives/https%3A%2F%2Flink.zhihu.com%2F%3Ftarget%3Dhttp%3A%2F%2Fwww.python.org%2Fdownloads%2F)

下载之后，将其安装在您的PC上。在命令提示符下使用以下命令查找PC上安装PYTHON的位置：cmd python。

然后转到高级系统设置并添加新变量并将其命名为PYTHON_NAME并粘贴复制的路径。

查找路径变量，选择其值并选择“编辑”。

如果值不存在，请在值的末尾添加分号，然后键入％PYTHON_HOME％

**Q14、python中是否需要缩进？**

缩进是Python必需的。它指定了一个代码块。循环，类，函数等中的所有代码都在缩进块中指定。通常使用四个空格字符来完成。如果您的代码没有必要缩进，它将无法准确执行并且也会抛出错误。

**Q15、Python数组和列表有什么区别？**

Python中的数组和列表具有相同的存储数据方式。但是，数组只能包含单个数据类型元素，而列表可以包含任何数据类型元素。

**Q16、Python中的函数是什么？**

函数是一个代码块，只有在被调用时才会执行。要在Python中定义函数，需要使用def关键字。

**Q17、什么是__init__?**

__init__是Python中的方法或者结构。在创建类的新对象/实例时，将自动调用此方法来分配内存。所有类都有__init__方法。

**Q18、什么是lambda函数？**

lambda函数也叫匿名函数，该函数可以包含任意数量的参数，但只能有一个执行操作的语句。

**Q19、Python中的self是什么？**

self是类的实例或对象。在Python中，self包含在第一个参数中。但是，Java中的情况并非如此，它是可选的。它有助于区分具有局部变量的类的方法和属性。init方法中的self变量引用新创建的对象，而在其他方法中，它引用其方法被调用的对象。

**Q20、区分break，continue和pass？**

![img](https://upload-images.jianshu.io/upload_images/13717038-124b7cb1f1cbba61.jpg)

**Q21、[:: – 1}表示什么？**

[:: – 1]用于反转数组或序列的顺序。

**Q22、如何在Python中随机化列表中的元素？**

可以使用shuffle函数进行随机列表元素。举例如下：



![img](https://upload-images.jianshu.io/upload_images/13717038-354910aa666694d9.png)

代码输出为：



![img](https://upload-images.jianshu.io/upload_images/13717038-55ccf76e0e0219db.png)

**Q23、什么是python迭代器？**

迭代器是可以遍历或迭代的对象。

**Q24、如何在Python中生成随机数？**

random模块是用于生成随机数的标准模块。该方法定义为：



![img](https://upload-images.jianshu.io/upload_images/13717038-8010fe0a7c7f5bde.png)

作者：千锋教育

链接：https://zhuanlan.zhihu.com/p/71913026

来源：知乎

著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

random.random()方法返回[0,1]范围内的浮点数。该函数生成随机浮点数。随机类使用的方法是隐藏实例的绑定方法。可以使用Random的实例来显示创建不同线程实例的多线程程序。其中使用的其他随机生成器是：

randrange(a,b)：它选择一个整数并定义[a，b]之间的范围。它通过从指定范围中随机选择元素来返回元素。它不构建范围对象。

uniform(a,b)：它选择一个在[a，b)范围内定义的浮点数

normalvariate(mean,sdev)：它用于正态分布，其中mean是平均值，sdev是用于标准偏差的sigma。

使用和实例化的Random类创建一个独立的多个随机数生成器。

**Q25、range＆xrange有什么区别？**

在大多数情况下，xrange和range在功能方面完全相同。它们都提供了一种生成整数列表的方法，唯一的区别是range返回一个Python列表对象，x  range返回一个xrange对象。这就表示xrange实际上在运行时并不是生成静态列表。它使用称为yielding的特殊技术根据需要创建值。该技术与一种称为生成器的对象一起使用。因此如果你有一个非常巨大的列表，那么就要考虑xrange。

**Q26、如何在python中写注释？**

Python中的注释以＃字符开头。也可以使用doc-strings（三重引号中包含的字符串）进行注释。

**Q27、什么是pickling和unpickling？**

Pickle模块接受任何Python对象并将其转换为字符串表示形式，并使用dump函数将其转储到文件中，此过程称为pickling。从存储的字符串中检索原始Python对象的过程称为unpickling。

**Q28、python中的生成器是什么？**

返回可迭代项集的函数称为生成器。

**Q29、你如何把字符串的第一个字母大写？**

在Python中，capitalize()函数可以将字符串的第一个字母大写。如果字符串在开头已经包含大写字母，那么它将返回原始字符串。

**Q30、如何将字符串转换为全小写？**

要将字符串转换为小写，可以使用lower()函数。

**Q31、如何在python中注释多行？**

注释多行代码时。所有要注释的行都要在开头前加#。还可以使用快捷方式来注释多行，就是按住Ctrl键并在每个想要包含＃字符的地方左键单击并键入一次＃。

**Q32、什么是Python中的文档Docstrings？**

Docstrings实际上不是注释，它们是文档字符串。这些文档字符串在三引号内。它们没有分配给任何变量，因此有时也用于注释。

**Q33、operators中的is、not和in各有什么功能？**

Operators是特殊函数，它们比较一个或多个值并产生相应的结果。其中is：当2个操作数为true时返回true（例如：“a”是’a’）

not：返回布尔值的倒数

in：检查某个元素是否存在于某个序列中

**Q34、Python中help()和dir()函数的用法是什么？**

Help()和dir()这两个函数都可以从Python解释器直接访问，并用于查看内置函数的合并转储。

help()函数：help()函数用于显示文档字符串，还可以查看与模块，关键字，属性等相关的使用信息。

dir()函数：dir()函数用于显示定义的符号。

**Q35、当Python退出时，为什么不清除所有分配的内存？**

当Python退出时，尤其是那些对其他对象具有循环引用的Python模块或者从全局名称空间引用的对象并没有被解除分配或释放。

无法解除分配C库保留的那些内存部分。

退出时，由于拥有自己的高效清理机制，Python会尝试取消分配/销毁其他所有对象。

**Q36、Python中的字典是什么？**

Python中的内置数据类型称为字典。它定义了键和值之间的一对一关系。字典包含一对键及其对应的值。字典由键索引。

**Q37、如何在python中使用三元运算符？**

三元运算符是用于显示条件语句的运算符。这包含true或false值，并且必须为其评估语句。其基本语法为：

三元运算符是用于显示条件语句的运算符。这包含true或false值，并且必须为其评估语句。其基本语法为：

[on_true] if [expression] else [on_false] x，y = 25,50big = x if x <y else y

**Q38、为什么使用\* args，\** kwargs？**

当我们不确定将多少个参数传递给函数，或者我们想要将存储的列表或参数元组传递给函数时，我们使用*  args。**当我们不知道将多少关键字参数传递给函数时使用kwargs，或者它可以用于将字典的值作为关键字参数传递。标识符args和kwargs是一个约定，你也可以使用* bob和** billy。

**Q39、len()函数有什么作用？**

len()函数可用于确定字符串，列表，数组等的长度。

**Q40、在Python中split()，sub()，subn()功能。**

如果要修改字符串，Python的“re”模块提供了3种方法。他们是：

split() – 使用正则表达式模式将给定字符串“拆分”到列表中。

sub() – 查找正则表达式模式匹配的所有子字符串，然后用不同的字符串替换它们

subn() – 它类似于sub()，并且还返回新字符串。

**Q41、什么是负指数，功能是什么？**

Python中的序列是索引的，它由正数和负数组成。积极的数字使用’0’作为第一个索引，’1’作为第二个索引，进程继续使用。

负数的索引从’-1’开始，表示序列中的最后一个索引，’ – 2’作为倒数第二个索引，序列像正数一样前进。

负索引用于从字符串中删除任何换行符，并允许该字符串除了作为S [： – 1]给出的最后一个字符。负索引还用于显示索引以正确的顺序表示字符串。

**Q42、什么是Python包？**

Python包是包含多个模块的命名空间。

**Q43、如何在Python中删除文件？**

要在Python中删除文件，您需要导入OS模块。之后，您需要使用os.remove()函数。

**Q44、什么是python的内置类型？**

Python中的内置类型如下：整型、浮点型、复数、字符串、布尔等。

**Q45、NumPy中有哪些操作Python列表的函数？**

Python的列表是高效的通用容器。它们支持（相当）有效的插入，删除，追加和连接，Python的列表推导使它们易于构造和操作。

它们有一定的局限性：它们不支持像素化加法和乘法等“向量化”操作，并且它们可以包含不同类型的对象这一事实意味着Python必须存储每个元素的类型信息，并且必须执行类型调度代码在对每个元素进行操作时。

NumPy不仅效率更高; 它也更方便。你可以免费获得大量的向量和矩阵运算，这有时可以避免不必要的工作。它们也得到有效实施。

NumPy数组更快，你可以使用NumPy，FFT，卷积，快速搜索，基本统计，线性代数，直方图等内置。

**Q46、如何将值添加到python数组？**

可以使用append()，extend()和insert(i，x)函数将元素添加到数组中。

**Q47、如何删除python数组的值？**

可以使用pop()或remove()方法删除数组元素。这两个函数之间的区别在于前者返回已删除的值，而后者则不返回。

**Q48、Python有OOps概念吗？**

Python是一种面向对象的编程语言。这意味着可以通过创建对象模型在python中解决任何程序。同时Python可以被视为程序语言和结构语言。

**Q49、深拷贝和浅拷贝有什么区别？**

在创建新实例类型时使用浅拷贝，并保留在新实例中复制的值。浅拷贝用于复制引用指针，就像复制值一样。这些引用指向原始对象，并且在类的任何成员中所做的更改也将影响它的原始副本。浅拷贝允许更快地执行程序，它取决于所使用的数据的大小。

深拷贝用于存储已复制的值。深拷贝不会将引用指针复制到对象。它引用一个对象，并存储一些其他对象指向的新对象。原始副本中所做的更改不会影响使用该对象的任何其他副本。由于为每个被调用的对象创建了某些副本，因此深拷贝会使程序的执行速度变慢。

**Q50、如何在Python中实现多线程？**

Python有一个多线程库，但是用多线程来加速代码的效果并不是那么的好，

Python有一个名为Global Interpreter Lock（GIL）的结构。GIL确保每次只能执行一个“线程”。一个线程获取GIL执行相关操作，然后将GIL传递到下一个线程。

虽然看起来程序被多线程并行执行，但它们实际上只是轮流使用相同的CPU核心。

所有这些GIL传递都增加了执行的开销。这意味着多线程并不能让程序运行的更快。