# Arquivo para os estudantes preencherem as lacunas
# Preencha os espaços em branco (______) com o código correto para interagir com o MongoDB

# LACUNA 1: Importe a função get_database do arquivo pymongo_get_connection_eventos
from pymongo_get_connection_eventos import get_database
import pymongo

def main():
    # 1. Obtendo a conexão com o banco de dados
    dbname = get_database()
    if dbname is None:
        print("Não foi possível conectar ao banco de dados. Encerrando.")
        return

    # 2. Selecionando a coleção 'participantes'
    # LACUNA 2: Nome da coleção
    colecao = dbname['participantes']
    

    print("\n--- 1. INSERÇÃO (Create) ---")
    # LACUNA 3: Crie a estrutura do documento a ser inserido, inclua pelo menos 4 campos
    novo_participante = {"_id":"part021",
      "nome":"participante 21" ,
     "email":"participante21@email.com ",
        "idade": 50,
         " evento_id": "evt021",
          "confirmado": "true" }

    # Inserindo um único documento
    # Dica: Qual método usamos para inserir apenas UM documento?
    try:
     colecao.insert_one(novo_participante) # LACUNA 4: Método de inserção
     print("Participante inserido com sucesso!")

    except pymongo.errors.PyMongoError as e:
       print(f"Erro ao inserir participante {e}")



    print("\n--- 2. CONSULTA (Read) ---")
    # Buscando o participante recém-inserido pelo ID
    # LACUNA 5: Crie um filtro de busca para a coleção que você selecionou
    filtro_busca = {"_id":"part021"}
   

    # Dica: Qual método usamos para buscar apenas UM documento?
    # LACUNA 5: Método de busca
    try:
     participante_encontrado = colecao.find_one(filtro_busca) 
     print(f"Participante encontrado: {participante_encontrado}")

    except pymongo.errors.PyMongoError as e:
        print(f"Participante nao encontrado {e}")


    print("\n--- 3. ATUALIZAÇÃO (Update) ---")
    # LACUNA 6: Crie um filtro para atualização
    filtro_update = {"_id":"part021"}

    try:
    # LACUNA 7: Monte a estrutura de atualização
     novos_valores ={"$set":{"nome":"Débora Fernanda"}}
    # LACUNA 8: Teste a atualização
     colecao.update_one(filtro_update,novos_valores)
     print("Participante atualizado com sucesso!")

    except pymongo.errors.PyMongoError as e:
       print(f"O participante nao foi atualzadp!{e}")
       

    print("\n--- 4. EXCLUSÃO (Delete) ---")
    # Excluindo o participante de teste
    # LACUNA 9: Crie um filtro para exclusão
    filtro_delete = {"_id":"part021"}
    
    # Dica: Qual método usamos para excluir apenas UM documento?
    try:
     colecao.delete_one(filtro_delete)# LACUNA 6: Método de exclusão
     print("Participante excluído com sucesso!")

    except pymongo.errors.PyMongoError as e:
       print(f"O participante não foi excluiido {e}")
       
    
    print("\n--- 5. CONSULTA AVANÇADA ---")
    # Crie uma consulta utilizando agregação ou operadores de comparação
    # Faça um comentário, indocando o que a consulta faz, exemplo: Listando os participantes em ordem alfabética

    # Essa consulta busca o participante pela idade usando um filtro de numeração que é o $gte (maior ou ==)

    filtro = {"idade": {"$gte": 20}} #"esse filtro vai trazer os participantes com a idade maior ou então == a 20 anos

    projecao = {"nome": 1,
                "idade": 1,
                "_id": 0} #essa projecao traz o campos que quero mostrar
    
    try:
      resultado = colecao.find(filtro,projecao)

      for colecao in resultado:
         print(f"Nome:{colecao['nome']}|Idade:{colecao['idade']}")
      print("Listagem dos partc. com idade maior ou igual a 20")

    except pymongo.errors.PyMongoError as e:
       print(f"Erro na listagem dos participantes {e}")
   
if __name__ == "__main__":
    main()
