import streamlit as st
import pyrebase

# Firebase Related Code ----------

# Firebase Configuration Key
firebaseConfig = {
    'apiKey': "AIzaSyCQN5x-d2igUj7cIdZSY1zVUP1PuutvV7k",
    'authDomain': "cyber-mads.firebaseapp.com",
    'projectId': "cyber-mads",
    'storageBucket': "cyber-mads.appspot.com",
    'messagingSenderId': "358193935335",
    'databaseURL': "https://cyber-mads-default-rtdb.asia-southeast1.firebasedatabase.app/", 
    'appId': "1:358193935335:web:df3d1139f2aab3059d0342"
}

# Firebase Authentication
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

# Database
db = firebase.database()
storage = firebase.storage() 

# End of Firebase Related Code ---

def login_user(email, password):
    user = auth.sign_in_with_email_and_password(email,password)

def signup_user(name, username, password):
	email = username
	user = auth.create_user_with_email_and_password(email, password)
	st.success("Account Successfully created!")
	st.balloons()

def app():
	st.title("Welcome to C-IDS by Cyber MADS")

	html_template = """ 

	<h2 style="background-color: blue; color: white; font-family: 'Lucida Sans'; text-align: center;">American Express CodeStreet 2021 submission by Manas | Ankita | Devika | Sayon </h2>

	"""

	st.markdown(html_template, unsafe_allow_html=True) 
	
	# ------------- Authentication ----------------
	login_or_signup = st.selectbox("Login or Sign Up", ("Select your preferrence", "Login", "Sign Up"))

	if login_or_signup == "Login":
		login = st.form("Login Form")
		email = login.text_input("Please enter your username/email ID")
		password = login.text_input('Password',  value = '', max_chars = None, key = None, type = 'password')
		submit = login.form_submit_button("Submit")
		if submit: 
			login_user(email, password)
			st.write("You have logged in Successfully!!!")
			st.balloons()

	elif login_or_signup == "Sign Up": 
		sign_up = st.form("Sign Up Form")
		name = sign_up.text_input("May we know your name?")
		age = sign_up.radio("Are you above 18 years of age?", ('Yes', 'No'))
		username = sign_up.text_input("Enter your username or email ID")
		password = sign_up.text_input('Password',  value = '', max_chars = None, key = None, type = 'password')
		confirm_password = sign_up.text_input('Re-enter your Password',  value = '', max_chars = None, key = None, type = 'password')
		if confirm_password == password and confirm_password != '': 
			st.write("You have been authenticated access to our platform. Welcome {}".format(username))
		submit = sign_up.form_submit_button("Create my account")
		if submit:
			signup_user(name, username, password)

	else: 
		logo = 'cyber-mads.jpg'
		st.image(logo, caption='Cyber MADS LOGO', width=None, use_column_width=True)

# -------- End of Authentication ---------
