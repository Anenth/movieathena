from flask import Flask, render_template , request
 
app = Flask(__name__)      
 
####
##### App structure
####

@app.route('/')
def landingPage():
    return render_template('landingPage.html')

@app.route('/user/<username>')
def show_user_profile(username=None):
    # show the user profile for that user
    return render_template('user.html',username=username)

@app.route('/<moviename>')
def show_movie(moviename):
    return 'Movie %s' % moviename

@app.route('/<moviename>/about')
def show_movie_about(moviename):
    return 'Movie %s analytics, cast and other details' % moviename

@app.route('/browse')
def browse_movies():
    return ' Browse movies'

@app.route('/browse/<category>')
def browse_movies_category(category):
    return ' Browse %s movies here' % category
 

####
##### Form submit urls
####

@app.route('/login')
def login():
	username = request.args['email']
	password = request.args['password']
	return 'Login succesfull %s %s',username,password

@app.route('/signup')
def sign_up():
    return 'Signup succesfully proceed to login'

####
##### Error handlers
####

@app.errorhandler(404)
def not_found(error):
    return "Better luck next time :P", 404


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=8123)