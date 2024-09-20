import pickle

class MyClass:
    def __init__(self, message):
        self.message = message

    def display(self):
        return self.message

# Criando uma instância da classe
obj = MyClass("cat /etc/passwd")

# Serializando o objeto
serialized_obj = pickle.dumps(obj)

# Serialization in File
with open("data.pkl", "wb") as file:
    file.write(serialized_obj)

# Loading
with open("data.pkl", "rb") as file:
    loaded_obj = pickle.load(file)

# Deserialization
print(loaded_obj.display())
