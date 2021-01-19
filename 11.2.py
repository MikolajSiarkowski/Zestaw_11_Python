import random
def selectsort(L, left, right):
    for i in range(left, right):
        
        k = i
        for j in range(i+1, right+1):
            if L[j] < L[k]:
                k = j
        item = L[k]
        
        while k > i:
            L[k] = L[k-1]
            k = k-1
        L[i] = item
        g.write(str(item)+"\t"+str(i)+"\n")
    g.write(str(L[right])+"\t"+str(right)+"\n")

filepath="dane.txt"
filepath1="dane1.txt"
f=open(filepath,"w")
g=open(filepath1,"w")
L=[]
for i in range(50):
    L.append(i)
random.shuffle(L)
for i in range(len(L)):
    f.write(str(L[i])+"\t"+str(i)+"\n")
print("lista przed sortowaniem:\n",L)
selectsort(L,0,49)
print("\nlista po sortowaniu:\n",L)
f.close()
g.close()
