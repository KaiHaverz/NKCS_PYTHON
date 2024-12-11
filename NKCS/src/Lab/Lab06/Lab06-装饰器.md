# Lab06-装饰器

## 1 基本信息

| **姓名**     | **李懋**          |
| ------------ | ----------------- |
| **学号**     | **2213189**       |
| **实验题目** | **Python 装饰器** |
| **完成时间** | **2024.11.1**     |



## 2 实验目的

- 复习并练习 Python 装饰器



## 3 实验内容

- 参考资料：菜鸟教程 https://www.runoob.com/w3cnote/python-func-decorators.html

### 3.1 问答题

- 见云文档：https://nankai.feishu.cn/docx/RTJTdY2JWoBPuIxt7z3cJ42Vncf



### 3.2 编程题

#### 3.2.1 基础题

- 实现一个**装饰器**，通过一次调用使函数重复执行5次

![image-20241106204349047](E:\TyporaPictures\image-20241106204349047.png)

- 改写后

![image-20241106204519183](E:\TyporaPictures\image-20241106204519183.png)



#### 3.2.2 进阶题

1. 在通讯录的基础上，进行扩展
   1. 通过编写装饰器，为每个**功能模块函数**的每次调用设置认证。要求：
      - 每次调用函数的时候需要验证用户是否登录。如果未登录要求用户进行登录，并提示用户输入用户名和密码（与文件中的信息对比），成功后调用函数；如果已经登录则直接调用函数
   2. 在上述的基础上，编写装饰器，为**每个函数**添加记录调用的功能
      - 每次调用函数的时候，都将调用的**函数名**和**调用时间**记录在**文本文件**当中

![img](https://nankai.feishu.cn/space/api/box/stream/download/asynccode/?code=ZWM4ZWViMTBmYTcyMjAwMGI2NGMxODlkYWRkMzcyYTJfNXVVQ3JWMWhIbVBKVjUydmNzUFR0UlZYS0dUd0dGZkNfVG9rZW46Ym94Y25KVHV4QTRMeDdrOHk0SUE3Z3BmeTViXzE3MzA4OTg5NDc6MTczMDkwMjU0N19WNA)



2. **涉及到的知识点与问题：**

- 文件的读取
  - 如何将文本文件读取为其他数据结构，比如dict？可能需要结合使用高阶函数？
- 装饰器的嵌套
  - 既想要验证登录，又想要记录日记，就需要多层装饰器嵌套。这时候装饰器先运行哪一个（参考问答题第四题）？如果需要记录装饰器函数的名称需要怎么办？
    - [Python functools.wraps 详解_jiang_huixin的博客-CSDN博客_@functools.wraps](https://blog.csdn.net/jiang_huixin/article/details/112468649)
  - 或许交换装饰器的顺序可以改善这种情况？

![image-20241106221903272](E:\TyporaPictures\image-20241106221903272.png)

![image-20241106221913403](E:\TyporaPictures\image-20241106221913403.png)



#### 3.2.3 附加题

- 编写下载网页内容的函数，要求：

  - 用户传入一个url，函数返回下载页面的结果（存储在html格式文件中）

  - 编写装饰器，实现缓存网页内容功能
    -  当传入url时，如果缓存文件内有值（文件大小不为0），就优先从缓存文件中读取网页的内容。否则就去下载页面，之后缓存在文件中。

- **例如：**
  -  用户输入百度网址，程序发现没有下载过，于是将百度网页进行下载并保存为缓存文件“baidu.html”，并打开了这个文件。当用户再次输入百度的网址时，程序发现本地已经有“baidu.html”，则不需要再次从服务器对网页进行下载了，只需要打开这个本地文件即可。

![image-20241106220619831](E:\TyporaPictures\image-20241106220619831.png)



## 4 实验心得

1. 多查看菜鸟教程，很完整，多上手实现代码
2. 认真做问答题，期末可能有原题（相似的）



## 5 源代码

- 见附件
- Github仓库