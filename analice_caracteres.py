
def analice_items(CSV, datos):

    # Recorrer todos los items
    for item in datos['items']:
        id = item['id']
        startingCause = item['startingCause']
        chatId = item['chat']['chat']['chatId']
        channelId = item['chat']['chat']['channelId']
        contactId = item['chat']['chat']['contactId']

        type = ''
        text = ''
        from_ = ''
        textSinSalto = ''
        caracteres = 0
        cola = ''
        idAgente = ''

        # Recorrer todos los Mensajes
        for message in item['messages']:
            creationTime = message['creationTime']
            template = 0
            type = message['content']['type']
            if type == 'text' and 'text' in message['content']:
                text = message['content']['text']
                if 'queueId' in message:
                    cola = message['queueId']
                if text.find('Template') >= 0:
                    template = 1
                from_ = message['from']
                if from_ == 'agent':
                    idAgente = message['agentId']
                textSinSalto = text.replace("\n", " ")
                caracteres = len(textSinSalto.split())
                cadena = (('{};{};{};{};{};{};{};{};{};{};' +
                           '{};{};' +
                           '{}\n').format(id,
                                          creationTime,
                                          chatId,
                                          channelId,
                                          contactId,
                                          startingCause,
                                          from_,
                                          type,
                                          textSinSalto,
                                          caracteres,
                                          template,
                                          cola,
                                          idAgente
                                          )
                          )
                CSV.append(cadena)
