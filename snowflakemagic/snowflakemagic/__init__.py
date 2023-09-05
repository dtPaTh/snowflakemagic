__version__='1.0.0'

from .snowflakemagic import Snowflakemagic

def load_ipython_extension(ipython):
    ipython.register_magics(Snowflakemagic)
