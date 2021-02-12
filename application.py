'''
Citations
https://www.geeksforgeeks.org/selecting-rows-in-pandas-dataframe-based-on-conditions/
https://www.geeksforgeeks.org/how-to-convert-string-to-integer-in-pandas-dataframe/
https://humansofdata.atlan.com/2016/07/machine-learning-python/
https://datatofish.com/replace-values-pandas-dataframe/
https://stackoverflow.com/questions/35277075/python-pandas-counting-the-occurrences-of-a-specific-value
https://pythonhow.com/accessing-dataframe-columns-rows-and-cells/
'''


import pandas as pd

#data preprocessing
df = pd.read_csv("Titanic.csv")
df = df.replace(['?'],0)
df['age'] = df['age'].astype(float)

survived_female = len(df[(df['sex'] == 'female') & (df['survived'] == 1 )])
survived_male = len(df[(df['sex'] == 'male') & (df['survived'] == 1 )])

print("Number of male survived {}".format(survived_male))
print("Number of female survived {}".format(survived_female))

if survived_male > survived_female:
    print("More number of Male survived than Female")
else:
    print("More number of Female survived than Male")

mean_fare = df['fare'].astype('float64').mean()
rich = len(df[(df['fare'].astype('float64') >= mean_fare) & (df['survived'] == 1 )])
poor = len(df[(df['fare'].astype('float64') < mean_fare) & (df['survived'] == 1 )])

print("Number of rich people survived {}".format(rich))
print("Number of poor people survived {}".format(poor))
if rich > poor:
    print("More rich people survived than poor people")
else:
    print("More poor people survived than rich people")

young = len(df[(df['age'] <= 21) & (df['survived'] == 1 ) ])
middle = len(df[(df['age'] > 21) & (df['age'] <=58 ) & (df['survived'] == 1 )])
old = len(df[(df['age'] > 58 ) & (df['survived'] == 1 )])

print("Number of young people survived {}".format(young))
print("Number of middle people survived {}".format(middle))
print("Number of old people survived {}".format(old))
