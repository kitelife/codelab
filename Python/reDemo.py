#!-*- coding: utf-8 -*-

import re
m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')

print "m.string:", m.string
print "m.re:", m.re
print "m.pos:", m.pos
print "m.endpos:", m.endpos
print "m.lastindex:", m.lastindex
print "m.lastgroup:", m.lastgroup

print "m.group(1,2):", m.group(1, 2)
print "m.groups():", m.groups()
print "m.groupdict():", m.groupdict()
print "m.start(2):", m.start(2)
print "m.end(2):", m.end(2)
print "m.span(2):", m.span(2)
print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')

### output ###
# m.string: hello world!
# m.re: <_sre.SRE_Pattern object at 0x016E1A38>
# m.pos: 0
# m.endpos: 12
# m.lastindex: 3
# m.lastgroup: sign
# m.group(1,2): ('hello', 'world')
# m.groups(): ('hello', 'world', '!')
# m.groupdict(): {'sign': '!'}
# m.start(2): 6
# m.end(2): 11
# m.span(2): (6, 11)
# m.expand(r'\2 \1\3'): world hello!

p = re.compile(r'(\w+) (\w+)(?P<sign>.*)', re.DOTALL)
 
print "p.pattern:", p.pattern
print "p.flags:", p.flags
print "p.groups:", p.groups
print "p.groupindex:", p.groupindex
 
### output ###
# p.pattern: (\w+) (\w+)(?P<sign>.*)
# p.flags: 16
# p.groups: 3
# p.groupindex: {'sign': 3}

#将正则表达式编译成Pattern对象
pattern = re.compile(r'world') 
 
# 使用search()查找匹配的子串，不存在能匹配的子串时将返回None 
# 这个例子中使用match()无法成功匹配 
match = pattern.search('hello world!') 
 
if match: 
    # 使用Match获得分组信息 
    print match.group() 
 
### 输出 ### 
# world

p = re.compile(r'\d+')
print p.split('one1two2three3four4')
 
### output ###
# ['one', 'two', 'three', 'four', '']

p = re.compile(r'\d+')
print p.findall('one1two2three3four4')
 
### output ###
# ['1', '2', '3', '4']

p = re.compile(r'\d+')
for m in p.finditer('one1two2three3four4'):
    print m.group(),
 
### output ###
# 1 2 3 4

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print p.sub(r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print p.sub(func, s)
 
### output ###
# say i, world hello!
# I Say, Hello World!

p = re.compile(r'(\w+) (\w+)')
s = 'i say, hello world!'
 
print p.subn(r'\2 \1', s)
 
def func(m):
    return m.group(1).title() + ' ' + m.group(2).title()
 
print p.subn(func, s)
 
### output ###
# ('say i, world hello!', 2)
# ('I Say, Hello World!', 2)
