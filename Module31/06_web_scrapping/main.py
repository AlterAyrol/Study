import json
import requests
import re


test_requests = requests.get('http://www.columbia.edu/~fdc/sample.html')
data = test_requests.text
text_output = re.findall(r'<h3 .*?>(.*?)</h3>', data)
text_output2 = re.findall(r'<h3 id="\w+">(.*?)</h3>', data)

print(text_output)
print(text_output2)




#<h3 id="\w+">(\w+)</h3>
#<h3 .*?>(.*?)</h3>