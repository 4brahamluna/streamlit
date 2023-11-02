#IMPORTANDO A BIBLIOTECA
import googlemaps

#INSERINDO SUA KEY PARA CONSULTA DO GOOGLE MAPS
gmaps = googlemaps.Client(key='AIzaSyAbpKnIGTYrxhME4vheUpoL8w_wJxof7mg')

#CRIANDO VARIÁVEIS DA MATRIZ

#inserindo as cidades de origem
origem = ['natal','brasilia','sao paulo']
#inserindo as cidades de destino
destino = ['curitiba','rio de janeiro','belo horizonte']
#criando um laço que vai imprimir uma distância para cada uma das rotas (cada origem para cada um dos destinos)
for c_origem in origem:
    for c_destino in destino:
            consulta = gmaps.distance_matrix(c_origem, c_destino)
            
            print(consulta)
            
#TENHO QUE COLOCAR ESSE LAÇO PARA CRIAR UMA TABELA
#A PARTIR DESSES DADOS DA TABELA, POSSO REALIZAR O PROBLEMA DO CAIXEIRO VIAJANTE.
