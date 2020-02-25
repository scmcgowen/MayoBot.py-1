import importlib
import urllib.request
import os
import discord
import requests
from discord.ext import commands


def download_module(url: str, name: str):
    urllib.request.urlretrieve(url, './modules/' + name + '.py')


def check_module(name: str) -> str:

    klass = []
    try:
        my_module = importlib.import_module("modules.%s" % name)
        klass = getattr(my_module, name)

        if issubclass(klass, commands.Cog):
            print("Successfully loaded module %s." % name)
            return "fine"
        else:
            print("Couldn't load module/class %s: Module does not extend to 'commands.Cog'" % name)
            return "Module does not extend to 'commands.Cog'"

    except ImportError as e:
        print("Couldn't load module/class %s: ImportError" % name)
        print(str(e))
        return str(e)
    except AttributeError as e:
        print("Couldn't load module/class %s: AttributeError" % name)
        print(str(e))
        return str(e)
    except Exception as e:
        print("Couldn't load module/class %s: Generic error:%s" %(name, str(e)))
        return str(e)


def delete_module_file(name: str):
    if os.path.isfile("modules/%s.py" % name):
        os.remove("modules/%s.py" % name)
    else:
        raise FileNotFoundError
