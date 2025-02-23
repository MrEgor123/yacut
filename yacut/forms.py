from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .validators import validate_unique_short_link


class URLMapForm(FlaskForm):
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
            ), validate_unique_short_link
        ]
    )
    submit = SubmitField('Создать')
