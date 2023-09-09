from flask import Blueprint, render_template, request, redirect, url_for
import re
import xml.etree.ElementTree as ET
import model.connectDB as db

# ประกาศ router โดยให้ Url เป็น /check
checkBlueprint = Blueprint('check', __name__, url_prefix='/check')

# # Route ที่มีของ /check('/')
@checkBlueprint.route('/', methods=["GET","POST"])
def getCheck():

    # ประกาศ Regex Pattern สำหรับการใช้ Check Pattern ในแบบต่างๆ
    chceckHttps = r'^\s*https://\S'
    checkHttp = r'^\s*http://\S'
    chekJson = r'^\s*\{.*\}\s*$'
    checkXml = r'<\?xml.*?\?>'

    # ประกาศ Data = - เพื่อไม่ให้ Insert null
    data = "-"
    # Check Method GET
    if request.method == 'GET':
        # รับค่าจาก ตัวแปร URL จากหน้าบ้านมาใช้งาน
        try:
            url = request.args.get['url']
        except:
            url = 'http://www.google.com'

        # ประกาศ message ของ MONIC OIBER
        monic = 'Reading ' + url
        oiber = 'Getting ' + url

        # Check Pattern Http, Https
        if re.search(chceckHttps, url):
            monic = monic + ("  This website is so secure!")
        elif re.search(checkHttp, url):
            oiber
    # Check Method Post
    elif request.method == 'POST':
        # รับค่าจาก ตัวแปร URL และ Data จากหน้าบ้านมาใช้งาน
        try:
            url = request.form['url']
            data = request.form['data']
        except:
            url = 'POST'
            data = 'DATA'

        # ประกาศ message ของ MONIC OIBER
        monic = 'Posting ' + data + ' to ' + url
        oiber = 'Sending ' + data + ' to ' + url

        # Check Pattern Json, XML
        if re.match(chekJson, data):
            monic = monic + '  JSON is coming!'
            oiber = oiber + '  Warning! This website is not secure.'
        elif re.search(checkXml, data):
            oiber = oiber + '  Warning! This website is not secure. XML is too verbose.'

    # นำค่าที่ได้ทั้งหมดลง Database
    db.insert_data(url, data, monic, oiber)
    return redirect(url_for('index.index'))
