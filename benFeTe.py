#by :jing
#本福特代码，算邪道，大家看下就好，毕竟定律没证明
import re
import matplotlib.pyplot as plt
from tkinter import *
import tkinter.filedialog
root = Tk()
def xz():
	filename = tkinter.filedialog.askopenfilename()
	print(filename);
	btn = Button(root,text="弹出选择文件对话框",command=xz)
	btn.pack()
	testBenFuTe(filename);
	root.mainloop()

#2019-3-3这种
def subUnNeedNum(content):
	#不匹配的改成[date]
	pattern = re.compile(r'(\d{4}-\d{1,2}-\d{1,2})')
	content = pattern.sub("[date]",content)
	return content
	
#03-42这种	
def subUnNeedNumV1(content):
	#不匹配的改成[date]
	pattern = re.compile(r'(\d{1,2}-\d{1,2})')
	content = pattern.sub("[date]",content)
	return content
	
def subUnNeedNumV2(content):
	#不匹配的改成[date]
	pattern = re.compile(r'2018')
	content = pattern.sub("[date]",content)
	return content
	

def subUnNeedNumV3(content):
	#不匹配的改成[date]
	pattern = re.compile(r'\d+.\d+%')
	content = pattern.sub("[percent]",content)
	return content
	
def subUnNeedNumV4(content):
	#不匹配的改成[date]
	pattern = re.compile(r'[(](.*)[)]')
	content = pattern.sub("[noNeedNum]",content)
	return content

def getNeedNum(content):
	#所有数据的正则表达式
	pattern = re.compile(r'[-]*\d+[.]*\d*')
	nums = re.findall(pattern,content)
	return nums

#获取文章的字符串
def getFileContent(filePath):
	#获取整个文章
	fr = open(filePath, 'r', encoding='utf-8')
	content = fr.read()
	return content
	
#本福特首位数字统计并分析
def benFuTeAnlasys(nums):
	numsAdd = [0,0,0,0,0,0,0,0,0]
	for num in nums:
		if(num[0] != '-'):
			#排除负数的情况
			numsAdd[int(num[0])-1]= numsAdd[int(num[0])-1] +1;
			#print(num[0])
	return numsAdd;
	
#根据本福特定律画出相关的折线图
def drawPicture(numsAdd):
	x = [1,2,3,4,5,6,7,8,9];
	plt.plot(x,numsAdd);
	plt.plot(x,numsAdd,"r-",linewidth=2)
	plt.plot(x,numsAdd, "go", markersize=8)
	plt.grid(True)
	#plt.plot(x, numsAdd);
	plt.show();

#画出百分图
def drawPicturePer(numsAdd):
	x = [1,2,3,4,5,6,7,8,9];
	plt.plot(x,numsAdd);
	plt.plot(x,numsAdd,"r-",linewidth=2)
	plt.plot(x,numsAdd, "go", markersize=8)
	plt.grid(True)
	
	plt.show();

#计算出百分数	
def calNumsAddPer(numsAdd):
	numsAddPer = [0,0,0,0,0,0,0,0,0]
	numsAll = 0;#j计算总数
	for num in numsAdd:
		numsAll=numsAll+num
	numsAddPer = [round(num*100/numsAll,2) for num in numsAdd]
	print("样本总数："+str(numsAll));
	print("	1	2	3	4	5	6	7	8	9")
	print("概率：	",end="")
	[print(str(num)+'%	',end = '') for num in numsAddPer]
	print("")
	return numsAddPer;



#计算方差
def calEx(numsAddPer):
	numStanard = [30.1,17.6,12.5,9.7,7.9,6.7,5.8,5.1,4.6]
	#abs(numsAddPer -numStanard)
	i = 0;
	count = 0;
	for i in range(0,9):
		count += abs((numsAddPer[i]-numStanard[i])*(numsAddPer[i]-numStanard[i]));
		#print(i);
	num = count/9
	print("方差 = "+str(count/9));
	print("方差越大，数据越不靠谱，越有造假概率，本福特邪道，看看就好")
	

def testBenFuTe(filePath):
	content = getFileContent(filePath);
	content = subUnNeedNum(content);
	content = subUnNeedNumV1(content);
	content = subUnNeedNumV2(content);
	content = subUnNeedNumV3(content);
	content = subUnNeedNumV4(content);
	print(content);
	print("==============以上是原文======================")
	nums = getNeedNum(content);
	numsAdd = benFuTeAnlasys(nums);
	numsAddPer = calNumsAddPer(numsAdd);
	calEx(numsAddPer);
	drawPicture(numsAdd);	
	
xz();
