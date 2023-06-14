import json

def login(parent, session, data):
    x = json.dumps({"hi":"lo"})  
    parent._set_response()
    parent.wfile.write(x.encode())

def logout(parent, session, data):
    pass

def get_user(parent, session, data):
    pass