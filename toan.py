import pandas as pd 
import numpy as np 
import pickle 
import streamlit as st 
from PIL import Image 





def welcome(): 
	return 'welcome all'

# defining the function which will make the prediction using 
# the data which the user inputs 
def prediction(Type, Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Target, Diff_temperature,classifier): 

	prediction = classifier.predict( 
		[[Type, Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Target, Diff_temperature]]) 
	if prediction==1:
		prediction= 'No failure'
	elif prediction==2:
		prediction= 'Power Failure'
	elif prediction==3:
		prediction= 'Tool Wear Failure'
	elif prediction==4:
		prediction= 'Overstrain Failure'
	elif prediction==5:
		prediction= 'Random Failures'
	elif prediction==6:
		prediction= 'Heat Dissipation Failure'
	print(prediction) 
	return prediction 
	

# this is the main function in which we define our webpage 
def main(): 
	# giving the webpage a title 
	st.title("ĐỒ ÁN THIẾT KẾ") 
	
	# here we define some of the front end elements of the web page like 
	# the font and background color, the padding and the text to be displayed 
	html_temp = """
	<div style="background-color:yellow;padding:13px">
    	<h1 style="color:black;text-align:center;">Predictive Maintenance</h1>
	</div>

	"""
	
	# this line allows us to display the front end aspects we have 
	# defined in the above code 
	st.markdown(html_temp, unsafe_allow_html = True) 
	
	image = Image.open("Image_Failure/AI-Driven-Predictive-Maintenance-for-Induction-Motors.webp")
	
	
	status = st.radio("Select Model: ", ('Decision Tree', 'KNN'))
	if status == 'Decision Tree':
		pickle_in = open('classifier.pkl', 'rb') 
		classifier = pickle.load(pickle_in) 
		st.success("Decision Tree Mode")
	elif status == 'KNN':
		pickle_in = open('classifier1.pkl', 'rb') 
		classifier = pickle.load(pickle_in) 
		st.success("KNN Mode")

	# the following lines create text boxes in which the user can enter 
	# the data required to make the prediction 
	Type = st.number_input("Type") 
	Air_temperature = st.number_input("Air_temperature") 
	Process_temperature = st.number_input("Process_temperature") 
	Rotational_speed = st.number_input("Rotational_speed") 
	Torque = st.number_input("Torque") 
	Tool_wear = st.number_input("Tool_wear") 
	Target = st.number_input("Target") 
	Diff_temperature = st.number_input("Diff_temperature") 

	result ="" 
	
	# the below line ensures that when the button called 'Predict' is clicked, 
	# the prediction function defined above is called to make the prediction 
	# and store it in the variable result 
	if st.button("Start Predict"): 
		result = prediction(Type, Air_temperature, Process_temperature, Rotational_speed, Torque, Target,Tool_wear, Diff_temperature,classifier) 
	st.success('The output is {}'.format(result)) 
	


	
if __name__=='__main__': 
	main() 
