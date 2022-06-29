from eventlet import wsgi
import eventlet
from Project.settings import app










if __name__=='__main__':
    wsgi.server(eventlet.listen(('127.0.0.1', 3333)), app)