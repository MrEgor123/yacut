from flask import flash, redirect, render_template, url_for

from . import app, db
from .models import URLMap
from .forms import URL_mapForm
from .utils import get_unique_short_id


@app.route('/', methods=['GET', 'POST'])
def index_view():
    form = URL_mapForm()
    if form.validate_on_submit():
        short = form.custom_id.data or get_unique_short_id()
        url_map = URLMap(
            original=form.original_link.data,
            short=short
        )
        db.session.add(url_map)
        db.session.commit()
        flash(url_for('short', short=short, _external=True))
    return render_template(
        'main.html',
        form=form
    )


@app.route('/<string:short>', methods=['GET', 'POST'], endpoint='short')
def opinion_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )
