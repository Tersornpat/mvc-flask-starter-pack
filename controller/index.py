from flask import Blueprint, render_template

indexBlueprint = Blueprint('index', __name__)

"localhost:5000/"
@indexBlueprint.route('/', methods=["GET"])
def index():
    return render_template('index.html')
