from modules import banco
import threading

cliente = banco.BancoMongo()


if __name__ == "__main__":
    user = input('Nickname: ')
    try:
        f = threading.Thread(target=cliente.select)
        f.start()
    except Exception as e:
        print(f'Falha ao criar thread: {e}')
    
    while f.isAlive:
        mens = input()
        cliente.cadastrar(user, mens)