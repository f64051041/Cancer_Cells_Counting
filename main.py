import cv2
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np



def connected_count(img):
    x=img.shape[0]
    y=img.shape[1]
    A=np.ones((x,y))*(-1)
    count=1    
    for i in range(x):
        for j in range(y):
            if(img[i][j]==255):
                if((j-1)<0):
                    A[i][j]=count
                    count+=1                    
                else:    
                    if A[i][j-1]!=-1:
                        A[i][j]=A[i][j-1]
                    else:
                        A[i][j]=count
                        count+=1
    
    B=np.ones((count+1))*(-1)
    for i in range(x):
        for j in range(y):
            if((i-1)>=0):
                if (A[i][j]!=-1):
                    if((A[i-1][j])!=-1 and A[i][j]!=A[i-1][j]):
                        B[int(A[i][j])]=int(A[i-1][j])
    
    count_=-1
    
    for i in range(count+1):
        if B[i]==-1:
            count_+=1
    return count_        

                

            
                


#img = Image.open('cv.png')
img = cv2.imread('cv.png',0)
ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th1 = 255 - th1
kernel = np.ones((3,3), np.uint8)
img=cv2.erode(th1, kernel, iterations = 5)
img = cv2.dilate(img, kernel, iterations = 3)
cv2.imwrite('answer_1.jpg', th1)
#print(connected_count(th1))
print('Number of object is',connected_count(img))


#plt.imshow(img, 'gray')
#plt.show()
