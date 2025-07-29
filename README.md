# End-to-End-Db-workflow
This project demonstrates a complete machine learning workflow built around the Titanic dataset—from pulling data from a MySQL database, preprocessing and feature engineering, building a LightGBM classification model inside a pipeline, and saving the model's predictions back into the database.

📌 Project Overview

Goal: Predict passenger survival on the Titanic using a custom ML pipeline and store results in a MySQL table for future use or dashboard integration.

✅ Key Components

Data Source: Titanic dataset pulled from a MySQL database

Preprocessing: Custom feature engineering using FunctionTransformer

Modeling: LightGBM Classifier with RandomizedSearchCV for hyperparameter tuning

Integration: Writes prediction results back into a new or existing table in MySQL

🏗️ Project Structure

titanic_ml_project/
│
├── db_pull.py              # Loads Titanic data from MySQL
├── features.py             # Contains custom feature engineering functions
├── model_pipeline.py       # Builds and trains the ML pipeline
├── save_predictions.py     # Pushes predictions to a new/existing DB table
├── .env                    # Stores DB credentials (never push to GitHub)
├── README.md               # Project documentation

⚙️ How It Works

1. 🔌 Data Connection

Connects to a local or remote MySQL database using credentials from .env and loads the titanic_train table into a pandas DataFrame.

from db_pull import get_data

df = get_data()

2. 🧠 Feature Engineering

Adds two new columns:

length_of_name: Length of the passenger's full name.

is_a_minor: Flags passengers under 18 as minors.

from features import add_features
df = add_features(df)

3. 🧲 Model Pipeline

Uses FunctionTransformer to add features inside a pipeline.

Fits an LGBMClassifier wrapped inside RandomizedSearchCV for optimization.

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import FunctionTransformer
from lightgbm import LGBMClassifier

4. 📂 Save Predictions

The test set predictions are added as a new column (prediction) and written to a new MySQL table (titanic_with_predictions).

from save_predictions import save_predictions

save_predictions(df_with_preds, table_name='titanic_with_predictions')

💠 Requirements

pandas
sqlalchemy
pymysql
scikit-learn
lightgbm
python-dotenv

Install all dependencies using:

pip install -r requirements.txt

🧪 Example Run Flow

Setup your .env with DB credentials:

db_username=root
db_password=yourpassword
db_host=localhost
db_port=3306
db_database=your_database

Run in order:

python model_pipeline.py

📊 Output Example

Saved table in MySQL (titanic_with_predictions) includes:

PassengerId

Pclass

Sex

Age

Fare

Embarked

prediction

1

3

male

22

7.25

S

0

2

1

female

38

71.3

C

1

📁 Future Improvements

Add more complex feature engineering (e.g. family size, cabin prefix).

Export the trained model using joblib.

Add a Flask or FastAPI interface for real-time inference.

🧑‍💻 Author

Emmanuel Nwankwo Ota - Machine Learning Engineer | Real-world AI & database integration enthusiastBuilt with ❤️ using Python, MySQL, and scikit-learn

