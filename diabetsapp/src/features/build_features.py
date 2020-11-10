import numpy as np
import pandas as pd
from sklearn.preprocessing  import StandardScaler

def readData(): 
    data = pd.read_csv('data/raw/diabetes.csv')
    return data

def replace_zeros(data):
    data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']] = data[['Glucose','BloodPressure','SkinThickness','Insulin','BMI']].replace(0, np.NaN)
    return data

def impute_median(data, var):
    """ Function to inpute the missing values with median based on Outcome class

    Args:
        data (Pandas.DataFrame): dataset
        var (string): colonna dove sostituire i valori null con la mediana

    Returns:
        [type]: [description]
    """
    temp = data[data[var].notnull()]
    temp = temp[[var, 'Outcome']].groupby(['Outcome'])[[var]].median()
    data.loc[(data['Outcome'] == 0 ) & (data[var].isnull()), var] = temp.loc[0 ,var]
    data.loc[(data['Outcome'] == 1 ) & (data[var].isnull()), var] = temp.loc[1 ,var]
    return data

def preprocessing(data):

    print("Starting feature engineering...")
    print("Replacing zeros values...")
    data = replace_zeros(data)

    print("Fill with median...")
    data = impute_median(data, 'Glucose')
    data = impute_median(data, 'BloodPressure')
    data = impute_median(data, 'SkinThickness')
    data = impute_median(data, 'Insulin')
    data = impute_median(data, 'BMI')

    #separate features and target as x & y
    y = data['Outcome']
    x = data.drop('Outcome', axis = 1)
    columns = x.columns

    #scale the values using a StandardScaler
    print('Applying Standard Scaler...')

    scaler = StandardScaler()
    scaler = scaler.fit(x)
    X = scaler.transform(x)

    #features DataFrame 
    features = pd.DataFrame(X, columns = columns)

    print('Finish preprocessing with success!')

    return features, y

if __name__ == "__main__":
    data = readData()
    preprocessing(data)