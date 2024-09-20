# Remote Code Execution

3 types of RCE:

Injection Attacks: Applications, like those using SQL, take user input as commands. In an injection attack, an attacker sends malformed input that gets executed as part of the command, allowing them to manipulate the application or run arbitrary code.

Out-of-Bounds Write: Applications allocate fixed memory for data. If done incorrectly, an attacker can send input that overwrites memory, potentially allowing them to execute code stored there.

Deserialization Attacks: Apps often combine data into a single string for easier transmission. If a user sends specially formatted data, it might be treated as executable code during deserialization.

## About RCE Deserialization 

Serialization gathers data from objects, converts them to a string of bytes, and writes them to disk. The data can be deserialized and the original objects can be recreated. 

## What is Pickle?
Pickle is a Python module that allows you to serialize and deserialize objects. Serialization is essential when you want to persist a data or send it across a network.

# References

https://www.imperva.com/learn/application-security/remote-code-execution/