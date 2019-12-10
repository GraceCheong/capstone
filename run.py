from flask import Flask, request, jsonify
import database

app = Flask(__name__)
app.config['TESTING'] = True

database.check_rev()

@app.route('/insert', methods=['POST'])
def insert():
    resp = ""

    type = request.form["type"]

    try:
        if(type == "wine"):
            name = request.form["wine"]
            try:
                if database.insert_wine(name) == False:
                    resp = "wine already exigsted"
                else:
                    resp = "inserted {}".format(name)
            except Exception as ee:
                print(ee)

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

@app.route('/wine/<wine_name>', methods=['GET'])
def get_wine(wine_name):

    try:
        wine_id = database.select_wine(wine_name)
        resp = database.select_rev(wine_id=wine_id)

    except Exception as e:
        print(e)
        resp = e.args

    return jsonify(resp)

if __name__ == "__main__":
    app.run()
