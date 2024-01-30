agenda = []

print('Bem-vindo a sua agenda!')
while True:
  print('\n1. Digite 1 para cadastrar um contato: ')
  print('2. Digite 2 para editar um contato: ')
  print('3. Digite 3 para favoritar um contato: ')
  print('4. Digite 4 para ver os seus contatos: ')
  print('5. Digite 5 para excluir um contato: ')
  print('6. Digite 6 para sair: ')

  opcao = int(input('\nEscolha o que deseja fazer: '))

  if opcao == 6:
    break
