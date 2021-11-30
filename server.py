from wsgiref.simple_server import make_server
from jinja2 import Environment, FileSystemLoader

HTML = open('index.html', 'r').read()


# application es la función encargada de responder a las peticiones
# env es un diccionario con la información de la petición
# start_response es un callback que tiene el status code y la lista de headers
def application(env, start_response):
    # Un header se representa en tuplas que tienen dos elementos
    headers = [ ('Content-type', 'text/html') ]
    start_response('200 OK', headers)

    envi = Environment(loader=FileSystemLoader('templates'))

    template = envi.get_template('hello.html')

    html = template.render({ 'title': 'jinja2', 'name': 'Daniel' })

    return [bytes(html, 'utf-8')]



if __name__ == '__main__':
    # Crear el servidor
    # maker_server(direccion, puerto, función que resolverá cada petición)
    server = make_server('localhost', 8000, application)
    server.serve_forever()