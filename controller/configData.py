from flask import Blueprint, render_template,request,redirect,url_for
import model.connectDB as db

dataBlueprint = Blueprint('configData',  __name__, url_prefix='/configdata')

@dataBlueprint.route('/', methods=['GET', 'POST'])
def getData():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        db.insert_data(username, email)

    data_list =  db.get_all_data()
    return render_template('showTable.html', data_list=data_list)

@dataBlueprint.route('/adddata')
def addData():
    try:
        db.insert_data('john_doe', 'john@example.com')
        db.insert_data('jane_smith', 'jane@example.com')
        return "Add Data Succeed"
    except:
        return "Add Data Failed"
    
@dataBlueprint.route('/deletedata')
def deletedata():
    db.remove_all_data()
    return redirect(url_for('configData.getData'))