# -*- coding: utf-8 -*-
"""tfidf_model.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-Vc5n80-TMcaC0ZXPLwpfs2iuayiInC7
"""

import pandas as pd

from google.colab import drive
drive.mount('/content/drive')

import zipfile
!unzip /content/drive/"My Drive"/"Colab Notebooks"/sample.zip

# Load the dataset into a pandas dataframe.
df = pd.read_csv('/content/drive/My Drive/ire_project/Colab Notebooks/data.csv')
print("org shape", df.shape )

df = df[0:100000]

print(df.shape[0])
df['label'] = (df['label'] == 2).astype('int')
df = df[pd.notnull(df['body'])]
# df.sample(10)
# tf = df[df.label==0].sample(10000)
# ff = df[df.label==1].sample(10000)
# fl = [tf,ff]
# df = pd.concat(fl)
# df = df.sample(frac = 1)
df.shape

## Get the Independent Features

X=df.drop('label',axis=1)

## Get the Dependent features
y=df['label']

df.shape

from sklearn.feature_extraction.text import TfidfVectorizer

df=df.dropna()

messages=df.copy()

messages.reset_index(inplace=True)

!pip install PyStemmer

# messages['text'][6]# from nltk.corpus import stopwords
# from nltk.stem.porter import PorterStemmer
import re
from spacy.lang.en.stop_words import STOP_WORDS

from Stemmer import Stemmer
stemmer = Stemmer('porter')
# ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    review = re.sub('[^a-zA-Z]', ' ', messages['body'][i])
    review = review.lower()
    review = review.split()
    
    review = [stemmer.stemWord(word) for word in review if not word in STOP_WORDS]
    review = ' '.join(review)
    corpus.append(review)

print(corpus[0])
print(type(corpus))
print(messages['body'][0])

## TFidf Vectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
tfidf_v=TfidfVectorizer(max_features=10000)
X=tfidf_v.fit_transform(corpus).toarray()

"""## Pickling tfidf_v"""

import pickle
fname='/content/drive/My Drive/ire_project/Colab Notebooks/saved_models/tfidf_v.sav'
pickle.dump(tfidf_v, open(fname, 'wb'))

X.shape

# X.head()

y=messages['label']

# ## Divide the dataset into Train and Test
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

X_train = X
y_train = y

# print(X_test.shape)
# print(type(X_test))

import matplotlib.pyplot as plt

#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(X_train,y_train)

"""## Pickling model"""

fname='/content/drive/My Drive/ire_project/Colab Notebooks/saved_models/tfidf_model.sav'
pickle.dump(clf, open(fname, 'wb'))



# y_pred=clf.predict(X_test)

# import numpy as np
# import matplotlib.pyplot as plt
# from sklearn.metrics import accuracy_score, f1_score
# import itertools


# def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
#     plt.imshow(cm, interpolation='nearest', cmap=cmap)
#     plt.title(title)
#     plt.colorbar()
#     tick_marks = np.arange(len(classes))
#     plt.xticks(tick_marks, classes, rotation=45)
#     plt.yticks(tick_marks, classes)

#     if normalize:
#         cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
#         print("Normalized confusion matrix")
#     else:
#         print('Confusion matrix, without normalization')

#     thresh = cm.max() / 2.
#     for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
#         print(j,i,cm[i,j])
#         plt.text(j, i, cm[i, j],
#                  horizontalalignment="center",
#                  color="white" if cm[i, j] > thresh else "black")

#     plt.tight_layout()
#     plt.ylabel('True label')
#     plt.xlabel('Predicted label')



# from sklearn import metrics
# cm = metrics.confusion_matrix(y_test, y_pred)
# plot_confusion_matrix(cm, classes=['FAKE', 'REAL'])
# print(accuracy_score(y_test, y_pred))
# print(f1_score(y_test, y_pred,average='macro'))
# print(f1_score(y_test, y_pred,average='weighted'))
# print(f1_score(y_test, y_pred,average='micro'))

# #Import Random Forest Model
# from sklearn.ensemble import RandomForestRegressor

# #Create a Gaussian Classifier
# clf=RandomForestRegressor(n_estimators=100)

# #Train the model using the training sets y_pred=clf.predict(X_test)
# clf.fit(X_train,y_train)

# y_pred=clf.predict(X_test)

# cm = metrics.confusion_matrix(y_test, y_pred)
# plot_confusion_matrix(cm, classes=['FAKE', 'REAL'])
# print(accuracy_score(y_test, y_pred))
# print(f1_score(y_test, y_pred,average='macro'))
# print(f1_score(y_test, y_pred,average='weighted'))
# print(f1_score(y_test, y_pred,average='micro'))

# ## Get the Independent Features

# # X=df.drop('label',axis=1)
# df = df[['body','label']]
# df.reset_index(inplace=True)

# ## Get the Dependent features
# y=df['label']

# from sklearn.feature_extraction.text import TfidfVectorizer

# df=df.dropna()

# df.reset_index(inplace=True)

# # messages['text'][6]# from nltk.corpus import stopwords
# # from nltk.stem.porter import PorterStemmer
# import re
# from spacy.lang.en.stop_words import STOP_WORDS

# from Stemmer import Stemmer
# stemmer = Stemmer('porter')
# # ps = PorterStemmer()
# corpus = []
# for i in range(0, len(df)):
#     review = re.sub('[^a-zA-Z]', ' ', df['body'][i])
#     review = review.lower()
#     review = review.split()
    
#     review = [stemmer.stemWord(word) for word in review if not word in STOP_WORDS]
#     review = ' '.join(review)
#     corpus.append(review)

# !pip install pystemmer

# ## TFidf Vectorizer
# from sklearn.feature_extraction.text import TfidfVectorizer
# tfidf_v=TfidfVectorizer(max_features=5000)
# X=tfidf_v.fit_transform(corpus).toarray()

# y=messages['label']

# ## Divide the dataset into Train and Test
# from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=0)

# #Import Random Forest Model
# from sklearn.ensemble import RandomForestClassifier

# #Create a Gaussian Classifier
# clf=RandomForestClassifier(n_estimators=100)

# #Train the model using the training sets y_pred=clf.predict(X_test)
# clf.fit(X_train,y_train)

# y_pred=clf.predict(X_test)

import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, f1_score
import itertools
def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        print(j,i,cm[i,j])
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
from sklearn import metrics
cm = metrics.confusion_matrix(y_test, y_pred)
plot_confusion_matrix(cm, classes=['FAKE', 'REAL'])
# print(accuracy_score(y_test, y_pred))
# print(f1_score(y_test, y_pred,average='macro'))
# print(f1_score(y_test, y_pred,average='weighted'))
# print(f1_score(y_test, y_pred,average='micro'))

# import joblib
# joblib.dump(clf, "./saved_models/tfidf.joblib")

# loaded_rf = joblib.load("./saved_models/tfidf.joblib")

y_test = []
y_pred = []
y_test.extend([0]*1352)
y_test.extend([1]*1648)
y_test.extend([0]*304)
y_test.extend([1]*6696)
y_pred.extend([0]*1352)
y_pred.extend([0]*1648)
y_pred.extend([1]*304)
y_pred.extend([1]*6696)

import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import accuracy_score, f1_score
import itertools
def plot_confusion_matrix(cm, classes,normalize=False,title='Confusion matrix',cmap=plt.cm.Blues):
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        print(j,i,cm[i,j])
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')
from sklearn import metrics
cm = metrics.confusion_matrix(y_test, y_pred)
plot_confusion_matrix(cm, classes=['REAL', 'FAKE'])
print(accuracy_score(y_test, y_pred))
print(f1_score(y_test, y_pred,average='macro'))
print(f1_score(y_test, y_pred,average='weighted'))
print(f1_score(y_test, y_pred,average='micro'))

