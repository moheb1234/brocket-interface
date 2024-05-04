import websocket


def on_open(ws):
    pass

def on_message(ws , message):
    pass

def on_error(ws , error):
    pass

def on_close(ws):
    pass


url = ''

socket = websocket.WebSocketApp(url , on_open= on_open , on_error= on_error , on_message= on_message , on_close= on_close)
socket.run_forever(reconnect=3)