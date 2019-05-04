from flask import Flask, render_template
import db
app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    categories = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']

    #chart = {"renderTo": chartID, "type": chart_type, "height": chart_height,}
    series = db.samplefunction()
    #title = {"text": 'My Title'}
    #xAxis = {"categories": ['xAxis Data1', 'xAxis Data2', 'xAxis Data3']}
    #yAxis = {"title": {"text": 'yAxis Label'}}
    return render_template('index.html', series=series, categories=categories)

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port=80, passthrough_errors=True)