print("THIS IS THE CURRENCY CHANGE PROGRAM ")
print("AVAILABLE OPTIONS ARE: RUPEES , POUND , EUROS , US DOLLAR , CANADIAN DOLLAR , CHINESE YUAN , RUSSIAN RUBEL")
i1=input("ENTER 1ST")
i=i1.upper()
f1=input("ENTER 2ND")
f=f1.upper()
ind=0
curr=["RUPEES","POUND","EUROS","US DOLLAR","CANADIAN DOLLAR","CHINESE YUAN","RUSSIAN RUBAL"]
val=[1,0.01,0.012,0.012,0.016,0.088,0.74]
if i=="RUPEES":
    for j in range(len(curr)):
        if curr[j]==f:
            ind=j
else:
    for j in range(len(curr)):
        if curr[j]==i:
            ind=j
a=float(input("ENTER AMOUNT"))
if i=="RUPEES":
    print(a*val[ind])
else:
    print(a/val[ind])

