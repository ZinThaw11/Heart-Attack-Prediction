import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('heart.csv')
with st.form("my_form1"):
        
         st.title('Heart Attack Prediction')       
         st.subheader("Please fill the Patient Circustances")
         
         age = st.slider("What's is your age", 0,101,25)
         sex = st.radio("What's your gender:", ['Male', 'Female'])
         cp  = st.radio("What's your Chest Pain Level:", ['0','1','2','3'])
         trestbps = st.slider("Resting Blood Pressure", 80,200,25)
         chol = st.slider("Cholestoral",100,800,25)
         fbs = st.selectbox("fasting blood sugar > 120 mg/dl:", ('Yes','No'))
         restecg = st.radio("What's your Resting Electrocardiographic Results:", ['No abnormalities','Minor','Major'])
         thalach = st.number_input("maximum heart rate achieved", value=None, placeholder="Type a number...")
         exang = st.selectbox("Exercise Induced Angina", ('Yes','No'))
         oldpeak = st.slider("Oldpeak:",0.0,10.0,2.5)
         slope = st.radio("The slope of the peak exercise ST segment",['Upsloping','Flat','Downsloping'])
         ca = st.radio("Number of major vessels",['0','1','2','3','4'])
         thal = st.slider("Thallium stress test result",0,10,3)

         submitted = st.form_submit_button("Submit")

         if submitted:
                 inputdata = {'age':age, 
                          'sex':sex, 
                          'cp':cp, 
                          'trestbps':trestbps, 
                          'chol':chol,
                          'fbs':fbs, 
                          'restecg':restecg,
                          'thalach':thalach, 
                          'exang':exang, 
                          'oldpeak':oldpeak, 
                          'slope':slope, 
                          'ca':ca,
                          'thal':thal}
                 features = pd.DataFrame(inputdata, index=[0])
                 features
                 features_dummy = pd.get_dummies(features)

                 x = df[['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach',
                         'exang', 'oldpeak', 'slope', 'ca', 'thal']]
                 y = df['target']

                 X_train, X_test, y_train, y_test = train_test_split(x,y,test_size=0.2, random_state=25)

                 model = "nb_model"
                 load_model = pickle.load(open(model, "rb"))
                 testsdata1 = pd.get_dummies(features)
                 testsdata2 = testsdata1.reindex(columns = X_train.columns.values, fill_value=0)

                 clfres = load_model.predict(testsdata2)
                 if clfres == 1:
                     st.error('You have a chance of heart attaack!', icon="🚨")
                 else:
                     st.success("You do not have a chance of heart attack!", icon="✅")
