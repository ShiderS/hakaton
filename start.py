from flask import Flask, render_template, redirect
from forms.analyze import GetCsvFile
from main import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mpwidogbkKLGJANDKLGJIANDKVJOERHG895TJ'


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = GetCsvFile()
    if form.validate_on_submit():
        f = form.file_csv.data
        if f.filename != '':
            app = Main(f.filename)
            save_to = f'static/saved_files/{f.filename}'
            f.save(save_to)
            return redirect(f'/result/output.csv')
        return redirect('/')
    return render_template('index.html', title='Хакатон', form=form)


@app.route('/result/<file>')
def prepare_csv(file):
    f = open(f'static/saved_files/{file}', 'r')
    return render_template('result.html', file=file, content=f.read())


if __name__ == "__main__":
    app.run()
