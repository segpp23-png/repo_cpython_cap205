from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
df = pd.read_csv("data_limpia.csv")
X = df.drop["target"], axis = 1)
y = df["target"]
X_train, X_test, y_train, y_test = train_test_split(X, y, train_size = 0.8)
model = RandomForestClassifier()
model.fit(X_train, y_train)
# Luego calculamos indicadores de calidad
