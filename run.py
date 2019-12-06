from flask import Flask, request
import database

app = Flask(__name__)
app.config['TESTING'] = True

@app.route('/insert', methods=['POST'])
def insert():
    resp = ""

    type = request.form["type"]
    try:
        if(type == "wine"):
            name = request.form["wine"]
            try:
                print(database.insert_wine(name))
            except Exception as ee:
                print(ee)

            resp = "inserted {}".format(name)

        elif(type == "rev"):
            wine = request.form["wine"]
            review_str = request.form["review"]

            wine_id = database.select_wine(wine)
            database.insert_rev(wine_id=wine_id, review=review_str)

            resp = "inserted {} : {}".format(wine, review_str)

    except Exception as e:
        print(e)
        resp = e.args

    return resp

if __name__ == "__main__":
    app.run(debug=True)
