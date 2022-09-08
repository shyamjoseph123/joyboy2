import ...

bot= ChatBot('parent')
conv = open('chats.txt','r').readlines()

bot.set_trainer(listTrainer)
bot.train(conv)

while True:
    request = input('student: ')
    response = bot.get_response(request)
    print('student: ', response)