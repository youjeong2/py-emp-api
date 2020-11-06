import pandas as pd
import numpy as np

def drop_duplicated_brand():
    df = pd.read_csv('data/cheese_list2.csv', encoding = 'utf-8')

    # brand 공백제거
    # brand = df['brand']
    # df_brand = [i.replace(" ", "" ) for i in df['brand']]
    # print(df_brand)
    
    # boolean = df_brand.duplicated()
    c = df.drop_duplicates('brand', keep=False) 
    # df2 = df['rank'] = np.arange(96)
    # print(c)
    d = c.value_counts
    print(d)
drop_duplicated_brand()