import h5py
import numpy as np
import pickle
kd = pickle.load(open("all_data.pickle2","r"))
fi = h5py.File("kdd1999.h5py","w")
X = []
y = []
for value,label in kd:
    X.append(value)
    y.append(label)
X = np.array(X)
y = np.array(y)
dataset = fi.create_dataset("features",data= X)
dataset0 = fi.create_dataset("targets",data=y)
print "Conversion completed"
fi.close()