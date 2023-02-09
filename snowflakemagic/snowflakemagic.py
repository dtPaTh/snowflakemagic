from IPython.core.magic import (Magics, magics_class, line_magic, line_cell_magic)
import snowflake.connector
import os
from dotenv import load_dotenv 

@magics_class
class Snowflakemagic(Magics):

    connection = None
    username = None
    password = None
    account = None

    @line_magic('snowflake_auth')
    def auth(self, line):        
        
        load_dotenv() # add this line
    
        self.account = os.getenv('snowflake_account')

        sso_user = os.getenv('snowflake_ssouser')
        if len(sso_user.strip()) > 0:
            self.username = sso_user
            self.connection = snowflake.connector.connect(
                authenticator='externalbrowser',    
                user=self.username,
                account=self.account,
            )

        else: 
            self.username = os.getenv('snowflake_username')
            self.password = os.getenv('snowflake_password')
            self.connection = snowflake.connector.connect(
              user=self.username,
              password=self.password,
              account=self.account,
            )
            
        return None
    
    
    @line_cell_magic('snowflake')
    def executecell(self, line, cell=''):        
        if self.username: 
            if len(cell) > 0:
                try:
                    cursor = self.connection.cursor(snowflake.connector.DictCursor)
                    results = []               
                    
                    cmds = cell.split(";")[:-1]
                    if len(cmds) == 0: 
                        cmds = [cell]

                    for cmd in cmds:
                        cmd.strip()
                        if len(cmd) > 0 :
                            result = cursor.execute(cmd).fetchall()
                            results.append(result)                
                    
                    if len(line) > 0:
                        self.shell.user_ns.update({line: results[-1]})
                finally:
                    try:
                        cursor.close()
                    except Exception as e:
                        return e
                
                if len(line) == 0:
                    return results[-1]
                else: 
                    return "Succesfully executed query"
            else:
                try:
                    cursor = self.connection.cursor(snowflake.connector.DictCursor)
                    result = cursor.execute(line).fetchall()
                finally:
                    try:
                        cursor.close()
                    except Exception as e:
                        return e

                    return result
        else: 
            return None

    @line_magic('snowflake_script')
    def executescript(self, line):        
        if len(line) > 0 and os.path.isfile(line):
            with open(line) as f:
                contents = f.read()
                return self.executecell(line='',cell=contents)
        else: 
            return "Script not found!"

    def __del__(self):
        self.connection.close()