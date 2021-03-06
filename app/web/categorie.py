from app.models.article import Category
from . import web
from flask import current_app
from flask import render_template,request
from app.models.article import Article



@web.route('/category/<int:id>/')
# category 显示页面
def category(id):
    page = request.args.get('page', 1, type=int)
    pagination = Category.query.get_or_404(id).articles.order_by(
        Article.created.desc()).paginate(page,per_page=current_app.config['PER_PAGE'],
                                         error_out=False)
    articles = pagination.items


    return render_template('index.html',articles=articles,
                           pagination=pagination, endpoint='.category',
                           id=id, category_id=id)

