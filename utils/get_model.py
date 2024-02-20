import pickle

model = pickle.load(open('model.pkl', 'rb'))

def get_model():
    return model
