#PHABLO DOS SANTOS - ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
import json

def menu_navegacao():
    print('-- Menu de Navegação --')
    print('1 - Estudantes')
    print('2 - Disciplinas')
    print('3 - Professores')
    print('4 - Turmas')
    print('5 - Matriculas')
    print('6 - Sair')

    return input('Digite a opção escolhida: ').capitalize()

def menu_operacao():
    print('1 - Criar')
    print('2 - Listar')
    print('3 - Atualizar')
    print('4 - Deletar')
    print('5 - Voltar')

    return input('Digite a opção escolhida: ').capitalize()

def cadastro(codigo, nome, nome_arquivo, cpf=None):
    if cpf is None:
        dado = {'Código': codigo, 'Nome': nome}
    else:
        dado = {'Código': codigo, 'Nome': nome, 'CPF': cpf}

    lista = leitura_arquivo(nome_arquivo)
    lista.append(dado)
    salvar_arquivo(lista, nome_arquivo)
    return input('Dados salvos com sucesso. Para continuar aperte ENTER: ')

def cadastro_turma_matricula(primeiro_codigo, segundo_codigo, nome_arquivo, terceiro_codigo=None):
    if terceiro_codigo is None:
        dado = {'Código': primeiro_codigo, 'Código 2': segundo_codigo}
    else:
        dado = {'Código': primeiro_codigo, 'Código 2': segundo_codigo, 'Código 3': terceiro_codigo}

    lista = leitura_arquivo(nome_arquivo)
    lista.append(dado)
    salvar_arquivo(lista, nome_arquivo)
    return input('Dados salvos com sucesso. Para continuar aperte ENTER: ')

def listagem(nome_arquivo):
    lista = leitura_arquivo(nome_arquivo)
    if len(lista) == 0:
        print(f'Não há nenhum cadastro para ser listado')
    for elemento in lista:
        for chave, dado in elemento.items():
            print(f'{chave}: {dado}', end='   ')
        print('')
    return input('Para continuar aperte ENTER: ')

def atualizacao_pessoas(nome_arquivo):
    lista = leitura_arquivo(nome_arquivo)
    if len(lista) == 0:
        print('Não há nada para atualizar')
        return input('Para continuar aperte ENTER: ')
    else:
        try:
            codigo = int(input('Informe o codigo: '))
        except ValueError:
            print('O código precisa ser um número')
            return input('Para continuar aperte ENTER: ')
        while True:
            for elemento in lista:
                if codigo == elemento['Código']:
                    try:
                        codigo_atualizado = int(input('Informe o codigo atualizado: '))
                    except ValueError:
                        print('O código precisa ser um número')
                        return input('Para continuar aperte ENTER: ')
                    nome_atualizado = input('Informe o nome atualizado: ')
                    cpf_atualizado = input('Informe o cpf atualizado: ')

                    elemento['Código'] = codigo_atualizado
                    elemento['Nome'] = nome_atualizado
                    elemento['CPF'] = cpf_atualizado

                    salvar_arquivo(lista, nome_arquivo)
                    print('Dados atualizados:')
                    for chave, dado in elemento.items():
                        print(f'{chave}: {dado}', end='   ')
                    return input('\nPara continuar aperte ENTER: ')
            else:
                print('Esse cadastro não existe')
                input('Para continuar aperte ENTER: ')
                break

def atualizacao_disciplinas(nome_arquivo):
    lista = leitura_arquivo(nome_arquivo)
    if len(lista) == 0:
        print('Não há nada para atualizar')
        return input('Para continuar aperte ENTER: ')
    else:
        try:
            codigo = int(input('Informe o codigo: '))
        except ValueError:
            print('O código precisa ser um número')
            return input('Para continuar aperte ENTER: ')
        while True:
            for elemento in lista:
                if codigo == elemento['Código']:
                    try:
                        codigo_atualizado = int(input('Informe o codigo atualizado: '))
                    except ValueError:
                        print('O código precisa ser um número')
                        return input('Para continuar aperte ENTER: ')
                    nome_atualizado = input('Informe o nome atualizado: ')

                    elemento['Código'] = codigo_atualizado
                    elemento['Nome'] = nome_atualizado

                    salvar_arquivo(lista, nome_arquivo)
                    print('Dados atualizados:')
                    for chave, dado in elemento.items():
                        print(f'{chave}: {dado}', end='   ')
                    return input('\nPara continuar aperte ENTER: ')
            else:
                print('Esse cadastro não existe')
                input('Para continuar aperte ENTER: ')
                break

def atualizacao_turmas(nome_arquivo, arquivo_1, arquivo_2, codigo_antigo):
    lista = leitura_arquivo(nome_arquivo)
    lista_1 = leitura_arquivo(arquivo_1)
    lista_2 = leitura_arquivo(arquivo_2)
    if len(lista) == 0:
        print('Não há nada para atualizar')
        return input('Para continuar aperte ENTER: ')
    else:
        while True:
            for elemento in lista:
                if codigo_antigo == elemento['Código']:
                    print('Agora insira os dados atualizados')
                    print('Lembre-se do formato:\n[''Código'']: código atualizado  [Código 2]: segundo código atualizado  [''Código 3'']: terceiro codigo atualizado')
                    codigo_atualizado = int(input('Informe o primeiro codigo atualizado: '))
                    codigo_1 = int(input('Informe o segundo código atualizado: '))
                    codigo_2 = int(input('Informe o terceiro código atualizado: '))
                    for elemento_1 in lista_1:
                        if elemento_1['Código'] == codigo_1:
                            for elemento_2 in lista_2:
                                if elemento_2['Código'] == codigo_2:
                                    elemento['Código'] = codigo_atualizado
                                    elemento['Código 2'] = codigo_1
                                    elemento['Código 3'] = codigo_2

                                    salvar_arquivo(lista, nome_arquivo)
                                    print('Dados atualizados:')
                                    for chave, dado in elemento.items():
                                        print(f'{chave}: {dado}', end='   ')
                                    return input('\nPara continuar aperte ENTER: ')
            else:
                print('Não é possível atualizar está lista com dados que nao estejam previamente registrados.')
                input('Para continuar aperte ENTER: ')
                break

def atualizacao_matriculas(nome_arquivo, codigo_1, codigo_2, novo_codigo_1, novo_codigo_2):
    lista = leitura_arquivo(nome_arquivo)
    if len(lista) == 0:
        print('Não há nada para atualizar')
        return input('Para continuar aperte ENTER: ')
    else:
        for elemento in lista:
            if elemento['Código'] == codigo_1 and elemento['Código 2'] == codigo_2:
                elemento['Código'] = novo_codigo_1
                elemento['Código 2'] = novo_codigo_2

                salvar_arquivo(lista, nome_arquivo)
                print('Dados atualizados:')
                for chave, dado in elemento.items():
                    print(f'{chave}: {dado}', end='   ')
                return input('\nPara continuar aperte ENTER: ')

def deletar(nome_arquivo):
    lista = leitura_arquivo(nome_arquivo)
    if len(lista) == 0:
        print('Não há nada para deletar')
        return input('Para continuar aperte ENTER: ')
    else:
        codigo = int(input('Informe o codigo: '))
        while True:
            for elemento in lista:
                if codigo == elemento['Código']:
                    lista.remove(elemento)

                    salvar_arquivo(lista, nome_arquivo)
                    print('Cadastro removido:')
                    return input('Para continuar aperte ENTER: ')
            else:
                print('Esse cadastro não existe!')
                input('Para continuar aperte ENTER: ')
                break

def deletar_turmas_matriculas(nome_arquivo, codigo_1, codigo_2, codigo_3=None):
    lista = leitura_arquivo(nome_arquivo)
    if len(lista) == 0:
        print('Não há nada para deletar')
        return input('Para continuar aperte ENTER: ')
    elif codigo_3 is None:
        while True:
            for elemento in lista:
                if codigo_1 == elemento['Código'] and codigo_2 == elemento['Código 2']:
                    lista.remove(elemento)

                    salvar_arquivo(lista, nome_arquivo)
                    print('Cadastro removido:')
                    return input('Para continuar aperte ENTER: ')
            else:
                print('Esse cadastro não existe!')
                input('Para continuar aperte ENTER: ')
                break
    else:
        while True:
            for elemento in lista:
                if codigo_1 == elemento['Código'] and codigo_2 == elemento['Código 2'] and codigo_3 == elemento['Código 3']:
                    lista.remove(elemento)

                    salvar_arquivo(lista, nome_arquivo)
                    print('Cadastro removido:')
                    return input('Para continuar aperte ENTER: ')
            else:
                print('Esse cadastro não existe!')
                input('Para continuar aperte ENTER: ')
                break

def salvar_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo:
        json.dump(lista, arquivo, ensure_ascii=False)

def leitura_arquivo(nome_arquivo):
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as arquivo:
            lista = json.load(arquivo)
        return lista
    except:
        return []

# Menu de navegação
arquivo_estudantes = 'estudantes.json'
arquivo_disciplinas = 'disciplinas.json'
arquivo_professores = 'professores.json'
arquivo_turmas = 'turmas.json'
arquivo_matriculas = 'matriculas.json'
while True:
    menu_principal = menu_navegacao()
    # Menu de operações
    if menu_principal == 'Estudantes' or menu_principal == '1':
        while True:
            print('[Estudantes] -- Menu de Operações --')
            menu_secundario = menu_operacao()
            # Cadastro
            if menu_secundario == 'Criar' or menu_secundario == '1':
                codigo = int(input('Digite o código do estudante: '))
                nome = input('Digite o nome do estudante: ')
                cpf = input('Digite o cpf do estudante: ')
                cadastro(codigo, nome, arquivo_estudantes, cpf)
            # Listagem
            elif menu_secundario == 'Listar' or menu_secundario == '2':
                listagem(arquivo_estudantes)
            # Atualização
            elif menu_secundario == '3' or menu_secundario == 'Atualizar':
                atualizacao_pessoas(arquivo_estudantes)
            #Excluir estudantes
            elif menu_secundario == '4' or menu_secundario == 'Deletar':
                deletar(arquivo_estudantes)
            #Retorno para o menu de navegação
            elif menu_secundario == 'Voltar' or menu_secundario == '5':
                break
            # Entradas inválidas no menu de operações
            else:
                print('Opção Inválida')
    elif menu_principal == 'Disciplinas' or menu_principal == '2':
        while True:
            print('[Disciplinas] -- Menu de Operações --')
            menu_secundario = menu_operacao()
            # Cadastro
            if menu_secundario == 'Criar' or menu_secundario == '1':
                codigo = int(input('Digite o código da disciplina: '))
                nome = input('Digite o nome da disciplina: ')
                cadastro(codigo, nome, arquivo_disciplinas)
            # Listagem
            elif menu_secundario == 'Listar' or menu_secundario == '2':
                listagem(arquivo_disciplinas)
            # Atualização
            elif menu_secundario == '3' or menu_secundario == 'Atualizar':
                atualizacao_disciplinas(arquivo_disciplinas)
            #Excluir estudantes
            elif menu_secundario == '4' or menu_secundario == 'Deletar':
                deletar(arquivo_disciplinas)
            #Retorno para o menu de navegação
            elif menu_secundario == 'Voltar' or menu_secundario == '5':
                break
            # Entradas inválidas no menu de operações
            else:
                print('Opção Inválida')
    elif menu_principal == '3' or menu_principal == 'Professores':
        while True:
            print('[Professores] -- Menu de Operações --')
            menu_secundario = menu_operacao()
            # Cadastro
            if menu_secundario == 'Criar' or menu_secundario == '1':
                codigo = int(input('Digite o código do Professor: '))
                nome = input('Digite o nome do Professor: ')
                cpf = input('Digite o cpf do Professor: ')
                cadastro(codigo, nome, arquivo_professores, cpf)
            # Listagem
            elif menu_secundario == 'Listar' or menu_secundario == '2':
                listagem(arquivo_professores)
            # Atualização
            elif menu_secundario == '3' or menu_secundario == 'Atualizar':
                atualizacao_pessoas(arquivo_professores)
            #Excluir estudantes
            elif menu_secundario == '4' or menu_secundario == 'Deletar':
                deletar(arquivo_professores)
            #Retorno para o menu de navegação
            elif menu_secundario == 'Voltar' or menu_secundario == '5':
                break
            # Entradas inválidas no menu de operações
            else:
                print('Opção Inválida')
    elif menu_principal == '4' or menu_principal == 'Turmas':
        while True:
            print('[Turmas] -- Menu de Operações --')
            menu_secundario = menu_operacao()
            # Cadastro
            if menu_secundario == 'Criar' or menu_secundario == '1':
                codigo_turma = int(input('Digite o código da turma: '))
                codigo_professor = int(input('Digite o codigo do professor: '))
                codigo_disciplina = int(input('Digite o código do disciplina: '))
                lista_professores = leitura_arquivo(arquivo_professores)
                lista_disciplina = leitura_arquivo(arquivo_disciplinas)
                for professor in lista_professores:
                    if professor['Código'] == codigo_professor:
                        for disciplina in lista_disciplina:
                            if disciplina['Código'] == codigo_disciplina:
                                cadastro_turma_matricula(codigo_turma, codigo_professor, arquivo_turmas, codigo_disciplina)
            # Listagem
            elif menu_secundario == 'Listar' or menu_secundario == '2':
                print('Código: código da turma, Código 2: código do professor, Código 3: código da disciplina')
                listagem(arquivo_turmas)
            # Atualização
            elif menu_secundario == '3' or menu_secundario == 'Atualizar':
                print('Lembre-se de verificar se o cadastro da turma está correto.\nNão será possível atualizar se o novo professor e a nova disciplina não estiver(em) cadastrado(s).\nPara cadastrar novos professores ou novas disciplinas é necessário ir nos seus menus correspondentes (Professores ou Disciplinas).')
                print('Formato para a atualização da lista de turmas:\n[''Código'']: código da turma  [Código 2]: código do professor  [''Código 3'']: codigo da disciplina')
                codigo_turma = int(input('Digite o código da turma: '))
                atualizacao_turmas(arquivo_turmas, arquivo_professores, arquivo_disciplinas, codigo_turma)
            # Excluir estudantes
            elif menu_secundario == '4' or menu_secundario == 'Deletar':
                print('Verifique se o código do professor e da disciplina correspondem com turma')
                lista = leitura_arquivo(arquivo_turmas)
                codigo_del_turma = int(input('Digite o código da turma do cadastro a ser deletado: '))
                codigo_del_professor = int(input('Digite o código do professor do cadastro a ser deletado: '))
                codigo_del_disciplina = int(input('Digite o código da disciplina do cadastro a ser deletado: '))
                for turma in lista:
                    if turma['Código'] == codigo_del_turma and turma['Código 2'] == codigo_del_professor and turma['Código 3'] == codigo_del_disciplina:
                        deletar_turmas_matriculas(arquivo_turmas, codigo_del_turma, codigo_del_professor, codigo_del_disciplina)
            # Retorno para o menu de navegação
            elif menu_secundario == 'Voltar' or menu_secundario == '5':
                break
            # Entradas inválidas no menu de operações
            else:
                print('Opção Inválida')
    elif menu_principal == '5' or menu_principal == 'Matriculas':
        while True:
            print('[Matriculas] -- Menu de Operações --')
            menu_secundario = menu_operacao()
            # Cadastro
            if menu_secundario == 'Criar' or menu_secundario == '1':
                print('Lembre-se de verificar se a turma e o estudante estão cadastrados.\nNão será possível criar uma mátricula para estudantes e turmas não cadastrados previamente.\nPara cadastrar novas turmas ou novos estudantes é necessário ir nos seus menus correspondentes (Turmas ou Estudantes).')
                codigo_turma = int(input('Digite o codigo da turma: '))
                codigo_estudante = int(input('Digite o código do estudante: '))
                lista_turma = leitura_arquivo(arquivo_turmas)
                lista_estudante = leitura_arquivo(arquivo_estudantes)
                for turma in lista_turma:
                    if turma['Código'] == codigo_turma:
                        for estudante in lista_estudante:
                            if estudante['Código'] == codigo_estudante:
                                cadastro_turma_matricula(codigo_turma, codigo_estudante, arquivo_matriculas)
            # Listagem
            elif menu_secundario == 'Listar' or menu_secundario == '2':
                print('Código: código da turma, Código 2: código do estudante')
                listagem(arquivo_matriculas)
            # Atualização
            elif menu_secundario == '3' or menu_secundario == 'Atualizar':
                print('Lembre-se de verificar se a turma e o estudante estão cadastrados.\nNão será possível atualizar se a nova turma e o novo estudante não estiver(em) cadastrado(s).\nPara cadastrar novas turmas ou novos estudantes é necessário ir nos seus menus correspondentes (Turmas ou Estudantes).')
                print('Formato para a atualização da lista de matrículas:\n[''Código'']: código da turma  [Código 2]: código do estudante')
                codigo_turma = int(input('Digite o código da turma atual: '))
                codigo_estudante = int(input('Digite o código do estudante atual: '))
                lista_turma = leitura_arquivo(arquivo_turmas)
                lista_estudante = leitura_arquivo(arquivo_estudantes)
                lista_matricula = leitura_arquivo(arquivo_matriculas)
                for turma in lista_turma:
                    for estudante in lista_estudante:
                        if estudante['Código'] == codigo_estudante and turma['Código'] == codigo_turma:
                            for matricula in lista_matricula:
                                if matricula['Código'] == codigo_turma and matricula['Código 2'] == codigo_estudante:
                                    nova_turma = int(input('Digite o código da nova turma: '))
                                    novo_estudante = int(input('Digite o código do novo estudante: '))
                                    for nturma in lista_turma:
                                        for nestudante in lista_estudante:
                                            if nturma['Código'] == nova_turma and nestudante['Código'] == novo_estudante:
                                                atualizacao_matriculas(arquivo_matriculas, codigo_turma, codigo_estudante, nova_turma, novo_estudante)
            # Excluir estudantes
            elif menu_secundario == '4' or menu_secundario == 'Deletar':
                lista = leitura_arquivo(arquivo_matriculas)
                codigo_del_turma = int(input('Digite o código da turma da matrícula a ser deletada: '))
                codigo_del_estudante = int(input('Digite o código da estudante da matrícula a ser deletada: '))
                for matricula in lista:
                    if matricula['Código'] == codigo_del_turma and matricula['Código 2'] == codigo_del_estudante:
                        deletar_turmas_matriculas(arquivo_matriculas, codigo_del_turma, codigo_del_estudante)
            # Retorno para o menu de navegação
            elif menu_secundario == 'Voltar' or menu_secundario == '5':
                break
            # Entradas inválidas no menu de operações
            else:
                print('Opção Inválida')
    #Saída
    elif menu_principal == 'Sair' or menu_principal == '6':
        break
    #Entradas inválidas no menu de navegação
    else:
        print('Opção Inválida')
