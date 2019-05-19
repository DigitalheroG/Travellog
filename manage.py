from flask import session
from info.modules.index import index_blu
from flask_script import Manager
from flask_migrate import  Migrate,MigrateCommand
from info import app,db,socketio
from info.modules import models
from info.utils.common import do_index_class
from info.modules.news import news_blu
from info.modules.profile import profile_blu
from info.modules.chat import chart_blu

app.register_blueprint(index_blu)
app.register_blueprint(news_blu)
app.register_blueprint(profile_blu)
app.register_blueprint(chart_blu)

from info.modules.models import User
from info.modules.admin import admin_blu
app.register_blueprint(admin_blu,url_prefix="/admin")



manager = Manager(app)
Migrate(app,db)
manager.add_command('db',MigrateCommand)

app.add_template_filter(do_index_class,"index_class")

@manager.option ('-n','-name',dest="name")
@manager.option('-p','-password',dest="password")
def createsuperuser(name,password):
    if not all([name,password]):

        print("参数不足")
    user= User()
    user.nick_name=name
    user.mobile=name
    user.password =password
    user.is_admin=True
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        print(e)
    print("添加成功")

@app.route('/')
def hello_world():
    session["name"]="itheeima"
    return "aaaaaa"


if __name__ == '__main__':
    manager.run()
    socketio.run(app, debug=True)