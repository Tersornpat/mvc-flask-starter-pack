from flask import Blueprint, render_template
import model.connectDB as db

# ประกาศชื่อของ router ตัวใหญ่
indexBlueprint = Blueprint('index', __name__)

# Route ที่มีของ /index('/')
@indexBlueprint.route('/', methods=["GET"])
def index():
    # ทำการ get data ทั้งหมดของ Database มาแสดงในตัวแปร messages
    messages = db.get_all_data();
    # นำ messages ไปแสดงผลหน้าบ้าน
    return render_template('index.html' , messages = messages)
