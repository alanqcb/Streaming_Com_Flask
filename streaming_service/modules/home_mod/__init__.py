from flask import Blueprint, render_template, abort, send_from_directory, request,url_for
from jinja2 import TemplateNotFound
import os

home_mod = Blueprint('home_mod', __name__, template_folder='templates')


@home_mod.route('/', defaults={'page': 'index.html'}, methods=('get', 'post'))
@home_mod.route('/<page>')
def show(page):
    global template_dir
    try:
        # print(request.args.get('user'))
        return render_template(f'home_mod/{page}')
    except TemplateNotFound:
        abort(404)

@home_mod.route('/favicon.ico')
def favicon():
    global template_dir
    try:
        # print(request.args.get('user'))
        return ''
    except TemplateNotFound:
        abort(404)
