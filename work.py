#项目1 从键盘输入一个学生数学，语文，英语成绩，计算总分平均分
Chinese = float(input("语文成绩："))
Math = float(input("数学成绩："))
English = float(input("英语成绩："))

Total = Chinese + Math + English
Average = Total / 3
print("总分={},平均分={}.format(Total,Average))
	
#项目2 验证哥德巴赫猜想 任何一个6以上的偶数都可以分解为2个素数的和
def prime_num(n):
	if (n > 1):
		for i in range(2, n//2+1):
			if (n % i) == 0:
				return  0        
				break
			else:
				return 1
	else:
		return 0
		
if __name__ == '__main__':
	Input_Num = int(input("请输入一个大于等于6的偶数:"))
	if (Input_Num < 6 or Input_Num % 2 != 0):
		print("Wrong Number!")
	else:
		Num_range = int(Input_Num / 2)
		for i in range(2, Num_range):
			if(prime_num(i) and prime_num(Input_Num - i)):
				print(Input_Num, "=", i, "+", Input_Num - i)
				break

#项目3 打印万年历
import calendar
def CountDays(year,month):
	Leap = calendar.isleap(year)
	largemonth = [1, 3, 5, 7, 8, 10, 12]
	littlemonth = [4, 6, 9, 11]
	IsLarge = 0
	if(month in largemonth):
		IsLarge = 1
	elif(month in littlemonth):
		IsLarge = 0
	if(month == 2 and Leap):
		return 29
	elif(month == 2 and not Leap):
		return 28
	if(IsLarge):
		return 31
	else:
		return 30
		
date = int(input("请输入您想打印的年月份(yyyymm):"))
year = int(date / 100)
month = date % 100
if(month < 0 or month > 12):
	print("You enter a wrong date!")
else:
	print("------ ",year, "年", month, "月 ------")
	print("Sun Mon Tue Wed Thu Fri Sat") 
	weekday = calendar.weekday(year,month, 1) + 1
	for j in range(0, weekday % 7):
		print("    ",end = "")
	for i in range(0, CountDays(year, month)):	
		print("%-4d"%(i + 1),end = "")
		if ((i+ weekday + 1) % 7 == 0):
			print()
	print()
	
	
#项目4 字典
keys=[]
dic={}
def rdic():
  fr = open('dic.txt','r')  
  for line in fr:
    line = line.replace("\n",'')
    v = line.split(':')
    dic[v[0]] = v[1]
    keys.append(v[0])
  fr.close()
def centre():
	n = input("请输入进入相应模块（添加、查询、退出）：")
	if n == "添加":
		key= input("plsease input English：")
		if key not in keys:
			value=input("please input Chinese:")
			dic[key]=value
			keys.append(key)
		else:
			t=input("如果添加新的意思请输入 Y,否则输入N:")
			if ( t=='Y'):
				temp=""
				temp=temp+dic[key]
				key1= input("请输入中文")
				temp=temp+","+key1
				print(temp)
        
				dic[key]=temp
				print(dic)
				return 0
			else:
				return 0
	elif n== "查询":
		key= input("plsease input English：")
		print(keys)
		print(dic)
		if key not in keys:
			print("the english not in the dic.")
		else :
			print(dic[key])
	elif n == "退出" :
		return 1
	else :
		print("输入有误")
		return 0
def wdic():
	with open('dic.txt','w') as fw:
		for k in keys:
			fw.write(k+':'+dic[k]+'\n')
def main():
	rdic()
	while True:
		print(keys)
		print(dic)
		n=centre()
		print(keys)
		print(dic)
		if(n == 1):
			break
		if(n == 0):
			continue
	wdic()
main()


#项目5 学生信息管理
stuInfo=[]
def main():
    while True:
        printMenu()  #打印菜单
        key=int(input('请输入功能对应的数字：'))
        if(key == 1):
            addInfo() #添加学生信息
        elif(key == 2):
            delInfo() #删除学生信息
        elif(key == 3):
            modifystuInfo() #修改学生信息
        elif(key == 4):
            showstuInfo() #查看学生所有信息
        elif(key == 5):   #退出系统
            quitConfirm=input('真的要退出吗？（Yes or No）：')
            if (quitConfirm =='Yes'):
                break   #结束循环
            else:
                print('输入有误，请重新输入')
                
#打印功能提示         
def printMenu():
    print('='*30)
    print('学生信息管理系统V1.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.显示所有学生信息')
    print('5.退出系统')
    print('='*30)
    
#添加学生信息  
def addInfo():
    newname=input('输入新学生的名字:')
    newsex=input('输入新学生的性别:')
    newphone=input('输入新学生的号码:')
    newInfo={}
    newInfo['name'] = newname
    newInfo['sex'] = newsex
    newInfo['phone'] = newphone
    stuInfo.append(newInfo)
    
#删除学生信息
def delInfo():
    delNum = int(input('请输入要删除的序号：'))-1
    del stuInfo[delNum]
    
#修改学生信息
def modifystuInfo():
    stuId = int(input('请输入要修改的学生序号：'))-1
    newname = input('输入修改后学生的名字:')
    newsex = input('输入修改后学生的性别:')
    newphone = input('输入修改后学生的号码:')
    stuInfo[stuId]['name'] = newname
    stuInfo[stuId]['sex'] = newsex
    stuInfo[stuId]['phone'] = newphone
 
#显示所有学生信息
def showstuInfo():
    print('='*30)
    print('学生信息如下：')
    print('='*30)
    i = 1
    for tempInfo in stuInfo:
        print('%d  %s  %s  %s'%(i, tempInfo['name'], tempInfo['sex'], tempInfo['phone']))
        i+=1
        
main() 


#项目6 教材记录管理
class Book():
	def __init__(self, ISBN, Title, Author, Publisher):
		self.ISBN = ISBN
		self.Title = Title
		self.Author = Author
		self.Publisher = Publisher
		
	def show(self):
		print(self. ISBN, self.Title, self.Author, self.Publisher)
		
class BookList():
	def __init__(self):
		self.books = []
	def show(self):
		print(self.ISBN, self.Title, self.Author, self.Publisher)
		for i in self.books:
			self.show()
				
	#插入
	def __Insert(self,s):
		i = 0
		while(i < len(self.books) and s.ISBN > self.books[i]):
			i=i+1
			self.books.insert(i,s)
			print("Insert Success!")
			
	#更新		
	def __Update(self,s):
		i = 0
		while(i < len(self.books) and s.ISBN != self.books[i]):
			i=i+1
			if(s.ISBN == self.books[i]):
				del self.books[i]
				self.books.insert(i,s)
				print("Update Success!")
			else:
				print("Update Error")
				
	#删除			
	def __Delete(self):
		while(i < len(self.books) and s.ISBN != self.books[1]):
			i=i+1
			if(s.ISBN == self.books[i]):
				del self.books[i]
				print("Delete Success!")
			else:
				print("Delete Error!")

	def Insert(self):
		ISBN = input('ISBN:')
		Title = input('Title:')
		Author = input('Author:')
		Publisher = input('Publisher:')
		if (ISBN != '' and Title != ''):
			self.__Insert(Book(ISBN, Title, Author, Publisher))
		else:
			print("ISBN or Title Error, Name Can not be Empty")
		
	def Update(self):
		ISBN = input('ISBN:')
		Title = input('Title:')
		Author = input('Author:')
		Publisher = input('Publisher:')
		if (ISBN != '' or Title != '' or Author != '' or Publisher != ''):
			self.__Update(Book(ISBN, Title, Author, Publisher))
		else:
			print("Update Error, Name Can not be Empty")
		
	def Delete(self):
		ISBN = input('ISBN:')
		Title = input('Title:')
		Author = input('Author:')
		Publisher = input('Publisher:')
		if (ISBN != '' or Title != '' or Author != '' or Publisher != ''):
			self.__Delete(Book(ISBN, Title, Author, Publisher))
		else:
			print("Update Error, Name Can not be Empty")
		
	#执行
	def Scan(self):
		while True:
			#输入">"开始执行不同操作
			s = input(">")
			if(s == 'show'):
				self.show()
			elif(s == 'insert'):
				self.Insert()
			elif(s == 'update'):
				self.Update()
			elif(s == 'delete'):
				self.Delete()
			#等于excit时退出
			elif(s=='exit'):
				break
			else:
				print("Enter Error!")
				print("Please show, insert, update，delete or exit!") 
				return 0
			self.File()

	def File(self):
		f = open('books.txt','wt+',encoding = 'utf-8')
		for i in self.books:
			f.write(i.ISBN + '\n')
			f.write(i.Title + '\n')
			f.write(i.Author +'\n')
			f.write(i.Publisher + '\n')
		f.close()

Bl = BookList()
Bl.Scan()
#print(BookList.books)


#1.﻿有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
m = 0
for i in range (1, 5):
	for j in range (1, 5):
		for k in range(1, 5):
			if( i != j and i != k and j != k ):
				m += 1
				print(i, j, k)
print("Total number =", m);
 

#2.企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
                              #利润高于10万元,低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
							  #20万到40万之间时，高于20万元的部分，可提成5%；
							  #40万到60万之间时高于40万元的部分，可提成3%；
							  #60万到100万之间时，高于60万元的部分，可提成1.5%，
							  #高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
print("Please Input Profit(单位万)")
I=int(input())
_Reward = 0.0
_ratio = 0.0
Reward = 0.0 
Profitarr = [0, 10, 20, 40, 60, 100]
ratio = [0, 0.1, 0.075, 0.05, 0.03, 0.15, 0.01]
for i in range(0, 6):
	if(I < 0):
		print("You have no Profit!")
		break
	elif(I > Profitarr[i]):
		_Reward = I - Profitarr[i]
		_ratio = ratio[i + 1]
		Reward += (Profitarr[i] - Profitarr[i - 1]) * ratio[i]
Reward += _Reward * _ratio
Reward = round(Reward * 10000)
print("应发奖金为:", Reward, _Reward, _ratio)							 


#3.一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math
def isSqr(n):
    a = int((math.sqrt(n)))
    return a * a == n

for i in range(0, 10000):
	if(i < 101 and isSqr(-i + 100) and isSqr(-i + 268)):
		print(-i)
	elif(isSqr(i + 100) and isSqr(i + 268)):
		print(i)
 

#4.输入某年某月某日，判断这一天是这一年的第几天？
def isleapyear(n):
	leapyear = bool(0)
	if( n < 0 ):
		print("not a year")
		leapyear = bool(0)
	elif( (n % 400 == 0) or (n % 100 != 0 and n % 4 == 0) ):
		leapyear = bool(1)
	return leapyear

print("Please Enter the Date(yyyymmdd):")
date = int(input())
year = int(date / 10000)
month = int((date % 10000) / 100)
day = date % 100
day_num = 0
montharr = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
for i in range(0, month - 1):
	day_num += montharr[i]
if(isleapyear(year) and month > 2):
	day_num += day + 1
else:
	day_num += day

print("This is the", day_num, "date of this year")
 

#5.输入三个整数x,y,z，请把这三个数由小到大输出。
print("Please Enter 3 int")
x = int(input())
y = int(input())
z = int(input())
list = [x, y, z]
list.sort()
print(list)
 

#$6.斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#在数学上，费波那契数列是以递归的方法来定义：F0 = 0     (n=0)F1 = 1    (n=1)Fn = F[n-1]+ F[n-2](n=>2)输出这个序列的前10项。
def Fib(n):
	if( n == 1 ):
		return 0
	elif( n == 2 ):
		return 1
	else:
		return Fib(n - 1) + Fib(n - 2)

for i in range(1, 11):
	print(Fib(i))
 

#7.输出 9*9 乘法口诀表。
for i in range(1, 10):
	print()
	for j in range(1, 10):
		print("%d * %d = %d" %(i, j, i*j), end = " ")
 
#8.程序暂停一秒输出。
import time
time.sleep(1)
print("Pause 1 second")

#9.程序暂停一秒输出，并格式化当前时间。
import time
time.sleep(1)
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
 
 
#10.古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？
def Num(n):
	if (n <= 0):
		print("Wrong Number!")
	elif (n == 1 or n == 2):
		return 1
	else:
		return Num(n-1) + Num(n-2)

print(Num(5))
 
 
#11.判断101-200之间有多少个素数，并输出所有素数。程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。 　　　　　
import math
def Is_prime(n):
	t = int(math.sqrt(n))
	for i in range(2, t+1):
		if (n % i == 0):
			return bool(0)
			break;
	return bool(1)  

prime_num = 0
for i in range(101, 201):
	if(Is_prime(i)):
		print(i)
		prime_num += 1
print("Total Prime Num =", prime_num)
 

#12.打印出所有的"水仙花数"，所谓"水仙花数"是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个"水仙花数"，因为153=1的三次方＋5的三次方＋3的三次方。
for i in range(100, 1000):
	a = int(i / 100)
	b = int((i % 100) / 10)
	c = i % 10
	if(i == a**3 + b**3 + c**3):
		print(i)
 

#13.将一个正整数分解质因数。例如：输入90,打印出90=2*3*3*5。
n = int(input("input number:"))
print("%d = " %n, end = "")
for i in range(2,n + 1):
    while (n != i):
        if(n % i == 0):
            print("%d*"%i,end = "")
            n = n / i
        else:
            break
print( "%d" % n)
 
 
#14.利用条件运算符的嵌套来完成此题：学习成绩>=90分的同学用A表示，60-89分之间的用B表示，60分以下的用C表示。
Grades = int(input("Please Enter Your Grades:"))
if(Grades > 100 or Grades < 0):
	print("Not a Grades!")
elif(Grades >= 90):
	print("A")
elif(Grades >= 60):
	print("B")
else:
	print("C")
 

#15.输出指定格式的日期。程序分析：使用 datetime 模块。

 

#16.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。
import string
str = input("Please Enter str")
letters = 0
space = 0
digit = 0
others = 0
for i in range(0, len(str)):
	if(str[i].isalpha()):
		letters += 1
	elif(str[i].isspace()):
		space += 1
	elif(str[i].isdigit()):
		digit += 1
	else: 
		others += 1
print("Total letters=%d space=%d digit=%d others=%d"%(letters, space, digit, others))
 

#17.求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。
Total_num = int(input("Total Num = "))
_s = 0
s = 0
a = int(input("Please Enter Your Num "))
for i in range(0, Total_num):
	_s += a * 10 ** i
	s += _s
print("Sum = ",s)
 

#18.一个数如果恰好等于它的因子之和，这个数就称为"完数"。例如6=1＋2＋3.编程找出1000以内的所有完数。
def WanShu(n):
	s = 0
	for i in range(1,n):
		if(n % i == 0):
			#print(i, end =" ")
			s += i
	return s

for i in range(1, 1001):
	if(WanShu(i) == i):
		print(i)

 
#19.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
def Total_road(n):
	high = 100
	total_road = high
	for i in range(0, n - 1):
		high = high/2
		total_road += high * 2
	return total_road

def Last_road(n):
	high = 100
	for i in range(0, n):
		high = high/2
	return high
	
print("Total_road = ", Total_road(10))
print("Last high = ", Last_road(10))
 

#20.猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。
#以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
def Total_Peach(n):
	if(n < 1):
		print("date wrong!")
	if(n == 1):
		return 1
	else:
		return (Total_Peach(n - 1) + 1) * 2

print(Total_Peach(10))


#21.两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。
for i in range(ord('x'),ord('z') + 1):
    for j in range(ord('x'),ord('z') + 1):
        if i != j:
            for k in range(ord('x'),ord('z') + 1):
                if (i != k) and (j != k):
                    if (i != ord('x')) and (k != ord('x')) and (k != ord('z')):
                        print( 'order is a -- %s\t b -- %s\tc -- %s' % (chr(i),chr(j),chr(k)))
 

#22 使用*号打印一个菱形图案。  
for i in range(1, 5):
	for j in range(4 - i):
		print(end = " ")
	for k in range(2*i - 1):
		print("*", end = "")
	print()
for i in range(1, 4):
	for j in range(i):
		print(end = " ")
	for k in range(7 - 2 * i):
		print("*", end = "")
	print()
		
 
#23.有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。
def Upper(n):
	if(n == 1):
		return 2
	if(n == 2):
		return 3
	else:
		return Upper(n-1) + Upper(n-2) 
		
def Under(n):
	if(n == 1):
		return 1
	if(n == 2):
		return 2
	else:
		return Under(n-1) + Under(n-2)
		
Total = 0
for i in range(1, 21):
	Total += Upper(i)/Under(i)
print(Total)
 
 
#24.求1+2!+3!+...+20!的和。
def factorial(n):
	if(n == 0):
		return 1
	elif(n == 1):
		return 1
	else:
		return n * factorial(n - 1)

total = 0;
for i in range(1,21):
	total += factorial(i)
print(total)
 

#25.利用递归方法求5!。
def factorial(n):
	if(n == 0):
		return 1
	elif(n == 1):
		return 1
	else:
		return n * factorial(n - 1)
print(factorial(5))
 

#26.利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。
def Oppsite(s,length):
	if(length == 0):
		return
	print(s[length - 1], end = "")
	Oppsite(s,length - 1)

s = input("Please Enter a String:")
length = len(s)
Oppsite(s, length)
 

#27.有5个人坐在一起，问第五个人多少岁？他说比第4个人大2岁。问第4个人岁数，他说比第3个人大2岁。问第三个人，又说比第2人大两岁。问第2个人，说比第一个人大两岁。最后问第一个人，他说是10岁。请问第五个人多大？
def Age(n):
	if(n == 0):
		return 0
	elif(n == 1):
		return 10
	else:
		return Age(n-1) + 2
print(Age(5))


#28.给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。
Integer = input("Please Enter An Integer\n")
Length = len(Integer)
print("该整数是%d位数"%Length)
for i in range(0, Length):
	print(Integer[Length - i -1])
 

#29.一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。
for i in range(10000, 100000):
	a = int(i / 10000)
	b = int(i % 10000 / 1000)
	d = int(i % 100 / 10)
	e = int(i % 10)
	if(a == e and b == d):
		print("%d是一个回文数"%i)
		

#30.请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。
Week = input("Please Input First Letter of Week\n")
if(Week == 'M'):
	print("Monday!")
elif(Week == 'T'):
	_Week = input("Please Input Second Letter of Week\n")
	if(_Week == "u"):
		print("Tuesday!")
	elif(_Week -- "h"):
		print("Thurthday!")
	else:
		print("Not a Week Day!")
elif(Week == 'W'):
	print("Wednesday!")
elif(Week == 'F'):
	print("Friday!")
elif(Week == 'S'):
	_Week = input("Please Input Second Letter of Week\n")
	if(_Week == 'a'):
		print("Saturday!")
	elif(_Week == 'u'):
		print("Sunday!")
	else:
		print("Not a Week Day!")
else:
	print("Not a Week Day!")
 

#31.按相反的顺序输出列表的值。
list = ['a', 'b', 'c']
for i in list[::-1]:
	print(i)
 

#32.按逗号分隔列表。
list = ['a','b','c','d','e']
s = ','.join(str(n) for n in list)
print(s)
 

#33.求100之内的素数。
num=[];
i=2
for i in range(2,101):
   j=2
   for j in range(2,i):
      if(i%j==0):
         break
   else:
      num.append(i)
print(num)
 

#34.对10个数进行排序。
num=[]
print("请输入10个数")
for i in range(10):
	num.append(int(input("Please Enter a Number(%d):"%(i+1))))
print(num)
num.sort()
print(num)
 

#35.求一个3*3矩阵主对角线元素之和。
a = []
sum = 0.0
for i in range(0, 3):
	a.append([])
	for j in range(0, 3):
		a[i].append(float(input("Please Input Your Number:")))
for i in range(0, 3):
	sum += a[i][i]
print(sum)
 

#36.有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。
list = [1, 3, 6, 65]
Num = int(input("Please Enter Your Number:"))
list.append(Num)
list.sort()
print(list)
 

#37.将一个数组逆序输出。
list = [1, 65, 23, 36, 10]
list.sort()
for i in range(0, len(list)):
	print(list[len(list) - i - 1], end = " ")
print()


#38.两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：X = [[12,7,3],    [4 ,5,6],    [7 ,8,9]]Y = [[5,8,1],    [6,7,3],    [4,5,9]]
x = [[12, 7, 3],
	 [4 ,5, 6],
	 [7, 8, 9]]
y = [[5, 8, 1],
	 [6, 7, 3],
	 [4, 5, 9]]
Result = [[0, 0, 0],
		  [0, 0, 0],
		  [0, 0, 0]]
		  
for i in range(len(x)):
	for j in range(len(x[0])):
		Result[i][j] = x[i][j] + y[i][j]
print(Result)
 

#39.统计 1 到 100 之和。
sum = 0
for i in range(101):
	sum += i
print(sum)


#40.打印出杨辉三角形（要求打印出10行如下图）。　　
num = 10
list1 =[] #list 用来保存杨辉三角
for n in range(num):
	row =[1]
	list1.append(row)

	if (n == 0):
		print(row)
		continue
	for m in range(1,n):
		row.append(list1[n - 1][m - 1] + list1[n - 1][m])
	row.append(1)
 
	print(row)
 

#41.输入数组，最大的与第一个元素交换，最小的与最后一个元素交换，输出数组。
list = []
for i in range(8):
	Num = int(input("Number"))
	list.append(Num)
list.sort()
length = len(list)
t = list[0]
list[0] = list[length - 1]
list[length - 1] = t
print(list)
 

#42.有n个整数，使其前面各数顺序向后移m个位置，最后m个数变成最前面的m个数

 

#43.有n个人围成一圈，顺序排号。从第一个人开始报数（从1到3报数），凡报到3的人退出圈子，问最后留下的是原来第几号的那位。
n = int(input("请输入总人数："))
n_list = []
a = -1
flag = True

for i in range(1, n + 1):
    n_list.append(i)

while flag:
    for j in range(3):
        if len(n_list) == 1:
            print(n_list[0])
            flag = False
            break
        if a == len(n_list) - 1:
            a = -1
        a += 1
        if j == 2:
            n_list.remove(n_list[a])
            a -= 1
 

#44.海滩上有一堆桃子，五只猴子来分。第一只猴子把这堆桃子平均分为五份，多了一个，这只猴子把多的一个扔入海中，拿走了一份。第二只猴子把剩下的桃子又平均分成五份，又多了一个，它同样把多的一个扔入海中，拿走了一份，第三、第四、第五只猴子都是这样做的，问海滩上原来最少有多少个桃子？

 

#45.已知809*??=800*??+9*?? 其中??代表的两位数, 809*??为四位数，8*??的结果为两位数，9*??的结果为3位数。求??代表的两位数，及809*??后的结果。
for i in range(10, 100):
	if(i * 8 < 100 and 9 * i > 100 and 800 * i < 100000):
		print(i)
		break
 

#46.编写程序输入一个八进制数，把一个八进制数转换为十进制
def toShiJinZhi(v):
    n = 0   
    for i in range(len(v)):
        n = n * 8 + ord(v[i]) - ord('0')
    return n

Str = input(print("请输入一个八进制的数"))	
print(toShiJinZhi(Str))
 
#47.求0—7这8个数字所能组成的奇数个数。
sum = 4
s = 4
for j in range(2, 9):
    print(sum)
    if j <= 2:
        s *= 7
    else:
        s *= 8
    sum += s
print('sum = %d' % sum)
 

#48.输入一个奇数，然后判断最少几个 9 除于该数的结果为整数。

 

#49.某个公司采用公用电话传递数据，数据是四位的整数，在传递过程中是加密的，加密规则如下：每位数字都加上5,然后用和除以10的余数代替该数字，再将第一位和第四位交换，第二位和第三位交换。
