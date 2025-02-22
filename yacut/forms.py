from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import (URL, DataRequired, Length, Optional, Regexp,
                                ValidationError)

from .models import URLMap


class URL_mapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка', validators=[
            DataRequired(message='Обязательное поле:'),
            Length(1, 26), URL(
                require_tld=True, message='Некорректная ссылка'
            )
        ]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки', validators=[
            Optional(),
            Length(1, 16),
            Regexp(
                r'^[A-Za-z0-9]+$',
                message='Можно использовать только [A-Za-z0-9]'
            )
        ]
    )
    submit = SubmitField('Создать')

    def validate_custom_id(self, field):
        if field.data and URLMap.query.filter_by(short=field.data).first():
            raise ValidationError(
                'Предложенный вариант короткой ссылки уже существует.')
