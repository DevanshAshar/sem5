import re
file = open('abc.txt','r')
text = file.read()
pattern = r'M(?:r|rs|s)\. [a-zA-Z]+' #?: batata hai ki voh bracket ke andar jo hai voh saath mein hi aane chaiye as a grp
names = re.findall(pattern,text)
print(names)
pattern=r'[a-zA-Z0-9]+\.[a-zA-Z]+\@[a-zA-Z]+\.[a-zA-Z]{2,}' #+ tabhi use karte jab uske pehle compulsory chaiye hi chaiye
emails= re.findall(pattern,text)
print(emails)
pattern=r'^\d{,10}$' #sirf sidha sidha 10 digit hoga line pe toh bataaega
mobile=[line for line in text.split('\n') if re.match(pattern,line)]
print(mobile)
pat = r'^((?:(?:https?):\/\/)|(?:www\.))?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$' #^ start of line and $ end of line pe use karte
matching_lines = [line for line in text.split('\n') if re.match(pat, line)]
print(matching_lines)
