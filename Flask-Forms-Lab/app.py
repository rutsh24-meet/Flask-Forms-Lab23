from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)



facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]

accounts = {"siwarha":"123", "rut":"456", "tamar":"789"}

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_check = request.form['username']
        pass_check = request.form['password']
        for key, value in accounts.items():
            if key == user_check and value == pass_check:
                return redirect(url_for('home'))
        return render_template('login.html')

  
@app.route('/home', methods=['GET', 'POST'])  
def home():
	return render_template('home.html', facebook_friends=facebook_friends)


def all_lower(my_list):
    return [i.lower() for i in my_list]


@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])  
def friend_exists(name):
	check = False
	lower_list = all_lower(facebook_friends)
	if name.lower() in lower_list:
		check = True
	return render_template('friend_exists.html', is_in = check, name_pass = name)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
