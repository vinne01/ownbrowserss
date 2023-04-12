import pickle
l=[2,3,4,5,6,7,8]
file=open("vijj.txt","wb")
pickle.dump(l,file)
file.close()
