import streamlit as st
import cv2



#pencil sktech 




def main():
	st.title(" Our Instagram Filter App")
	st.write(" Select an Filter from available options") 
	file_image = st.sidebar.file_uploader("Upload your Image to Apply Filter", type=['jpeg','jpg','png'])
	option= st.sidebar.selectbox('Pick any of available filter option',('pencilsketch','pencilsketch'))
	if file_image is None:
		st.write("You have not uploaded any image")
	
if __name__== '__main__':
	main()