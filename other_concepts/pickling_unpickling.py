
import pickle

f= open("txt.txt",'ab')
value=10
pickle.dump( value,f)

f =open("txt.txt",'r')
value = pickle.load(f)

print(value)

