from wtforms.validators import ValidationError
from .models import URLMap


def validate_unique_short_link(form, field):
    if field.data and URLMap.query.filter_by(short=field.data).first():
        raise ValidationError(
            'Предложенный вариант короткой ссылки уже существует.'
        )
