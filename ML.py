# student data in this relation between student marks and attendence


import pandas as pd

data={'name':["shivam","kanu","ram","lucky","ansh","gagan"],

     'marks':[89,98,99,100,79,80],  
        
      'attendence':[85,78,90,95,68,70]
}


df=pd.DataFrame(data)

print(df)

df.to_csv("data.csv",index=False)


import pandas as pd 


data=pd.read_csv("data.csv")
print(data)



import matplotlib.pyplot as plt
plt.bar(df["attendence"],df["marks"])

plt.title('relation between marks and attendence')

plt.xlabel("attendence")
plt.ylabel("marks")


plt.show()




from sklearn.linear_model import LinearRegression


model=LinearRegression()

x=df[["attendence"]]
y=df["marks"]


model.fit(x,y)

attendence=float(input("enter the your attendence"))


output=model.predict([[attendence]])

print(output)

if attendence<=50:
    print("yee kam marks h")
elif attendence>=50:
    print("yee ache marks h")    












