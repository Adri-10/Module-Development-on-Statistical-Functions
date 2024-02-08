# -*- coding: utf-8 -*-
"""
Created on Sat Aug 21 20:35:58 2021

@author: Amit Roy
"""

#%%
#Group Lab Assignment 2
#Main.py file of Group 8

#%%
import pandas as pd
import Group8

#%%
#reading data file
columns = ['A1','A2','A3','A4','A5','A6','A7','A8','A9','A10','A11','A12','A13','A14','A15']
df = pd.read_csv('australian.csv', names=columns, sep=' ')
df.info()
print(type(df))
print(df)

#%%

#1. Count
series1 = df['A1']
print("Module Output:", Group8.count(series1))
print("Pandas Output:", df[['A1']].count())
#As there are 690 instances, so the count is accurate

#%%
#2. Describe
series2 = df['A2'].tolist()
print("Module Output:", Group8.describe(series2))
print("Pandas Output:", df[['A2']].describe())

#%%
#3. Min Max
series3 = df['A5'].tolist()
print("Module Output for Minimum:", Group8.minimum(series3))
print("Module Output for Maximum:", Group8.maximum(series3))
print("\n")
print("Pandas Output for Minimum:", df[['A5']].min())
print("Pandas Output for Maximum:", df[['A5']].max())


#%%
#Amit Roy
#2019-1-60-006
#4. Argmin Argmax
series4 = df['A2']
print("Module Output(Argmin):", Group8.argmin(series4))
print("Pandas Output(Argmin):", df['A2'].argmin())
print("\n")
print("Module Output(Argmax):", Group8.argmax(series4))
print("Pandas Output(Argmax):", df['A2'].argmax())

#%%
#5. Idxmin IdxMax
# Adri Saha
# ID: 2019-1-60-024
#3. Min Max
series5 = df['A2']
print("Module Output(Minimum Index):", Group8.idx_minimum(series5))
print("Module Output(Maximum Index):", Group8.idx_maximum(series5))
print("\n")
print("Pandas Output(Minimum Index):", df[['A2']].idxmin())
print("Pandas Output(Maximum Index):", df[['A2']].idxmax())

#%%
# Adri Saha
# ID: 2019-1-60-024
#6. Quantile
series6 = df['A7']
print("Module Output Q1(First Quantile):", Group8.quantile(series6,0.25))
print("Pandas Output Q1(Second Quantile):", df[['A7']].quantile(0.25))
print("\n")
print("Module Output Q2(Second Quantile):", Group8.quantile(series6,0.50))
print("Pandas Output Q2(Second Quantile):", df[['A7']].quantile(0.50))
print("\n")
print("Module Output Q3(Third Quantile):", Group8.quantile(series6,0.75))
print("Pandas Output Q3(Third Quantile):", df[['A7']].quantile(0.75))


#%%
#7. Sum
series7 = df['A1']
print("Module Output of sum:",Group8.sum(series7))
print("Pandas Output of sum:", df[['A1']].sum())
#%%
#8.  Mean
series8 = df['A8']
print("Module Output:", "%.6f" %Group8.mean(series8))
print("Pandas Output:", df[['A8']].mean())

#%%
#9. Median
series9 = df['A13']
print("Module Output:", Group8.median(series9))
print("Pandas Output:", df[['A13']].median())

#%%
#10. Mad
# Adri Saha
# ID: 2019-1-60-024
#10. Mad
series10 = df['A10']
print("Module Output of Mean absolute deviation(MAD):", Group8.mad(series10))
print("Pandas Output Mean absolute deviation(MAD):", df[['A10']].mad())

#%%
#Amit Roy
#2019-1-60-006
#11. Product
#11. Product
series11 = df['A8']
print("Module Output for product:", Group8.product(series11))
print("Pandas Output for product:", df[['A8']].prod())

#%%
# Adri Saha
# ID: 2019-1-60-024
#12. Var
series12 = df['A7']
print("Module Output for variance:", '%.6f'%Group8.var(series12))
print("Pandas Output for variance:", df[['A7']].var())
#%%
# Adri Saha
# ID: 2019-1-60-024
#13.Std
series13 = df['A13']
print("Module Output for standard deviation:", '%.6f'%Group8.std(series12))
print("Module Output for standard deviation:", df[['A13']].std())

#%%
#Amit Roy
#2019-1-60-006
#14. Skew
series14 = df['A14']
print("Module Output:", Group8.skew(series14))
print("Pandas Output:", df[['A14']].skew())

#%%
#Amit Roy
#2019-1-60-006
#15. kurtosis
series15 = df['A1']
print("Module Output:", Group8.kurt(series15))
print("Pandas Output:", df[['A1']].kurt())
#%%
#Amit Roy
#2019-1-60-006
#16. Cumulative_sum
series16 = df['A11']
print("Module Output:", Group8.cumulative_sum(series16))
print("Pandas Output:", df[['A11']].cumsum())

#%%
#Amit Roy
#2019-1-60-006
#17. Cummin
series17 = df['A12']
print("Module Output cummin:", Group8.cummin(series17))
print("Pandas Output cummin:", df[['A12']].cummin())
#%%
#Amit Roy
#2019-1-60-006
# Cummax
print("Module Output cummax:", Group8.cummax(series17))
print("Pandas Output cummax:", df[['A12']].cummax())
#%%
#Amit Roy
#2019-1-60-006
#18. Cumprod
series18 = df['A3']
print("Module Output:", Group8.cumulative_product(series18))
print("Pandas Output:", df[['A3']].cumprod())


#%%
#19. Diff
series19 = df['A14']
print("Module Output:", Group8.diff(series19))
print("Pandas Output:", df[['A14']].diff())


#%%
#Amit Roy
#2019-1-60-006
#20. Pct Change
series20 = df['A14']
print("Module Output:", Group8.pct(series20))
print("Pandas Output:", df[['A14']].pct_change())

#%%

#Extra Implementations
 

#%%
#IQR
# Adri Saha
# ID: 2019-1-60-024
series22 = df['A3']
print("Module Output for Interquartile Range(IQR):", Group8.iqr(series22))

#%%

#Median absolute deviation
# Adri Saha
# ID: 2019-1-60-024
series25 = df['A10']
print("Module Output for Median absolute deviation (Mead):", Group8.mead(series25))
print("pandas Output for Mean absolute deviation (Mad):", Group8.mad(series25))

#%%
# Adri Saha
# ID: 2019-1-60-024
#absolute function
#series26 = df['A11']
print("Module Output (abs):", Group8.absolute(-155))
print("pandas Output (abs):", abs(-155))

#%%

#Sorting
# Adri Saha
# ID: 2019-1-60-024
series21 = df['A3']
print("Module Output for sort:", Group8.sort(series21))
print("Pandas Output for sort:", df[['A3']].sort_values(by ='A3'))

#%%
#Amit Roy
#2019-1-60-006

print( "linear regreassion: ")

seies13=df['A13']

series14=df['A14']

Group8.linearregression( seies13,series14 )
#%%

#Amit Roy
#2019-1-60-006

a1=df['A1']
a2=df['A2']
a3=df['A3']
a4=df['A4']
a5=df['A5']
a6=df['A6']
a7=df['A7']
a8=df['A8']
a9=df['A9']
a10=df['A10']
a11=df['A11']
a12=df['A12']
a13=df['A13']
a14=df['A14']
a15=df['A15']

print("query: ")

Group8.query( a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15 )

#%%

#Amit Roy
#2019-1-60-006

df1=df[:2]

#print("co realtion in pandas: " ,df1.corr() )

Group8.corela(a1, a2)

#%%

#Amit Roy
#2019-1-60-006

print("non uni: ")

Group8.nonuni(a1, a2)

#%%

#print("mode: ")

Group8.mode(a1)

#%%

#Amit Roy
#2019-1-60-006

print("trimed mean: ",Group8.trimedMean(a1) )


#%%

print("search 2: ",Group8.search(a1, 1))

#%%

#Amit Roy
#2019-1-60-006

Group8.nonuni(a1, a2)

#%%

Group8.append()

#%%

print(Group8.rev(a1))

#%%

print( Group8.c_all(a1) )

#%%

print( Group8.c_any(a1) )

#%%