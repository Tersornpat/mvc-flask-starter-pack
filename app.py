from flask import Flask

from controller.index import indexBlueprint
from controller.configData import dataBlueprint
  
app = Flask(__name__, template_folder='view')

app.register_blueprint(indexBlueprint)
app.register_blueprint(dataBlueprint)
  
if __name__ == "__main__":
    app.run(debug=True)
    

