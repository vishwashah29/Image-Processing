import pickle

# store pickle object
color_dic={'red':0,'green':1 , 'blue':2}
pickle_out=open('dict.pickle','wb')
pickle.dump(color_dic,pickle_out)
pickle_out.close()

# recover pickle object

pickle_in=open('dict.pickle','rb')
c_dict=pickle.load(pickle_in)
print(c_dict)
pickle_in.close()
print(c_dict['blue'])