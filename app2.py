import streamlit as st

st.set_page_config(
    page_title="My Streamlit App",
    page_icon="🚀",
    layout="wide",
)

st.title("Welcome to Muath App")

st.divider()

name = st.text_input("Enter your name:")

python_score = st.slider("Python:", 0, 100, 50)
cloud_score = st.slider("Cloud:", 0, 100, 70)
database_score = st.slider("Database:", 0, 100, 75)

score = {
    "Python": python_score,
    "Cloud": cloud_score,
    "Database": database_score
}

def caculate_average(student_scores):
    total = sum(student_scores.values())
    average = total / len(student_scores)
    return average  


def get_grade(average):
    if average >= 70:
        return "distinction"
    elif average >= 60:
        return "Merit"
    elif average >= 40:
        return "Pass"
    else:
        return "Fail"



if st.button("calculate_average", use_container_width=True):

    if not name:
        st.warning("Please enter a student name.")
    else:
        average = caculate_average(score)
        grade = get_grade(average)

        st.subheader(f"Results for {name}")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Average Score", f"{average:.1f}%")

        with col2:
            st.metric("Final Grade", grade)