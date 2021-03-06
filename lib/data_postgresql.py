# Ron Mitsugo Zacharski
#
#   BP1 (best practices 1): Code that is database specific 
#   should be in a separate file
#
from datetime import date
import psycopg2
import psycopg2.extras

from lib.config import *

def connectToPostgres():
  connectionString = 'dbname=%s user=%s password=%s host=%s' % (POSTGRES_DATABASE, POSTGRES_USER, POSTGRES_PASSWORD,POSTGRES_HOST)
  print connectionString
  # BP2  Use try-except blocks
  try:
    return psycopg2.connect(connectionString)
  except Exception as e:    # BP2 especially this part where you print the exception
  	print(type(e))
	print(e)
	print("Can't connect to database")
	return None
	



# generic execute statement
# select=True if it is a select statement
#        False if it is an insert
#
def execute_query(query, conn, select=True, args=None):
	print "in execute query"
	cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
	results = None
	try: 
		quer = cur.mogrify(query, args)   # BP6  never use Python concatenation
		                                  # for database queries
		cur.execute(quer)
		if select:
			results = cur.fetchall()
		conn.commit()   # BP5  commit and rollback frequently
	except Exception as e:
		conn.rollback()
		print(type(e))
		print(e)
	cur.close()      # BP3 Dispose of old cursors as soon as possible
	return results

#
#  app specific
#



def new_event(name, day, etime, location,contact):
	conn = connectToPostgres()
	if conn == None:
		return None
	query_string = "INSERT INTO events (name, day, etime, location,contact) VALUES (%s, %s, %s, %s, %s)"
	execute_query(query_string, conn, select=False,  args=(name, day, etime, location,contact))
	conn.close()   # BP4 keep connection open as long as required
	return 0

def get_todays_events():
	today = date.today()
	todayF = today.isoformat()
	conn = connectToPostgres()
	if conn == None:
		return None
	query_string = "SELECT * FROM events WHERE day = %s"
	results = execute_query(query_string, conn,  args=(todayF,))
	conn.close()
	return results


def get_all_events():
	conn = connectToPostgres()
	if conn == None:
		return None
	query_string = "SELECT * FROM events"
	results = execute_query(query_string, conn)
	conn.close()
	return results


def add_member(name, phone, email, password, about):
	conn = connectToPostgres()
	if conn == None:
		return None

	# BP7  Never store passwords in the clear

	query_string = "INSERT INTO members (name, phone, email, password, about) VALUES (%s, %s, %s, crypt(%s, gen_salt('bf')), %s)"
	execute_query(query_string, conn, select=False,  args=(name, phone, email, password, about))
	conn.close()

