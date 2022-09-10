#  compile示例。
import re

pattern = re.compile(r'([a-z]+) ([a-z]+)', re.I)  # re.l表示忽略大小写

m = pattern.match('Hello World Wide Web')

print(m)  # 匹配成功，返回一个Match对象< sre.SRE _Match object at 0x10bea83e8>

print(m.group(0))  # 返回匹配成功的整个子串'Hello World'

print(m.span(0))  # 返回匹配成功的整个子串的索引(0, 11)

print(m.group(1))  # 返回第一- 个分组匹配成功的子串'Hello'

print(m.span(1))  # 返回第一一个分组匹配成功的子串的索引(0, 5)

print(m.group(2))  # 返回第二个分组匹配成功的子串'World'

print(m.span(2))  # 返回第二个分组匹配成功的子串索引(6, 11)

print(m.groups())  # 等价于(m.group(1), m.group(2), ... (Hell', "World')

# m.group(3)  # 不存在第三个分组Traceback (most recent call last;: File "<stdin>", line 1, in <module> IndexEror. no such group
