from flask_socketio import SocketIO,emit
from flask import abort, jsonify
from info.modules.chat import chart_blu
from info import socketio
from flask import render_template
from flask import request
from flask import session
from info.utils.common import user_login_data
from flask import g
from datetime import datetime
# -*- coding: utf-8 -*-
import eventlet
eventlet.monkey_patch()
from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room, rooms
from datetime import datetime
# to generate a random secret key
import os
# refresh pyc everytime I change code
import sys
from info.modules.models import User, News, Category,IndexCategory
from info.utils.common import user_login_data
from flask import g
from info.utils.response_code import RET
from flask import current_app, jsonify


@chart_blu.route('/')
def index():
    user_id = session.get("user_id", None)
    user = None
    if user_id:
        # 尝试查询用户的模型
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)

    categories2 = IndexCategory.query.all()

    category_li2 = [ ]
    for category2 in categories2:
        category_li2.append(category2.to_dict())

    data = {
        "user": user.to_dict() if user else None,
        "category_li2": category_li2,
    }

    return render_template('chat/index2.html',data=data)

@chart_blu.route('/guestlist')
def guestlist():
    user_id = session.get("user_id", None)
    user = None
    if user_id:
        # 尝试查询用户的模型
        try:
            user = User.query.get(user_id)
        except Exception as e:
            current_app.logger.error(e)
    data={
        "user": user.to_dict() if user else None,
    }
    return jsonify(data=data)

@socketio.on('connect')
def user_connect():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - Server connected successfully.')

# offline
@socketio.on('disconnect')
def user_disconnect():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ' - Client disconnected.')

# a user press enter after input a valid username
@socketio.on('is_online')
def user_joined(name):
    emit('online_name', name, broadcast=True)

# `inviter` selects `guest`, sending 2 usernames
@socketio.on('build_private_room')
def creat_private_room(names):
    print('The inviter is: [' + names['inviter'] + '], the guest is: [' + names['guest'] + ']')
    r = [names['inviter'], names['guest']]
    r.sort()
    room = ''.join(r)
    emit('invite_match_user', {
        'inviter': names['inviter'],
        'guest': names['guest'],
        'room': room,
        'isActive': 'true'
    }, broadcast=True)

# 2 filtered users emit this event, then join room
@socketio.on('join_private_room')
def the_private_room(data):
    join_room(data['room'])
    print('Users: ' + data['inviter'] + ', ' + data['guest'] + ' joined the room [' + data['room'] + '].')

# send private messages
@socketio.on('private_message')
def handle_message(data):
    emit('room_message', data, room=data['room'])
