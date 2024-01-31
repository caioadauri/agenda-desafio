
def adicionar_contato(contatos, nome, telefone, email):
  contato = {'nome': nome, 'telefone': telefone, 'email': email, 'favorito': False}
  contatos.append(contato)

def mostrar_contato(contatos):
  print('\nLista de contatos')
  for i, contato in enumerate(contatos, start=1):
    nome = contato['nome']
    telefone = contato['telefone']
    email = contato['email']
    favorito = '☆' if contato['favorito'] == True  else ''
    print(f'\n{i}. {nome} {telefone} {email} {favorito}')
  return

def favoritar_contato(contatos, indice_contatos):
  indices_ajustados = indice_contatos - 1
  if indices_ajustados >= 0 and indices_ajustados < len(contatos):
    contatos[indices_ajustados]['favorito'] = True
    print(f'Contato do indice {indice_contatos} foi favoritado')
  else:
    print(f'O indice {indice_contatos} não existe')
  return

def editar_contato(contatos, indice_contatos, novo_nome, novo_telefone, novo_email):
  indices_ajustados = indice_contatos - 1
  if indices_ajustados >= 0 and indices_ajustados < len(contatos):
    contatos[indices_ajustados]['nome'] = novo_nome
    contatos[indices_ajustados]['telefone'] = novo_telefone
    contatos[indices_ajustados]['email'] =  novo_email
    print(f'O contato de indice {indice_contatos} foi atualizado')
  else:
    print(f'O indice {indice_contatos} não existe existe')
  return

contatos = []

print('Bem-vindo a sua agenda!')
while True:
  print('\n1. Digite 1 para cadastrar um contato: ')
  print('2. Digite 2 para editar um contato: ')
  print('3. Digite 3 para favoritar um contato: ')
  print('4. Digite 4 para ver os seus contatos: ')
  print('5. Digite 5 para excluir um contato: ')
  print('6. Digite 6 para sair: ')

  opcao = int(input('\nEscolha o que deseja fazer: '))

  if opcao == 1:
    nome = input('Digite o nome do contato: ')
    telefone = input('Digite o telefone do contato: ')
    email = input('Digite o email do contato: ')
    adicionar_contato(contatos,nome, telefone, email)
  elif opcao == 2:
    mostrar_contato(contatos)
    indice = int(input('Digite o número do contato que deseja atualizar:' ))
    nome = input('Digite o nome: ')
    telefone = input('Digite o telefone: ')
    email = input('Digite o email: ')
    editar_contato(contatos, indice,  nome, telefone, email)
  elif opcao == 3:
    mostrar_contato(contatos)
    indice = int(input('Digite o número do contato que deseja favoritar: '))
    favoritar_contato(contatos, indice)
  elif opcao == 4:
    mostrar_contato(contatos)
  elif opcao == 6:
    break



