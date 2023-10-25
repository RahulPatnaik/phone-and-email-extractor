import pyperclip, re

phonenumregex = re.compile(r'''(
   (\d{3}|\(\d{3}\))?              
   (\s|-|\.)?                           
   (\d{3})                          
   (\s|-|\.)                        
   (\d{4})                          
   (\s*(ext|x|ext.)\s*(\d{2,5}))?    
 )''', re.VERBOSE)

emailregex = re.compile(r'''(
[a-zA-Z0-9._%+-]+
@
[a-zA-Z0-9.-]+
(\.[a-zA-Z]{2,4})
)''',re.VERBOSE)

text = str(pyperclip.paste())      #paste the text

matches = []
for groups in phonenumregex.findall(text):
    phonenum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] != '':
        phonenum += ' x' + groups[8]
    matches.append(phonenum)
for groups in emailregex.findall(text):
    matches.append(groups[0])

if len(matches)>0:
    pyperclip.copy('\n'.join(matches)) #it only takes one single string at a time , so you must use the .join() function
    print('Copied to the clipboard')
    print('\n'.join(matches))
else :
    print('No phone numbers or email addresses found.')
