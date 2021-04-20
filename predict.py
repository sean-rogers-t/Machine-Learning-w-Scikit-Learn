import pandas as pd
import numpy as np
from datetime import datetime
from datetime import timedelta
import re
if __name__=="__main__":
    
    df=pd.read_csv("sphist.csv")
    df['Date']=pd.to_datetime(df['Date'])
    df.sort_values(by='Date',ascending=True,inplace=True)
    df=df.reset_index(drop=True)
    
    def prev_year(date):
        prevyear=pd.Timestamp(date.year-1,date.month,date.day)
        return prevyear
    
    for index,row in df.iterrows():
        if index<250:
            df.loc[index,'yr_avg']=0
            df.loc[index,'five_day']=0
        else:
            last_five_days=df.loc[index-6:index]
            five_day=last_five_days['Close'].mean()
            
            date=df.loc[index,'Date']
            if date.day!=29:
                prevyear=prev_year(date)
                prev_df=df[(df['Date']>=prevyear) & (df['Date']<date)]
                yr_avg=prev_df['Close'].mean()
                df.loc[index,'yr_avg']=yr_avg
                
            if date.day==29:
                new_date=date-timedelta(days=1)
                prevyear=prev_year(new_date)
                prev_df=df[(df['Date']>=prevyear) & (df['Date']<date)]
                yr_avg=prev_df['Close'].mean()
                df.loc[index,'yr_avg']=yr_avg
                
    data=df[df["Date"] > datetime(year=1951, month=1, day=2)]
    data=data.dropna(axis=0)
    
    train=data[data['Date'] < datetime(year=2013, month=1 , day=1)]
    test=data[data['Date'] >= datetime(year=2013, month=1 , day=1)]
                


