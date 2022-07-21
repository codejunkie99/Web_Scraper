from textblob import TextBlob
import pandas as pds
from csv import writer
df = pds.read_csv(r"C:\Users\Arnav Das\Desktop\sentiment.csv") #modify excel sheet with index on the first column and remove scores by users
df.set_index('Index', inplace=True)
result2 = []

for index, row in df.iterrows():
    y = str(row["Review"])
    edu = TextBlob(y)
    x = edu.sentiment.polarity
    z = edu.sentiment.subjectivity
    if x < 0:
        result =  ' ' + "Negative" + ' ' + str(x) + ' ' + str(z)
    elif x ==0:
        result =  ' ' + "Neutral" + ' ' + str(x) + ' ' + str(z)
    elif x>0 and x<=1:
        result = ' ' + "Positive" + ' ' + str(x) + ' ' + str(z)
    print(result)

    






