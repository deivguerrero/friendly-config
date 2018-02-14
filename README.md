# Friendly Configuration.  

Simple wrapper for yaml files.  

```python
import mconfig

mconfig.load("/path/file.yml")

mconfig.get("key.subkey")
```  

- **mconfig.load(path:str)** : 
	- Expect an absolute path (str) of the yml file.

- **mconfig.get(key:str, response:Object)**: 
	- Wait for a key (str) in the format "key", "key.sub_key", "key.sub_key1. ··· .sub_keyN".  
	- If the key exists it will return its contents, otherwise it will return response (default None).  

**Enjoy!**