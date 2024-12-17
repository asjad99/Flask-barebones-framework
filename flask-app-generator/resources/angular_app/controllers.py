import os

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response

from [[APP_NAME]] import app

# special file handlers
@app.route('/favicon.ico')
def favicon():
	return send_from_directory(os.path.join(app.root_path, 'static'), 'img/favicon.ico')

# 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# catch-all url handler
@app.route('/')
@app.route('/about')
def index():
	return make_response(open('[[APP_NAME]]/templates/index.html').read())

# API
from [[APP_NAME]].core import api_manager
from [[APP_NAME]].models import Post
api_manager.create_api(Post, methods=['GET', 'POST'])
