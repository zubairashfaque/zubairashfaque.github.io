import streamlit as st
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import base64
import os
from bokeh.models.widgets import Div


# Set page configurations
#st.set_page_config(page_title="Zubair Ashfaque's Portfolio", page_icon="🧑‍🔬", layout="wide")
# Set page configurations
st.set_page_config(
    page_title="Zubair Ashfaque's Portfolio",
    page_icon="🧑‍🔬",
    layout="wide",
    initial_sidebar_state="auto"
)
with open("style.css") as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html=True)

#####################
#####################
# Navigation

st.markdown(
    '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
    unsafe_allow_html=True)

st.markdown("""
<nav class="navbar fixed-top navbar-expand-lg navbar-dark" style="background-color: #000000;">
  <a class="navbar-brand" href="#personal-details" target="_blank"> 
  <span class="green">Zubair</span> 
  <span class="white">Ashfaque</span> 
  </a>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
    <ul class="navbar-nav">
      <li class="nav-item active">
        <a class="nav-link disabled" href="#PERSONAL-DETAILS">Home <span class="sr-only">(current)</span></a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#education-certificate">Education & Certificate</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#work-experience">Work Experience</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#skills">Skills</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#my-projects">My Projects</a>
      </li>
      <li class="nav-item">
        <a class="nav-link" href="#social-media">Social Media</a>
      </li>
    </ul>
  </div>
</nav>
""", unsafe_allow_html=True)


# Header
# ---- LOAD ASSETS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")
with st.container():
    left_column, right_column = st.columns([3, 1])
    with left_column:
        st.markdown(
            "<p style='font-size:25px; color: #0A0A0A; text-align: left; margin:0;padding:0;line-height: .75em;text-align: left'>I am</p> ",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:50px; color: #72ab00; text-align: left;margin:0;padding:0;line-height: 1.25em;text-align: left '>Zubair Ashfaque</p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;text-align: left;padding-bottom: 15px;'>Data Scientist | Machine Learning</p>",
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:15px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;text-align: left '>Certified TensorFlow developer and Google data analyst with 12 years of experience leading cross-functional teams to ensure accuracy and integrity around data and insights in a variety of industries. Highly skilled in predictive modeling, machine learning, deep learning, and data visualization.</p>",
            unsafe_allow_html=True)

        m = st.markdown("""
        <style>
        div.stButton > button:first-child {
            background-color: #ffffff;
            color:#0A0A0A;
        }
        div.stButton > button:hover {
            background-color: #72ab00;
            color:#0A0A0A;
            border-color: #72ab00;

        div.stButton > button:visited  {
            background-color: #72ab00;
            color:#0A0A0A;
            border-color: #72ab00;
            }

        div.stButton > button:focus  {
            background-color: #72ab00;
            color:#0A0A0A;
            border-color: #72ab00;
            }        
        </style>""", unsafe_allow_html=True)
        with open("data/ZA_Resume.pdf", "rb") as file:

            btn = st.download_button(
                label="RESUME",
                data=file,
                file_name="dowloaded.pdf",
                mime="application/octet-stream"
            )
        if st.button('My Projects'):
            js = "window.location.href = '#my-projects'"
            html = '<img src onerror="{}">'.format(js)
            div = Div(text=html)
            st.bokeh_chart(div)
    with right_column:
        image = Image.open('images/Zubi_2.png')
        st.image(image, width=250)

st.write("---")

st.markdown('## PERSONAL DETAILS', unsafe_allow_html=True)
st.success('''
A few interesting things about me. I am also an avid gamer. I love to play competitive strategy games and first-person shooters. Lastly, I love learning. Every day I push myself to learn something new, whether that be about machine learning, software engineering, or about anything.
''')
st.write("---")
# ---- HEADER SECTION ----
# CLOUD = Image.open("images/cloud.jpg")
# NLP = Image.open("images/nlp_2.jpg")
NLP = ("images/nlp_2.jpg")
CLOUD = ("images/cloud.jpg")
ML = ("images/ml.jpg")
analysis = ("images/analytics.png")
parallel = ("images/parallel.png")
statistics = ("images/statistics.jpg")
mlops = ("images/mlops-og.png")

with st.container():
    st.title("Areas of Interest")
    st.markdown(
        "<p style='font-size:25px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>Take a look at some of the things I love working on.</p>",
        unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #5D6D7E !important;
                text-align: center
            }
            .logo-img1 {
                display: block;
                float:center;
                margin-left: auto;
                margin-right: auto;
                width: 100px;
            }
            </style>
            """,
            unsafe_allow_html=True)
        st.markdown(
            f"""<img class="logo-img1" src="data:image/png;base64,{base64.b64encode(open(analysis, "rb").read()).decode()}"> <p class="logo-text">Data Analytics</p> """,
            unsafe_allow_html=True)

        # st.image(CLOUD, width =100)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I love telling a story. Getting to the heart of a problem and coming up with a solution.</p>",
            unsafe_allow_html=True)
        # st.image(CLOUD, width =100)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #5D6D7E !important;
                text-align: center
            }
            .logo-img1 {
                display: block;
                float:center;
                margin-left: auto;
                margin-right: auto;
                width: 100px;
            }
            </style>
            """,
            unsafe_allow_html=True)
        st.markdown(
            f"""<img class="logo-img3" src="data:image/png;base64,{base64.b64encode(open(NLP, "rb").read()).decode()}"> <p class="logo-text">NLP</p> """,
            unsafe_allow_html=True)
        # st.image(NLP, width =200)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I love to do text analytics to some of the hardest questions in business.</p>",
            unsafe_allow_html=True)
    with col2:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #0A0A0A !important;
                text-align: center
            }
            .logo-img2 {
                display: block;
                float:center;
                margin-left: auto;
                margin-right: auto;
                width: 150px;
            }
            </style>
            """,
            unsafe_allow_html=True)
        st.markdown(
            f"""<img class="logo-img2" src="data:image/png;base64,{base64.b64encode(open(ML, "rb").read()).decode()}"> <p class="logo-text">Machine Learning</p> """,
            unsafe_allow_html=True)
        # st.image(NLP, width =200)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I am passionate about learning the theory that is pushing the cutting edge of ML.</p>",
            unsafe_allow_html=True)
        # st.image(CLOUD, width =100)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I am passionate about learning the theory that is pushing the cutting edge of ML.</p>", unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #0A0A0A !important;
                text-align: center
            }
            .logo-img4 {
                display: block;
                float:center;
                margin-left: auto;
                margin-right: auto;
                width: 110px;
            }
            </style>
            """,
            unsafe_allow_html=True)
        st.markdown(
            f"""<img class="logo-img1" src="data:image/png;base64,{base64.b64encode(open(CLOUD, "rb").read()).decode()}"> <p class="logo-text">CLOUD</p> """,
            unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I utilize AWS & GCP to develop and productionize machine learning systems.</p>",
            unsafe_allow_html=True)
    with col3:
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #0A0A0A !important;
                text-align: center
            }
            .logo-img5 {
                display: block;
                float:center;
                margin-left: auto;
                margin-right: auto;
                width: 250px;
            }
            </style>
            """,
            unsafe_allow_html=True)
        st.markdown(
            f"""<img class="logo-img5" src="data:image/png;base64,{base64.b64encode(open(mlops, "rb").read()).decode()}"> <p class="logo-text">MLOps</p> """,
            unsafe_allow_html=True)
        # st.image(NLP, width =200)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I have in-depth knowledge of MLOps (machine learning operations) and love to learn about more it.</p>",
            unsafe_allow_html=True)
        st.markdown(
            """
            <style>
            .logo-text {
                font-weight:25 !important;
                font-size:25px !important;
                color: #0A0A0A !important;
                text-align: center
            }
            .logo-img3 {
                display: block;
                float:center;
                margin-left: auto;
                margin-right: auto;
                width: 120px;
            }
            </style>
            """,
            unsafe_allow_html=True)
        #st.markdown(
         #   f"""<img class="logo-img3" src="data:image/png;base64,{base64.b64encode(open(statistics, "rb").read()).decode()}"> <p class="logo-text">STATS</p> """,
         #   unsafe_allow_html=True)
        # st.image(NLP, width =200)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
        #st.markdown(
        #   "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I Love to Learn Stats.</p>",
        #   unsafe_allow_html=True)

        # st.image(CLOUD, width =100)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>CLOUD</p>", unsafe_allow_html=True)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>I am passionate about learning the theory that is pushing the cutting edge of ML.</p>", unsafe_allow_html=True)
        st.markdown(
            f"""<img class="logo-img4" src="data:image/png;base64,{base64.b64encode(open(parallel, "rb").read()).decode()}"> <p class="logo-text">Parallel Computing</p> """,
            unsafe_allow_html=True)
        # st.image(NLP, width =200)
        # st.markdown("<p style='font-size:25px; color: #5D6D7E; text-align: left;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>NLP</p>", unsafe_allow_html=True)
        st.markdown(
            "<p style='font-size:20px; color: #5D6D7E; text-align: center;margin:0;padding:2;line-height: 1.25em;padding-bottom: 15px;'>HIVE, Hadoop,PySpark and Databriks</p>",
            unsafe_allow_html=True)


#####################
# Custom function for printing text
def txt(a, b):
    col1, col2 = st.columns([4, 1])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt2(a, b):
    col1, col2 = st.columns([1, 4])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)


def txt3(a, b):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.markdown(a)
    with col2:
        st.markdown(b)


def txt4(a, b, c):
    col1, col2, col3 = st.columns([1.5, 2, 2])
    with col1:
        st.markdown(f'`{a}`')
    with col2:
        st.markdown(b)
    with col3:
        st.markdown(c)


#####################
st.write("---")

st.markdown('''
## Education & Certificate
''')

txt('**Bachelor in Telecom Systems** , *Beaconhouse National University*, Pakistan',
    '2005 – 2009')
txt('**TensorFlow Developer** , *Tensorflow.org*',
    '2020 – 2023')
txt('**Google Data Analytics** , *https://grow.google/certificates/data-analytics*',
    'Present')
txt('**Machine Learning Engineering for Production (MLOps) Specialization** , *Coursera – deeplearning.ai*',
    'Present')
txt('**TensorFlow: Advanced Techniques** , *Coursera – deeplearning.ai*',
    'Present')
txt('**IBM Data Science** , *Coursera – IBM*',
    'Present')
txt('**Deep Learning Specialization** , *Coursera – deeplearning.ai*',
    'Present')
txt('**Machine Learning on Google Cloud** , *Coursera – Google*',
    'Present')
txt('**Practical Machine Learning on H2O** , *Coursera – H2O.ai*',
    'Present')
#####################
st.write("---")

st.markdown('''
## Work Experience
''')

txt('**Freelance Data Scientist**',
    '2019 – present')
st.markdown('''
- Coordinating our work with the work of the 20-person UK team with GIT.
- In 2020, we developed a probabilistic model of disease progression when we got the news about COVID-19.
- Meeting with stakeholders to present analysis and understand business requirements.
- Take ownership of projects and build proofs-of-concept (POCs) that can demonstrate utilization, value, and lead to scalable solutions.
- Analysed the data with SciPy and Pandas and presented it using Matplotlib.
''')

txt('**System Analyst**, VEON',
    '2017 – present')
st.markdown('''
**Summary**: Responsible for leading & executing advanced analytics & data science initiatives for the revenue assurance in the organization. Worked with key stakeholders to scope, develop, & present ML models.
- Designed and implemented a machine learning system that predicts grey traffic with `83%` `accuracy`.
- Perform revenue controls and a variety of statistical analyses using `Microsoft excel`, `python`, and `SQL`.
- Developed early iteration of ETL pipelines using RAID (WEDO) and Python (including `SQLAlchemy`, `paramiko`, `Dask`, `Hadoop`, `Hive`) with logging, data cataloging, & job status tracking for processing `1M+` text and binary files.
- Designed data models & schema, created DDL & DML scripts for Oracle RDBMS Database.
''')

txt('**Enterprise Application Integration Planning**, VEON',
    '2012 – 2017')
st.markdown('''
**Summary**: Responsible for leading & assist in the development of technology roadmaps to evolve the API estate in conjunction with internal and external TELCO solution providers
- API tester with full system development lifecycle experience, including designing, developing, and implementing test plans, test cases, and test processes fueling swift corrective actions, significant cost savings, and fault-free audits.
- Hands-on technology professional accustomed to working in complex, project-based environments. Multifaceted experience in QA software testing, software development, and user-acceptance testing.
- Review requirements, specifications, and technical design documents to provide timely and meaningful feedback.
- Create detailed, comprehensive, and well-structured test plans and test cases.
- Estimate, prioritize, plan and coordinate testing activities.
- Design, develop, and execute automation scripts using open source tools.
- Identify, record, document thoroughly, and track bugs
- Perform thorough regression testing when bugs are resolved.
- Develop and apply testing processes for new and existing products to meet client needs.
- Investigate the causes of non-conforming software and train users to implement solutions.
''')

#####################
st.write("---")

st.markdown('''
## Skills
''')
txt3('Programming', '`Python` [`scikit-learn`, `pandas`, `NumPy`, `genism`, `spacy`, `PySpark`], `SQL` [`Postgres`, `MySQL`, `Oracle`]')
txt3('Data visualization', '`matplotlib`, `seaborn`, `Tabluea`, `Facets`')
txt3('Machine Learning', '`scikit-learn`, `RapidMiner`, `H2O [AutoML, ML models]`, `MLFlow`')
txt3('Deep Learning', '`TensorFlow`, `Keras`' )
txt3('Model deployment', '`streamlit`, `Flask`, `Jenkins`, `FastAPI`, `Docker`, `Kubernetes`, `Docker`')
txt3('Deep Learning', '`TensorFlow`, `Keras`' )
txt3('Cloud', '`AWS`, `GCP`' )

#####################
st.markdown('''
## Social Media
''')
txt2('LinkedIn', 'https://www.linkedin.com/in/zubair-ashfaque-ab100621/')
txt2('Twitter', 'https://twitter.com/zubairashfaque')
txt2('GitHub', 'https://github.com/zubairashfaque/')


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_cmaqoazd.json")
img_contact_form = Image.open("images/yt_contact_form.png")
img_lottie_animation = Image.open("images/yt_lottie_animation.png")

# ---- PROJECTS ----
with st.container():
    st.write("---")
    st.markdown('''
    ## My Projects
    ''')
    #st.header("My Projects")
     # Add your NLP Sentiment Analysis project here
    st.header("NLP - Sentiment Analysis With Naive Bayes")
    
    # Provide project details
    st.write("This project involved performing sentiment analysis on a dataset of text data to determine the sentiment (positive, negative, or neutral) of each piece of text. This project uses the Naïve Bayes algorithm to classify the sentiment of input text and displays the results using a user-friendly Streamlit app.")
    
    # Add clickable links to the captions
    github_link = "https://github.com/zubairashfaque/Sentiment-Analysis-with-Naive-Bayes-Streamlit"
    medium_link = "https://medium.com/p/a31021764fb4"
    streamlit_link = "https://rtadeployment-za.streamlit.app/"
    st.markdown(f"[GitHub Repository]({github_link}) | [Medium Project Blog]({medium_link}) | [Deployed Application Link]({streamlit_link})")

     # Add your NLP Sentiment Analysis project here
    st.header("Imbalanced Datasets - Road Accident Severity Misclassification Problem")
    
    # Provide project details
# Provide project details
    st.write("I addressed the challenge of imbalanced data in the 'Road Accident Severity Misclassification Problem' by employing oversampling, undersampling, and a hybrid approach to balance the dataset. These techniques involved the generation of synthetic data for the minority class while reducing the dominance of the majority class.")
    st.write("Once the dataset was balanced, I applied various machine learning models, including Decision Tree, Random Forest, Gradient Boosting Machine (GBM), AdaBoost, Gradient Tree Boosting (GTB), Extra Trees, XGBoost, LightGBM, CatBoost, and HistGradientBoosting. These models were employed to tackle the task of accident severity classification while considering the dataset's inherent imbalance. The primary objective was to determine the most suitable model and data sampling strategies for training an effective predictive model, ultimately leading to successful deployment.")

    # Add clickable links to the captions
    github_link = "https://github.com/zubairashfaque/Sentiment-Analysis-with-Naive-Bayes-Streamlit"
    medium_link = "https://medium.com/p/a31021764fb4"
    streamlit_link = "https://rtadeployment-za.streamlit.app/"
    st.markdown(f"[GitHub Repository]({github_link}) | [Medium Project Blog]({medium_link}) | [Deployed Application Link]({streamlit_link})")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I'm a freelance Data Scientist & Machine learning specialist with twelve years of experience developing data science products and predictive models for clients from all over the world, working with startups and individuals from industries like healthcare, retail, and telecommunication.

My main area of expertise is deep learning, and MLOps. I have experience with the complete machine learning workflow, from the project conception (including asking the question: is machine learning is the best solution?) to model deployment in production, passing through the data collection process, implementation of experimental and state-of-the-art architectures, and error analysis and optimization.

I prefer to work on long-term and hourly projects, but I'm open to working on exciting projects of all sizes.
            """
        )
    with right_column:
        st_lottie(lottie_coding, height=400, key="coding")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/mianashfaque@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()

