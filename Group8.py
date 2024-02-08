# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:35:29 2021

@author: Amit Roy
"""

#All module of Group 8

#Count
#amit roy
def count(series):
    count=0
    for i in series:
        if(i!=None):
            count+=1
    return count

#Describe 
#adri saha
def describe(series):
    print('count\t', '%.5f'%count(series), end = '\n')
    print('mean\t', '%.5f'%mean(series), end = '\n')
    print('std\t\t', '%.5f'%std(series), end = '\n')
    print('min\t\t', '%.5f'%minimum(series), end = '\n')
    print('25%\t\t', '%.5f'%quantile(series,0.25), end = '\n')
    print('50%\t\t', '%.5f'%quantile(series,0.50), end = '\n')
    print('75%\t\t', '%.5f'%quantile(series,0.75), end = '\n')
    print('max\t\t', '%.5f'%maximum(series), end = '\n')

#Minimum
#Moumita Das
#2018-2-60-097
def minimum(series):
    minimum=series[0]
    for i in series:
        minimum=min(minimum,i)
    return minimum

#Maximum
#Moumita Das
#2018-2-60-097
def maximum(series):
    maximum=series[0]
    for i in series:
       maximum=max(maximum,i)
    return maximum

#arg min
#amit roy
def argmin(series):
    indexesMin=[]
    for i in range (0,len(series),1):
        if(series[i]==minimum(series) ):
            indexesMin.append(i) 
    return indexesMin

#arg max
def argmax(series):
    indexesMax=[]
    for i in range (0,len(series),1):
        if(series[i]==maximum(series) ):
            indexesMax.append(i)
    return indexesMax


#idxmin
# Adri Saha
# ID: 2019-1-60-024
def idx_minimum(series):
    minimum=series[0] 
    index=0
    indexMin=-1
    for i in series:
        if(minimum>i):
            minimum=i
            indexMin=index
        index=index+1
    return indexMin

#idxmax
# Adri Saha
# ID: 2019-1-60-024
def idx_maximum(series):
    maximum=series[0] 
    index=0
    indexMax=-1
    for i in series:
        if(maximum<i):
            maximum=i
            indexMax=index
        index=index+1
    return indexMax     

#quantile
# Adri Saha
# ID: 2019-1-60-024
def quantile(series,q):
    n=len(series)
    sorted=sort(series)
    return sorted[int((n+1)*q)]


#Sum
#Azizul  Hakim  
#Id: 2018-2-60-052 

def sum(series):
   sum1 =0
   for i in series:
        sum1+=i
   return sum1

#mean
#Azizul  Hakim  
# 2018-2-60-052 

def mean(series):
    n=len(series)  
    mean=sum(series)/n
    return mean

#Median
#Azizul  Hakim  
# 2018-2-60-052 

def median(series):
    n=len(series)
    series=sort(series)
    if n%2!=0: #odd
        median=series[int(n/2)]
    else:  #even
        mid1=series[int(n/2)]
        mid2=series[int((n/2)-1)]
        median=(mid1+mid2)/2
    return median


#Mean Absolute Deviation
# Adri Saha
# ID: 2019-1-60-024
def mad(series):
    n=len(series)
    sum1=0
    for i in series:
        sum1+=absolute(i-mean(series)) 
    return sum1/n


#Prod
#Amit roy
#2019-1-60-006
def product(series):
    mul=1
    for i in series:
        mul=mul*i
    return mul

#Var
# Adri Saha
# ID: 2019-1-60-024
def var(series):
    total=0
    n=len(series)
    for i in series:
        mean2=mean(series)
    total+=(i-mean2)**2
    variance=total/(n-1)
    return variance

#Standard Deviation
# Adri Saha
# ID: 2019-1-60-024
def std(series):
     import math
     sd=math.sqrt(var(series))
     return sd

#%%
#Skewness
#Amit roy
#2019-1-60-006
def skew(a1):
 mean1= mean(a1)
 sum=0

 for i in a1:
    sum+=abs(i-mean1)*abs(i-mean1)*abs(i-mean1)

 n=len(a1)
 sk=sum/((n-1)*std(a1)**3)

#print("skew ness: ",sk)
 return sk
#%%
#Kurtosis
#Amit roy
#2019-1-60-006
def kurt(a1):
   sum=0
   sum1=0
   mean1= mean(a1)  
   for i in a1:
    sum+=(i-mean1)**4
  
   for i in a1:
    sum1+=(i-mean1**2)**2

#kur=n*(sum/sum1)
   n=len(a1) 
   kur=sum/( (n-1)*std(a1)**4 )

   return kur
#%%
#Cumulative Sum
#Amit roy
#2019-1-60-006
def cumulative_sum(series):
    sum=0
    summations=[]
    for i in series:
        sum+=i
        summations.append(sum)
    print(summations)


#Cumulative Minimum
#Cumulative Minimum
#Amit roy
#2019-1-60-006
def cummin(series):
    min_list=[]
    min_list.append(series[0])
    for i in range(0,len(series)-1):
        if (min_list[i]<series[i+1]):
            min_list.append(min_list[i])
        else:
            min_list.append(series[i+1])
    return min_list 
#Cumulative Maximum
#Amit roy
#2019-1-60-006
def cummax(series):
    max_list=[]
    max_list.append(series[0])
    for i in range(0,len(series)-1):
        if (max_list[i]>series[i+1]):
            max_list.append(max_list[i])
        else:
            max_list.append(series[i+1])
    return max_list  
#cumprod
#amit roy
def cumulative_product(series): 
    mul=1
    for i in series:
        mul=mul*i
    return mul

#Diff
#Moumita Das
#2018-2-60-097

def diff(series):
    for i in range (2,len(series),1):
        return series[i]-series[i-1]

#Percentage Change

#Amit roy
#2019-1-60-006

def pct(a100):
  for i in range(0,len(a100 ),1 ):
    for j in range(i,len(a100 ),1 ):
       if(a100[i]!=0): 
         num2=a100[j]
         num1=a100[i]
         perIncre =((num2 - num1)/num1)*100
         if(perIncre>0):
            print("Percentage is Increased by ",perIncre," %")
         else:
            print("Percentage is Decreased by ",perIncre," %")
        
#Extra Implementation

# Adri Saha
# ID: 2019-1-60-024
#Interquartile Range
def iqr(series):
    return quantile(series,0.75)-quantile(series,0.25)

#Median Absolute Deviation
def mead(series):
    series_mean = mean(series)
    for i in series:
        meadi=absolute(i-series_mean)
        return meadi
    
#abs function
import math
def absolute(series):    
    return (math.sqrt(series*series));

#Sorting
def sort(attribute):
    sorted_list = list(attribute)
    for i in range(len(attribute)):
        for j in range(i+1,len(attribute)):
            if(sorted_list[i]>sorted_list[j]):
                temp=sorted_list[i]
                sorted_list[i]=sorted_list[j]
                sorted_list[j]=temp
    return sorted_list

#%%
#Amit roy
#2019-1-60-006

def linearregression(a13 , a14):
    #linear regrassion
#Amit roy
#2019-1-60-006
 x=0
 y=0
 x2=0
 y2=0
 xxbar=0
 yybar=0
 xybar=0

 n=len(a13)

 for i in range(0,n,1):
    x+=a13[i]
    y+=a14[i]
    x2+=a13[i]*a13[i]
    y2+=a14[i]*a14[i]

 xbar=mean(a13)

 ybar=mean(a14)
    
 for i in range(0,n,1):
    xxbar += (a13[i] - xbar) * (a13[i] - xbar);
    yybar += (a14[i] - ybar) * (a14[i] - ybar);
    xybar += (a13[i] - xbar) * (a14[i] - ybar);    


    
 slope  = xybar / xxbar;
 intercept = ybar - slope * xbar;    

 print("slope: ",slope)

 print("intercept: ",intercept)

 rss=0
 ssr=0

 for i in range(0,n,1):
    fit = slope*a13[i] + intercept
    rss += (fit - a14[i]) * (fit - a14[i])
    ssr += (fit - ybar) * (fit - ybar)

 degreesOfFreedom = n-2
 r2    = ssr / yybar

 svar  = rss / degreesOfFreedom;
 svar1 = svar / xxbar;
 svar0 = svar/n + xbar*xbar*svar1;

 print("regression: ",r2)
#%%
#query having mean is greater than 5

#Amit roy
#2019-1-60-006

def query(a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15):

#a1=df['A1']
#a2=df['A2']
#a3=df['A3']
#a4=df['A4']
#a5=df['A5']
#a6=df['A6']
#a7=df['A7']
#a8=df['A8']
#a9=df['A9']
#a10=df['A10']
#a11=df['A11']
#a12=df['A12']
#a13=df['A13']
#a14=df['A14']
#a15=df['A15']

 if( mean(a1)>5 ):
    print("A1")

 if( mean(a2)>5 ):
    print("A2")
    
 if( mean(a3)>5 ):
    print("A3")

 if( mean(a4)>5 ):
    print("A4")

 if( mean(a5)>5 ):
    print("A5")

 if( mean(a6)>5 ):
    print("A6")    
    
 if( mean(a7)>5 ):
    print("A7")

 if( mean(a7)>5 ):
    print("A7")
    
 if( mean(a8)>5 ):
    print("A8")

 if( mean(a9)>5 ):
    print("A9")

 if( mean(a10)>5 ):
    print("A10")

 if( mean(a11)>5 ):
    print("A11")    

 if( mean(a12)>5 ):
    print("A12")

 if( mean(a13)>5 ):
    print("A13")

 if( mean(a14)>5 ):
    print("A14")

 if( mean(a15)>5 ):
    print("A15") 

#%%

#co relation

#Amit roy
#2019-1-60-006

def corela( a1,a2 ):

 x=0
 y=0
 z=0
 p=0
 n=len(a1)
 for i in a1:
    x+=i

 for i in a2:
    y+=i

 xbar=x/n
 ybar=y/n
 
 mulsum=0
 
 for i in range(0,n,1):
     mulsum+=abs(a1[i]-xbar)*abs( a2[i]-ybar )
 
 sqSum=0   
 sqSum1=0
 
 for i in range(0,n,1):
     sqSum+=abs(a1[i]-xbar)**2
     sqSum1+=abs(a2[i]-ybar)**2 
    
 
 corr=mulsum/( sqSum*sqSum1 )**(-.5)   
 
 print("co relation: ",corr)
 
 
#%%

#Amit roy
#2019-1-60-006

def nonuni(a1,a2):
   h=[]

   t=[]

   for i in range(0,len(a1),1 ):
    if( a1[i]!=a2[i] ):
        h.append(a1[i])
        t.append(a2[i])
        
   print("values of a: ",h)

   print("values of b: ",t)
 #%%  
#Moumita Das
#2018-2-60-097
def mode(a1):
    #implement the mode function

 import numpy as np

#a1=df['A1']

 a11=np.array(a1)

#elements=[]

 element=[]

 for i in range(0,maximum(a1) +1,1):
    element.append(0)

 for i in range(0,len( a11 ),1 ):
    element[ a11[i] ]=element[ a11[i] ]+1

 ans=0

 for i in range(0,len(element),1 ):
    if(i>ans):
       ans=i        
    elif ( i==ans and i!=0 ):
       ans=0
       
 print("mode: ",ans)       


#%%

#trimed mean

#Azizul  Hakim  
# 2018-2-60-052 


def trimedMean(a1):
    sort(a1)
    a=[] 
    for i in range(2,len(a1)-2,1 ):
        a.append(a1[i])
    if( len(a)==0 ):
        return None
    return mean(a)
    
#%%   

#Moumita Das
#2018-2-60-097

def search( a1,p ):
    a=[]    
    for i in a1:
        if(i==p):
            a.append(i)

    return a

#%%

#Moumita Das
#2018-2-60-097

def rev(a1):
    n=len(a1)
    for i in range(0,int(n/2),1):
        temp=a1[i]
        a1[i]=a1[n-i-1]
        a1[n-i-1]=temp
    return a1

#%%

#Moumita Das
#2018-2-60-097

#to implement the append function

class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

def append():

 list1 = SLinkedList()
 list1.headval = Node(123)
 e2 = Node(124)
 e3 = Node(125)

 list1.headval.nextval = e2

 e2.nextval = e3
     
 listprint(list1)
    

#%%

#all() function

#Azizul  Hakim  
# 2018-2-60-052 

def c_all(a):
   for i in a:
       if not i:
           return False
   return True

#%%

#any() function
#Azizul  Hakim  
# 2018-2-60-052 
def c_any(a1):
    for i in a1:
        if i:
            return True
    return False
