import os

directory = '../'
if directory in os.listdir(os.getcwd()):
    if os.path.isfile(os.path.join(os.getcwd(),directory)):
        return f'Error: "{directory}" is not a directory'
else:
    return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

result = dict()
rezultat = ''

for f in os.listdir(os.path.join(os.getcwd(),directory)):
    if os.path.isfile(os.path.join(os.getcwd(),directory,f)):
        result[f] = 'file_size=' + str(os.path.getsize(os.path.join(os.getcwd(),directory,f))) + ' bytes, is_dir=False'
    else:
        result[f] = 'file_size=' + str(os.path.getsize(os.path.join(os.getcwd(),directory,f))) + ' bytes, is_dir=True'
return str(result)

'''
patha = '../'

pathb = '/bin'

print(os.path.abspath(path))

print('==================')

print(os.path.abspath(patha))

print('==================')

print(os.path.abspath(pathb))

nume = os.path.abspath(patha)
lista = os.listdir(nume)

print(lista)
'''