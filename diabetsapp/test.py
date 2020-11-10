
import pandas as pd

from src.data import make_dataset
from src.features import build_features


if __name__ == "__main__":
    print("\n---- TEST FUNCTIONS -----\n")

    # Get the dataset path
    dataset_path = make_dataset.debug_path()

    df = pd.read_csv(dataset_path, sep=',', low_memory=False)
    print(f"Dataset: {df.head()}")

    # Feature Engineering
    X, y = build_features.preprocessing(df)

    # Train the Model
    