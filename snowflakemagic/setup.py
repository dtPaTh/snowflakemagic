from distutils.core import setup

setup(name='snowflakemagic',
      version='0.1',
      description='Query Snowflake using magic functions',
      author='Patrick Thurner',
      author_email='patrick.thurner@gmail.com',
      install_requires=['snowflake-connector-python','python-dotenv']

     )

