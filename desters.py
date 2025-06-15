import os
#from pathlib import Path

test = 'calculator'

nume = os.getcwd()
print(f'numele directorului curent {nume}')

cale = ''
cale = nume
print(f'Cale {cale}')

#rezultat = ''
result = dict()
new_lista = []
lista_finala = []
lista = []
lista = os.listdir(cale)
print(f'Lista cu directoare: {lista}')

print("OS Jointly", os.path.join(cale,test))

if test in lista:
    print('OK')
    if os.path.isdir(os.path.join(cale,test)):
        print(f'Se pare ca asta e un director denumit {test}')
        new_lista = os.listdir(os.path.join(cale,test))
        for f in new_lista:
            if os.path.isfile(os.path.join(cale,test,f)):
                # print(f'tipateste in pula mea caracteristicile lui {f}')
                # rezultat = '- ' + f + ': file_size=' + str(os.path.getsize(os.path.join(cale,test,f))) + ' bytes, is_dir=False'
                # result[('- ' + f)] = 'file_size=' + str(os.path.getsize(os.path.join(cale,test,f))) + ' bytes, is_dir=False'
                result[f] = 'file_size=' + str(os.path.getsize(os.path.join(cale,test,f))) + ' bytes, is_dir=False'
            else:
                 # print(f'tipateste in pula mea caracteristicile directorului {f}')   
                 # rezultat = '- ' + f + ': file_size=' + str(os.path.getsize(os.path.join(cale,test,f))) + ' bytes, is_dir=True' 
                 # result[('- ' + f)] = 'file_size=' + str(os.path.getsize(os.path.join(cale,test,f))) + ' bytes, is_dir=True'
                 result[f] = 'file_size=' + str(os.path.getsize(os.path.join(cale,test,f))) + ' bytes, is_dir=True'
            #lista_finala.append(rezultat)
    elif os.path.isfile(os.path.join(cale,test)):
        print(f'Se pare ca asta un fisier {test}')
    else: 
        print('Sa ma fut pe el de Python')
else:
    print('KKT')

#print(lista_finala)

print('=========================')

print(result)