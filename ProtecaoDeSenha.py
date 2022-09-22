from getpass import getpass, getuser



class selecinar_cor:
    x ='\033[41m'
    v='\033[42m'
    r='\033[0m'
    
    
    
usuarios_BD = ['lucas','fulano']
senhas_BD = ['123','456']
while True:
    
    req_user = input('Insira seu login de usuario').lower()

    if req_user in usuarios_BD:
        i = usuarios_BD.index(req_user)
        senha_inserida = getpass(prompt='Insira sua senha')
        
        if senha_inserida == senhas_BD[i]:
            
            print(f'Bem vindo, {req_user.title()}!')
            break
        else:
            print(selecinar_cor.x + 'tente novamente, senha incorreta' + selecinar_cor.r)
        
    else:
        print(selecinar_cor.x + 'tente novamente, usuario não encontrado' + selecinar_cor.r )
        
print('...')