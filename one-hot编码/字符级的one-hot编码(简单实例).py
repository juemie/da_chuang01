import string
import numpy as np

samples = ['The cat sat on the mat.', 'The dog ate my homework.']
characters = string.printable  # 所有可打印的ASCII字符
token_index = dict(zip(range(1, len(characters) + 1), characters))

max_length = 50
results = np.zeros(shape=(len(samples),
                          max_length,
                          max(token_index.keys()) + 1))

for i, sample in enumerate(samples):
    for j, character in enumerate(sample):
        index = token_index.get(character)
        results[i, j, index] = 1  # 将结果保存在results中

print(results)
