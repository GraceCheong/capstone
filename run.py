from flask import Flask, request

app = Flask(__name__)

@app.route('/insert', methods=['POST'])
def insert():

    type = request.form.get("type", "")
    try:
        if(type == "wine"):
            name = request.form.get("wine", "")
            database.insert_wine(name)
            resp = "inserted {}".format(name)
        elif(type == "rev"):
            wine = request.form.get("wine", "")
            review_str = request.form.get("review", "")

            id = database.select_wine(wine)
            database.insert_rev(wine_id=id, review=review_str)

            resp = "inserted {} : {}".format(wine, review_str)
    except Exception as e :
        print(e)
        
    return resp



if __name__ == "__main__":
    app.run()
