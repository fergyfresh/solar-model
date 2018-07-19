from __future__ import absolute_import
from flask import Flask, request, url_for, redirect, render_template
from os import getenv

from .nrel import PVWattsV6
from .utils import OutputFormatter

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        # take data from post and call function
        api = PVWattsV6(
            getenv("API_KEY"),
            request.form['lat'],
            request.form['lon'],
            request.form['array_type'],
            request.form['tilt'],
            request.form['azimuth'],
            request.form['module_type'],
            request.form['losses'],
            request.form['system_capacity']
            )
        status_code, data = api.get_data()
        if status_code == 200:
            output = OutputFormatter(data)
            output.write_csv()
            return render_template('display.html', table=data)
        elsif status_code == 422:
            error = data
        else:
            error = "Oops something bad happened, try again!"
    return render_template('index.html', error) 
