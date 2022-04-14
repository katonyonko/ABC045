from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="045"
#問題
problem="d"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc061_b".format(times, problem)) as res:
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
  from collections import defaultdict
  H,W,N=map(int,input().split())
  d=defaultdict(int)
  for i in range(N):
    a,b=map(int,input().split())
    a-=1; b-=1
    for j in range(3):
      for k in range(3):
        if 0<a+j-1<H-1 and 0<b+k-1<W-1:
          d[(a+j-1,b+k-1)]+=1
  ans=[0]*10
  for key in d:
    ans[d[key]]+=1
  ans[0]=(H-2)*(W-2)-sum(ans[1:])
  print(*ans,sep='\n')
  """ここから上にコードを記述"""

  print(test_case[__+1])