import getpass
import pg8000

# class Login:
#     def __init__(self):
#         # Database credentials
#         self.params = {
#             'database': 'csci403',
#             "user": username,
#             "password": "urpassword",
#             "host": 'ada.mines.edu'
#         }

#     def db(self):
#         """Returns a connection object to the database."""
#         return pg8000.connect(**self.params)

def connect():
    login = input("Username: ")
    secret = getpass.getpass()

    credentials = {'user'    : login,
                'password': secret, 
                'database': 'csci403',
                'host'    : 'ada.mines.edu'}

    db = pg8000.connect(**credentials)

    cursor = db.cursor()
    cursor.execute(f"SET search_path TO group120798")

def execute_query(db, query):
    try:
        # The 'with' block ensures the cursor is closed automatically
        with db.cursor() as c:
            c.execute(query)
            result = c.fetchall()
            print(result)

            # Commit changes for INSERT/UPDATE/DELETE
            db.commit() 
            
            # Fetch results for SELECT queries
            if c.description:
                result = c.fetchall()
            else:
                result = True # Success indicator for non-SELECTs
                
            return result, None
            
    except Exception as e:
        db.rollback()  # Undo changes if an error occurs
        return None, str(e)
    finally:
        db.close() # Always close the connection to free server resources

# --- Example Usage ---
# 1. Fetching data
# rows, error = execute_query("SELECT * FROM users WHERE id = %s", (1,))

# # 2. Inserting data
# success, error = execute_query("INSERT INTO users (name) VALUES (%s)", ("Alex",))
