AI-Powered Public Health Risk Intelligence Platform
Overview

AI-Powered Public Health Risk Intelligence Platform is an end-to-end data science and artificial intelligence solution designed to support proactive public health surveillance, disease risk prediction, and evidence-based decision-making. The platform integrates demographic, environmental, healthcare, mobility, and social intelligence data to identify regions at elevated public health risk before outbreaks escalate.

By leveraging machine learning, geospatial analytics, time-series forecasting, explainable AI, and interactive dashboards, the platform provides actionable insights for public health agencies, policymakers, and healthcare organizations to strengthen preparedness and optimize resource allocation.

Objectives
Predict public health risk levels using machine learning.
Detect potential disease outbreak hotspots.
Analyze environmental and socioeconomic determinants of health.
Assess healthcare system capacity and accessibility.
Forecast disease trends using time-series models.
Monitor public sentiment and health misinformation.
Visualize health intelligence through interactive GIS dashboards.
Support data-driven public health planning and intervention.
Key Features
End-to-end data preprocessing pipeline
Advanced feature engineering
Machine learning risk prediction
Explainable AI (SHAP)
Disease hotspot detection
Environmental risk analysis
Healthcare capacity assessment
Social media health intelligence
Interactive geospatial dashboards
Time-series outbreak forecasting
Automated visualization generation
Streamlit web application
Project Structure
AI-Powered-Public-Health-Risk-Intelligence-Platform/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic_health_data.csv
│
├── notebooks/
│
├── src/
│   ├── preprocessing.py
│   ├── feature_engineering.py
│   ├── train_model.py
│   ├── prediction.py
│   ├── gis_analysis.py
│   ├── nlp_analysis.py
│   └── dashboard.py
│
├── models/
│   └── health_risk_model.pkl
│
├── charts/
├── maps/
├── dashboard/
│
├── requirements.txt
├── README.md
└── LICENSE
Dataset

A realistic synthetic public health dataset was developed to simulate nationwide surveillance data across multiple Nigerian states.

Dataset Size
20,000+ observations
Multiple regions
Multi-year temporal coverage
Realistic feature correlations
Features
Category	Variables
Demographics	Population, Population Density, Average Age
Environment	Rainfall, Temperature, Humidity
Pollution	Air Quality Index (AQI), Water Quality
Healthcare	Hospital Access, Bed Capacity, Doctor Ratio
Disease Surveillance	Disease Cases, Disease Type, Mortality Rate
Social Intelligence	Health Posts, Sentiment, Misinformation Index
Mobility	Mobility Index
Vaccination	Vaccination Coverage
AI Output	AI Risk Score, Risk Level
Workflow
Synthetic Dataset
        │
        ▼
Data Cleaning
        │
        ▼
Feature Engineering
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Model Training
        │
        ▼
Model Evaluation
        │
        ▼
Explainable AI
        │
        ▼
GIS Mapping
        │
        ▼
Interactive Dashboard
Machine Learning Pipeline
Data Preprocessing
Missing value handling
Duplicate removal
Data normalization
Label encoding
Feature scaling
Train/Test split
Feature Engineering

New predictive variables include:

Healthcare Pressure Index
Climate Risk Score
Disease Transmission Score
Population Vulnerability Score
Environmental Risk Score
Mosquito Breeding Index
Public Concern Score
Hospital Efficiency Index
Vaccination Gap
Composite Risk Index
Machine Learning Models

The platform supports multiple algorithms:

Random Forest
Gradient Boosting
XGBoost
LightGBM
Logistic Regression
CatBoost (optional)
Evaluation Metrics

Classification performance is assessed using:

Accuracy
Precision
Recall
F1 Score
ROC-AUC
Confusion Matrix
Cross Validation
Explainable AI

Model transparency is enhanced through:

SHAP Summary Plots
Feature Importance
Partial Dependence Analysis
Local Feature Explanations

These techniques help explain the factors contributing to predicted public health risks.

Geospatial Intelligence

The platform generates interactive spatial analyses including:

Disease hotspot maps
Public health risk heatmaps
Air pollution maps
Hospital accessibility maps
Population vulnerability maps
Vaccination coverage maps
Flood and environmental risk maps

Libraries used include:

GeoPandas
Folium
Plotly
Contextily
Time-Series Forecasting

Future disease trends can be forecast using:

Prophet
ARIMA
LSTM (optional)

Forecasts support early warning and resource planning.

Dashboard

The Streamlit dashboard provides:

National risk overview
Regional disease trends
Environmental monitoring
Healthcare capacity visualization
AI-generated risk predictions
GIS maps
Model explanation panels
Forecast dashboards
Visualizations

Example outputs include:

Disease trend analysis
Feature importance rankings
Correlation heatmaps
Risk distribution plots
SHAP summary plots
Confusion matrix
Choropleth maps
Hotspot density maps
Time-series forecasts
Vaccination coverage dashboards
Technologies Used
Programming
Python
Data Processing
Pandas
NumPy
Machine Learning
Scikit-learn
XGBoost
LightGBM
CatBoost
Visualization
Matplotlib
Plotly
Folium
GeoPandas
Explainable AI
SHAP
Dashboard
Streamlit
Installation

Clone the repository:

git clone https://github.com/joanjosh17/AI-Powered-Public-Health-Risk-Intelligence-Platform.git

cd AI-Powered-Public-Health-Risk-Intelligence-Platform

Install dependencies:

pip install -r requirements.txt
Usage
1. Preprocess the data
python src/preprocessing.py
2. Generate engineered features
python src/feature_engineering.py
3. Train the machine learning model
python src/train_model.py
4. Generate predictions
python src/prediction.py
5. Run GIS analysis
python src/gis_analysis.py
6. Launch the dashboard
streamlit run src/dashboard.py
Example Outputs
models/
    health_risk_model.pkl

charts/
    confusion_matrix.png
    feature_importance.png
    correlation_heatmap.png
    shap_summary.png

maps/
    disease_hotspots.html
    public_health_risk_map.html
Future Improvements
Real-time data ingestion from surveillance systems
Integration with weather and climate APIs
Satellite imagery for environmental monitoring
Transformer-based NLP for health misinformation detection
Deep learning models for outbreak prediction
Automated alert notifications
Cloud deployment using Docker and Kubernetes
CI/CD pipelines for automated model updates
Skills Demonstrated
Public Health Data Science
Predictive Analytics
Machine Learning
Feature Engineering
Geospatial Analytics
Time-Series Forecasting
Explainable AI
Data Visualization
Dashboard Development
Python Software Engineering
Model Evaluation
Health Intelligence Systems
Acknowledgements

This project is inspired by modern public health surveillance and health intelligence frameworks that combine artificial intelligence, geospatial analytics, and epidemiological modeling to support early warning, outbreak preparedness, and data-driven public health decision-making.

License

This project is released under the MIT License.

Author

Jonah Buka

Passionate about building AI-driven, data-centric solutions that address real-world public health challenges through machine learning, geospatial analytics, and interactive data visualization.
