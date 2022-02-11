# chat/views.py
from django.shortcuts import render
from datetime import datetime
from .models import Chat
from asgiref.sync import sync_to_async
import json

def index(request):
    return render(request, 'chat/index.html', {})

def room(request, room_name):
    msgs = groupMsg('chat_'+room_name)
    print(msgs)
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'msgs': json.dumps(msgs)
    })
@sync_to_async    
def saveMsg(user,msg, group):
    print('cheguei aqui')
    try:
        msg =   Chat(
                    usuario=user,
                    mensagem = msg,
                    group=group,
                    data_registro=datetime.now()
                )
        msg.save()
    except Exception as e:
        raise
    
def groupMsg(group):
    try:
        msgs = Chat.objects.filter(group=group)
        msgsList = {}
        cont = 0
        for msg in msgs:
            item = {
                'usuario': msg.usuario,
                'mensagem': msg.mensagem,
                'data_registro': msg.data_registro.strftime('%d/%m/%Y %H:%M')
            }
            msgsList[cont] = item
            cont += 1 
    except:
        msgs = {}
    return msgsList