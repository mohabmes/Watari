# Watari
Modular voice command-line virtual assistant. 

## How to write custom module
```
from core.Module import Module

class CustomModule(Module):
    priority = 0
    disable = False

    def __init__(self):
        self.keywords = ['Custom', 'Module'] # Keywords to activate this module whenever called.

    def get_keywords(self):
        return self.keywords

    def get_priority(self):
        return self.priority

    def loop(self, keyword):
        # Do something every 30 minutes.
        pass

    def start(self, keyword):
         # Do something when any of the keywords is called.
         pass
```
- Add the class to `/modules` directory.
- Register your CustomModule class to `/modules/__init__.py`
- Take a look at [Time module](https://github.com/mohabmes/Watari/blob/main/modules/Time.py).

## Read additional configs
- To read the additional config array of a certain custom module use `get_config()` specified in `config/config.json` file.

### Requiement
- numpy
- gtts
