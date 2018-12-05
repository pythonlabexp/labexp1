from flask.app import Flask
from flask.globals import request, session
from flask.templating import render_template

app = Flask(__name__)
app.secret_key = 'ASF$^UHgfjf890'
print(app.config)


@app.route('/')
@app.route('/save', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('contact.html')
    if request.method == 'POST':
        name=request.form
        print( name["username"])
        
        session['user'] = name["username"]
        session['address'] = name["paddr"]
        session['phone']=name["phonenumber"]
        
        
        return render_template('sucess.html')


if __name__ == '__main__':
    app.run(debug=True)
    
    
