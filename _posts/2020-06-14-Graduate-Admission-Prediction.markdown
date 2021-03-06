---
layout: post
title: Graduate Admission Prediction
date: 2020-06-14 00:00:00 +0300
description: In this blog, I will discuss how to predict admission probability on the basis of your portfolio. (optional)
img: pro_grad_pic_1.jpeg # Add image post (optional)
fig-caption: # Add figcaption (optional)
tags: [ZUBI_ASH, PROJECT, REGRESSION, Admission] # add tag
---

##  Project Description
All around the world, it's the dream of every student to get admission to the Ivy League and students are often worried about their chances of admission to graduate school. The aim of this blog is to show how different regression models can be built to predict the chance of admission into a particular university based on the student's profile. This model will give students a clear idea about their admission probability in a particular university.


{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_3.png)

## Introduction

The eight Ivy League schools — Brown, Columbia, Cornell, Dartmouth, Harvard, the University of Pennsylvania, Princeton and Yale — had a total of 281,060 applicants for the class of 2021. Of those applicants, less than 10% got admissions offers. Harvard had the lowest acceptance rate out of all the Ivies, at just 5%.

Clearly, getting into any Ivy League school is an impressive achievement. So, how do people do it?

Get those grades and test scores up!!!

For starters, if you want to go to an Ivy, you’re going to need stellar grades and test scores. These are the two most important admissions factors according to The National Association for College Admission Counseling. Ambitious students should take rigorous courses that they can do well in***.

### 1. DATA

The dataset contains several parameters which are considered important during the application for Masters Programs.
The parameters included are :

1. GRE Scores ( out of 340 )
2. TOEFL Scores ( out of 120 )
3. University Rating ( out of 5 )
4. Statement of Purpose and Letter of Recommendation Strength ( out of 5 )
5. Undergraduate GPA ( out of 10 )
6. Research Experience ( either 0 or 1 )
7. Chance of Admit ( ranging from 0 to 1 )

`data source: https://www.kaggle.com/mohansacharya/graduate-admissions`
[link to kaggle dataset!](https://www.kaggle.com/mohansacharya/graduate-admissions)

### 2. IMPORT LIBRARIES AND LOAD DATASETS

Let’s start with loading all the libraries and dependencies.

{% highlight ruby %}
#=> Importing modules
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
{% endhighlight %}

{% highlight ruby %}
admission_df = pd.read_csv('Admission_Predict.csv')
#=> Printing out the head of the dataset
admission_df.head()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_3.JPG)






### 3. EXPLORE DATASET


Getting a concise `summary` of the dataframe admission_df.

{% highlight ruby %}
admission_df.info()
{% endhighlight %}

OUTPUT.

{% highlight ruby %}

<class 'pandas.core.frame.DataFrame'>
RangeIndex: 500 entries, 0 to 499
Data columns (total 8 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   GRE Score          500 non-null    int64  
 1   TOEFL Score        500 non-null    int64  
 2   University Rating  500 non-null    int64  
 3   SOP                500 non-null    float64
 4   LOR                500 non-null    float64
 5   CGPA               500 non-null    float64
 6   Research           500 non-null    int64  
 7   Chance of Admit    500 non-null    float64
dtypes: float64(4), int64(4)
memory usage: 31.4 KB

{% endhighlight %}

Getting `statistical summary` of data frame admission_df.

{% highlight ruby %}
admission_df.describe()
{% endhighlight %}

OUTPUT.

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_4.png)

We can see that there is a column named `Serial No.` which are just ids no use of it so we can remove it.

{% highlight ruby %}
admission_df = admission_df.drop(['Serial No.'], axis = 1)
{% endhighlight %}

We want to sure there are no `null` elements in our data.

{% highlight ruby %}
#=> checking the null values
admission_df.isnull().sum()
{% endhighlight %}

RESULT: 

{% highlight ruby %}

GRE Score            0
TOEFL Score          0
University Rating    0
SOP                  0
LOR                  0
CGPA                 0
Research             0
Chance of Admit      0
dtype: int64

{% endhighlight %}


Grouping by University ranking  
{% highlight ruby %}
df_university = admission_df.groupby(by = 'University Rating').mean()
df_university
{% endhighlight %}


RESULT: 

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_5.JPG)

Performing data visualiztion for batter understanding.

Let's check the destribution of `data`.

{% highlight ruby %}
 admission_df.hist(bins = 30, figsize = (20, 20), color = 'r')
{% endhighlight %}

RESULT: 

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_6.JPG)

It is clear from the distributions, students with varied merit apply for the university.

{% highlight ruby %}
sns.pairplot(admission_df)
{% endhighlight %}

RESULT: 
{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_7.png)

Understanding the relation between different factors responsible for graduate admissions

{% highlight ruby %}
fig = sns.regplot(x="GRE Score", y="TOEFL Score", data=admission_df)
plt.title("GRE Score vs TOEFL Score")
plt.show()
{% endhighlight %}

RESULT: 

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_9.JPG)


People with higher GRE Scores also have higher TOEFL Scores which is justified because both TOEFL and GRE have a verbal section which although not similar are relatable

{% highlight ruby %}
fig = sns.regplot(x="GRE Score", y="CGPA", data=admission_df)
plt.title("GRE Score vs CGPA")
plt.show()
{% endhighlight %}

RESULT: 

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_10.JPG)

Although there are exceptions, people with higher CGPA usually have higher GRE scores maybe because they are smart or hard working



{% highlight ruby %}
fig = sns.lmplot(x="CGPA", y="LOR ", data=admission_df, hue="Research")
plt.title("GRE Score vs CGPA")
plt.show()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_11.JPG)

LORs are not that related with CGPA so it is clear that a persons LOR is not dependent on that persons academic excellence. Having research experience is usually related with a good LOR which might be justified by the fact that supervisors have personal interaction with the students performing research which usually results in good LORs

{% highlight ruby %}
fig = sns.lmplot(x="GRE Score", y="LOR ", data=admission_df, hue="Research")
plt.title("GRE Score vs CGPA")
plt.show()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_12.JPG)

GRE scores and LORs are also not that related. People with different kinds of LORs have all kinds of GRE scores

{% highlight ruby %}
fig = sns.regplot(x="CGPA", y="SOP", data=admission_df)
plt.title("GRE Score vs CGPA")
plt.show()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_13.JPG)

CGPA and SOP are not that related because Statement of Purpose is related to academic performance, but since people with good CGPA tend to be more hard working so they have good things to say in their SOP which might explain the slight move towards higher CGPA as along with good SOPs


{% highlight ruby %}
fig = sns.regplot(x="GRE Score", y="SOP", data=admission_df)
plt.title("GRE Score vs CGPA")
plt.show()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_14.JPG)


Similary, GRE Score and CGPA is only slightly related


{% highlight ruby %}
fig = sns.regplot(x="GRE Score", y="SOP", data=admission_df)
plt.title("GRE Score vs CGPA")
plt.show()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_15.JPG)


Applicants with different kinds of SOP have different kinds of TOEFL Score. So the quality of SOP is not always related to the applicants English skills.


Correlation among variables

{% highlight ruby %}
corr_matrix = admission_df.corr()
plt.figure(figsize = (12, 12))
sns.heatmap(corr_matrix, annot = True)
plt.show()
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_11.JPG)


### 4. PREPROCESSING - CREATE TRAINING AND TESTING DATASET

Checking columns 

{% highlight ruby %}
admission_df.columns
{% endhighlight %}

{% highlight ruby %}
Index(['GRE Score', 'TOEFL Score', 'University Rating', 'SOP', 'LOR ', 'CGPA',
       'Research', 'Chance of Admit'],
      dtype='object')
{% endhighlight %}


{% highlight ruby %}
X = admission_df.drop(columns = ['Chance of Admit'])
{% endhighlight %}

{% highlight ruby %}
y = admission_df['Chance of Admit']
{% endhighlight %}

{% highlight ruby %}
X.shape
{% endhighlight %}

RESULT:
`(500, 7)`

{% highlight ruby %}
X = np.array(X)
y = np.array(y)
{% endhighlight %}

{% highlight ruby %}
y = y.reshape(-1,1)
y.shape
{% endhighlight %}

RESULT:
`(500, 1)`


Scaling the data before training the model

{% highlight ruby %}
from sklearn.preprocessing import StandardScaler, MinMaxScaler
scaler_x = StandardScaler()
X = scaler_x.fit_transform(X)

scaler_y = StandardScaler()
y = scaler_y.fit_transform(y)
{% endhighlight %}



Spliting the data in to test and train sets

{% highlight ruby %}
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.15)
{% endhighlight %}


### 5. TRAIN AND EVALUATE A LINEAR REGRESSION MODEL

{% highlight ruby %}
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, accuracy_score
{% endhighlight %}


{% highlight ruby %}
LinearRegression_model = LinearRegression()
LinearRegression_model.fit(X_train, y_train)
{% endhighlight %}


{% highlight ruby %}
accuracy_LinearRegression = LinearRegression_model.score(X_test, y_test)
accuracy_LinearRegression
{% endhighlight %}

Result: `0.795970795592809`


### 6. TRAIN AND EVALUATE AN ARTIFICIAL NEURAL NETWORK

Let's see the `shortest message`

{% highlight ruby %}
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense, Activation, Dropout
from tensorflow.keras.optimizers import Adam
{% endhighlight %}

{% highlight ruby %}
ANN_model = keras.Sequential()
ANN_model.add(Dense(50, input_dim = 7))
ANN_model.add(Activation('relu'))
ANN_model.add(Dense(150))
ANN_model.add(Activation('relu'))
ANN_model.add(Dropout(0.5))
ANN_model.add(Dense(150))
ANN_model.add(Activation('relu'))
ANN_model.add(Dropout(0.5))
ANN_model.add(Dense(50))
ANN_model.add(Activation('linear'))
ANN_model.add(Dense(1))
ANN_model.compile(loss = 'mse', optimizer = 'adam')
ANN_model.summary()
{% endhighlight %}

{% highlight ruby %}
Model: "sequential"
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
dense (Dense)                (None, 50)                400       
_________________________________________________________________
activation (Activation)      (None, 50)                0         
_________________________________________________________________
dense_1 (Dense)              (None, 150)               7650      
_________________________________________________________________
activation_1 (Activation)    (None, 150)               0         
_________________________________________________________________
dropout (Dropout)            (None, 150)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 150)               22650     
_________________________________________________________________
activation_2 (Activation)    (None, 150)               0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 150)               0         
_________________________________________________________________
dense_3 (Dense)              (None, 50)                7550      
_________________________________________________________________
activation_3 (Activation)    (None, 50)                0         
_________________________________________________________________
dense_4 (Dense)              (None, 1)                 51        
=================================================================
Total params: 38,301
Trainable params: 38,301
Non-trainable params: 0
_________________________________________________________________
{% endhighlight %}

{% highlight ruby %}
ANN_model.compile(optimizer='Adam', loss='mean_squared_error')
{% endhighlight %}

{% highlight ruby %}
epochs_hist = ANN_model.fit(X_train, y_train, epochs = 100, batch_size = 20, validation_split = 0.2)
{% endhighlight %}


{% highlight ruby %}
Epoch 1/100
17/17 [==============================] - 0s 10ms/step - loss: 0.5987 - val_loss: 0.2677
Epoch 2/100
17/17 [==============================] - 0s 2ms/step - loss: 0.4072 - val_loss: 0.2840
Epoch 3/100
17/17 [==============================] - 0s 2ms/step - loss: 0.3481 - val_loss: 0.2514
Epoch 4/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2824 - val_loss: 0.2456
Epoch 5/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2683 - val_loss: 0.2753
Epoch 6/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2648 - val_loss: 0.2446
Epoch 7/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2748 - val_loss: 0.2646
Epoch 8/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2532 - val_loss: 0.2883
Epoch 9/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2452 - val_loss: 0.2392
Epoch 10/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2315 - val_loss: 0.2498
Epoch 11/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2238 - val_loss: 0.2151
Epoch 12/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2485 - val_loss: 0.2507
Epoch 13/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2523 - val_loss: 0.2406
Epoch 14/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2239 - val_loss: 0.2531
Epoch 15/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2190 - val_loss: 0.2153
Epoch 16/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2097 - val_loss: 0.2868
Epoch 17/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2120 - val_loss: 0.2647
Epoch 18/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2044 - val_loss: 0.2550
Epoch 19/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2062 - val_loss: 0.2609
Epoch 20/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2109 - val_loss: 0.2244
Epoch 21/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2051 - val_loss: 0.2444
Epoch 22/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2048 - val_loss: 0.2399
Epoch 23/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1909 - val_loss: 0.2379
Epoch 24/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1962 - val_loss: 0.2261
Epoch 25/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1883 - val_loss: 0.2631
Epoch 26/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2176 - val_loss: 0.2200
Epoch 27/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1901 - val_loss: 0.2430
Epoch 28/100
17/17 [==============================] - 0s 2ms/step - loss: 0.2034 - val_loss: 0.2405
Epoch 29/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1905 - val_loss: 0.2395
Epoch 30/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1976 - val_loss: 0.2455
Epoch 31/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1951 - val_loss: 0.2165
Epoch 32/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1888 - val_loss: 0.2279
Epoch 33/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1912 - val_loss: 0.2262
Epoch 34/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1950 - val_loss: 0.1985
Epoch 35/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1912 - val_loss: 0.2035
Epoch 36/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1943 - val_loss: 0.2680
Epoch 37/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1728 - val_loss: 0.2742
Epoch 38/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1930 - val_loss: 0.2100
Epoch 39/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1718 - val_loss: 0.2568
Epoch 40/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1726 - val_loss: 0.2058
Epoch 41/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1775 - val_loss: 0.2385
Epoch 42/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1781 - val_loss: 0.2659
Epoch 43/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1766 - val_loss: 0.2716
Epoch 44/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1962 - val_loss: 0.2207
Epoch 45/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1852 - val_loss: 0.2786
Epoch 46/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1662 - val_loss: 0.2267
Epoch 47/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1523 - val_loss: 0.2635
Epoch 48/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1558 - val_loss: 0.2660
Epoch 49/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1592 - val_loss: 0.2320
Epoch 50/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1483 - val_loss: 0.2649
Epoch 51/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1580 - val_loss: 0.2737
Epoch 52/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1372 - val_loss: 0.2154
Epoch 53/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1351 - val_loss: 0.2991
Epoch 54/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1715 - val_loss: 0.2176
Epoch 55/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1727 - val_loss: 0.2840
Epoch 56/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1444 - val_loss: 0.2457
Epoch 57/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1526 - val_loss: 0.2204
Epoch 58/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1563 - val_loss: 0.2948
Epoch 59/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1492 - val_loss: 0.2274
Epoch 60/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1400 - val_loss: 0.2485
Epoch 61/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1438 - val_loss: 0.2475
Epoch 62/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1603 - val_loss: 0.2517
Epoch 63/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1696 - val_loss: 0.2102
Epoch 64/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1461 - val_loss: 0.2394
Epoch 65/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1324 - val_loss: 0.2174
Epoch 66/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1441 - val_loss: 0.2413
Epoch 67/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1396 - val_loss: 0.2292
Epoch 68/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1415 - val_loss: 0.2504
Epoch 69/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1415 - val_loss: 0.2383
Epoch 70/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1299 - val_loss: 0.2379
Epoch 71/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1331 - val_loss: 0.2439
Epoch 72/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1316 - val_loss: 0.2343
Epoch 73/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1283 - val_loss: 0.2632
Epoch 74/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1504 - val_loss: 0.3116
Epoch 75/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1532 - val_loss: 0.2292
Epoch 76/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1389 - val_loss: 0.2442
Epoch 77/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1393 - val_loss: 0.2709
Epoch 78/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1295 - val_loss: 0.2829
Epoch 79/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1324 - val_loss: 0.2107
Epoch 80/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1208 - val_loss: 0.2660
Epoch 81/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1336 - val_loss: 0.2807
Epoch 82/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1174 - val_loss: 0.2388
Epoch 83/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1268 - val_loss: 0.2467
Epoch 84/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1393 - val_loss: 0.2446
Epoch 85/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1342 - val_loss: 0.2534
Epoch 86/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1181 - val_loss: 0.2381
Epoch 87/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1433 - val_loss: 0.2400
Epoch 88/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1151 - val_loss: 0.2853
Epoch 89/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1181 - val_loss: 0.2449
Epoch 90/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1191 - val_loss: 0.2596
Epoch 91/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1178 - val_loss: 0.2746
Epoch 92/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1200 - val_loss: 0.2831
Epoch 93/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1331 - val_loss: 0.2721
Epoch 94/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1027 - val_loss: 0.2789
Epoch 95/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1235 - val_loss: 0.2386
Epoch 96/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1177 - val_loss: 0.2672
Epoch 97/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1148 - val_loss: 0.2774
Epoch 98/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1154 - val_loss: 0.2934
Epoch 99/100
17/17 [==============================] - 0s 2ms/step - loss: 0.0984 - val_loss: 0.2418
Epoch 100/100
17/17 [==============================] - 0s 2ms/step - loss: 0.1098 - val_loss: 0.2488
{% endhighlight %}

{% highlight ruby %}
result = ANN_model.evaluate(X_test, y_test)
accuracy_ANN = 1 - result
print("Accuracy : {}".format(accuracy_ANN))
{% endhighlight %}

{% highlight ruby %}
3/3 [==============================] - 0s 665us/step - loss: 0.2416
Accuracy : 0.7584277391433716
{% endhighlight %}

{% highlight ruby %}
epochs_hist.history.keys()
{% endhighlight %}

`dict_keys(['loss', 'val_loss'])`

{% highlight ruby %}
plt.plot(epochs_hist.history['loss'])
plt.title('Model Loss Progress During Training')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.legend(['Training Loss'])
{% endhighlight %}

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_16.JPG)


#### TRAIN AND EVALUATE A DECISION TREE AND RANDOM FOREST MODELS
Now, I am going to use decision tree builds regression models. As we all know that decision tree breaks down a dataset into smaller subsets while at the same time an associated decision tree is incrementally developed. The final result is a tree with decision nodes and leaf nodes.


{% highlight ruby %}
from sklearn.tree import DecisionTreeRegressor
DecisionTree_model = DecisionTreeRegressor()
DecisionTree_model.fit(X_train, y_train)
{% endhighlight %}

{% highlight ruby %}
accuracy_DecisionTree = DecisionTree_model.score(X_test, y_test)
accuracy_DecisionTree
{% endhighlight %}

Result: `0.5616226623761651`

As we can see result is not so good.


Now we going to use renowned ensembling model `random forest`. In which it make up a random forest model which is an ensemble model. Predictions made by each decision tree are averaged to get the prediction of random forest model.A random forest regressor fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. 


{% highlight ruby %}
from sklearn.ensemble import RandomForestRegressor
RandomForest_model = RandomForestRegressor(n_estimators=100, max_depth = 10)
RandomForest_model.fit(X_train, y_train)
{% endhighlight %}

{% highlight ruby %}
accuracy_RandomForest = RandomForest_model.score(X_test, y_test)
accuracy_RandomForest
{% endhighlight %}

Result: `0.752819921074695`

Now result is much better.
#### 7. UNDERSTAND VARIOUS REGRESSION KPIs

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_18.JPG)

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_20.JPG)

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_21.JPG)

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_22.JPG)

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_23.JPG)

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_24.JPG)

{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_25.JPG)


#### 8. MODEL PERFORMANCE

After model fitting, we would like to assess the performance of the model by comparing model predictions to actual(TRUE) data


{% highlight ruby %}
y_predict = LinearRegression_model.predict(X_test)
plt.plot(y_test, y_predict, '^', color = 'r')
{% endhighlight %}


{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_17.JPG)



{% highlight ruby %}
y_predict_orig = scaler_y.inverse_transform(y_predict)
y_test_orig = scaler_y.inverse_transform(y_test)
{% endhighlight %}



{% highlight ruby %}
plt.plot(y_test_orig, y_predict_orig, '^', color = 'r')
{% endhighlight %}


{: .center}
![GOT]({{site.baseurl}}/assets/img/pro_grad_pic_17.JPG)


{% highlight ruby %}
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
from math import sqrt

RMSE = float(format(np.sqrt(mean_squared_error(y_test_orig, y_predict_orig)),'.3f'))
MSE = mean_squared_error(y_test_orig, y_predict_orig)
MAE = mean_absolute_error(y_test_orig, y_predict_orig)
r2 = r2_score(y_test_orig, y_predict_orig)
adj_r2 = 1-(1-r2)*(n-1)/(n-k-1)

print('RMSE =',RMSE, '\nMSE =',MSE, '\nMAE =',MAE, '\nR2 =', r2, '\nAdjusted R2 =', adj_r2) 

{% endhighlight %}


{% highlight ruby %}
RMSE = 0.057 
MSE = 0.0032666218189135966 
MAE = 0.04155201155403992 
R2 = 0.795970795592809 
Adjusted R2 = 0.7746543115502666
{% endhighlight %}




#### 9. Please find below Graduate Admission Prediction jupyter notebook on github

[link to github!](https://github.com/zubairashfaque/REGRESSION/tree/master/Graduate_Admission_Prediction)


`***` Taken from: https://www.usatoday.com/story/college/2017/04/26/heres-what-it-really-takes-to-get-into-the-ivy-league-these-days/37430681/ 
