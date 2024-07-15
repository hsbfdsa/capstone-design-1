from flask import Blueprint, render_template
from flask import request
from app.models import Complaint, Comment, User
from app import db

bp = Blueprint('complaint', __name__, url_prefix='/complaint')


@bp.route('/list/')
def _list():
    page = request.args.get('page', type=int, default=1)
    kw = request.args.get('kw', type=str, default='')
    filter_status = request.args.get('filter_status', type=str, default='')
    sort_order = request.args.get('sort_order', type=str, default='desc')  # 정렬 순서 받아오기

    complaint_list = Complaint.query.order_by(Complaint.create_date.desc())

    if sort_order == 'desc':
        complaint_list = Complaint.query.order_by(Complaint.create_date.desc())
    else:
        complaint_list = Complaint.query.order_by(Complaint.create_date.asc())

    if kw:
        search = '%%{}%%'.format(kw)
        complaint_list = complaint_list \
            .filter(
                Complaint.author.ilike(search) |    # Complaint 작성자 필터
                Complaint.content.ilike(search)    # Complaint 내용 필터
            )
        
    if filter_status == 'done':
        complaint_list = complaint_list.filter(Complaint.comment_set.any())
    elif filter_status == 'pending':
        complaint_list = complaint_list.filter(~Complaint.comment_set.any())

    complaint_list = complaint_list.paginate(page=page, per_page=10)

    return render_template('complaint/complaint_list.html', complaint_list=complaint_list, page=page, kw=kw, sort_order=sort_order)


@bp.route('/detail/<int:complaint_id>/')
def detail(complaint_id):
    complaint = Complaint.query.get_or_404(complaint_id)
    return render_template('complaint/complaint_detail.html', complaint=complaint)