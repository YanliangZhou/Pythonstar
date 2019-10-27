# 9-15 Python Module of the Week ：要了解Python标准库，一个很不错的资源是网站Python Module of the Week。请访问
# http://pymotw.com/ 并查看其中的目录，在其中找一个你感兴趣的模块进行探索，或阅读模块collections 和random 的文档。
import collections

print(collections.Counter(['Python', 'C', 'Java', 'Python', 'C', 'C']))
print(collections.Counter({'Python': 2, 'C': 3, 'Java': 1}))
print(collections.Counter(Python=2, C=3, Java=1))