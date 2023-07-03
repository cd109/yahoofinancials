import streamlit as st
import cv2
from PIL import Image
import numpy as np
def dodgeV2(x,y):
    return cv2.divide(x,255-y,scale=256)

def pencilsketch(input_image):
    # Convert out input image from BGR to Gray 
    gray_image=cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)
    # INVERT our gray image 255 - gray_image
    invert_image=cv2.bitwise_not(gray_image)
    # Blur the image using a Gaussian function , Kernal (21,21) 
    blur_image=cv2.GaussianBlur(invert_image, (21,21),sigmaX=0,sigmaY=0)
    # Dodge Division 
    pencilsketch_image=dodgeV2(gray_image,blur_image)
    return pencilsketch_image

    

def main():
	st.title(" Our Instagram Filter App")
	st.write(" Select an Filter from available options") 
	file_image = st.sidebar.file_uploader("Upload your Image to Apply Filter", type=['jpeg','jpg','png'])
	option= st.sidebar.selectbox('Pick any of available filter option',('pencilsketch','brannan'))
	if file_image is None:
		st.write("You have not uploaded any image")
	else:
		if option == "pencilsketch":
			input_img = Image.open(file_image)
			final_sketch = pencilsketch(np.array(input_img))
			st.write("**Input Photo**")
			st.image(input_img, use_column_width=True)
			st.write("**Output Pencil Sketch**")
			st.image(final_sketch, use_column_width=True)
			result = Image.fromarray(final_sketch)
 
if __name__== '__main__':
	main()