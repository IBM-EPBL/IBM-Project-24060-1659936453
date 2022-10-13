import pandas as pd  
      
lists = [[1, 'aaa', 22], [2, 'bbb', 25], [3, 'ccc', 24]] 
      
df = pd.DataFrame(lists, columns =['ID', 'Name', 'Age']) 
print(df)
