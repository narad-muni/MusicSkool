import http.server
import json
from urllib.parse import urlparse, parse_qs
from utils.db import execute_query
from utils.migrate import init, poppulate

# A dictionary to store session data
sessions = {}


class MyHandler(http.server.BaseHTTPRequestHandler):

    def get_session_id(self):
        # Retrieve the session ID from the request headers (Cookie)
        if 'Cookie' in self.headers:
            cookies = self.headers['Cookie'].split('; ')
            for cookie in cookies:
                name, value = cookie.split('=')
                if name == 'session_id':
                    return value
        return None

    def generate_session_id(self):
        # Generate a unique session ID (you can modify this as per your requirements)
        import uuid
        return str(uuid.uuid4())

    def _set_response(self, status_code=200, content_type='application/json'):
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_POST(self):
        parsed_path = urlparse(self.path)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')

        session_id = self.get_session_id()

        if session_id is not None and session_id in sessions:
            # If session exists, retrieve the session data
            session_data = sessions[session_id]

        try:
            data = json.loads(post_data)
        except: 
            pass

        if(parsed_path == "/api/login"):
            pass
        else:
            error_resp = {
                'status': 'error',
                'message': 'some error occured'
            }

            response_json = json.dumps(error_resp)

            self._set_response()
            self.wfile.write(response_json.encode())

    def do_GET(self):
        parsed_path = urlparse(self.path)

        if parsed_path.path == '/users':
            users = execute_query('SELECT * FROM users')
            response = json.dumps(users)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(response.encode())
        elif parsed_path.path == '/':
            with open('pages/index.html', 'r') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode())
        else:
            with open('pages/404.html', 'r') as file:
                content = file.read()
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                self.wfile.write(content.encode())

# init()
poppulate()

# Specify the port you want to use
PORT = 8000

# Create the HTTP server with your custom handler
httpd = http.server.HTTPServer(('localhost', PORT), MyHandler)

print(f"API server running at http://localhost:{PORT}")

# Start the server
httpd.serve_forever()


'''

def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()

            # Check if a session cookie is present
            session_id = self.get_session_id()

            if session_id is not None and session_id in sessions:
                # If session exists, retrieve the session data
                session_data = sessions[session_id]
                self.wfile.write(f"Logged in as {session_data['username']}".encode())
            else:
                # If no session, show login form
                self.wfile.write(b"You are not logged in. <a href='/login'>Login</a>")

        elif self.path == '/login':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b\'''
                <form action="/login" method="post">
                    <p><input type="text" name="username" placeholder="Username"></p>
                    <p><input type="submit" value="Login"></p>
                </form>
            \''')

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

    def do_POST(self):
        if self.path == '/login':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode()

            # Parse the form data
            form_data = parse_qs(post_data)
            username = form_data.get('username', [''])[0]

            # Generate a session ID
            session_id = self.generate_session_id()

            # Store the session data
            sessions[session_id] = {'username': username}

            # Set the session ID as a cookie
            self.send_response(302)
            self.send_header('Location', '/')
            self.send_header('Set-Cookie', f'session_id={session_id}; Path=/')
            self.end_headers()

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b"404 Not Found")

'''