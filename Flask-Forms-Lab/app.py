from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


username = "siwarha"
password = "123"
facebook_friends=["Loai","Kenda","Avigail", "George", "Fouad", "Gi"]
friend_exists = ''

@app.route('/', methods=['GET', 'POST'])  # '/' for the default page
def login():
	username = "siwarha"
	password = "123"
	if request.method == 'GET':  # Checking for get, if get means not the corect action, return login
		return render_template('login.html')
	else:  # If POST, continue
		user_check = request.form['username']
		pass_check = request.form['password']
		if user_check == username and pass_check == password:
			return render_template('home.html', username = "siwarha", password = "123")

  
@app.route('/home', methods=['GET', 'POST'])  
def home():
	return render_template('home.html', facebook_friends=facebook_friends)

@app.route('/friend_exists/<string:name>', methods=['GET', 'POST'])  
def friend_exists(name):
	check = False
	if name in facebook_friends:
		check = True
	return render_template('friend_exists.html', is_in = check, name_pass = name)


if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
    debug=True
	)
