import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

shabits=pd.read_csv('BOOTCAMP-DATA-SCIENCE-main\TALLER PANDAS\student_habits_performance.csv')
print(shabits.head())

study_hours_per_day = shabits['study_hours_per_day']
study_hours_per_day=np.array(study_hours_per_day)

q1=np.percentile(study_hours_per_day,25)
q2=np.percentile(study_hours_per_day,50)
q3=np.percentile(study_hours_per_day,75)
iqr=q3-q1

print(f"El primer cuartil es: {q1}")
print(f"El segundo cuartil es: {q2}")
print(f"El tercer cuartil es: {q3}")
print(f"El intercuartil es: {iqr}")
print("")

stuy_hours_per_gender=shabits.groupby("gender")["study_hours_per_day"].mean()#agrupa la lista por generos y saca el promedio de horas de estudio de cada genero
most_studious=stuy_hours_per_gender.idxmax()#elige el indice con el promedio mas alto
print(stuy_hours_per_gender)
print(f"El genero que mas estudio en promedio fue : {most_studious}")

print("")

social_media_hours_per_gender=shabits.groupby("gender")["social_media_hours"].mean()
most_social_gender=social_media_hours_per_gender.idxmax()
print(social_media_hours_per_gender)
print(f"El genero mas social fue: {most_social_gender}")

print("")

score_per_gender=shabits.groupby("gender")["exam_score"].mean()
most_scored_gender=score_per_gender.idxmax()
print(score_per_gender)
print(f"El genero con mas nota promedio fue: {most_scored_gender}")


correlation = shabits[["sleep_hours", "study_hours_per_day","mental_health_rating" ,"exam_score"]].corr()

print("Matriz de correlación:") #entre mas se acerce a 1 mas relacion tienen las variables
print(correlation)
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.title("Correlación entre horas de sueño,,salud mental estudio y nota de examen")
plt.show()