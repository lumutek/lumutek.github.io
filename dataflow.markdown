---
layout: page
title: DataFlow
permalink: /dataflow/
background: '/images/bd_vis.jpg'
---
# Lukas Mueller

## Project Name: DataFlow

### Data Science Dashboard with sklearn, multiple linear/logistic regression, ensemble learning, data cleaning, and data visualization.

### Overview:
Having recently completed the Google Advanced Data Analytics Professional track, I thought it would be a great idea to continue cultivating my new data science skills.
Like the MLDash project, this project uses previous work as a starting point, and iterative development will take place as a series of enhancements. The state of the code 
before and after each enhancement is provided to illustrate code evolution. A chronologically ordered update summaries can be easily viewed in the narratives section below.

#### Initial Commit
You can view the code for the initial commit at [Origin][1-origin].

#### Key Code Samples
```python
#Define the y (outcome) variable.
y = df1['left']

# Define the X (predictor) variables.
X = df1.copy()
X = X.drop(['left'], axis = 1)

# Perform the split operation on your data.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)

# Define xgb to be your XGBClassifier.
xgb = XGBClassifier(objective='binary:logistic', random_state=0)

# Define parameters for tuning as `cv_params`.
cv_params = {'max_depth': [10],
              'min_child_weight': [0.75, 0.8, 0.85],
              'learning_rate': [0.375, 0.4, 4.225],
              'n_estimators': [10],
              'subsample': [1, 2 ,10],
              'colsample_bytree': [0.6, 0.65, 0.75]
              }

# Define your criteria as `scoring`.
scoring = {'accuracy', 'precision', 'recall', 'f1'}

xgb_cv = GridSearchCV(xgb, cv_params, scoring = scoring, cv = 5, refit = 'f1', n_jobs = -1, verbose=True)


%%time
# fit the GridSearch model to training data
xgb_cv = xgb_cv.fit(X_train, y_train)
xgb_cv
```
#### Data Visualizations Used
##### Description of Variables
![Description of Variables](/images/gada_variables.jpg "Description of Variables")
##### Heatmap of Correlations Between Variables
![Heatmap](/images/gada_heatmap.jpg "Heatmap of Correlations Between Variables")

##### Pearson Correlation Matrix
![Correlation Matrix](/images/gada_corr_matrix.jpg "Pearson Correlation Matrix")

##### Confusion Matrix for Model Predicting Employee Departure
![Confusion Matrix](/images/gada_conf_matrix.jpg "Confusion Matrix for prediction of employee leaving company")

##### Relative Feature Importance
![Feature Importance](/images/gada_feat_imp.jpg "Relative Feature Importance")


[1-origin]: https://github.com/lumutek/lumutek.github.io/tree/main/DataFlow/1-Origin
