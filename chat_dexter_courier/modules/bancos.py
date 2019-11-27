from pymongo import MongoClient, DESCENDING
import time

class BancoMongo():

    def __init__(self):
        try:
            client = MongoClient('192.168.201.128")
            self.db = client['chat']
        except Exception as e:
            print(f'ERRO: {e}')
            exit()

    def cadastrar(self, name, mensagem):
        date = {
            'nome':  name,
            'mensagem': mensagem,
            'hora': time.strftime('%d-%m-%Y %H:%M:%S')
        }
        self.db.chat.insert(date)

    def select(self):
        ultimo = [x for x in self.db.chat.find().sort('_id', DESCENDING)]
        while True:
            date = [x for x in self.db.chat.find().sort('_id', DESCENDING)]
            if date != ultimo:
                ultimo = date
                print(f'[{date[0]["hora"]}] {date[0]["nome"]} : {date[0]["mensagem"]} \n')
                time.sleep(2)

if __name__ == "__main__":
    obj = BancoMongo()
    obj.select
