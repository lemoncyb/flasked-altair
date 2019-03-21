import random
import pandas as pd
from itertools import repeat


#Iterable
list_data = [10, 20, 30, 20, 15, 30, 45]
list_name = ['l'+str(x) for x in range(1,8,1)]
df_list = pd.DataFrame({'data':list_data, 'name':list_name})

water_1 = [x for x in range(34, 134, 1)]
water_2 = ['y' + str(x) for x in range(0, 100, 1)]
df_water = pd.DataFrame({'Value': water_1, 'Name': water_2})

# Generate stock price randomly for 5 corps during 10 years
mon = ['Jan 1', 'Feb 1', 'Mar 1', 'Apr 1', 'May 1', 'Jun 1', 'Jul 1', 'Aug 1', 'Sep 1', 'Oct 1', 'Nov 1', 'Dec 1']
months = mon*10
year = range(2000, 2010, 1)
years = [x for y in year for x in repeat(y, 12)]
date = [m+' '+str(y) for m,y in zip(months,years)]
dates = date*5
corps = ['MSFT','AMZN','IBM','GOOG','AAPL']
symbol = [x for c in corps for x in repeat(c, 12*10)]
price = [random.uniform(10, 60) for x in range(0,12*10*5,1)]
df_stocks = pd.DataFrame({'symbol':symbol, 'date':dates, 'price':price})

#Dicts of iterables
cat_1 = ['y1', 'y2', 'y3', 'y4']
name_1 = ['x'+str(x) for x in range(0, 21, 1)]
index_1 = range(0, 21, 1)
multi_iter1 = {'index': index_1, 'name': name_1}
for cat in cat_1:
    multi_iter1[cat] = [random.randint(10, 100) for x in index_1]
df_0 = pd.DataFrame(multi_iter1)
