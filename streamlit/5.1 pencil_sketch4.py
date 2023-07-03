import streamlit as st
import cv2
from PIL import Image
import numpy as np
from pilgram import css
from pilgram import util
import base64
from io import BytesIO
def dodgeV2(x,y):
    return cv2.divide(x,255-y,scale=256)

def get_image_download(img):
    """
    INPUT : PIL image 
    OUTPUT: html hyperlink 
    """
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode()
    href = f'<a href="data:file/jpg;base64,{img_str}">Download Your Filter Enabled Image </a>'
    return href 
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

def mayfair(im):
    """Applies Mayfair filter.
    Arguments:
        im: An input image.
    Returns:
        The output image.
    """

    cb = util.or_convert(im, 'RGB')
    size = cb.size
    pos = (.4, .4)

    cs1 = util.fill(size, [255, 255, 255, .8])
    cm1 = css.blending.overlay(cb, cs1)

    cs2 = util.fill(size, [255, 200, 200, .6])
    cm2 = css.blending.overlay(cb, cs2)

    cs3 = util.fill(size, [17, 17, 17])
    cm3 = css.blending.overlay(cb, cs3)

    mask1 = util.radial_gradient_mask(size, scale=.3, center=pos)
    cs = Image.composite(cm1, cm2, mask1)

    mask2 = util.radial_gradient_mask(size, length=.3, scale=.6, center=pos)
    cs = Image.composite(cs, cm3, mask2)
    cr = Image.blend(cb, cs, .4)  # opacity

    cr = css.contrast(cr, 1.1)
    cr = css.saturate(cr, 1.1)

    return cr

def brannan(im):
    """Applies Brannan filter.
    Arguments:
        im: An input image.
    Returns:
        The output image.
    """

    cb = util.or_convert(im, 'RGB')
    cs = util.fill(cb.size, [161, 44, 199, .31])
    cr = css.blending.lighten(cb, cs)

    cr = css.sepia(cr, .5)
    cr = css.contrast(cr, 1.4)

    return cr

def main():
	st.title(" Our Instagram Filter App")
	st.write(" Select an Filter from available options") 
	file_image = st.sidebar.file_uploader("Upload your Image to Apply Filter", type=['jpeg','jpg','png'])
	option= st.sidebar.selectbox('Pick any of available filter option',('pencilsketch','brannan','mayfair'))
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
			st.markdown(get_image_download(result), unsafe_allow_html=True)
		elif option == "brannan":
			input_img = Image.open(file_image)
			final_sketch = brannan(input_img)
			st.write("**Input Photo**")
			st.image(input_img, use_column_width=True)
			st.write("**Output Brannan**")
			st.image(final_sketch, use_column_width=True)
			result = Image.fromarray(np.array(final_sketch))
			st.markdown(get_image_download(result), unsafe_allow_html=True)
		elif option == "mayfair":
			input_img = Image.open(file_image)
			final_sketch = mayfair(input_img)
			st.write("**Input Photo**")
			st.image(input_img, use_column_width=True)
			st.write("**Output mayfair**")
			st.image(final_sketch, use_column_width=True)
			result = Image.fromarray(np.array(final_sketch)) 
			st.markdown(get_image_download(result), unsafe_allow_html=True)
if __name__== '__main__':
	main()