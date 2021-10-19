

add = open('d:/cadnome.txt', 'a')

print('Ola!')
print('Deseja cadastra quantos nomes')

count = int( input())
x = 1
while(x <= count):
       
    print('Digite o nome a ser adicionado')  
    name = str(input())
    add.writelines(f'{name}\n')
    x += 1
   
add.close()    
