import tracemalloc
import time

def process(line):
    pass  # 这里不考虑获取内容后的处理，process函数可以直接返回什么都不做

filepath = 'log.txt'

# 1. 直接读取文件内容到内存列表中
print("直接读取文件到内存列表中：")
tracemalloc.start()
start_time = time.time()

with open(filepath, 'r') as f:
    lines = f.readlines()

for line in lines:
    process(line)

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"内存占用：当前 {current / 10 ** 6} MB，峰值 {peak / 10 ** 6} MB")
print(f"用时：{end_time - start_time} 秒")

# 分割线
print("\n" + "=" * 40 + "\n")


# 2. 自定义迭代器实现文件读取
print("使用自定义迭代器逐行读取文件：")
tracemalloc.start()
start_time = time.time()

class LineIterator:
    def __init__(self, filepath):
        self.filepath = filepath
        self.file = open(filepath, 'r')

    def __iter__(self):
        return self

    def __next__(self):
        line = self.file.readline()
        if not line:
            self.file.close()
            raise StopIteration
        return line

line_iter = LineIterator(filepath)
for line in line_iter:
    process(line)

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"内存占用：当前 {current / 10 ** 6} MB，峰值 {peak / 10 ** 6} MB")
print(f"用时：{end_time - start_time} 秒")

# 分割线
print("\n" + "=" * 40 + "\n")


# 3. 使用生成器实现迭代器
print("使用生成器实现迭代器：")
tracemalloc.start()
start_time = time.time()


def line_generator(filepath):
    with open(filepath, 'r') as file:
        for line in file:
            if "Create" in line:  # 只处理包含 "Create" 的日志信息
                yield line


line_gen = line_generator(filepath)
for line in line_gen:
    process(line)

end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"内存占用：当前 {current / 10 ** 6} MB，峰值 {peak / 10 ** 6} MB")
print(f"用时：{end_time - start_time} 秒")