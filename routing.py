from flask import Blueprint
from flask import render_template, request
from flask import jsonify
from dataParse import dataParse

bp = Blueprint('routing', __name__)

@bp.route("/", methods = ["POST", "GET"])
def add_page():
    result = 0

    if request.method == "GET":
        return render_template("Calculator.html")
    
    if request.method == "POST":
        data = request.get_json()
        args = (data['value'])
        print(args)
        result = dataParse(args)
        print(result)
        return jsonify(result=result)