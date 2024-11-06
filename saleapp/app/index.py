from flask import render_template
import dao
from saleapp.app import app


@app.route("/")
def index():
    cates=dao.load_categories()
    pro = dao.load_product()
    return render_template("index.html",categories=cates, products=pro)



if __name__ == '__main__':
    app.run(debug=True)
