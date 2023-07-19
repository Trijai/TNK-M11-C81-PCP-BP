from flask import Flask, render_template, request, redirect
import os

STATIC_DIR = os.path.abspath('static')

app = Flask(__name__, static_folder=STATIC_DIR)
app.use_static_for_root = True

blockData={}

@app.route("/", methods= ["GET", "POST"])
def home():
     return render_template('signup.html')
    
# Create a route '/signup' with methods GET and POST   

# Define signup function

    # Access global blockData
    
    # Check if request method is POST
    
        # Get username, email, password from the signup form in the respective variables
        
        # Create a new block with username, email and password 
        
        
        # Use return redirect('/signin') to load signin route
        
    
    # if not POST request the signup page
    

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    global blockData
    
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
      
        # Check if blockData's username and password is same as variable username and password
        
                    # return the profile.html and variable block containing blockData
                    

        return "Invalid credentials!"

    return render_template('signin.html')

    
if __name__ == '__main__':
    app.run(debug = True, port=4000)



