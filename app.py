from flask import Flask, render_template, request, redirect, url_for, flash, abort

app = Flask(__name__)
app.secret_key = "ganti-dengan-kunci-rahasia"

CARS = [
    {"id": 1, "name": "Toyota Avanza", "year": 2022, "price": 180000000, "type": "MPV", "trans": "Manual", "desc": "MPV keluarga irit dan nyaman, cocok untuk harian.","img":"avanza.png"},
    {"id": 2, "name": "Honda Brio RS", "year": 2023, "price": 150000000, "type": "Hatchback", "trans": "Matic", "desc": "Hatchback lincah, ideal untuk dalam kota.","img":"brio.png"},
    {"id": 3, "name": "Mitsubishi Xpander", "year": 2021, "price": 190000000, "type": "MPV", "trans": "Automatic","desc": "Kabin lega dengan kabin 7 penumpang.", "img":"xpander.png"},
    {"id": 4, "name": "Toyota Fortuner", "year": 2020, "price": 560000000, "type": "SUV", "trans": "Automatic", "desc": "SUV tangguh untuk segala medan.", "img":"fortuner.png"},
]

@app.template_filter("rupiah")
def rupiah(v):
    return "Rp {:,.0f}".format(v).replace(",", ".")

@app.route("/")
def home():
    return render_template("index.html", cars=CARS[:3])

@app.route("/mobil")
def cars():
    q = request.args.get("tipe", "")
    data = [c for c in CARS if not q or c["type"] == q]
    return render_template("cars.html", cars=data, selected=q)

@app.route("/mobil/<int:car_id>")
def car_detail(car_id):
    car = next((c for c in CARS if c["id"] == car_id), None)
    if car is None:
        abort(404)
    return render_template("car_detail.html", car=car)

@app.route("/kontak", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        flash(f"Terima kasih, {request.form['nama']}! Pesan Anda sudah kami terima.", "success")
        return redirect(url_for("contact"))
    return render_template("contact.html")

@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404

if __name__ == "__main__":
    app.run(debug=True)
