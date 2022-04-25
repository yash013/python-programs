import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

cancer_data = load_breast_cancer()
df = pd.DataFrame(cancer_data['data'],columns=cancer_data['feature_names'])
df['target'] = cancer_data['target']

X = df[cancer_data.feature_names].values
y = df['target'].values
# print('data dimensions', X.shape)

X_train, X_test, y_train, y_test = train_test_split(X,y, random_state = 101)

rf = RandomForestClassifier(n_estimators=10, random_state=111)
rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))

worst_cols = [col for col in df.columns if 'worst' in col]
# print(worst_cols)

X_worst = df[worst_cols]
X_train, X_test, y_train, y_test = train_test_split(X_worst, y, random_state=101)

rf.fit(X_train, y_train)
print(rf.score(X_test, y_test))

# ft_imp = pd.Series(rf.feature_importances_,index=cancer_data.feature_names).sort_values(ascending=False)
# print(ft_imp.head(10))

# dt = DecisionTreeClassifier()
# dt.fit(X_train, y_train)

# print("decision tree accuracy:",dt.score(X_test, y_test))


# first_raw = X_test[0]
# print(rf.predict([first_raw]))
# print("true value:", y_test[0])
# print("Random forest accuracy:",rf.score(X_test, y_test))    # accuracy
