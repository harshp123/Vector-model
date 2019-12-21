import nltk
from nltk.corpus import stopwords
import math
x1="Dr jay triloki has done many reasearch in web mining doamin web mining is the research topic these days web mining is intersting"
x2="Harsh is interning under Dr jay triloki in web mining"
def convertintolist(x):
    l=[]
    l=x.split(" ")
    return l
def removestopwords(x):
    l=[]
    a=x.split(" ")
    p=set(stopwords.words("english"))
    for i in a:
        if i not in p:
            l.append(i)
    return l
def convertintounique(a):
    l=[]
    for i in a:
        if i not in l:
            l.append(i)
    return l
#caluclating count of indvisual term and returning the count
def termfrequency(term, document):
    return (document.count(term))/len(document)
#calculating inverse documnet frequency of all words in the document
def inversedocumentfrequency(term,p1,p2):
    count=0
    x=0
    if i in p1:
        count=count+1
    if i in p2:
        count=count+1
    return 1+math.log(2/count)
#represnation of vector model
def repsvectormodel(x,l):
    r={}
    for i in l:
        if i in x:
            r.update({i:1})
        else:
            r.update({i:0})
    return r
def findvectormodel(y,d3):
        return y[i]*d3[i]
def calccosinesim(x,y):
    p=0
    q=0
    r=0
    for i in x.keys():
        if i in y.keys():
            p=p+x[i]*y[i]
    for i in x.keys():
        q=q+x[i]**2
    for i in y.keys():
        r=r+y[i]**2
    return p/(math.sqrt(q)*math.sqrt(r))
p=removestopwords(x1)
p1=convertintounique(p)
p=removestopwords(x2)
p2=convertintounique(p)
d1={}
d2={}
#calling termfrequency function to calculate term frequency for 1st documnet
for i in p1:
    d1.update({i:termfrequency(i,convertintolist(x1))})
print("term frequency for 1st documnet : ",d1)

for i in p2:
    d2.update({i:termfrequency(i,convertintolist(x2))})
print("term frequency for 2nd documnet  : ",d2)
l1=p1.copy()
l1.extend(p2)
l2=convertintounique(l1)
d3={}
for i in l2:
    d3.update({i:inversedocumentfrequency(i,p1,p2)})
print("inverse documnet frequency for all words in both document : ",d3)
print(repsvectormodel(p1,l2))
print(repsvectormodel(p2,l2))
d4={}
for i in p1:
    d4.update({i:findvectormodel(d1,d3)})
print(d4)
d5={}
for i in p2:
    d5.update({i:findvectormodel(d2,d3)})
print(d5)
print(calccosinesim(d4,d5))
