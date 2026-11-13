import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeClassifier
import random
import json

st.set_page_config(page_title="AI interview preparation", layout= "wide")
  # read question from file(json)
with open("questions.json", "r") as file:
    question_bank = {k.strip(): v for k, v in json.load(file).items()}


st.sidebar.title(" AI Interview Preparation 📝 ")
menu=st.sidebar.radio(
   "Navigation",
   [  
        "HOME",
        "STUDENT PROFILE",
        "SKILL ASSESMENT",
        "DASHBOARD",
        "AI ROADMAP",      
        "INTERVIEW QUESTIONS", 
        "PROGRESS TRACKER",
        "PLACEMENT PREPARATION"
    ] 

)  

menu= menu.strip()

if 'scores' not in st.session_state:
    st.session_state.scores={}

if 'student_name'not in st.session_state:
    st.session_state.student_name=""

if 'role'not in st.session_state:
    st.session_state.role=""
st.write(menu)
if menu== "HOME":
    
    st.title=("AI Interview prepration system")

    st.markdown("""
     ### Crack Technical Interviews with AI-powered Analysis

     Analyze your coding skills,detect weak areas,
    generate interview questions, and build a smart roadmap.

     """)

    col1,col2,col3= st.columns(3)

    col1.metric("Students Practicing"," 100+")
    col2.metric("Questions Available", "500+")
    col3.metric("Success Rate", "87%")

    st.divider()
    st.subheader("🎯 What This system Can Do")
    col1,col2 = st.columns(2)
    with col1:
     st.info(" 📊 Skill Assesment")
     st.info(" 📑 weak Topic Detection")
     st.info("📍  AI Learning Roadmap")



     with col2:
       st.info(" 📖 Interview Questions")
       st.info(" 📈 Progress Tracking")
       st.info(" 👨🏻‍💻  AI Readiness prediction")
     st.divider()
     st.success(" Start your prepration journey today")
    

elif menu=="STUDENT PROFILE":  
    st.title=(" 👩🏾‍🎓Student profile")
    name=st.text_input("Enter your name ")

    role=st.selectbox("Preferred Role",
                      [
                          "Frontend Developer",
                          "Backend Developer",
                          "Data Analyst",
                          "ML engineer"
                      ])
    
    degree=st.selectbox("Degree",[ "B.Tech", "BCA","MCA"," BSc(IT)","MSc( IT)", "M.Tech"])

    year=st.selectbox("Year",[ "1st year", "2nd year", "3rd year", " final year" ])
    if st.button("Save profile"):
       st.session_state.student_name=name
       st.session_state.role=role

       st.success("Profile saved succesfully")


elif menu == "SKILL ASSESMENT":
    st.title=("🧠 Skill Assesment")
    st.markdown("Rate yourself out of 100")

    arrays=st.slider("Array",0, 100, 50)
    linked_list=st.slider("Linked list", 0,100,50)
    stack=st.slider("Stack", 0, 100,50)
    queue=st.slider("Queue", 0,100,50)
    Dbms=st.slider("DBMS",0,100,50)
    Os=st.slider("OS",0,100,50)

    if st.button("Analyze Skills"):
        st.session_state.scores= {
            "Arrays": arrays,
            "Linked List":linked_list,
            "Stack":stack,
            "Queue": queue,
            "Dbms":Dbms,
            "OS":Os
        }
        st.success("Skill Analysisi completed")

elif menu=="DASHBOARD":
   st.title=("Dashboard Analytics")

   if not st.session_state.scores:
      st.warning("Please complete Skill Assesmant first")

   else:
       scores=st.session_state.scores
       df=pd.DataFrame({"Topic":list(scores.keys()),"Scores" :list(scores.values())})
       col1,col2,col3=st.columns(3)
       avg_scores=sum(scores.values())/len(scores)

       weak_topics=[k for k,v in scores.items() if v<40]
       strong_topics=[k for k,v in scores.items() if v>=80]

       col1.metric("Average Score", f"{avg_scores:.2f}%")
       col2.metric("Weak Topics", len(weak_topics))
       col3.metric("Strong Topic",len(strong_topics))

       st.subheader("Topic performance")
       fig, ax = plt.subplots(figsize=(5,5))
       ax.bar(df['Topic'],df['Scores'])
       plt.xticks(rotation=20)
       st.pyplot(fig)

       st.subheader(" 🚨 weak topic detection")

       if weak_topics:
          for topic in weak_topics:
              st.error(f"weak topic:{topic}")
       else:
          st.success("No weak topic detected")
       st.subheader("Strong topic")

       if strong_topics:
          for topic in strong_topics:
              st.success(f"Strong Topic:{topic}")


elif menu=="AI ROADMAP":
    st.title=("AI ROADMAP")

    if not st.session_state.scores:
       st.warning("please complete skill assesment first")

    else:
        scores= st.session_state.scores
        weak_topics = [k for k,v in scores.items() if v <50]
        if not weak_topics:
           st.success("Excellent performance ! keep practicing advanced problems.")
        else:
           for topic in weak_topics:
              st.subheader(f" 🎓 {topic} Roadmap") 
              if topic == "Arrays":
                 st.write("Week 1 :- Array basics")
                 st.write("Week 2 :- sliding windows")
                 st.write("Week 3 :- prefix sum")
                 st.write("Week 4 :- Leetcode problems")

              elif topic == "Linked List":
                 st.write("Week 1 :- Linked list basics")
                 st.write("Week 2 :- Reverse Linked list")
                 st.write("Week 3 :- Fast and slow pointers")
                 st.write("Week 4 :- Interview problems")

              elif topic == "Stack":
                 st.write("Week 1 :- Stack basics")
                 st.write("Week 2 :- Monotonic Stack")
                 st.write("Week 3 :- Expression Evaluation")
                 st.write("Week 4 :- Advanced problems")

              elif topic == "Queue":
                 st.write("Week 1 :- Queue Basics")
                 st.write("Week 2 :- Circular Queue")
                 st.write("Week 3 :- Priority Queue")
                 st.write("Week 4 :- Graph Application")

              elif topic == "DBMS":
                 st.write("Week 1 :- SQL Basics")
                 st.write("Week 2 :- Joins")
                 st.write("Week 3 :- Normalization")
                 st.write("Week 4 :- Transactions and Indexing")

              elif topic == "OS":
                 st.write("Week 1 :- Process and Thread")
                 st.write("Week 2 :- Scheduling")
                 st.write("Week 3 :- Deadlock")
                 st.write("Week 4 :- Memory management")

elif menu == "INTERVIEW QUESTIONS":
   st.title=("Interview Question Generator")

   topic = st.selectbox("select Topic", list(question_bank.keys()))

   difficulty = st.selectbox("Difficulty", ["Easy", "Medium", "Hard"])

   if st.button("Generate Questions"):
      questions = random.sample(question_bank[topic], 3)
      st.subheader(f"{difficulty} Level Question")

      for i, q in enumerate(questions, start=1):
         st.write(f"{i}.{q}")

elif menu == "PROGRESS TRACKER":
   st.title=("progress tracker")

   if not st.session_state.scores:
      st.warning("Please complete skill assesment first")

   else:
        scores = st.session_state.scores
        progress_df = pd.DataFrame({
          'Topic': list(scores.keys()),
          'current score': list(scores.values()),
          'Target score': [100] * len(scores)
        })

        st.dataframe(progress_df)
        st.subheader("Interview Readiness")

        avg_scores = sum(scores.values()) / len(scores)

        X = [[20], [35], [45], [65], [75], [85], [95]]
        Y = ['Low', 'Low', 'Medium', 'Medium', 'Good', 'Good', 'Excellent']

        model = DecisionTreeClassifier()
        model.fit(X,Y)
        prediction= model.predict([[avg_scores]])

        st.success(f"Interview readiness level: {prediction[0]}")

        if prediction[0] == 'Low':
           st.error("You need strong preparation before placements")

        elif prediction[0] == 'Medium':
           st.warning("You are improving but still need practice")

        elif prediction[0] == 'Good':
           st.info("Good preparation level.keep parcticing")

        else:
           st.success("Excellent preparation level")

elif menu == "PLACEMENT PREPARATION":
   st.title=("🎯placement preparation hub")
   company=st.selectbox("Select Target Company",["Google","Microsoft","Amazon","Tcs","Infosys"])
   if st.button(f"Generate Company Roadmap"):
       st.write(f"Loading targeted roadmap for {company}")
       roadmap={"Google":[
                    "Python",
                    "DSA",
                    "System Design",
                    "DBMS",
                    "OS",
                    "Mock Interview"
            ], 
            "Microsoft":[
               "Python",
               "DSA",
               "OOP",
               "DBMS",
               "OS"
            ],
            "Amazon":[
               "DSA",
               "OOP",
               "Leadrship",
               "Principles",
               "system Design"
            ],
            "Tcs":[
               "Aptitude",
               "python",
               "SQL",
               "DBMS",
               "HR Interview"
            ],
            "Infosys":[
               "Aptitude",
               "Python",
               "OOP",
               "DBMS",
               "OS",
               "HR Interview"
            ]
      } 

       for topic in roadmap.get(company,[]):
          st.checkbox(topic) 


          