import re

content = 'Hello 1234567 World_This is a Regex Demo'

#content ='''Hello 1234567 World_This
 #is a Regex Demo
#'''
#content = 'pice is $5.00'
#result = re.match("^Hello.*Demo$",content)
#result = re.match('^Hello\s\d{3}\s\d{4}\s\w{10}.*Demo$',content)
#result = re.search("^\d.*Demo$",content)
#result = re.match("^Hello\s(\d+)\s4.*Demo$",content)
#result = re.match("^Hello\s(\d+).*?Demo$",content,re.S)
#result = re.match('pice is \$5\.00',content)
result = re.search('^Hel.*?(\d+).*?Demo',content)
#print(len(content))
print('%'*40)
print(result)
print('#'*40)
#print(result.group(1))
#print(result.group(2))
#print('#'*40)
#print(result.span())
