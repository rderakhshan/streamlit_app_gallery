import streamlit as st
from streamlit_option_menu import option_menu
import streamlit.components.v1 as html
from  PIL import Image
import streamlit as st
import numpy as np
import cv2
from  PIL import ImageChops
import pandas as pd
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import numpy as np
import plotly.express as px
from  PIL import Image
import io 



st.set_page_config(page_title="Sharone's Streamlit App Gallary", page_icon="", layout="wide")

sysmenu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(sysmenu,unsafe_allow_html=True)

#Add a logo (optional) in the sidebar
logo = Image.open(r'C:\Users\13525\Desktop\Insights_Bees_logo.png')
profile = Image.open(r'C:\Users\13525\Desktop\medium_profile.png')
#st.sidebar.image(logo, width=130 )
with st.sidebar:
    
    choose = option_menu("App Gallary", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )
    

# choose = option_menu("App Gallary", ["About", "Photo Editing", "Project Planning", "Python e-Course", "Contact"],
#                         icons=['house', 'camera fill', 'kanban', 'book','person lines fill'],
#                         menu_icon="app-indicator", default_index=0,
#                         styles={
#     "container": {"padding": "3!important", "background-color": "#fafafa"},
#     "icon": {"color": "orange", "font-size": "20px"}, 
#     "nav-link": {"font-size": "12px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
#     "nav-link-selected": {"background-color": "#0d0000"},
# },
# orientation='horizontal'
# )


with st.sidebar.form(key='columns_in_form1',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
    st.write('<style>div.row-widget.stRadio > div{flex-direction:row;} </style>', unsafe_allow_html=True) #Make horizontal radio buttons
    rating=st.radio("Please rate the app",('1','2','3','4','5'),index=4)    #Use radio buttons for ratings
    #text=st.text_input(label='Please leave your feedback here') #Collect user feedback
    submitted = st.form_submit_button('Submit')





#st.sidebar.image(logo,  width=120)

if choose == "About":
#Add the cover image for the cover page. Used a little trick to center the image
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">About the Author</p>', unsafe_allow_html=True)
        
    with col2:               # To display brand logo
        
        st.image(logo, width=130 )
    st.write("Sharone Li is a data science practitioner, enthusiast and blogger. She writes data science articles and tutorials about Python, data visualization, Streamlit, etc. She is also an amatuer violinist who loves classical music.\n\nTo know more about Sharone, pelase visit her Medium blog site at: https://medium.com/@insightsbees")    
    st.image(profile, width=700 )




    

elif choose == "Photo Editing":
    #Create two columns with different width
    col1, col2 = st.columns( [0.8, 0.2])
    with col1:               # To display the header text using css style
        st.markdown(""" <style> .font {
        font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
        st.markdown('<p class="font">Upload your photo here...</p>', unsafe_allow_html=True)
        
    with col2:               # To display brand logo
        st.image(logo,  width=150)
    #Add file uploader to allow users to upload photos
    uploaded_file = st.file_uploader("", type=['jpg','png','jpeg'])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        
        col1, col2 = st.columns( [0.5, 0.5])
        with col1:
            st.markdown('<p style="text-align: center;">Before</p>',unsafe_allow_html=True)
            st.image(image,width=300)  

        with col2:
            st.markdown('<p style="text-align: center;">After</p>',unsafe_allow_html=True)

            converted_img = np.array(image.convert('RGB')) 
            gray_scale = cv2.cvtColor(converted_img, cv2.COLOR_RGB2GRAY)
            inv_gray = 255 - gray_scale
            slider = st.sidebar.slider('Adjust the intensity', 25, 255, 125, step=2)
            blur_image = cv2.GaussianBlur(inv_gray, (slider,slider), 0, 0)
            sketch = cv2.divide(gray_scale, 255 - blur_image, scale=256)
            st.image(sketch, width=300)

# elif choose == "Data Profiling":
#     # Streamlit book properties
#     #Add an app title. Use css to style the title
#     st.markdown(""" <style> .font {                                          
#         font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
#         </style> """, unsafe_allow_html=True)
#     st.markdown('<p class="font">Import your data and generate a Pandas data profiling report easily...</p>', unsafe_allow_html=True)


#     uploaded_file = st.file_uploader("Upload your csv file:", type=['csv'])
#     if uploaded_file is not None:
#         df=pd.read_csv(uploaded_file)
#         st.write(df.head())
        
#         if st.button('Generate Report'):
            
#             profile=ProfileReport(df,
#                 minimal=True,
#                 title="User uploaded table",
#                 progress_bar=True,
#                 dataset={
#                     "description": 'This profiling report was generated by Insights Bees',
#                     "copyright_holder": 'Insights Bees',
#                     "copyright_year": '2022'
#                 }) 

#             st_profile_report(profile)

elif choose == "Project Planning":
#Add a file uploader to allow users to upload their project plan file
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Upload your project plan</p>', unsafe_allow_html=True)

    uploaded_file = st.file_uploader("Fill out the project plan template and upload your file here. After you upload the file, you can edit your project plan within the app.", type=['csv'], key="2")
    if uploaded_file is not None:
        Tasks=pd.read_csv(uploaded_file)
        Tasks['Start'] = Tasks['Start'].astype('datetime64')
        Tasks['Finish'] = Tasks['Finish'].astype('datetime64')
        
        grid_response = AgGrid(
            Tasks,
            editable=True, 
            height=300, 
            width='100%',
            )

        updated = grid_response['data']
        df = pd.DataFrame(updated) 
        
        if st.button('Generate Gantt Chart'): 
            fig = px.timeline(
                            df, 
                            x_start="Start", 
                            x_end="Finish", 
                            y="Task",
                            color='Completion Pct',
                            hover_name="Task Description"
                            )

            fig.update_yaxes(autorange="reversed")          #if not specified as 'reversed', the tasks will be listed from bottom up       
            
            fig.update_layout(
                            title='Project Plan Gantt Chart',
                            hoverlabel_bgcolor='#DAEEED',   #Change the hover tooltip background color to a universal light blue color. If not specified, the background color will vary by team or completion pct, depending on what view the user chooses
                            bargap=0.2,
                            height=600,              
                            xaxis_title="", 
                            yaxis_title="",                   
                            title_x=0.5,                    #Make title centered                     
                            xaxis=dict(
                                    tickfont_size=15,
                                    tickangle = 0,
                                    rangeslider_visible=True,
                                    side ="top",            #Place the tick labels on the top of the chart
                                    showgrid = True,
                                    zeroline = True,
                                    showline = True,
                                    showticklabels = True,
                                    tickformat="%x\n",      #Display the tick labels in certain format. To learn more about different formats, visit: https://github.com/d3/d3-format/blob/main/README.md#locale_format
                                    )
                        )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.write('---') 
   
    else:
        st.warning('You need to upload a csv file.')

elif choose == "Python e-Course":

    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Learn Python for Data Science</p>', unsafe_allow_html=True)

    st.subheader('Import Data into Python')
    st.markdown('To start a data science project in Python, you will need to first import your data into a Pandas data frame. Often times we have our raw data stored in a local folder in csv format. Therefore let\'s learn how to use Pandas\' read_csv method to read our sample data into Python.\n\n Below is the code to import the data into Python. Notice that in line 2, we use pd.read_csv() method by specifying the file path within the brackets to import the csv data into Python and store it in a Pandas data frame. We name this pandas data frame as df.\n\n You will notice that we also put \'r\' before the file path. This is because the path contains backslashes and they are treated as an escape character. So if you have, say, \\t in a filename Windows will treat that as a tab character instead of a path separator. An alternative way is to specify file paths with forward slashes.')

    #Display the first code snippet
    code = '''import pandas as pd #import the pandas library\ndf=pd.read_csv(r'C:\\Users\\13525\\Desktop\\ecourse_app\\ecourse_streamlit\\data.csv') #read the csv file into pandas\ndf.head() #display the first 5 rows of the data'''
    st.code(code, language='python')

    #Allow users to check the results of the first code snippet by clicking the 'Check Results' button
    df=pd.read_csv(r'C:\Users\13525\Desktop\ecourse_app\ecourse_streamlit\data.csv')
    df_head=df.head()
    if st.button('Check Results', key='1'):
        st.write(df_head)
    else:
        st.write('---')

    #Display the second code snippet
    code = '''df.tail() #display the last 5 rows of the data'''
    st.code(code, language='python')

    #Allow users to check the results of the second code snippet by clicking the 'Check Results' button
    df=pd.read_csv(r'C:\Users\13525\Desktop\sample_data.csv')
    df_tail=df.tail()
    if st.button('Check Results', key='2'):
        st.write(df_tail)
    else:
        st.write('---')     

    #Display the third code snippet
    st.write('   ')
    st.markdown('After we import the data into Python, we can use the following code to check the information about the data frame, such as number of rows and columns, data types for each column, etc.')
    code = '''df.info()''' 
    st.code(code, language='python')

    #Allow users to check the results of the third code snippet by clicking the 'Check Results' button
    import io 
    buffer = io.StringIO()
    df.info(buf=buffer)
    s = buffer.getvalue()
    if st.button('Check Results', key='3'):
        st.text(s)
    else:
        st.write('---')

elif choose == "Contact":
    st.markdown(""" <style> .font {
    font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Contact Form</p>', unsafe_allow_html=True)
    with st.form(key='columns_in_form2',clear_on_submit=True): #set clear_on_submit=True so that the form will be reset/cleared once it's submitted
        #st.write('Please help us improve!')
        Name=st.text_input(label='Please Enter Your Name') #Collect user feedback
        Email=st.text_input(label='Please Enter Email') #Collect user feedback
        Message=st.text_input(label='Please Enter Your Message') #Collect user feedback
        submitted = st.form_submit_button('Submit')
        if submitted:
            st.write('Thanks for your contacting us. We will respond to your questions or inquiries as soon as possible!')

