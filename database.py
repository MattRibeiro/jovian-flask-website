from sqlalchemy import create_engine, text
import json, os

# take a results.all() results and convert to list of dicts
def sqlresults_to_dict(results):
  return [dict(record._mapping) for record in results]

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * FROM jobs;"))
    return sqlresults_to_dict(result.all())

# DB_CONNECT_DATA schema:
# {
#   "database": "secret",
#   "username": "secret",
#   "host":     "secret",
#   "password": "secret"
# }
db = json.loads(os.environ['DB_CONNECT_DATA'])

# The exact format for this came from a sqlalchemy example for MariaDB
# https://docs.sqlalchemy.org/en/20/dialects/mysql.html#mariadb-support
connect_string = f"mysql+pymysql://{db['username']}:{db['password']}@{db['host']}/{db['database']}?charset=utf8mb4"

# somehow this is enough to connect securely to the db. My guess is that
# the SSL connection finds a trusted CA in the system ahead of this ficticous
# ca.pem file (as far as I know, it doesn't exist)
connect_args = {"ssl": {"ssl_ca": "ca.pem"}}

engine = create_engine(connect_string, connect_args=connect_args)
