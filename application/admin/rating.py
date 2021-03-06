from application.admin import bp
from flask import render_template, flash, redirect, url_for, request
from flask_login import login_required
from application.admin.forms import RatingForm, PresentationsForm
from application.core import ratingservice, channelservice


@login_required
@bp.route('/rating', methods=['GET', 'POST'])
def ratings():
    rating_form = RatingForm()
    presentations_form = PresentationsForm()
    if rating_form.validate_on_submit():
        images = request.files.getlist('image')
        ratingservice.save_rating(images)
        flash('Рейтинг обновлён', category='success')
        flash('Рекомендуется перейти в бота и запросить у него новые файлы, '
              'чтобы в последующем он отправлял их быстрее', category='warning')
        return redirect(url_for('admin.ratings'))
    return render_template('admin/rating.html', title='Рейтинги',
                           form=rating_form, area='ratings',
                           presentation_form=presentations_form)


@login_required
@bp.route('/presentations', methods=['POST'])
def presentations():
    form = PresentationsForm()
    if form.validate_on_submit():
        files = request.files.getlist('presentations')
        channelservice.update_presentations(files)
        flash('Файлы презентаций обновлены', category='success')
    return redirect(url_for('admin.ratings'))
