from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField


class GetCsvFile(FlaskForm):
    file_csv = FileField('Выберите csv-файл: ')
    submit = SubmitField('Отправить файл')
