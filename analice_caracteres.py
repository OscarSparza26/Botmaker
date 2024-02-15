
def analice_items(CSV, datos):

    # Recorrer todos los items
    for item in datos['items']:
        id = item['id']
        creationTime = item['creationTime']
        startingCause = item['startingCause']

        #if startingCause != "WhatsAppTemplate":
         #   continue

        #  Cabecera para todos los mensaje
        chatId = item['chat']['chat']['chatId']
        #

        type = '',
        text = '',
        usuario = '',
        textSinSalto = ''
        caracteres = 0

        # Recorrer todos los Mensajes
        for message in item['messages']:
            template = 0
            type = message['content']['type']
            if type == 'text' and 'text' in message['content']:
                text = message['content']['text']
                if text.find('Template') >= 0:
                    template = 1
                usuario = message['from']
                textSinSalto = text.replace("\n", " ")
                caracteres = len(textSinSalto.replace(" ", ""))
                cadena = (('{};{};{};{};{};{};{};{};' +
                           '{}\n').format(id,
                                          creationTime,
                                          chatId,
                                          startingCause,
                                          usuario,
                                          type,
                                          textSinSalto,
                                          caracteres,
                                          template
                                          )
                          )
                CSV.append(cadena)
