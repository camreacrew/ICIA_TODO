from flask import Flask, render_template, redirect, request
import datetime as dt

finance_app = Flask(__name__)

finances=[]

fno = 1

@finance_app.route("/list")
def index():
    hap = sum(item["price"] for item in finances)
    return render_template("finance/list.html", finances=finances, sum=hap)

@finance_app.route("/write", methods=['post'])
def write():
    global fno
    item = request.form.get('item')
    price = int(request.form.get('price'))
    date = dt.datetime.now().strftime('%Y-%m-%d')
    new_finance = {'fno':fno, 'item':item, 'price':price, 'date':date}
    finances.append(new_finance)
    fno += 1
    return redirect("/list")

@finance_app.route("/delete", methods=['post'])
def delete():
    fno = int(request.form.get('fno'))
    for finance in finances:
        if finance['fno']==fno:
            finances.remove(finance)
    return redirect("/list")


finance_app.run(debug=True)