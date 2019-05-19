from flask import Blueprint

chart1_blu =Blueprint("chart1",__name__,url_prefix="/chart1")

from . import views
