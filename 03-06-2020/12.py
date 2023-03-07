class string:
    def __init__(self):
        a=input("enter a sting=")
        self.a=a
    def count(self):
        vowel=upper=lower=consonant=space=0
        for i in self.a:    
            if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or  i=='U' or i=='O'):
               vowel=vowel+1
            elif(i==" "):
                space=space+1
            else:
                consonant=consonant+1
            if(i.isupper()):
                upper=upper+1
            if(i.islower()):
                 lower=lower+1
        print(" vowels:{}\n consonats:{}\n space:{}\n upper:{}\n lower:{}\n".format(vowel,consonant,space,upper,lower))
s=string()
s.count()
