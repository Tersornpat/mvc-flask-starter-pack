from flask import Flask

from controller.index import indexBlueprint
from controller.check import checkBlueprint
app = Flask(__name__, template_folder='view')

#ทำการประกาศ Router ว่าเรามี Route อะไรบ้าง
app.register_blueprint(indexBlueprint)
app.register_blueprint(checkBlueprint)

if __name__ == "__main__":
    app.run(debug=True)
    

