# 字符串切割。

import re

ret = re.findall('a', 'eva egon yuan')  # 返回所有满足匹配条件的结果，放在列表里

print(ret)  # 结果:[a','a]

ret = re.search('a', 'eva egon yuan').group()

print(ret)  # 结果:'a'

ret = re.match('a', 'abc').group()

print(ret)  # 结果:'a'

ret = re.split('[ab]', 'abcd')  # 先按'a'分割得到"和"bcd',在对"和'bcd'分别按'b'分割

print(ret)  # 结果: [",", 'cd]
