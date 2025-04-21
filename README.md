
# Flight Price Prediction

This project uses machine learning to predict airline ticket prices based on flight and travel details. It includes an end-to-end pipeline from data preprocessing to model training, hyperparameter tuning, and web deployment using Visual Studio. The app enables users to input flight information and receive real-time price predictions.

## Features
- Data preprocessing & feature engineering (date, time, duration)
- Handled missing values using SimpleImputer
- EDA with Seaborn & Matplotlib
- Trained regression models: Linear Regression, Random Forest,- LGBMRegressor,Decision tree,XGboost Regressor
- Hyperparameter tuning using GridSearchCV & RandomizedSearchCV
Web app deployment using Django in Visual Studio
## Tech Stack

- Python, Pandas, NumPy

- Scikit-learn, Seaborn, Matplotlib

- Visual Studio (for frontend interface)
## Dataset and model evaluation

- Dataset sourced from Kaggle. It includes features like airline, departure time, arrival time, duration, total stops, and more
-  Best model: XGBoost Regressor
- Accuracy: R² = 0.85 using RandomizedSearchCV

## Website Preview
![Image Alt](https://github.com/karu012/airline_fare_prediction/blob/212e4a94722bdc585ab58734f7f22195f80b6198/Screenshot%202025-04-21%20201545.png)
![Image Alt](https://github.com/karu012/airline_fare_prediction/blob/91407e72a69d66e9976f07e93ddfafbfbe5ad7b2/Screenshot%202025-04-21%20201710.png)
![Image Alt](https://github.com/karu012/airline_fare_prediction/blob/2e207466aa0160f90e1e590311d0cdaa2ff59aed/Screenshot%202025-04-21%20201824.jpg)