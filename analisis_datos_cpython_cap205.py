import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
cpython = pd.read_csv("https://github.com/robintux/Datasets4StackOverFlowQuestions/raw/refs/heads/master/cpython_commit_history_pre.csv")
cpython["date"] = pd.to_datetime(cpython["date"], utc = True)
cpython["year"] = cpython["date"].dt.year
cpython["month"] = cpython["date"].dt.to_period("M")

# Evolución temporal de commits
# Número de commits por año

commits_by_year = cpython.groupby("year").size()
plt.figure(figsize = (14,6))
commits_by_year.plot(kind = "line", marker = "o")
plt.title("Evolución de commits de cpython por año")
plt.xlabel("Año")
plt.ylabel("Número de commits")
plt.grid(True)

#Fin
plt.tight_layout()
plt.savefig("Evolucion_commits_por_año.png", dpi = 300)
plt.show()

# Diagrama de barras de los top10 contribuyentes históricos al repositorio cpython
top10_authors = cpython["author"].value_counts().head(10)
plt.figure(figsize = (10,6))
top10_authors.plot(kind = "barh", color = "lightgreen")

# Invertimos el orden del eje y
plt.gca().invert_yaxis()

# Agreguemos etiquetas
plt.title("Top10 de contribuyentes de código a CPython")
plt.xlabel("Número de Commits")
plt.ylabel("Autor")

# Fin
plt.tight_layout()
plt.savefig("top10_developers.png", dpi = 300)
plt.show()