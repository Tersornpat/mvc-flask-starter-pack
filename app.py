from flask import Flask

from controller.index import indexBlueprint
from controller.configData import dataBlueprint
from controller.chat import chatBlueprint
  
app = Flask(__name__, template_folder='view')

app.register_blueprint(indexBlueprint)
app.register_blueprint(dataBlueprint)
app.register_blueprint(chatBlueprint)

if __name__ == "__main__":
    app.run(debug=True)
    

