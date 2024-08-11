import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
pd.options.mode.copy_on_write=True
data=pd.read_csv('play_tennis.csv')
print('first 5 values of data are:\n',data.head())
x=data.iloc[:,:-1]
y=data.iloc[:,-1]
print("\n values of x:\n",x.head())
print('\n first 5 values of train output:\n',y.head())
le_Outlook=LabelEncoder()
le_Temperature=LabelEncoder()
le_Humidity=LabelEncoder()
le_Windy=LabelEncoder()
le_PlayTennis=LabelEncoder()
x['outlook']=le_Outlook.fit_transform(x['outlook'])
x['temp']=le_Temperature.fit_transform(x['temp'])
x['humidity']=le_Humidity.fit_transform(x['humidity'])
x['wind']=le_Windy.fit_transform(x['wind'])
x.columns=['outlook','temp','humidity','wind']
y=le_PlayTennis.fit_transform(y)
print('\nnow the rain data is:\n',x.head())
print('\n now the train output is:\n',y)
classifier=DecisionTreeClassifier()
classifier.fit(x,y)
inp=["Overcast","Cool","Normal","Strong"]
inp_df=pd.DataFrame([inp],columns=['outlook','temp','humidity','wind'])
inp_df['outlook']=le_Outlook.transform(inp_df['outlook'])
inp_df['temp']=le_Temperature.transform(inp_df['temp'])
inp_df['humidity']=le_Humidity.transform(inp_df['humidity'])
inp_df['wind']=le_Windy.transform(inp_df['wind'])
y_pred=classifier.predict(inp_df)
predicted_label=le_PlayTennis.inverse_transform(y_pred)[0]
print("\n for input {0} ,we obtain {1} ".format(inp,predicted_label))
