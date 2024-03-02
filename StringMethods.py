#Strings are IMMUTABLE
a="Dinesh"
print(a)
print(a.upper()) #Converting to UPPERCASE
print(a.lower()) #Converting to LOWERCASE
d="!!!Arya!!!!!!!"
print(d.rstrip("!")) #Removing trailing spaces 
p="Hello world!! This is world.. "
print(p.replace("world","earth")) #Replacing Old-suubstring to New_substring
print(p.replace("world","earth",1)) #("Old-suubstring","New-substring",count)
print(p.split()) #Split the string into substrings and stored in a LIST
print(p.count("world"))
print(p.endswith("!")) #Boolean value
print(d.endswith("!"))
print(p.endswith("world",1,15))
print(p.find("world"))#find() Methods
print(p.find("H"))
print(p.find("M"))
print(p.index("H"))#index() Methods
q="WelcomeToTheConsole"
print(q)
print(q.isalnum()) #A-Z,a-z,0-9
print(q.isalpha()) #A-Z,a-z
print(q.islower()) #Boolean Value
print(q.isupper()) #Boolean Value
print(q.isprintable()) #Boolean Value
m="My name is DK!I am currently pursuing my B.Tech  in CSE.. "
print(m)
print(m.title()) #Uppercase the first letter of all substring of a String
print(m.istitle()) #Boolean value
print(m.startswith("M")) #Boolean Value
print(m.swapcase()) #Swapping lowercase-uppercase and uppercase-lowercase




