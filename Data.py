import psycopg2

class Login:
    def __init__(self):
        # Database credentials
        self.params = {
            'database': 'csci403',
            "user": "beverly",
            "password": "hilt885HASHCH!",
            "host": 'ada.mines.edu'
        }

    def db(self):
        """Returns a connection object to the database."""
        return psycopg2.connect(**self.params)

def execute_query(query, args=None):
    login = Login()
    db = login.db()
    query = "set search_path to group120798;"
    try:
        # The 'with' block ensures the cursor is closed automatically
        with db.cursor() as c:
            query = "set search_path to group120798;"
            c.execute(query)
            query = "select * from games"
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
rows, error = execute_query("SELECT * FROM users WHERE id = %s", (1,))

# 2. Inserting data
success, error = execute_query("INSERT INTO users (name) VALUES (%s)", ("Alex",))