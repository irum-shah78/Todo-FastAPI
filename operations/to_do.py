import sys
sys.path.append('./')
from connection import db_session
from model.sql_model import Todo
import decoders.todo as decode

def create_to_do(todo: str) -> dict:
  try:
    req = Todo(todo)
    db_session.add(req)
    db_session.commit()
    return {
      'status': 'ok',
      'message': 'Todo Added'
    }
  except Exception as e:
    db_session.rollback(res)
    return{
      'status': 'error',
      'message': str(e)
    }
  
# def get_all():
#   res = db_session.query(Todo).all()
#   docs = decode.decode_todos()
#   return { 'status': 'ok', 'data': docs}


def get_all():
  try:
    res = db_session.query(Todo).all()
    docs = decode.decode_todos(res)
    return { 'status': 'ok', 'data': docs}
  except Exception as e:
    db_session.rollback(res)
    return{
      'status': 'error',
      'message': str(e)
    }
  
def get_one(_id:int):
  try:
    criteria = {'_id': _id}
    res = db_session.query(Todo).filter_by(**criteria).one_or_none()
    if res is not None:
      record = decode.decode_todo(res)
      return{
      'status': 'ok',
      'data': record
    }
    else: 
      return {  
      'status': 'error',
      'message': f'Record with id {_id} do not Exist!!'
    }
  except Exception as e:
    db_session.rollback(res)
    return{
      'status': 'error',
      'message': str(e)
    }
  
def update_todo(_id:int , title: str ):
  try:
    criteria = {'_id': _id}
    res = db_session.query(Todo).filter_by(**criteria).one_or_none()
    if res is not None:
      record = res.todo = title
      db_session.commit()
      return{
      'status': 'ok',
      'message': 'Record Updated!!'
    }
    else: 
      return {  
      'status': 'error',
      'message': f'Record with id {_id} do not Exist!!'
    }
  except Exception as e:
    db_session.rollback(res)
    return{
      'status': 'error',
      'message': str(e)
    }
  
def delete_todo(_id:int ):
  try:
    criteria = {'_id': _id}
    res = db_session.query(Todo).filter_by(**criteria).one_or_none()
    if res is not None:
      db_session.delete(res)
      db_session.commit()
      return{
      'status': 'ok',
      'message': 'Record Deleted!!'
    }
    else: 
      return {  
      'status': 'error',
      'message': f'Record with id {_id} do not Exist!!'
    }
  except Exception as e:
    db_session.rollback(res)
    return{
      'status': 'error',
      'message': str(e)
    }

# res = create_to_do("Todo one")
# print(res)

# res = get_all()
# print(res)

# res = get_one(3)
# print(res)

# res = update_todo(2, 'Todo Updated' )
# print(res)

# res = delete_todo(2)
# print(res)