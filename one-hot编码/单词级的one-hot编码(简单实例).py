import numpy as np

samples = ['The cat sat on the mat.', 'The dog ate my homework.']

token_index = {}  # 索引字典
for sample in samples:
    for word in sample.split():
        if word not in token_index:
            token_index[word] = len(token_index) + 1  # 为每个唯一单词指定唯一索引。注意，没有为索引编号0指定单词

max_length = 10  # 对样本进行分词。只考虑每个样本前max_length个单词
results = np.zeros(shape=(len(samples),
                          max_length,
                          max(token_index.values()) + 1))

# print(results)

for i, sample in enumerate(samples):
    for j, word in list(enumerate(sample.split()))[:max_length]:
        index = token_index.get(word)
        results[i, j, index] = 1  # 将结果保存在results中

print(results)
