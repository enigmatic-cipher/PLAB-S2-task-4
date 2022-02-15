"""
Given a string as input. Print following pattern using For loop.
Input-> "hello"
Output-> #o#l#l#e#h#hello#
"""

st = "hello"
ln = len(st)
nw_st = ""
pt = "#"
for i in st[::-1]:
  nw_st = nw_st + pt + i
nw_st = nw_st + pt + st + pt
print(nw_st)

  