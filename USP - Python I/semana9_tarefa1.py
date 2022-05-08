import re
import math

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0

    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            else:
                pass
            freq[p] += 1
        else:
            freq[p] = 1
            unicas +=1

    return(unicas)

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''

    #print("texto")
    #print(texto)

    sentenças = separa_sentencas(texto)

    #print("sentenças")
    #print(sentenças)

    frases = []

    for i in sentenças:
        frases_aux = separa_frases(i)
        frases += frases_aux

    #print("frases")
    #print(frases)

    palavras = []

    for i in frases:
        palavras_aux = separa_palavras(i)
        palavras += palavras_aux

    #print("palavras")
    #print(palavras)
    #print(len(palavras))

    caracteres = []

    for i in palavras:
        palavras_diff = n_palavras_diferentes(palavras)
        palavras_unic = n_palavras_unicas(palavras)
        caracteres += i

    #print(caracteres)

    #print("palavras_diff")
    #print(palavras_diff)
    #print("palavras_unic")
    #print(palavras_unic)
    #print("caracteres")
    #print(caracteres)

    for i in palavras:
        caracteres.append(list(i))
        #print(i)

    #Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    #Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    #Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
    #Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    #Complexidade de sentença: Média simples do número de frases por sentença.
    #Tamanho médio de frase: Média simples do número de caracteres por frase.
    #print(len(sentenças))
    
    somafrases = 0
    for j in frases:
        somafrases += len(j)

    somasentencas = 0
    for j in sentenças:
        somasentencas += len(j)

    somapalavras = 0
    for j in palavras:
        somapalavras += len(j)


    wal = somapalavras/len(palavras) #tamanho medio de palavra
    ttr = palavras_diff/len(palavras) #relação Type-Token
    hlr = palavras_unic/len(palavras) #Entre a Razão Hapax Legomana
    sal = somasentencas/len(sentenças) #Entre o tamanho médio de sentença
    sac = len(frases)/len(sentenças) #complexidade média da sentença
    pal = somafrases/len(frases) #tamanho medio de frase

    #print([wal, ttr, hlr, sal, sac, pal])
    return([wal, ttr, hlr, sal, sac, pal])

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    Sab = 0
    for j in range(len(as_a)):
        Sab =  math.fabs(as_a[j] - as_b[j]) + Sab
    Sab = Sab/6
    return round(Sab,4)


def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    assinatura = []

    for i in textos:
        assinatura.append(calcula_assinatura(i))

    notas = []

    for i in assinatura:
        notas.append(compara_assinatura(i,ass_cp))

    suspeito = notas.index(min(notas)) + 1

    return suspeito


def run():
    textos = le_textos()
    ass_cp = le_assinatura()

    avalia_textos(textos, ass_cp)

#run()
#calcula_assinatura("NOSSA alegria diante dum sistema metafisico, nossa satisfação em presença duma construção do pensamento, em que a organização espiritual do mundo se mostra num conjunto lógico, coerente a harmônico, sempre dependem eminentemente da estética; têm a mesma origem que o prazer, que a alta satisfação, sempre serena afinal, que a atividade artística nos proporciona quando cria a ordem e a forma a nos permite abranger com a vista o caos da vida, dando-lhe transparência.")
#calcula_assinatura("Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.")
#calcula_assinatura("""Navegadores antigos tinham uma frase gloriosa:"Navegar é preciso; viver não é preciso".Quero para mim o espírito [d]esta frase,transformada a forma para a casar como eu sou:Viver não é necessário; o que é necessário é criar.Não conto gozar a minha vida; nem em gozá-la penso.Só quero torná-la grande,ainda que para isso tenha de ser o meu corpo e a (minha alma) a lenha desse fogo.Só quero torná-la de toda a humanidade;ainda que para isso tenha de a perder como minha.Cada vez mais assim penso.Cada vez mais ponho da essência anímica do meu sangueo propósito impessoal de engrandecer a pátria e contribuirpara a evolução da humanidade.É a forma que em mim tomou o misticismo da nossa Raça.""")