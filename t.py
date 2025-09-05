from datetime import *

data = input('\n ♦ Digite a data da viagem (dd.mm.aaaa): ')
data= datetime.strptime(data, '%d.%m.%Y')
print (data)