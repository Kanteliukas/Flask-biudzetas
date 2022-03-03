from flask import Flask, render_template, request
from main import app, db, Budget
from input_validation import validate_inputs
from print_entries import get_entries
from get_balance import get_balance

db.create_all()

@app.route("/", methods=["POST", "GET"])
def index():
    entries = False
    balance = False
    if request.method == "POST":
        if request.form["submit"] == "Išsaugoti":
            income_amount = request.form["income_amount"]
            expense_amount = request.form["expense_amount"]
            sender = request.form["sender"]
            extra_information = request.form["extra_information"]
            payment_option = request.form["payment_option"]
            bought_goods_or_services = request.form["bought_goods_or_services"]
            if not validate_inputs(income_amount, expense_amount):
                balance = "Įvestas blogas sumos formatas, formatas turi būti: 0.00"
            else:
                if income_amount != "":
                    db.session.add(Budget(
                        "Pajamos",
                        float(income_amount),
                        sender=sender,
                        extra_information=extra_information,
                    ))
                    db.session.commit()
                if expense_amount != "":
                    db.session.add(Budget(
                        "Išlaidos",
                        float(expense_amount),
                        payment_option=payment_option,
                        bought_goods_or_services=bought_goods_or_services,
                    ))
                    db.session.commit()
        elif request.form["submit"] == "Balansas":
            balance = get_balance()
        elif request.form["submit"] == "Išrašas":
            entries = get_entries()
    return render_template('User_input.html', balance=balance, entries=entries)


if __name__ == "__main__":
    app.run(debug=True)