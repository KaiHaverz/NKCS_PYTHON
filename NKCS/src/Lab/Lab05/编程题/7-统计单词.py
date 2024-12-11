import re
from collections import Counter

# 读取文件内容
with open('hamlet.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 剔除特殊符号
text = re.sub(r'[^a-zA-Z\s]', '', text)

# 将文本转换为小写
text = text.lower()

# 分割文本为单词列表
words = text.split()

# 统计单词频率
word_counts = Counter(words)

# 获取出现最多的10个单词
most_common_words = word_counts.most_common(10)

# 输出结果
for word, count in most_common_words:
    print(f'{word}: {count}')