from dataloading import Loader
import pandas as pd 
Path = r"Artifacts\\Test.csv"
loader = Loader()
df = loader.data_Loader(Path)

class clean:
    def __init__ (self):
        pass
