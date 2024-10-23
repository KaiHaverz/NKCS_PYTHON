# Lab01

## 1-基本信息

| 姓名     | 李懋                |
| -------- | ------------------- |
| 学号     | 2213189             |
| 年级     | 2022级              |
| IDE      | PyCharm PE 2024.1.4 |
| 操作系统 | macOS Sequoia 15.0  |
| 完成时间 | 2024.10.21          |



## 2-实验目的

1. 安装 python
2. 体验 python 的第三方功能



## 3-实验内容

### 3.1-python安装与虚拟环境配置

#### 3.1.1-python安装

1. 查看自己电脑中的python版本,并删除旧的版本

   ```python
   ls /usr/local/bin/python*
   #列出含有python的文件
   ```



![image-20241022142943959](../../../../../../../../Library/Application Support/typora-user-images/image-20241022142943959.png)

2. 从官网安装python最新版本 3.13.0

![image-20241022143008934](../../../../../../../../Library/Application Support/typora-user-images/image-20241022143008934.png)





3. 输入命令查看python版本

![image-20241022143038612](../../../../../../../../Library/Application Support/typora-user-images/image-20241022143038612.png)

4. 或者使用以下代码查看

```python
import sys
print(sys.version)
```

![image-20241022143140493](../../../../../../../../Library/Application Support/typora-user-images/image-20241022143140493.png)





#### 3.1.2-pip使用

- pip: python包管理工具





#### 3.1.3-虚拟环境

1. 作用:隔绝环境,避免污染
2. 安装方法

```python
pip3 install virtualenv
```

3. 我这里直接使用 venv

```shell
python3 -m venv myenv
```

4. 激活

```shell
source myenv/bin/activate
```

5. 退出: deactivate







### 3.2-iPython

1. pip install iPython
2. 输入 ipython,开始调用,提示符为 In [ ]:

![image-20241022143738266](../../../../../../../../Library/Application Support/typora-user-images/image-20241022143738266.png)

![image-20241022143805430](../../../../../../../../Library/Application Support/typora-user-images/image-20241022143805430.png)

3. PyCharm Console 自带 CPython,提示符>>>

![image-20241022143853519](../../../../../../../../Library/Application Support/typora-user-images/image-20241022143853519.png)





### 3.3 Python 之禅

- 在python console 中输入 import this

![image-20241022144410168](../../../../../../../../Library/Application Support/typora-user-images/image-20241022144410168.png)





### 3.4 MediaPipe

- MediaPipe是一款由Google开发并开源的数据流处理机器学习应用开发框架。支持面部检测、手势检测、人体骨骼检测、物体追踪等。



#### 3.4.1 手势识别实验

```python
import cv2
import mediapipe as mp

# 导入MediaPipe的绘图工具和手部解决方案
mp_drawing = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# 自定义绘制的颜色：荧光绿的线条，红色的关键点
hand_landmark_style = mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2)  #手部线条
hand_connection_style = mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=5)  #关键点

# 从摄像头获取视频输入
cap = cv2.VideoCapture(0)

# 使用Hands模型，设置检测和追踪的最小置信度为0.5
with mp_hands.Hands(
        min_detection_confidence=0.5,
        min_tracking_confidence=0.5) as hands:
    # 不断从摄像头读取帧
    while cap.isOpened():
        success, image = cap.read()
        if not success:
            print("无法读取摄像头帧，跳过该帧。")
            continue

        # 为了提升性能，可以将图像设置为不可写（传引用）
        image.flags.writeable = False
        # 将BGR颜色空间转换为RGB颜色空间
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # 处理图像，检测手部
        results = hands.process(image)

        # 将图像设置为可写状态
        image.flags.writeable = True
        # 将图像从RGB转换回BGR（因为OpenCV使用BGR显示）
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # 如果检测到手部标记点，进行绘制
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # 使用自定义样式绘制手部关键点和连接线
                mp_drawing.draw_landmarks(
                    image,
                    hand_landmarks,
                    mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=hand_connection_style,  # 红色关键点
                    connection_drawing_spec=hand_landmark_style  # 荧光绿线条
                )
                # 将翻转的图像保存到指定路径
                cv2.imwrite('result2.png', cv2.flip(image, 1))

        # 将图像水平翻转，以获得类似自拍的显示效果
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        # 按下空格键，退出循环
        if cv2.waitKey(5) & 0xFF == 32:
            break

# 释放摄像头资源
cap.release()

```

![image-20241022163407081](../../../../../../../../Library/Application Support/typora-user-images/image-20241022163407081.png)



### 3.5 天天向上

#### Q1

1. 代码
   1. 初始化成绩 1.0 ,浮点数
   2. 输入每日进步量,转化为浮点类型,便于后续的计算
   3. 定义一个函数
      1. 函数内部要声明全局变量
      2. 计算365天后的成绩
      3. 返回
   4. 输出,注意格式%f,控制小数位数

![image-20241022153602891](../../../../../../../../Library/Application Support/typora-user-images/image-20241022153602891.png)





#### Q2

1. 问题:工作日进步1%,休息日退步1%,工作5天,休息两天,问一年后的水平

![image-20241022160024812](../../../../../../../../Library/Application Support/typora-user-images/image-20241022160024812.png)

![image-20241022160145298](../../../../../../../../Library/Application Support/typora-user-images/image-20241022160145298.png)





#### Q3

1. A:工作日 260 天(近似),休息104天,B工作365天
2. 列出式子: (x^260) * (0.99^104) = (1.01^365)

![image-20241022161112730](../../../../../../../../Library/Application Support/typora-user-images/image-20241022161112730.png)





## 4-实验心得

1. MediaPipe是一个很有意思的库,能做一些比较有趣的内容,之后可以多研究,写一些更有趣的程序
2. 天天向上
   1. Q1:定义了一个函数写,通过输入进步和退步的幅度,最后输出,主要考察python的一些简单运算
   2. Q2:一年中260天工作,104天休息,近似一天忽略不计,然后直接计算出一年后的成绩
   3. Q3:列出式子分析,计算即可
3. 需要注意的点
   1. input输入是字符型
   2. %d %f %.2f 等等来控制输出的格式
   3. 程序写的尽量清晰
