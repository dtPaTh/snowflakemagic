# Snowflake Magic 

An ipython magic function allowing to use Snowflake SQL in your notebooks.

## Setup and Configuration

### Install the extension

```
pip install ./snowflakemagic
```

### Load extension
```
%reload_ext dqlmagic
```

## Available magic functions

### %snowflake_auth
Inline function connecting to your snowflake account. Reads connection parameters from .env file:

You can either authenticate via SSO, which opens an external browser, or using credentials. 

```snowflake_account="<YOUR-SNOWFLAKE-ACCOUNT>"```

If you want to connect via sso, provide your sso username: 

```snowflake_ssouser="<YOUR-SSO-USERNAME>"```

If you want to connect via use-credentials, provide the password, otherwise SSO authentication is used.
```
snowflake_user="<YOUR-USERNAME>"
snowflake_password="<YOUR-PASSWORD>"
```

For more details on .env file see [How to NOT embedded credential in Jupyter notebook](https://yuthakarn.medium.com/how-to-not-show-credential-in-jupyter-notebook-c349f9278466) or [python-dotenv](https://pypi.org/project/python-dotenv/)


### %snowflake and %%snowflake
You can query snowflake using either inline or cell functions. The response is returned in json format.

## Getting Started
If you are new to Jupyter notebooks, I recommend getting started using Jupyter notebooks in Visual Studio Code

1. Create your credentials as described above. 
2. Configure .env file
3. Start using getting-started.ipynp to learn how to use the magic functions
