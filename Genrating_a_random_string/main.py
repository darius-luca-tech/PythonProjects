import random 
import string 
def randomString(stringLength = 10): 
	letters = string.ascii_lowercase 
	return ''.join(random.choice(letters) for i in range(stringLength)) 

print("Parola este: %s", format(randomString(10)))
