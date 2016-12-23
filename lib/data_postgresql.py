# Ron Mitsugo Zacharski
#
#
from datetime import date
import psycopg2
import psycopg2.extras

from lib.config import *

def connectToPostgres():
  connectionString = 'dbname=%s user=%s password=%s host=%s' % (POSTGRES_DATABASE, POSTGRES_USER, POSTGRES_PASSWORD,POSTGRES_HOST)
  print connectionString
  try:
    return psycopg2.connect(connectionString)
  except Exception as e:
  	print(type(e))
	print(e)
	print("Can't connect to database")


# generic execute statement
# select=True if it is a select statement
#        False if it is an insert
#
def execute_query(query, conn, select=True, args=None):
	print "in execute query"
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	results = None
	try: 
		quer = cur.mogrify(query, args)
		cur.execute(quer)
		if select:
			results = cur.fetchall()
		conn.commit()
	except Exception as e:
		conn.rollback()
		print(type(e))
		print(e)
	cur.close()
	return results

#
#  app specific
#



def new_event(name, day, etime, location,contact):
	conn = connectToPostgres()
	query_string = "INSERT INTO events (name, day, etime, location,contact) VALUES (%s, %s, %s, %s, %s)"
	execute_query(query_string, conn, select=False,  args=(name, day, etime, location,contact))
	conn.close()

def get_todays_events():
	today = date.today()
	todayF = today.isoformat()
	conn = connectToPostgres()
	query_string = "SELECT * FROM events WHERE day = %s"
	results = execute_query(query_string, conn,  args=(todayF,))
	conn.close()
	return results


def get_all_events():
	conn = connectToPostgres()
	query_string = "SELECT * FROM events"
	results = execute_query(query_string, conn)
	conn.close()
	return results


def add_member(name, phone, email, about):
	conn = connectToPostgres()
	query_string = "INSERT INTO members (name, phone, email, about) VALUES (%s, %s, %s, %s)"
	execute_query(query_string, conn, select=False,  args=(name, phone, email, about))
	conn.close()

