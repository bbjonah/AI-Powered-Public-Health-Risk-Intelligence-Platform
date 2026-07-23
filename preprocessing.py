"""
==========================================================
AI-Powered Public Health Risk Intelligence Platform
File: src/preprocessing.py
==========================================================

This module handles:
1. Loading dataset
2. Data cleaning
3. Missing value handling
4. Duplicate removal
5. Feature engineering
6. Encoding categorical variables
7. Scaling numerical features
8. Train/Test split
9. Saving processed dataset
"""

import os
import joblib
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler


class DataPreprocessor:
    """
    End-to-end preprocessing pipeline.
    """

    def __init__(
        self,
        data_path="../data/synthetic_health_data.csv",
        output_dir="../data/processed"
    ):

        self.data_path = data_path
        self.output_dir = output_dir

        os.makedirs(self.output_dir, exist_ok=True)

        self.df = None

        self.label_encoders = {}
        self.scaler = StandardScaler()

    #######################################################################
    # LOAD DATA
    #######################################################################

    def load_data(self):

        print("=" * 60)
        print("Loading Dataset...")
        print("=" * 60)

        self.df = pd.read_csv(self.data_path)

        print(f"Dataset Shape : {self.df.shape}")

        return self.df

    #######################################################################
    # BASIC INFORMATION
    #######################################################################

    def dataset_summary(self):

        print("\nDataset Information")
        print("-" * 50)

        print(self.df.info())

        print("\nMissing Values")
        print("-" * 50)

        print(self.df.isnull().sum())

        print("\nDuplicate Rows")

        print(self.df.duplicated().sum())

    #######################################################################
    # CLEAN DATA
    #######################################################################

    def clean_data(self):

        print("\nCleaning Dataset...")

        # Remove duplicates
        self.df.drop_duplicates(inplace=True)

        # Standardize column names
        self.df.columns = (
            self.df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        return self.df

    #######################################################################
    # HANDLE MISSING VALUES
    #######################################################################

    def handle_missing_values(self):

        print("\nHandling Missing Values...")

        numeric_cols = self.df.select_dtypes(
            include=np.number
        ).columns

        categorical_cols = self.df.select_dtypes(
            include="object"
        ).columns

        for col in numeric_cols:
            self.df[col] = self.df[col].fillna(
                self.df[col].median()
            )

        for col in categorical_cols:
            self.df[col] = self.df[col].fillna(
                self.df[col].mode()[0]
            )

        return self.df

    #######################################################################
    # FEATURE ENGINEERING
    #######################################################################

    def feature_engineering(self):

        print("\nEngineering Features...")

        # Convert Date
        self.df["date"] = pd.to_datetime(self.df["date"])

        self.df["year"] = self.df["date"].dt.year
        self.df["month"] = self.df["date"].dt.month
        self.df["week"] = self.df["date"].dt.isocalendar().week.astype(int)
        self.df["day"] = self.df["date"].dt.day

        self.df["is_rainy_season"] = np.where(
            self.df["rainfall_mm"] > 150,
            1,
            0
        )

        self.df["high_pollution"] = np.where(
            self.df["aqi"] > 100,
            1,
            0
        )

        self.df["poor_water_quality"] = np.where(
            self.df["water_quality"] < 60,
            1,
            0
        )

        self.df["low_vaccination"] = np.where(
            self.df["vaccination_coverage"] < 60,
            1,
            0
        )

        self.df["healthcare_pressure"] = (
            self.df["disease_cases"] /
            self.df["bed_capacity"]
        )

        self.df["mortality_per_case"] = (
            self.df["mortality_rate"] /
            (self.df["disease_cases"] + 1)
        )

        return self.df

    #######################################################################
    # ENCODE CATEGORICAL VARIABLES
    #######################################################################

    def encode_features(self):

        print("\nEncoding Categorical Features...")

        categorical_cols = self.df.select_dtypes(
            include="object"
        ).columns

        for col in categorical_cols:

            encoder = LabelEncoder()

            self.df[col] = encoder.fit_transform(
                self.df[col].astype(str)
            )

            self.label_encoders[col] = encoder

        return self.df

    #######################################################################
    # SCALE NUMERIC FEATURES
    #######################################################################

    def scale_features(self):

        print("\nScaling Numerical Features...")

        exclude = [
            "ai_risk_score"
        ]

        numeric_cols = self.df.select_dtypes(
            include=np.number
        ).columns

        features = [
            col for col in numeric_cols
            if col not in exclude
        ]

        self.df[features] = self.scaler.fit_transform(
            self.df[features]
        )

        return self.df

    #######################################################################
    # SPLIT DATA
    #######################################################################

    def train_test_split(self):

        print("\nSplitting Dataset...")

        X = self.df.drop(
            columns=[
                "risk_level",
                "ai_risk_score"
            ]
        )

        y = self.df["risk_level"]

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=0.20,
            random_state=42,
            stratify=y
        )

        print(f"Training Samples : {len(X_train)}")
        print(f"Testing Samples  : {len(X_test)}")

        return X_train, X_test, y_train, y_test

    #######################################################################
    # SAVE PROCESSED DATA
    #######################################################################

    def save_processed_data(self):

        print("\nSaving Processed Dataset...")

        output_file = os.path.join(
            self.output_dir,
            "processed_health_data.csv"
        )

        self.df.to_csv(
            output_file,
            index=False
        )

        print(f"Saved to: {output_file}")

        # Save scaler
        joblib.dump(
            self.scaler,
            os.path.join(
                self.output_dir,
                "scaler.pkl"
            )
        )

        # Save encoders
        joblib.dump(
            self.label_encoders,
            os.path.join(
                self.output_dir,
                "label_encoders.pkl"
            )
        )

    #######################################################################
    # RUN COMPLETE PIPELINE
    #######################################################################

    def run(self):

        self.load_data()

        self.dataset_summary()

        self.clean_data()

        self.handle_missing_values()

        self.feature_engineering()

        self.encode_features()

        self.scale_features()

        X_train, X_test, y_train, y_test = self.train_test_split()

        self.save_processed_data()

        print("\nPreprocessing Complete!")

        return (
            X_train,
            X_test,
            y_train,
            y_test
        )


#######################################################################
# MAIN
#######################################################################

if __name__ == "__main__":

    processor = DataPreprocessor(
        data_path="../data/synthetic_health_data.csv"
    )

    X_train, X_test, y_train, y_test = processor.run()
