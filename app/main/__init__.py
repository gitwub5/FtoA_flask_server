from flask import Blueprint

main_bp = Blueprint('main', __name__)

from . import views

#테스트용
#from . import test_view 