def prediction(model, data):
    # predict new data using the model
    result = model.predict(data)  
    return result