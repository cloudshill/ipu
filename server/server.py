from aiohttp import web
import json
import socketio

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
# instance
sio.attach(app)


# @sio.on('connect')
# def on_connect(sid, data):
#     print(sid, data)
#     print('I\'m connected!')


@sio.on('notice')
def on_message(sid, data=None):
    print(data)
    print(sid)
    print('I received a message!')


@sio.on('bye')
def on_disconnect():
    print('I\'m disconnected!')


@sio.on('enter_room')
async def begin_chat(sid, data=None):
    print('begin_chat')
    print(data)
    print(sid)
    sio.enter_room(sid, 'chat_room')
    await sio.emit('enter_room',
                   data={
                       'comments': ['hoge comment', 'hoge2 comment'],
                       'users': ['user1', 'user2'],
                       'room': {'room_name': 'hoge room name'},
                   })


@sio.on('chat')
async def chat(sid, data):
    # data is json
    print('chat event')
    print('sid;', sid)
    print('data:', data)
    print('rooms:', sio.rooms(sid=sid))
    await sio.emit('chat', data=data, room='chat_room')


@sio.on('exit_room')
def exit_chat(sid):
    print('exit room')
    # print(data)
    print(sid)
    sio.leave_room(sid, 'chat_room')


if __name__ == '__main__':
    web.run_app(app, port=8000)