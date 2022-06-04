#!/usr/bin/env python
# coding: utf-8

# In[99]:


def search():
            from sklearn.neighbors import KNeighborsClassifier
            import pandas as pd
            import numpy as np
            from sklearn.model_selection import train_test_split
            df = pd.read_csv('lol.csv')
            X = df.iloc[:,1:].to_numpy()
            y = df.iloc[:,0].to_numpy()
            index1=float(index.get("1.0","end").strip())
            power1=float(power.get("1.0","end").strip())
            powerindex1=float(powerindex.get("1.0","end").strip())
            exp1=float(exp.get("1.0","end").strip())
            a=np.array([[index1,power1,powerindex1,exp1]])
            #設置樣本和測試 k=5 曼哈頓距離
            X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3,random_state=1) #70%樣本 30%測試
            #建模 
            clf=KNeighborsClassifier(n_neighbors=5,p=1,weights='distance',algorithm='brute')
            clf.fit(X_train,y_train)
            #test
            b=clf.predict(a)
            d="The rank of the player is :"+ str(b[0])
            label_5['text']=d #將分類結果輸入至label_5


# In[100]:


import tkinter as tk
win=tk.Tk()
win.title('LOL選手階級查詢系統')
win.geometry('600x400') #寬*高

#frame
frame1 = tk.Frame(win)
frame2 = tk.Frame(win)
frame3 = tk.Frame(win)
frame1.place(x=0,y=0)
frame1.config(width=600,heigh=400)
frame2.place(x=0,y=250)
frame2.config(width=600,heigh=400)
frame3.place(x=0,y=300)

#label
label_1=tk.Label(frame1,text='index :',font=('Arial',12))
label_1.grid(row=0,column=0,padx=0,pady=20)
label_2=tk.Label(frame1,text='power :',font=('Arial',12))
label_2.grid(row=1,column=0,padx=0,pady=20)
label_3=tk.Label(frame1,text='pwindex :',font=('Arial',12))
label_3.grid(row=2,column=0,padx=0,pady=20)
label_4=tk.Label(frame1,text='exp :',font=('Arial',12))
label_4.grid(row=3,column=0,padx=0,pady=20)

#text
index=tk.Text(frame1,width=50,height=2)
index.grid(row=0,column=1,padx=10,pady=10)
power=tk.Text(frame1,width=50,height=2)
power.grid(row=1,column=1,padx=20,pady=20)
powerindex=tk.Text(frame1,width=50,height=2)
powerindex.grid(row=2,column=1,padx=20,pady=20)
exp=tk.Text(frame1,width=50,height=2)
exp.grid(row=3,column=1,padx=20,pady=20)

#button
button=tk.Button(frame2,text='search',font=('Arial',12),width=50,height=1,command=search) 
button.grid(row=4,column=0,padx=20,pady=20)

#frame3
label_5=tk.Label(frame3,text='',font=('Arial',12))
label_5.grid(row=5,column=0,padx=20,pady=20)
win.mainloop()


# In[ ]:




