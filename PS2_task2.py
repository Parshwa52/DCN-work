import numpy as np
arr = [[1, 0, 0, 0, 1, 0, 1], [0, 1, 0, 0, 1, 1, 1], [0, 0, 1, 0, 1, 1, 0],
       [0, 0, 0, 1, 0, 1, 1]]
n = 7
k = 4
G = np.array(arr)
print("Generator----------")
print(G)
m = np.array([1, 0, 1, 0])
def syndrome_decode(codeword, n, k, G):
    
    HT = np.transpose(np.concatenate((np.identity(n - k),np.transpose(G[:, k:])) ,axis=1))
    
    syndrome = np.array(np.mod(np.dot(codeword, HT),2)) 
    
    print("H transpose : \n",HT,"\nSyndrome is : ",syndrome) 
    for row,i in zip(HT,range(n)):
        if np.array_equal(syndrome,row):
            codeword[i] ^= 1
            return(codeword,' Error is Detected and Corrected ',i)
    return(codeword,' No correction is necessary',-1)

codeword = np.mod(np.dot(m, G), 2)
print('Original codeword : ' , codeword)
codeword[2] = not [codeword[2]]

print('Recieved codeword : ' , codeword)
decodedop  = syndrome_decode(codeword, n, k, G)

print('codeword after Decoding: ' , decodedop[0],decodedop[1],end="")
if decodedop[2] != -1 :
    print('at index',decodedop[2],'of codeword')
else:print("")
print("Hence The corrected message at reciever's end is ",decodedop[0][:k])

