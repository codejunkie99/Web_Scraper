from textblob import TextBlob
import pandas as pds
from csv import writer
df = pds.read_csv(r"C:\Users\Arnav Das\Desktop\sentiment.csv")
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

    #Work in Progress
    #with open('result.csv', '+w', encoding='utf8', newline='') as x:
            #thewriter = writer(x)
            #header = ['Review', 'Sentiment', 'Polarity', 'Subjectivity']
            #thewriter.writerow(header)
            #info1 = [y, result,str(x),str(z)]
            #thewriter.writerow(info1)
            #print(info1)







