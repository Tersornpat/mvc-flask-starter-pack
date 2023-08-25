from flask import Blueprint,jsonify, render_template
import model.connectDB as db

dataBlueprint = Blueprint('configData',  __name__, url_prefix='/configdata')

@dataBlueprint.route('/')
def getData():
    data_list =  db.get_all_data()
    
    result_dict = []

    for entry in data_list:
        result_dict.append({
            "id": entry[0],
            "username": entry[1],
            "email": entry[2]
        })

    # return jsonify(data_list)
    return jsonify(result_dict)
    # return render_template('showTable.html', data_list=data_list)


@dataBlueprint.route('/adddata')
def addData():
    try:
        db.insert_data('john_doe', 'john@example.com')
        db.insert_data('jane_smith', 'jane@example.com')
        return "Add Data Succeed"
    except:
        return "Add Data Failed"