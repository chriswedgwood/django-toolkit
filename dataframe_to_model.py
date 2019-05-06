import numpy as np

for col in df.columns:
    arr = df[col]

    size = 0
    value = ""
    for ar in arr:
        if len(str(ar)) > size:
            size = len(str(ar))
            value = ar

    #print(col, size, type(speech_data.iloc[0][col]), ar)

    if type(df.iloc[0][col]) == np.int64:
        print(col + " = " + "models.IntegerField()")

    elif type(df.iloc[0][col]) == str:
        print(col + " = " + "models.CharField(max_length="+ str(size+3) +")")

    elif type(df.iloc[0][col]) ==  np.float64:
        print(col + " = " + "models.FloatField(null=True, blank=True, default=None)")    
    elif type(df.iloc[0][col]) ==  np.bool_:
        print(col + " = " + "models.BooleanField()")
