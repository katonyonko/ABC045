from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="045"
#問題
problem="b"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/abc{0}_{1}".format(times, problem)) as res:
  html = res.read().decode("utf-8")
# 2. Load a html by BeautifulSoup.
soup = BeautifulSoup(html, "html.parser")
# 3. Get items you want.
test_case = soup.select(".lang-ja pre")
test_case =[t.text for t in test_case[1:]]
x = '''
'''
y = '''
'''
additional_case = []
test_case += additional_case

for __ in range(0,len(test_case),2):
  sys.stdin = io.StringIO(test_case[__])

  """ここから下にコードを記述"""
  S=[input() for _ in range(3)]
  num=[0]*3
  now=0
  d={'a':0,'b':1,'c':2}
  dd={0:'A',1:'B',2:'C'}
  while num[now]<len(S[now]):
    num[now]+=1
    now=d[S[now][num[now]-1]]
  print(dd[now])
  """ここから上にコードを記述"""

  print(test_case[__+1])