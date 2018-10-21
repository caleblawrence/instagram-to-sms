from flask import Flask, render_template, request, url_for, send_from_directory
import os


app = Flask(__name__)

@app.route('/uploads/<username>/<filename>', methods=['GET', 'POST'])
def show_index(username, filename):
    image_directory = "/home/caleblawrence/Projects/instagramToSms/images/" + username
    return send_from_directory(image_directory, filename)