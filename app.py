# import the necessary modules
from flask import Flask , render_template , request , jsonify

# importing sentiment_analysis file as sa
import sentiment_analysis as sa

app = Flask(__name__)

# app route for index page
@app.route('/')
def home():
    return render_template('index.html')

# write a route for post request
@app.route('' , methods = [''])
def review():

    # extract the customer_review by writing the appropriate 'key' from the JSON data
    review = request.json.get('')

    # check if the customer_review is empty, return error
    if not review:

        return jsonify({'status' : 'error' , 
                        'message' : 'Empty response'})

    else:

        _ , _ = sa.predict(review)

        return jsonify({'':'' , '':''})


if __name__  ==  "__main__":
    app.run(debug = True)