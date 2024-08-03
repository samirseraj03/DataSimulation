
from dotenv import load_dotenv
from datetime import datetime , timedelta

import psycopg2
import os
import tools

# load  variabls
load_dotenv()


class Database:
    # Constructor
    def __init__(self):
        self.host = os.getenv('HOST')
        self.port = os.getenv('PORT')
        self.dbname = os.getenv('DBNAME')
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.connection = None
        self.cursor = None
    # Connect to database
    def connect(self):
        self.connection = psycopg2.connect(
            host=self.host,
            port=self.port,
            dbname=self.dbname,
            user=self.user,
            password=self.password
        )
        self.cursor = self.connection.cursor()



    def execute(self, query):
        self.cursor.execute(query)
        return self.cursor.fetchall()
    

    def commit(self):
        if self.connection:
            self.connection.commit()
            print("Transacción confirmada.")

    # Revertir cambios
    def rollback(self):
        if self.connection:
            self.connection.rollback()
            print("Transacción revertida.")
    
    # close connection
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()
        print("Conexión cerrada.")

    # willenter database
    def __enter__(self):
        self.connect()
        return self

    # willexit database
    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print(f"Exception: {exc_val}")
        try:
            if exc_type is None:  # Solo confirmar si no hubo excepción
                self.commit()
        except Exception as e:
            print(f"Commit error: {e}")
            self.rollback()  # Revertir cambios en caso de error durante commit
        finally:
            self.close()



# function to get all simulations
def get_simulations():
    # Uso de la clase Database
    try:
        query = f"""SELECT * FROM simulations _s 
                INNER JOIN machines _m ON  _s.machine_id = _m.machine_id"""

        # use class data base to get query
        with Database() as db:
            rows = db.execute(query)
            return rows
            #for row in rows:
            #     print(row)

    except Exception as e:
        print(f"Problem has occurried: {e}")


def filter_simulations_bystat(state):
    states = ['pending' , 'running' , 'finished' ]
    try:
        if (state in states):
            query = f"""SELECT * FROM simulations _s 
                FULL JOIN machines _m ON  _s.machine_id = _m.machine_id 
                WHERE _s.status = '{state}'"""
            print (query)
            with Database() as db:
                rows = db.execute(query)
                for row in rows:
                  print(row)
                return rows 
    except Exception as e:
        print(f"Problem has occurried: {e}")


def OrderList():
    try:
            query = """SELECT * FROM simulations _s 
            FULL JOIN machines _m ON  _s.machine_id = _m.machine_id 
            ORDER BY _s.name , start_date"""
            with Database() as db:
                rows = db.execute(query)
                return rows 
    except Exception as e:
        print(f"Problem has occurried: {e}")


def get_machines_available():
    try:
            query = """SELECT  _m.*,'available' AS available
                    FROM  machines _m
                    LEFT JOIN simulations _s ON _s.machine_id = _m.machine_id
                    WHERE _s.machine_id IS NULL AND _m.type_machine = 'fixtures';"""
            print (query)
            with Database() as db:
                rows = db.execute(query)
                for row in rows:
                  print(row)
                return rows 
    except Exception as e:
        print(f"Problem has occurried: {e}")



def post_simulation(list):
    
    try:
        query = f"""INSERT INTO simulations (simulation_id , name , status , start_date , end_date , machine_id) values (
                '{list['simulation_id']}' , '{list['name']}' , '{list['status']}' , '{list['start_date'] }', '{list['end_date']}' , '{list['machine_id']}' ) returning simulation_id"""
        with Database() as db:
            rows = db.execute(query)   
            for row in rows:
                print(row)
                return rows         
    except Exception as e:
        print(f"Problem has occurried: {e}")


def get_detailed_simulation(simulation_id):

    try:
        query = f""" SELECT * FROM simulations WHERE simulation_id = '{simulation_id}' """
        with Database() as db:
            rows = db.execute(query)   
            for row in rows:
                print(row)
                return rows         
    except Exception as e:
        print(f"Problem has occurried: {e}")


def get_data_simulations_realtime(simulation_id):
    try:
        query = f""" SELECT * FROM data_simulations INNER JOIN simulations _s ON  _s.simulation_id = data_simulations.simulation_id  
                 WHERE data_simulations.simulation_id = '{simulation_id}' ORDER BY data_id  DESC LIMIT 1; """
        with Database() as db:
            rows = db.execute(query)   
            for row in rows:
                print(row)
                return rows         
    except Exception as e:
        print(f"Problem has occurried: {e}")


def get_data_simulations(simulation_id):
    try:
        query = f""" SELECT * FROM data_simulations WHERE simulation_id = '{simulation_id}'  """
        with Database() as db:
            rows = db.execute(query)   
            for row in rows:
                print(row)
                return rows         
    except Exception as e:
        print(f"Problem has occurried: {e}")


if __name__ == '__main__':

    get_data_simulations_realtime('SIM456')

