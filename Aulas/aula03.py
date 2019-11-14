# dicionarios

# endereco = {'logradouro':'Rua Vergueiro',
#             'numero':'3057',
#             'cep':'04101-300',
#             'bairro':'Vila Mariana',
#             'cidade':'São Paulo',
#             'uf':'SP'
# }

# endereco2 = {'logradouro':{'user1':'Rua Vergueiro',
#                             'user2':'Rua Augusta'
#             },
#             'numero':{'user1','3057',
#                         'user2', '3058'
#             },
#             'cep':{'user1':'04101-300',
#                     'user2':'07197-140'
#             },
#             'bairro':{'user1':'Vila Mariana',
#                         'user2':'Cercqueira Cesar'
#             },
#             'cidade':{'user1':'São Paulo',
#                         'user2':'São Paulo'
#             },
#             'uf':{'user1':'SP',
#                     'user2':'SP'
#             }
# }
# #esse metodo serve para alterar valor
# endereco2.__setitem__('numero',{'user1':'3057',
#                                 'user2':'1032'})

# print(endereco2)
# print(endereco2.keys()) #MOSTRA AS CHAVES DO DICIONARIO (LOGRADOURO, NUMERO, ETC, ETC)

dados = {
    'cidades':{
        'saopaulo':{
            'nome':'São Paulo',
            'municipios':645,
            'populacao':12.18
        },
        'riodejaneiro':{
            'nome':'Rio de Janeiro',
            'municipios':92,
            'populacao':6.32
        },
        'minasgerais':{
            'nome':'Minas Gerais',
            'municipios':945,
            'populacao':9.25
        }
    }
}

# print a quantidade de municipios de minas gerais
print(dados['cidades']['minasgerais']['municipios'])
# print a quantidade municipios do rio
print(dados['cidades']['riodejaneiro']['municipios'])
# print a populacao de minas
print(dados['cidades']['minasgerais']['populacao'] * 1000000)
# print a população de sao paulo
print(dados['cidades']['saopaulo']['populacao'] * 1000000)
# print o nome de sao paulo
print(dados['cidades']['saopaulo']['nome'])
