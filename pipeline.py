from db_pull import get_data
from db_push import save_predictions
import pandas as pd
from sklearn.model_selection import RandomizedSearchCV
from sklearn.pipeline import Pipeline
from lightgbm import LGBMClassifier
from sklearn.preprocessing import FunctionTransformer
from sklearn.model_selection import train_test_split
from features import add_features


df = get_data()

features = ['Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']

cat_features = ['Sex', 'Embarked']

#target = ['Survived']

for col in cat_features:
  df[col] = df[col].astype('category')

feature_transformer = FunctionTransformer(add_features, validate=False)

x_train, x_test, y_train, y_test = train_test_split(df[features], df['Survived'],
test_size=0.2, random_state=101)

model = LGBMClassifier()

model_pipeline = Pipeline(steps=[
  ('feature_engineering', feature_transformer),
  ('model', model)
])

param_dist = {
  'model__num_leaves': [30,50],
  'model__learning_rate': [0.1,0.5,1],
  'model__n_estimators': [100,200]
}

grid = RandomizedSearchCV(
  estimator= model_pipeline,
  param_distributions= param_dist,
  n_iter=5,
  cv=4,
  scoring='accuracy',
  n_jobs=-1
)


grid.fit(x_train,y_train)


pred = grid.predict(x_test)

x_test_copy = x_test.copy()
x_test_copy['predictions'] = pred


save_predictions(x_test_copy)



