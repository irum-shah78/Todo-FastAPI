from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_user: str = 'postgres'
db_port: int = 5432
db_host: str = 'localhost'
db_password: str = 'admin'

uri: str = F'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/todo-app'

engine = create_engine(uri)

session = sessionmaker(
  bind=engine,
  autoflush=True
)

db_session = session()

try: 
  connection = engine.connect()
  connection.close()
  print('Connected!!!!')
except Exception as e:
  print(f'Error: {str(e)}')