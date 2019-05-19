from flask import Blueprint

chart_blu =Blueprint("chart",__name__,url_prefix="/chart")

from . import views
