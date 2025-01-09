from sklearn.preprocessing import LabelEncoder
from datacleaning import clean
le = LabelEncoder()
Clean = clean()
df = Clean.dfclean()
class Taransform :
    def __init__(self):
        pass 
    def datataransform (self):
        df['Item_Identifier']= le.fit_transform(df['Item_Identifier'])
        df['Item_Fat_Content']= le.fit_transform(df['Item_Fat_Content'])
        df['Item_Type']= le.fit_transform(df['Item_Type'])
        df['Outlet_Identifier']= le.fit_transform(df['Outlet_Identifier'])
        df['Outlet_Size']= le.fit_transform(df['Outlet_Size'])
        df['Outlet_Location_Type']= le.fit_transform(df['Outlet_Location_Type'])
        df['Outlet_Type']= le.fit_transform(df['Outlet_Type'])

        x = df.drop('Item_Outlet_Sales',axis=1, errors='ignore')
        y = df['Item_Outlet_Sales']
        

        return x, y
    
if 'Item_Outlet_Sales' in df.columns:
    y = df['Item_Outlet_Sales']
else:
    print("Column 'Item_Outlet_Sales' not found in the DataFrame.")
