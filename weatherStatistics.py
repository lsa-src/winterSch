y=[2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
yavg=[14.9,14.6,14.5,15.3,15.1,15.4,15.7,15.2,15.1,15.7]
ymax=[34.1,33,34.5,35,32.9,33.5,37.3,36.2,36.4,35]
ymin=[19,18.8,18.6,19.5,19.2,19.5,19.8,19.6,19.2,19.8]


#홀수년도
yodd = [] #빈리스트 생성, 홀수년을 찾아서 넣음
for item in y:
    if item % 2 == 1:
        yodd.append(item)
print(f'홀수년: {yodd}')

#년도
y = [str(item) for item in y]
print(y)

#년도와 평균 기온 딕셔너리 만들기
ytemp = dict(zip(y, yavg))
print(ytemp)
print()

#년도와 평균 기온 딕셔너리에서 평균기온 최소값과 그 년도를 추출하기
mintemp = min(ytemp.values())
ryear=[]
for year,temp in ytemp.items():
    if temp == mintemp:
        ryear.append(year)
# for item in ryear: print(item,end="")
print(f'평균기온최소{ryear}:{mintemp}℃')
print('-'*30)

# 1.ymax 최대값
maxv = max(ymax)

#2.최대값이 있는 위치
ylist=[]
for i in range(len(ymax)):
    if ymax[i] == maxv:
        ylist.append(y[i])

#3.y의 요소 인덱싱
# print(ylist)

print(f'최고기온최대{ylist}:{maxv}℃')
print('-'*30)

#1.ymin 최소값
minv = min(ymin)

#2.최소값이 있는 위치
ymlist=[]
for i in range(len(ymin)):
    if ymin[i] == minv:
        ymlist.append(y[i])
print(f'최저기온최저{ymlist}:{minv}℃')