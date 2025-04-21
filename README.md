1.Introduction

This project uses machine learning to predict airline ticket prices based on flight and travel details. It includes an end-to-end pipeline from data preprocessing to model training, hyperparameter tuning, and web deployment using Visual Studio. The app enables users to input flight information and receive real-time price predictions.

2.Features

Data preprocessing & feature engineering (date, time, duration)

Handled missing values using SimpleImputer

EDA with Seaborn & Matplotlib

Trained regression models: Linear Regression, Random Forest,LGBMRegressor,Decision tree,XGboost Regressor

Hyperparameter tuning using GridSearchCV & RandomizedSearchCV

Web app deployment using Django in Visual Studio

3.Tech Stack

Python, Pandas, NumPy

Scikit-learn, Seaborn, Matplotlib

Visual Studio (for frontend interface)

4. Dataset
   
Dataset sourced from Kaggle. It includes features like airline, departure time, arrival time, duration, total stops, and more

 Best model: XGBoost Regressor

 Accuracy: R² = 0.85 using RandomizedSearchCV

5.Website preview
 ![Image Alt]()
![Image Alt]()
![Image Alt]()
