class Pipeline:
    def __init__(self):
        self.filters = list()
 
    def add(self, filter):
        self.filters.extend(filter)
 
    def execute(self, message):
        print("Executando pipeline...")
        for message_filter in self.filters:
            message_filter(message)
 
def double_data(message):
    message['data'] = [x*2 for x in message['data']]
 
def update_header(message):
    message['header'] = 'esta é a mensagem atualizada'
 
pipeline = Pipeline()
 
pipeline.add([double_data,
              update_header]) # observe que estamos adicionando o objeto de função, não fazendo uma chamada de função
 
message = {'header': 'esta é a mensagem original',
           'data': [1,2,3]}
 
for key, value in message.items():
    print(key + ' : ' + str(value))