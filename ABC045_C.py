from urllib.request import urlopen
from bs4 import BeautifulSoup
import io
import sys

#ABCの回数
times="045"
#問題
problem="c"

 # 1. Get a html.
with urlopen("https://atcoder.jp/contests/abc{0}/tasks/arc061_a".format(times, problem)) as res:
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
  S=input()
  ans=0
  for i in range(1<<(len(S)-1)):
    tmp=0
    sign=[j for j in range(len(S)) if (i>>j)&1==1]
    if len(sign)>=1:
      for j in range(len(sign)-1):
        tmp+=int(S[sign[j]+1:sign[j+1]+1])
      tmp+=int(S[:sign[0]+1])
      tmp+=int(S[sign[-1]+1:])
    else:
      tmp+=int(S)
    ans+=tmp
  print(ans)
  """ここから上にコードを記述"""

  print(test_case[__+1])