import pickle

def to_pickle(obj, file, method):
    f = open(file, method)
    pickle.dump(obj, f)
    f.close()
