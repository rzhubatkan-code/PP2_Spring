import re 
text = input()
pattern = r"^ab*" # First task
result = re.search(pattern , text)

pattern2 = r"^ab{2 , 3}" #Second task
result = re.search(pattern2 , text) 

pattern3 = r"[a-z]+_[a-z]+" #Third task

result3 = re.findall(pattern3, text)

pattern4 = r"[A-Z][a-z]+" #Fourth task
result4= re.findall(pattern4, text)

pattern5 = r"a.*b$" #Fifth task 
result5 = re.search(pattern5 , text ) 

pattern6 = r"[ ,.]" # Sixth task 
replace = ":" 
result = re.sub(pattern6 , replace , text ) 


result = re.sub(r"^[a-b]" , r"[A-Z]" , text )
words = re.split(r" (?=[A-Z])" , text) #Task 8 
words = [w for w in words if w] 
print(words) 

result9 = re.sub(r"(\w)([A-Z])"  , r"\1 \2" , text) #Task 9 

result10 = re.sub(r"([a-z0-9])(A-Z)" , r"\1 \2"  , text).lower() #Task 10 
