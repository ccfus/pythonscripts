language = 'java'


if language == 'python':
	print('language is python')
elif language == 'java':
	print('language is java')
else:
	print('No match')

#------#

user = 'admin'
logged_in = True

if user == 'admin' and logged_in:
	print('admin page')
else:
	print('bad creds')

#------#

a = [1, 2, 3]
b = [1, 2, 3]

print (a == b)
print(id(a))
print(id(b))
print (a is b)