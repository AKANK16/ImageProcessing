import cv2
import numpy as np


from firebase import firebase
import json
firebase=firebase.FirebaseApplication('https://musafirclient.firebaseio.com')
#link to the firebase console

'''
#reading the firebase
result=firebase.get('Indicator',None) #indicator is the database key who's value you want to fetch,secoond arguement is child name
#get returns a json object
print(result)
'''



fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
cap=cv2.VideoCapture(1)
sent=False

while(1):
    ret, frame = cap.read()


    roi=frame[250:310,350:450]
    fgmask = fgbg.apply(roi) 
   


    for val in fgmask[1]:
        if val== 255 :
            print("Zebra croassing Jumped!")
            
            #writing to the firebase
            #result=firebase.post('Indicator',)
            if not sent:
                userId="H2iloWmbQkUc5j0RB0f3SVCOoYI2"
                result=firebase.post('/users/'+userId + "/violations",json.dumps({"Violation":"Zebra crossing jumping","Date":"2 March 2019", "Amount":"200"})) #pass 0,1,2 in argument 3 according to classifier's result
                sent=True

    
    cv2.imshow('frame',frame)
    cv2.imshow('bg',fgmask)
    cv2.imshow('roi',roi)


    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
cap.release()
cv2.destroyAllWindows()
