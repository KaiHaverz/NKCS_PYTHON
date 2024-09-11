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
                cv2.imwrite('./result2.png', cv2.flip(image, 1))

        # 将图像水平翻转，以获得类似自拍的显示效果
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))

        # 按下空格键，退出循环
        if cv2.waitKey(5) & 0xFF == 32:
            break

# 释放摄像头资源
cap.release()
