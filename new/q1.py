import numpy as np

X1=[0.5,-1.1,0.24,-0.22,-1.8]
X2=[0.15,-1.4,0.11,-0.28,-0.3]
X3=[0.1,-1.4,0.11,0.6,-1.11]
inputs = np.array([X1,X2,X3])

w=[0.1, 0.17,0.2,-1.1, -0.4]

d=np.array([1,-1,1])




epochs = 0
c = 2.5
outputs = []
e=10000
list_e = []

while(epochs<11):

  epochs+=1
  outputs=[]
  for i in range(3):
    y=0
    for j in range(5):
      y = y+ inputs[i][j]*w[j]
    if y>0:
      y=1
    elif y<0:
      y=-1
    outputs.append(y)
    w = w + c*(d[i]-y)*inputs[i];
    print(outputs,w)
  error = np.absolute(np.array(outputs) - np.array(d))
  error = np.mean(error)
  e=error;
  list_e.append(e)
  print(error)



  list_e
