import streamlit as st

# Page Settings
st.set_page_config(
    page_title="Grade Calculator",
    page_icon="🎓",
    layout="wide"
)

# Header
st.title("🎓 Student Grade Calculator")
st.write("Enter marks for all subjects and calculate performance.")

# Sidebar
st.sidebar.header("Student Details")

student_name = st.sidebar.text_input("Student Name")
roll_no = st.sidebar.text_input("Roll Number")

# Subject Inputs
st.subheader("📚 Enter Marks")

col1, col2 = st.columns(2)

with col1:
    python_marks = st.number_input("Python", 0, 100)
    math_marks = st.number_input("Mathematics", 0, 100)
    english_marks = st.number_input("English", 0, 100)

with col2:
    science_marks = st.number_input("Science", 0, 100)
    history_marks = st.number_input("History", 0, 100)

# Calculate Button
if st.button("📊 Calculate Result"):

    # Total
    total = (
        python_marks
        + math_marks
        + english_marks
        + science_marks
        + history_marks
    )

    # Percentage
    percentage = (total / 500) * 100

    # Grade Logic
    if percentage >= 90:
        grade = "A+"
        status = "Excellent 🌟"

    elif percentage >= 80:
        grade = "A"
        status = "Very Good 🎉"

    elif percentage >= 70:
        grade = "B"
        status = "Good 👍"

    elif percentage >= 60:
        grade = "C"
        status = "Average 🙂"

    elif percentage >= 50:
        grade = "D"
        status = "Pass ✅"

    else:
        grade = "F"
        status = "Fail ❌"

    # Highest and Lowest Subject
    subjects = {
        "Python": python_marks,
        "Mathematics": math_marks,
        "English": english_marks,
        "Science": science_marks,
        "History": history_marks
    }

    highest_subject = max(subjects, key=subjects.get)
    lowest_subject = min(subjects, key=subjects.get)

    # Dashboard Metrics
    st.subheader("📈 Result Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Marks", total)
    col2.metric("Percentage", f"{percentage:.2f}%")
    col3.metric("Grade", grade)

    # Progress Bar
    st.progress(int(percentage))

    # Student Details
    st.subheader("👨‍🎓 Student Information")

    st.write("**Name:**", student_name)
    st.write("**Roll Number:**", roll_no)

    # Performance
    st.subheader("🏆 Performance Analysis")

    st.success(status)

    st.write(
        f"**Highest Scoring Subject:** {highest_subject}"
    )

    st.write(
        f"**Lowest Scoring Subject:** {lowest_subject}"
    )

    # Subject Marks Table
    st.subheader("📋 Subject-wise Marks")

    st.table(subjects)