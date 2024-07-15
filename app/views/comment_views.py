from datetime import datetime
from .auth_views import login_required

from flask import Blueprint, url_for, request, render_template, g
from werkzeug.utils import redirect

from app import db
from app.models import Complaint, Comment

bp = Blueprint('comment', __name__, url_prefix='/comment')


@bp.route('/create/<int:complaint_id>', methods=('POST',))
@login_required
def create(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    content = request.form['content']
    comment = Comment(complaint=complaint, content=content, create_date=datetime.now(), user=g.user)
    complaint.comment_set.append(comment)
    db.session.commit()
    return redirect(url_for('complaint.detail', complaint_id=complaint_id))
