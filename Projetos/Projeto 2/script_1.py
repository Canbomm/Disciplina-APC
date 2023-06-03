dic_carga = {
    "Docente 1":{
        "Disciplina1 (codigo)":{
            "Turma 1":"60h (30 alunos)",
            "Turma 2":"30h (4 alunos)"
        },
        "Disciplina2 (codigo)":{
            "Turma 1":"20h (2 alunos)",
            "Turma 2":"10h (3 alunos)"
        }
    },
    "Docente 2":{
        "Disciplina1 (codigo)":{
            "Turma 1":"15h (50 alunos)",
            "Turma 2":"70h (20 alunos)"
        },
        "Disciplina2 (codigo)":{
            "Turma 1":"23h (6 alunos)",
            "Turma 2":"20h (0 alunos)"
        }
    }
}

dic_disciplina = {
    "1 Docente":{
        "Disciplina (codigo)":{
            "Turma A":1,
            "Turma B":3
        }
    },
    "2 Docentes":{
        "Disciplina (codigo)":{
            "Turma A":4,
            "Turma B":5
        }
    }
}

dic_matriculas = {
    "Codigo 1":"Número matriculados",
    "Codigo 2":200,
    "Codigo 3":20
}

dic_codigos = {
    "Codigo 1":"Nome da matéria",
    "CIC0090":"ESTRUTURAS DE DADOS"
}

############ TERMINEI A PARTE DOS DICIONÁRIOS PARA TESTE ##############

def leia(nome_arq,dic_carga,dic_disciplina,turmas):
    with open(nome_arq, encoding="UTF-8") as arquivo:
        # primeira linha do csv, nao me importa muito
        cabecalho = (next(arquivo)).rstrip()
        
        # trabalhando com o arquivo
        for linha in arquivo:
            # coletando os dados importantes
            dados = (linha.rstrip()).split(",")
            lixo = dados.pop(3),dados.pop(5),dados.pop(6),dados.pop(4)
            #print(dados)

            # criando o dic_carga
            docente,carga = (dados[3]).split("(")
            docente = docente[:-1]
            carga = int(carga[:-2])
            
            codigo = dados[0]
            disciplina = dados[1]
            turma = (f"Turma {dados[2]}")
            alunos = (f"{dados[4]} alunos")
            
            disc_cod = (f"{disciplina} {codigo}")
            disc_carga = (f"{carga}h ({alunos})")

            # colocando as informacoes no dicionario com as cargas
            docente_existe = dic_carga.get(docente)
            if docente_existe != None:
                disciplina_existe = dic_carga[docente].get(disc_cod)
                if disciplina_existe != None:
                    turma_existe = dic_carga[docente][disc_cod].get(disc_carga)
                    if turma_existe != None:
                        print("Cai no if loco la")
                    else:
                        dic_carga[docente][disc_cod][turma] = disc_carga
                else:
                    dic_carga[docente][disc_cod] = {turma:disc_carga}
            else:
                dic_carga[docente] = {disc_cod:{turma:disc_carga}}
            
            # criando um dicionario com as disciplinas e as turmas
            disciplina_cod = disciplina + " " + "(" + codigo + ")"
            if turmas.get(disciplina_cod) != None:
                turmas[disciplina_cod] += [dados[2]]
            else:
                turmas[disciplina_cod] = [dados[2]]

            # colocando as informacoes no dicionario sobre as disciplinas
            if dic_disciplina.get(disciplina_cod) != None:
                docentes = dic_disciplina[disciplina_cod]
                if not (procuraLista(docentes,docente)):
                    dic_disciplina[disciplina_cod] += [docente]
            else:
                dic_disciplina[disciplina_cod] = [docente]
        
        return dic_carga,dic_disciplina,turmas

def carga(cargas,docente):
    # espaco que vem antes de "printar" a turma:
    espacoT = " "*5
    carga_total = 0
    total_alunos = 0
    
    # ve se o docente foi lido:
    if cargas.get(docente) != None:
        print(f"{docente}:")
        disciplinas = cargas[docente]
        valores_acessados = []
        turmas_acessadas = {}
        index = 0
        
        # ve as disciplinas que o docente da:
        for chaveD in disciplinas:
            valores_acessados.append(chaveD)
            index += 1
            turmas = disciplinas[chaveD]
            carga_total_disc = 0

            # ve cada turma de cada disciplina:
            for chaveT in turmas:
                # printa cada Turma
                if turmas_acessadas.get(chaveD) != None:
                    turmas_acessadas[chaveD] += [f"{espacoT}{chaveT}: {turmas[chaveT]}"]
                else:
                    turmas_acessadas[chaveD] = [f"{espacoT}{chaveT}: {turmas[chaveT]}"]

                # coleta dados
                horario = turmas[chaveT]
                carga_horaria,alunos_matriculados = horario.split("(")
                carga_horaria = int(carga_horaria[:-2])
                matriculados = int((alunos_matriculados.split())[0])
                if matriculados > 6:
                    carga_total_disc += carga_horaria
            # trabalha com as cargas
            if carga_total_disc > 0:
                total_alunos += matriculados
                carga_total += carga_total_disc
        
        # printando a carga por aluno
        valores_acessados.sort()
        for chave in valores_acessados:
            formatando = chave.split()
            fcodigo = formatando.pop(-1)
            print(f" * {' '.join(formatando)} ({fcodigo}):")
            for linha in turmas_acessadas[chave]:
                print(linha)
        if total_alunos > 0:
            carga_aluno = carga_total/total_alunos
            print(f"[Carga total considerada: {carga_total}h ({carga_aluno:.2f}h/aluno)]")
        else:
            print(f"[Carga total considerada: 0h (0.00h/aluno)]")
    
    # nao encontrou o docente
    else:
        print(f"No hay {docente}...")

def matriculas():
    print(f"Chamaram o matriculas")
    return None

def disciplina(disciplinas,numero,turmas):
    # pega as disciplinas com o numero de docente desejado
    disciplinas_desejadas = []
    for chave in disciplinas:
        tamanho = len(disciplinas[chave])
        if tamanho >= numero:
            disciplinas_desejadas += [chave]
    disciplinas_desejadas.sort()

    # printa as disciplinas
    if len(disciplinas_desejadas) > 0:
        print(f"Turmas com pelo menos {numero} docentes:")
        for chave in disciplinas_desejadas:
            contados = contaGrupos(turmas[chave])
            turmas = ""
            for chave in contados:
                turmas += (str(chave) + "(" + ")")

            print(f" *  {chave}:{contados}")
    else:
        print(f"No hay {numero}...")

def procuraLista(lista,palavra):
    for linha in lista:
        if linha == palavra:
            return True
    return False

def contaGrupos(lista):
    contador = {}
    for elem in lista:
        if contador.get(elem) != None:
            contador[elem] += 1
        else:
            contador[elem] = 1
    return contador

dic_carga = {}
dic_disciplina = {}
turmas = {}
jaLidos = []

while True:
    comando = input()

    # executa o leia
    if (comando.split())[0] == "leia":
        nome_arq = (comando.split())[1:]
        nome_arq = " ".join(nome_arq)

        # verifica se o arquivo ja nao foi lido
        if not procuraLista(jaLidos,nome_arq):
            lendo = leia(nome_arq,dic_carga,dic_disciplina,turmas)
            dic_carga = lendo[0]
            dic_disciplina = lendo[1]
            turmas = lendo[2]
            jaLidos.append(nome_arq)
    
    # executa o carga
    elif (comando.split())[0] == "carga":
        docente = " ".join((comando.split())[1:])
        carga(dic_carga,docente)
    
    # executa o matriculas
    elif (comando.split())[0] == "matriculas":
        matriculas()
    
    # executa o disciplina
    elif (comando.split())[0] == "disciplina":
        num_docentes = int((comando.split())[-1])
        disciplina(dic_disciplina,num_docentes,turmas)
    
    # encerra o programa
    else:
        break
