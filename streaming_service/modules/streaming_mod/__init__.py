from flask import Blueprint, render_template, abort, send_from_directory, request,send_file, Response, jsonify
from jinja2 import TemplateNotFound
import os, re, mimetypes, psutil

process = psutil.Process(os.getpid())

streaming_mod = Blueprint('streaming_mod', __name__, template_folder='templates')

arquivos_atuais = []

def send_file_partial(path):
    """ 
        Simple wrapper around send_file which handles HTTP 206 Partial Content
        (byte ranges)
        TODO: handle all send_file args, mirror send_file's error handling
        (if it has any)
    """
    range_header = request.headers.get('Range', None)
    if not range_header: return send_file(path)

    size = os.path.getsize(path)    
    
    byte1, byte2 = 0, None
    
    m = re.search('(\d+)-(\d*)', range_header)
    g = m.groups()
    
    if g[0]: byte1 = int(g[0])
    if g[1]: byte2 = int(g[1])

    length = size - byte1
    if byte2 is not None:
        # length = byte2 - byte1
        length = byte2 + 1 - byte1
    
    data = None
    with open(path, 'rb') as f:
        print(f'Memória: {process.memory_info().rss}') 
        f.seek(byte1)
        data = f.read(length)

    rv = Response(data, 
        206,
        mimetype=mimetypes.guess_type(path)[0], 
        direct_passthrough=True)
    rv.headers.add('Content-Range', 'bytes {0}-{1}/{2}'.format(byte1, byte1 + length - 1, size))

    return rv



@streaming_mod.route('/', defaults={'page': 'index.html'}, methods=('get', 'post'))
@streaming_mod.route('/<page>')
def show(page):
    global template_dir
    try:
        if '{{' not in page:
            print(f'{os.getcwd()}\\streaming_service\\modules\\streaming_mod\\templates\\streaming_mod\\{page}')
            return send_file(f'{os.getcwd()}\\streaming_service\\modules\\streaming_mod\\templates\\streaming_mod\\{page}')
        else:
            return 'hello'
    except TemplateNotFound:
        abort(404)

@streaming_mod.route('/videos/<page>')
def enviar_video(page):
    try:
        return send_file_partial(f'{os.getcwd()}\\streaming_service\\videos\\{page}')

    except TemplateNotFound:
        abort(404)

@streaming_mod.route('/thumbnail/<page>')
def enviar_thumbnail(page):
    try:
        return send_file(f'{os.getcwd()}\\streaming_service\\videos\\thumbnail\\{page}')

    except TemplateNotFound:
        abort(404)


@streaming_mod.route('/static/<page>')
def enviar_static(page):
    try:
        return send_file(f'{os.getcwd()}\\streaming_service\\modules\\streaming_mod\\static\\{page}')

    except TemplateNotFound:
        abort(404)



@streaming_mod.route('/read')
def read_dir():
    global arquivos_atuais
    if len(arquivos_atuais) > 0  or request.args.get('update') == 'no':
        print('cached')
        return jsonify(arquivos_atuais)

    try:
        lista_arquivos = os.listdir(f'{os.getcwd()}\\streaming_service\\videos\\')
        b = [{'video':request.url_root +request.blueprint+'/videos/'+x,'thumbnail':request.url_root +request.blueprint+'/thumbnail/'+x.replace('.mp4', '.jpg')} 
                for x in lista_arquivos  if  '.mp4' in x]

        arquivos_atuais = b
        return jsonify(b)

    except TemplateNotFound:
        abort(404)
