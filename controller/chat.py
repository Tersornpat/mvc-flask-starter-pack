from flask import Blueprint, render_template, request

chatBlueprint = Blueprint('chat', __name__, url_prefix='/chat')

@chatBlueprint.route('/', methods=["GET","POST"])
def getChat():
    name = ''
    if request.method == 'POST':
        name = request.form['name']
    
    return render_template('chat.html', name=name)
