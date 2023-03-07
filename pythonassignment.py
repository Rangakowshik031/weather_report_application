def CheckPrime(n): 
 c=2
 while c<m:
    if m%c==0:
        print("Prime - No")
        break
    else:
        c=c+1
 if c>=m:
    print("Prime - Yes")
 
 

def CheckArmstrong(p): 
 t=p 
 sum=0 
 while p>0:  
     rem=p%10 
     sum=sum+rem*rem*rem 
     p=int(p/10) 
 if sum==t: 
     print("Armstrong - Yes") 
 else: 
     print("Armstrong - No") 
 
 

def Ispalindrome(m): 
 t=m
 su=0
 while m>0:
    rem=m%10
    su=su*10+rem
    m=int(m/10)
 #print(su)
 if su==t:
    print("Palindrome - Yes")
 else:
    print("Palindrome - No")
 
 
def CheckPerfectNumber(q):
    su=0
    for i in range(1,q):
        if q%i==0:
            su=su+i
    if su==q:
        print("Perfect number - Yes")
    else:
        print("Perfect number - No")
        
    
 
 
m=int(input("enter any number=")) 
CheckPrime(m)
CheckArmstrong(m)
Ispalindrome(m) 
CheckPerfectNumber(m)
