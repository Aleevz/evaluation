import random
import time
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

st.set_page_config(layout="wide")

# Definition of the file name
file_name = Path("results_experiment.csv")

if file_name.is_file():
    # If the file exists, it opens the file and read it
    df_results = pd.read_csv(file_name)
    st.session_state.user_id = df_results.iloc[-1]["participant_ID"].astype(int) + 1
else:
    # If it doesn't, it creates a .csv file with the name 'results_experiment.csv'
    df_results = pd.DataFrame(
        columns=["participant_ID", "question_number", "vis_type", "correct_answer", "time_(s)"]
    )  # Creation of a dataframe
    st.session_state.user_id = 1


# Function to get id and create a new one
def get_id(df):
    return 0 if df.empty else (df.iloc[-1, 0] + 1)


questions = [
    "Which school had the [size] number absences in [month]?",
    "In which month did [school] have the [size] number absences?",
]

months = [
    "September",
    "October",
    "November",
    "December",
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
]

school_options = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

participant_id = get_id(df_results)


def generate_random_data():
    data = np.random.randint(20, 100, size=(10, 11))

    df = pd.DataFrame(data, columns=months)
    df["School"] = school_options
    df = df[["School", *df.columns[:-1].tolist()]]

    return df


def generate_visualisation(df, no_question):
    fig = plt.figure(figsize=(12, 10))
    if no_question % 2 == 0:
        markers = ["o", "s", "^", "<", ">", "*", "+", "p", "D", "v"]

        for i, school in enumerate(df["School"]):
            plt.scatter(df.columns[1:], df.iloc[i, 1:], marker=markers[i], label=school, color="k", s=100, zorder=3)

        plt.title("Pupil Absences by School")
        plt.xlabel("Months")
        plt.ylabel("Number of Absences")
        plt.xticks(rotation=45)
        plt.legend(title="Schools", bbox_to_anchor=(1.05, 1), loc="upper left")
        plt.tight_layout()
    else:
        plt.imshow(df.iloc[:, 1:], cmap="binary", aspect="auto")

        plt.colorbar(label="Number of Absences")
        plt.xticks(ticks=np.arange(len(df.columns) - 1), labels=df.columns[1:], rotation=45)
        plt.yticks(ticks=np.arange(len(df["School"])), labels=df["School"])
        plt.title("Pupil Absences by School")
        plt.xlabel("Months")
        plt.ylabel("Schools")
        plt.tight_layout()
    return fig


def generate_whitescreen():
    fig = plt.figure(figsize=(12, 10))

    # Set the face color of the figure to white (this is the background color)
    fig.patch.set_facecolor('white')

    return fig


def generate_question_and_answers(data):
    # Select highest or lowest
    hl = "highest" if random.randint(0, 1) else "lowest"

    # Update the question with the relevant word
    question = random.choice(questions).replace("[size]", hl)

    # Check if this is a month question or school question
    if "[month]" in question:
        # Select a random month from list of school months
        month = random.choice(months)

        # Insert that month into the question
        question = question.replace("[month]", month)

        # Find the correct answer to the question
        correct_answer_idx = data[month].idxmax() if hl == "highest" else data[month].idxmin()
        correct_answer = f"School {data.iloc[correct_answer_idx]["School"]}"

        # Select three random incorrect answers
        answers = random.sample(
            [f"School {data.iloc[school]["School"]}" for school in data.index if school != correct_answer_idx], 3
        )
    else:
        schools = school_options

        # Select a random school
        school = random.randint(0, 9)

        # Update the question with that school
        question = question.replace("[school]", f"School {schools[school]}")

        # Find the correct answer to the question
        correct_answer = data.iloc[school][months].idxmax() if hl == "highest" else data.iloc[school][months].idxmin()

        # Select three random incorrect answers
        answers = random.sample([month for month in months if month != correct_answer], 3)

    # Append the correct answer into our list of answers at a random index
    answers.append(correct_answer)
    random.shuffle(answers)

    # Return the question, the list of potential answers, and the index of the correct answer
    return question, answers, answers.index(correct_answer)


def add_result(df, part_id, v_type, answer, t):
    # Create a new row as a DataFrame
    result = pd.DataFrame([[part_id, v_type, answer, t]], columns=df.columns)
    return pd.concat([df, result], ignore_index=True)


def process_answer(selected_answer, correct_answer):
    time_taken = time.time() - st.session_state.question_start_time
    correct = 1 if selected_answer == correct_answer else 0
    vis_type = "heatmap" if st.session_state.question_num % 2 == 0 else "scatterplot"

    results = {
        "participant_ID": st.session_state.user_id,
        "question_number": st.session_state.question_num,
        "vis_type": vis_type,
        "correct_answer": correct,
        "time_(s)": time_taken,
    }

    new_row = pd.DataFrame([results])

    st.session_state.user_results = pd.concat([st.session_state.user_results, new_row], ignore_index=True)

    print(st.session_state.user_results)

    st.markdown("""
                <style>
                body {
                    display: none;
                }
                </style>
                """, unsafe_allow_html=True)
    time.sleep(1)
    st.rerun()

# Iniciar el experimento
# if __name__ == "__main__":
# st.title("Visualisation Evaluation")


def start_experiment():
    global df_results
    st.session_state.experiment_started = True
    st.session_state.question_answered = False
    st.session_state.question_num = 0
    st.session_state.data = None
    st.session_state.question_data = None
    st.session_state.selected_answer = None
    st.session_state.question_start_time = None
    st.session_state.user_results = df_results
    st.empty()


if "experiment_started" not in st.session_state:
    st.session_state.experiment_started = False


# Si el experimento no ha comenzado, muestra la pantalla de bienvenida
if not st.session_state.experiment_started:
    st.title("Visualisation Evaluation")
    st.subheader("Instructions:")
    st.write("""You will complete 20 multiple-choice questions,
              where each question corresponds to one of the two types of
              visualizations: scatterplots or heatmaps.
              The questions are alternated between the two visualization types,
              with a brief one-second white screen between each question.

              \nThe experiment will take approximately 35 minutes.
              Once you select an answer option for each question,
              you will not have the opportunity to change it,
              and you will automatically proceed to the next question.
              Please read each question carefully and answer thoughtfully,
              as your responses cannot be modified once submitted.

              \nYour responses will be recorded anonymously.
              No personal data will be collected, and your identity will not be
              linked to your responses.""")
    if st.button("Start Experiment"):
        start_experiment()
        st.session_state.question_start_time = time.time()
        st.rerun()
else:
    col1, col2 = st.columns(2)

    if not st.session_state.question_answered:
        st.session_state.data = data = generate_random_data()
        vis = generate_visualisation(data, st.session_state.question_num)
        st.session_state.question_num += 1
        st.session_state.question_data = question, options, answer_idx = generate_question_and_answers(data)
        st.session_state.question_start_time = time.time()
    else:
        data = st.session_state.data
        question, options, answer_idx = st.session_state.question_data

    with col1:
        if not st.session_state.question_answered:
            st.pyplot(vis, use_container_width=True)

    with col2:
        st.subheader(question)
        answer = st.radio(" ", options, index=None)

        st.session_state.question_answered = not st.session_state.question_answered
        
        st.session_state.selected_answer = answer

        if st.session_state.selected_answer:
            process_answer(answer, options[answer_idx])
