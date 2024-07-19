# Polidoro Config

Polidoro Config it is a configuration manager for you project 

## Usage
Create a class inheriting from ConfigBase
```python
from pconfig import ConfigBase

class Config(ConfigBase):
	MY_VAR = 'default_value'
	...
```

When the class is instantiated will load from environment variables.

```python
# script.py
from pconfig import ConfigBase

class Config(ConfigBase):
	MY_VAR = 'default_value'

print(Config.MY_VAR)
```
```shell
>>> python script.py
default_value

>>> MY_VAR="new_value" python script.py
new_value
```

```{toctree}
:maxdepth: 1

apidocs/index
```


