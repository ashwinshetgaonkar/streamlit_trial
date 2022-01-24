import streamlit as st
import pandas as pd

st.markdown('''# **Hello World😍😎!**
---
This is my first streamlit app.
## Things learned
1.use of markdown

2.use of #

3.use of tripple quotes

4.use of **

### **blah**,*blah*,***blah***
---''')
st.header("Data")
df=pd.read_csv('advertising.csv')
df

# import numpy as np
# st.header("Plot")
# df2 = pd.DataFrame(
#      np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#      columns=['lat', 'lon'])

# st.map(df2)

st.markdown("---")
number = int(st.number_input('Enter your aga'))
st.write('The current number is ', number)

st.markdown("---")

title = st.text_input('Enter your name:', )
st.write('Your name is', title)

st.markdown("---")
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
st.sidebar.header('File uploader')
# uploaded_file = st.file_uploader("Choose a file")
uploaded_file = st.sidebar.file_uploader("Choose a file")
if uploaded_file is not None:
     # # To read file as bytes:
     # bytes_data = uploaded_file.getvalue()
     # st.write(bytes_data)

     # To convert to a string based IO:
     # stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
     # st.write(stringio)

     # To read file as string:
     # string_data = stringio.read()
     # st.write(string_data)


     # st.write(plt.imshow(stringio))
     # Can be used wherever a "file-like" object is accepted:
     # dataframe = pd.read_csv(uploaded_file)
     # st.write(dataframe.head())

     # if image is uploaded
     # img=mpimg.imread(uploaded_file)
     # plt.figure(figsize=(5,5))
     st.image(uploaded_file)
# video
# video_file = open('myvideo.mp4', 'rb')
# video_bytes = video_file.read()

st.video('https://www.youtube.com/watch?v=cuoPma70qac&t=991s',start_time=60)