import streamlit as st
import pickle
import pandas as pd
import joblib
model = joblib.load("joblib.joblib")

teams = ['Sunrisers Hyderabad',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Kings XI Punjab',
    'Chennai Super Kings',
    'Kings XI Punjab',
    'Rajasthan Royals',
    'Delhi Capitals']
st.header("rm Creation")
st.title("Ipl Win Predictor")
col1,col2 = st.columns(2)
with col1:
    Batting_Team = st.selectbox("Select Batting Team",teams)
with col2:
    Bowling_Team = st.selectbox("Select Bowling Team",sorted(teams))
target = st.number_input("Target")
c3,c4,c5 = st.columns(3)
with c3:
    score = st.number_input("Score")
with c4:
    overs = st.number_input("Overs")
with c5:
    wickets = st.number_input("Wickets")
if st.button("Probability"):
    runs_left = target - score
    balls_left = 120 - (overs*6)
    crr = score/overs
    rrr = (runs_left*6)/balls_left
    data = pd.DataFrame({
        "batting_team":[Batting_Team],
        "bowling_team":[Bowling_Team],
        "target":[target],
        "runs_need":[runs_left],
        "balls_left":[balls_left],
        "wickets":[wickets],
        "crr":[crr],
        "rrr":[rrr]
    })
    result = model.predict_proba(data)
    win = result[0][0]
    loss = result[0][1]
    st.header(f"{Batting_Team} : {round(loss*100)}%")
    st.header(f"{Bowling_Team} : {round(win*100)}%")
print(type(model))
