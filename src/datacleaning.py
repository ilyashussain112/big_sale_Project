from dataloading import Loader
import pandas as pd 
Path = r"Artifacts\\Train.csv"
loader = Loader()
df = loader.data_Loader(Path)

class clean:
    def __init__ (self):
        pass
    def dfclean (self, df=df):
        df.duplicated().sum()
        df.replace(to_replace='Low Fat', value='lf', inplace=True)
        df.replace(to_replace='Regular', value='reg', inplace=True)
        df['Item_Weight'] = df['Item_Weight'].fillna(df['Item_Weight'].median())
        df['Outlet_Size'] = df['Outlet_Size'].fillna(df['Outlet_Size'].mode()[0])
        return df 
