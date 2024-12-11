import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import time

# 初始化全局变量
peg_a = []
peg_b = []
peg_c = []
positions = {1: peg_a, 2: peg_b, 3: peg_c}
peg_width = 1  # 柱子的宽度


# 初始化汉诺塔盘子
def initialize_disks(num_disks):
    global peg_a
    peg_a = list(range(num_disks, 0, -1))  # 盘子按从大到小的顺序放置在 peg_a
    peg_b.clear()
    peg_c.clear()


# 绘制当前汉诺塔状态
def draw_hanoi(num_disks):
    plt.clf()  # 清空之前的绘图
    ax = plt.gca()
    ax.set_xlim(-2, 4)  # x 轴范围
    ax.set_ylim(0, num_disks + 1)  # y 轴范围

    # 绘制柱子
    for i, peg in enumerate([peg_a, peg_b, peg_c]):
        ax.add_patch(Rectangle((i, 0), peg_width, num_disks, edgecolor='black', facecolor='gray'))

        # 绘制每个盘子
        for j, disk in enumerate(peg):
            disk_width = 0.5 + disk  # 每个盘子的宽度随编号增加
            rect = Rectangle((i + 0.5 - disk_width / 2, j + 1), disk_width, 0.5, edgecolor='black', facecolor='blue')
            ax.add_patch(rect)

    plt.pause(1)  # 动画每帧之间暂停1秒
    plt.draw()


# 递归汉诺塔解决函数
def hanoi(n, from_peg, to_peg, aux_peg, num_disks):
    if n == 1:
        move_disk(from_peg, to_peg)
        draw_hanoi(num_disks)
        return
    hanoi(n - 1, from_peg, aux_peg, to_peg, num_disks)
    move_disk(from_peg, to_peg)
    draw_hanoi(num_disks)
    hanoi(n - 1, aux_peg, to_peg, from_peg, num_disks)


# 盘子移动逻辑
def move_disk(from_peg, to_peg):
    if len(positions[from_peg]) == 0:
        print(f"错误: 尝试从空的柱子 {from_peg} 移动盘子")
        return
    disk = positions[from_peg].pop()  # 从原柱子移除盘子
    print(f"移动盘子 {disk} 从柱子 {from_peg} 到柱子 {to_peg}")  # 打印移动日志
    positions[to_peg].append(disk)  # 放到目标柱子上


# 主函数
if __name__ == "__main__":
    # 让用户输入盘子数量
    num_disks = int(input("请输入汉诺塔的盘子数量："))

    # 初始化
    initialize_disks(num_disks)
    print(f"初始状态：\n柱子1: {peg_a}\n柱子2: {peg_b}\n柱子3: {peg_c}")

    # 绘制初始状态
    plt.figure()
    draw_hanoi(num_disks)

    # 开始汉诺塔递归
    hanoi(num_disks, 1, 3, 2, num_disks)

    # 保持窗口打开
    plt.show()
