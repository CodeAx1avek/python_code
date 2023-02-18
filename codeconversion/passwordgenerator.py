import random

string = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
small = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
special = ('!','@','#',"$","&")
length = 8
prin = "".join(random.choice(string+special+small) for i in range(length))

print(prin)