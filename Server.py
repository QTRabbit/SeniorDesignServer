#    UCI Senior Design Project #
#    WATCH THE INFLUENCE       #
#    Authors: Avik Banjerr     #
#             Ivan Madrigal    #
#             Quyen To         #



import socket
import sys
from CSVTester import *

data= []

### This is a simple encryption function      ###
### Every even index digit will shift down 2  ###
### Every odd index digit will shift up 4     ###

def EncryptNumber(message):
    size_message = len(message)
    newmessage = ["" for x in range(size_message)]
    
    pointer = 0
    counter = True
    for x in message:
        if(x == '0' and counter):        #Even number. 0 ---> 8
            newmessage[pointer] = '8'
            counter = False
            pointer += 1
            
        elif(x == '0'):                  #Odd number. 0 ---> 4
            newmessage[pointer] = '4'
            counter = True
            pointer += 1
            
        elif(x == '1' and counter):      #Even number. 1 ---> 9
            newmessage[pointer] = '9'
            counter = False
            pointer += 1
        
        elif(x == '1'):                   #Odd number. 1 ---> 5
            newmessage[pointer] = '5'
            counter = True
            pointer += 1
        
        elif(x == '2' and counter):      #Even number. 2 ---> 0
            newmessage[pointer] = '0'
            counter = False
            pointer += 1
        
        elif(x == '2'):                 #Odd number. 2 ---> 6
            newmessage[pointer] = '6'
            counter = True
            pointer += 1
        
        elif(x == '3' and counter):     #Even number. 3 ---> 1
            newmessage[pointer] = '1'
            counter = False
            pointer += 1

        elif(x == '3'):                 #Odd number. 3 ---> 7
            newmessage[pointer] = '7'
            counter = True
            pointer += 1
            
        elif(x == '4' and counter):     #Even number. 4 ---> 2
            newmessage[pointer] = '2'
            counter = False
            pointer += 1
            
        elif(x == '4'):                 #Odd number. 4 ---> 8
            newmessage[pointer] = '8'
            counter = True
            pointer += 1
        
        elif(x =='5' and counter):      #Even number. 5 ---> 3
            newmessage[pointer] = '3'
            counter = False
            pointer += 1
            
        elif(x ==  '5'):              #Odd number. 5 ---> 9 
            newmessage[pointer] = '9'
            counter = True
            pointer += 1
        
            
        elif(x == '6' and counter):    #Even number. 6 ---> 4
            newmessage[pointer] = '4'
            counter = False
            pointer += 1
            
        elif(x == '6'):               #Odd number. 6 ---> 0
            newmessage[pointer] ='0'
            counter = True
            pointer += 1
            
        elif(x == '7' and counter):  #Even number. 7 ---> 5
            newmessage[pointer] = '5'
            counter = False
            pointer += 1
            
        elif(x == '7'):               #Odd number. 7 ---> 1
            newmessage[pointer] = '1'
            counter = True
            pointer += 1
            
        elif(x == '8' and counter):   #Even number. 8 ---> 6 
            newmessage[pointer] = '6'
            counter = False
            pointer += 1
            
        elif(x == '8'):               #Odd number. 8 ---> 2
            newmessage[pointer] = '2'
            counter = True
            pointer += 1
            
        elif(x == '9' and counter):   #Even number. 9 ---> 7
            newmessage[pointer]= '7'
            counter = False
            pointer += 1
            
        elif(x == '9'):               #Odd number 9 ---> 3
            newmessage[pointer] = '3'
            counter = True
            pointer += 1
        else:
            newmessage[pointer] = x
            pointer += 1
            if(counter == True):
                counter = False
            else:
                counter = True
            
    newmessage = ''.join([str(elem) for elem in newmessage])
    return newmessage





def DecryptNumber(message):
    size_message = len(message)
    newmessage = ["" for x in range(size_message)]
    
    pointer = 0
    counter = True
    for x in message:
        if(x == '0' and counter):        #Even number. 0 ---> 2
            newmessage[pointer] = '2'
            counter = False
            pointer += 1
            
        elif(x == '0'):                  #Odd number. 0 ---> 6
            newmessage[pointer] = '6'
            counter = True
            pointer += 1
            
        elif(x == '1' and counter):      #Even number. 1 ---> 3
            newmessage[pointer] = '3'
            counter = False
            pointer += 1
        
        elif(x == '1'):                   #Odd number. 1 ---> 7
            newmessage[pointer] = '7'
            counter = True
            pointer += 1
        
        elif(x == '2' and counter):      #Even number. 2 ---> 4
            newmessage[pointer] = '4'
            counter = False
            pointer += 1
        
        elif(x == '2'):                 #Odd number. 2 ---> 8
            newmessage[pointer] = '8'
            counter = True
            pointer += 1
        
        elif(x == '3' and counter):     #Even number. 3 ---> 5
            newmessage[pointer] = '5'
            counter = False
            pointer += 1

        elif(x == '3'):                 #Odd number. 3 ---> 9
            newmessage[pointer] = '9'
            counter = True
            pointer += 1
            
        elif(x == '4' and counter):     #Even number. 4 ---> 6
            newmessage[pointer] = '6'
            counter = False
            pointer += 1
            
        elif(x == '4'):                 #Odd number. 4 ---> 0
            newmessage[pointer] = '0'
            counter = True
            pointer += 1
        
        elif(x =='5' and counter):      #Even number. 5 ---> 7
            newmessage[pointer] = '7'
            counter = False
            pointer += 1
            
        elif(x ==  '5'):              #Odd number. 5 ---> 1
            newmessage[pointer] = '1'
            counter = True
            pointer += 1
        
            
        elif(x == '6' and counter):    #Even number. 6 ---> 8
            newmessage[pointer] = '8'
            counter = False
            pointer += 1
            
        elif(x == '6'):               #Odd number. 6 ---> 2
            newmessage[pointer] ='2'
            counter = True
            pointer += 1
            
        elif(x == '7' and counter):  #Even number. 7 ---> 9
            newmessage[pointer] = '9'
            counter = False
            pointer += 1
            
        elif(x == '7'):               #Odd number. 7 ---> 3
            newmessage[pointer] = '3'
            counter = True
            pointer += 1
            
        elif(x == '8' and counter):   #Even number. 8 ---> 0
            newmessage[pointer] = '0'
            counter = False
            pointer += 1
            
        elif(x == '8'):               #Odd number. 8 ---> 4
            newmessage[pointer] = '4'
            counter = True
            pointer += 1
            
        elif(x == '9' and counter):   #Even number. 9 ---> 1
            newmessage[pointer]= '1'
            counter = False
            pointer += 1
            
        elif(x == '9'):               #Odd number 9 ---> 5
            newmessage[pointer] = '5'
            counter = True
            pointer += 1
        else:
            newmessage[pointer] = x
            pointer += 1
            if(counter == True):
                counter = False
            else:
                counter = True
    newmessage = ''.join([str(elem) for elem in newmessage])
    return newmessage



def Connect():
    HOST = "169.254.174.11" #this is your localhost
    PORT = 7000

    send_ecg = ECGCSV("ECGEX.csv")
    send_ppg = PPGCSV("ECGEX.csv")
    send_ecg = EncryptNumber(send_ecg)
    send_ppg = EncryptNumber(send_ppg)
    s = socket.socket() 
    print ('socket created')
    print("The Host is " + HOST)
    print("The Port is " + str(PORT))

    #Bind socket to Host and Port
    try:
        s.bind((HOST, PORT))
    except socket.error as err:
        print( 'Bind Failed, Error Code: ' + str(err[0]) + ', Message: ' + err[1])
        sys.exit()
    print ('Socket has been binded!')

    s.listen(5)
    print ('Socket is now listening\n')
    
    while 1:
        conn, addr = s.accept()
        print ('Connect with ' + addr[0] + ':' + str(addr[1]))
        buf = conn.recv(64)
        b = buf.decode(encoding='UTF-8')

        
        #print (buf)
        b = b[:-1]
        print(b)

        b = DecryptNumber(b)
        beginning = b[0] + b[1] + b[2] + b[3] 

        #ID WILL BE SET 4 DIGIT + 4 RANDOMLY GENERATED
        #FIRST FOUR WILL BE 0000
        if( beginning != "0000"):
            print("Following ID is Not Valid")
            print(b)
            conn.send(bytes("NO \r\n",'UTF-8'))
            conn.send(bytes(" \r\n",'UTF-8'))
            conn.send(bytes(" \r\n",'UTF-8'))
            continue
        
        if(b[4] == '0' and b[5] == '0' and b[6] == '0'):
            identif = b[7]
        elif(b[4] == '0' and b[5] == '0'):
            identif = b[6] + b[7]
        elif(b[4] == '0'):
            identif = b[5] + b[6] + b[7]
        else:
            identif = b[4] + b[5] + b[6] + b[7]

        print("The Server Has Connected To Patient Subject Number: ")
        print(identif)

        heart_rate = Load_Heart_Rate("HeartRate.csv", identif)
        body_temp = Load_Body_Temp("Body-Temperature-Measurements.csv", identif)

        heart_rate = EncryptNumber(heart_rate)
        body_temp = EncryptNumber(body_temp)
        #send_ecg = EncryptNumber(send_ecg)
        #send_ppg = EncryptNumber(send_ppg)
        
        #ya = CheckID(b)
        #make sure to inlude \n since the function called
        #use \r to end byte stream
        #in the client is readline and needs an end to line
        conn.send(bytes(heart_rate+" \n",'UTF-8'))
        conn.send(bytes(body_temp+" \n",'UTF-8'))
        conn.send(bytes(send_ppg+" \n",'UTF-8'))
        conn.send(bytes(send_ecg+" \r\n",'UTF-8'))
        #conn.send('abc999'.encode('utf-8')) #.encode('utf-8')
    s.close()


if __name__ == '__main__':
    #LoadData()
    Connect() 

