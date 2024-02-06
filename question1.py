
# Question 1
#Write a function to calculate the Euclidean distance and Manhattan distance between two vectors. 
#The vectors dimension is variable. Please don’t use any distance calculation functions available in Python.
def distCalculator(v1,v2):
    ch=input("Manhattan or Eucledian (M/E) : ")
    V=[]
    if ch.lower()=="e":
        try:
            V.append(v1)
            V.append(v2)
            sum=0
            for i in range(len(V)+1):
                sum+=(V[0][i]-V[1][i])**2
            distance=sum**(1/2)
            return distance
        except:
            return " Vectors must be of same dimensions"
    elif ch.lower()=="m":
        try:
            V.append(v1)
            V.append(v2)
            sum=0
            for i in range(len(V)+1):
                sum+=abs(V[0][i]-V[1][i])
            distance=sum
            return distance
        except:
            return " Vectors must be of same dimensions"
v1=[1,2,3]
v2=[2,2,2]
# euc=distCalculator(v1,v2)
# print(euc)


# Question 3
#Write a function to implement k-NN classifier. k is a variable and based on that the count of neighbors should be selected
def knn_Classifier(data,k):
    data=list(data.items())
    key=0
    for i in data[0]:
        if type(i)==int:
            key=i
    encodedlist=data.sort(key=lambda x: x[1])
    return encodedlist
    
# Question 3
#Write a function to convert categorical variables to numeric using label encoding. Don’t use any existing functionalities.
def labelEncoding(category):
    labels=[i+1 for i in range(len(category))]
    encoding=dict(zip(labels,category))
    return encoding

# colors=["blue","green","yellow","red"]
# Colors=labelEncoding(colors)
# print(Colors)

# Question 4
#Write a function to convert categorical variables to numeric using One-Hotencoding. Don’t use any existing functionalities.
def onehotEncoding(category):
    values=list(set(category))
    labels = [[0 for i in range(len(category))] for i in range(len(values))]
    for v in range(len(values)):    
        for i in range(len(category)):
            if values[v]==category[i]:
                labels[v][i]=1
    encoding=dict(zip(values,labels))
    return encoding

# colors=["blue","green","blue","red"]
# Colors=onehotEncoding(colors)
# print(Colors)
