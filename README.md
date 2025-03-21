# Visualization Evaluation

In the sphere of data analysis, visualisation is very important, as it transforms raw data into a form that's much more easily understood, and hence it reaches an even bigger audience. Visualisations use visual cues: color, shape, size, to emphasize trends, patterns, and anomalies, making it easy to bring important insight very quickly to the attention of the user. 

Equally important is user evaluation for these visualisations, since it would ensure that the design is intuitive, relevant, and accessible to the proper audience. It allows analysts and designers to observe real users interacting with visualisations, gathering feedback on how clear, usable, and functional the visualization is. This testing helps identify possible usability problems, such as misinterpretation of data arising from confusing designs, poor choice of visualisation types and color schemes. Through iteration guided by user feedback, designers can further refine visualizations to better meet users' needs and improve their ability to understand and act upon insights derived from data. In the end, user-centered visualisations increase the overall communication effectiveness with data and achieve a greater understanding and trust of the data.

## Objective
The principal objective of this project is to conduct an experiment which aims to systematically investigate the effectiveness of heatmaps and scatterplots in visualising pupil absences across a hypothetical dataset encompassing ten schools over an academic year. By assessing participants accuracy, response time, and the ability to interpret the data, the research seeks to determine which method is able to portray the information about pupil absences with a greater impact.

## Installation
To install and run the application, follow these steps:
### Clone this repository:
    git clone https://github.com/Aleevz/evaluation.git
    
### Navigate to the project directory:
    cd devaluation

### Install the necessary dependencies:
    pip install -r requirements.txt

## Running the Application
Run the following command in the project directory:
    streamlit run main.py

This application is an interactive experiment designed to evaluate the effectiveness of different types of visualizations (scatterplots and heatmaps) in representing student absence data across ten schools over an academic year.

### How the Application Works
1. Participant Registration: each participant is assigned a unique ID and their results are recorded in the results_experiment.csv file.
2. Data Generation: a random dataset is generated, representing the number of absences per month for 10 schools.
3. Question and Visualization Generation: the experiment consists of 20 multiple-choice questions, alternating between Scatterplots (display absences as points in a scatter plot) and Heatmaps (use a heatmap to show the number of absences). Each question asks participants to identify which school or month had the highest or lowest number of absences.
4. User Interaction: the corresponding visualization is displayed along with the question. The participant selects one of four possible answers. The response, along with the time taken, is recorded.
5. Results Logging: Accuracy, response time, and visualization type are stored in results_experiment.csv.

## Further Analysis & Reproducibility
To better understand the findings of this project, you can refer to the report, which details the statistical analysis conducted. We applied t-tests, confidence intervals, and hypothesis testing to determine whether there is a significant difference in accuracy and response time between the two visualization types (scatterplots and heatmaps).

If you would like to conduct your own experiments, we have provided a Jupyter Notebook containing all the necessary code to run hypothesis tests, statistical analyses, and visualizations of the results. This allows you to replicate our study or extend it with your own data.
