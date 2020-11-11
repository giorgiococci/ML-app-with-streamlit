def feature_engineering(pipeline, dataframe):
    # Transform the dataframe using a pipeline
    result = pipeline.transform(dataframe)
    return result