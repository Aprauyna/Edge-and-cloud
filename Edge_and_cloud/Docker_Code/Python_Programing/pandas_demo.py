import pandas as pd
import numpy as np

student_detail = ({
    'S.No' : ["1","2","3","4"],
    'Name' : ["Shivam","Arun","Akshita","Ritesh"]
})
df = pd.DataFrame(student_detail)
df_val = df.to_string(index=False)
print(df_val)