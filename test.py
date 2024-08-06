from fastapi.testclient import TestClient
from fastapi.encoders import jsonable_encoder


from main import app
import QueryDatabase

client = TestClient(app)




# testing filter
def test_filter_state():
    try:

        response = client.get("/simulations/running")
        data = QueryDatabase.filter_simulations_bystat('running')
        assert response.json() == jsonable_encoder(data)
        assert response.status_code == 200
        print("Test passed: OK")

    except Exception as e :
        print ('Test passed: NO' , e)

# testing simulations
def test_simualtions():
    try:

        response = client.get("/simulations")
        data = QueryDatabase.get_simulations()
        assert response.json() == jsonable_encoder(data)
        assert response.status_code == 200
        print("Test passed: OK")

    except Exception as e :
        print ('Test passed: NO' , e)

# testing order
def test_read_order():
    try:

        data = QueryDatabase.OrderList()
        response = client.get("/order")

        assert response.json() == jsonable_encoder(data)
        assert response.status_code == 200
        print("Test passed: OK")
    
    except Exception as e :
        print ('Test passed: NO' , e)

# testing inserts
def test_insert_simulation(_list):
    try:
        #post with body 
        response = client.post("/simulations" , data=_list)
        # compare body request with _list
        assert response.json()[0][0] == _list["simulation_id"]
        print("Test passed: OK")
    except Exception as e :
        print ('Test passed: NO' , e)



if __name__ == '__main__':

    list = {
        'simulation_id' : 'SAM587',
       'name' : 'For IA' ,
       'status' : 'Pending',
       'start_date' : '2024-08-01 09:00:00',
       'end_date' : '2024-07-30 08:00:00',
       'machine_id' : 'MACHINE_F'
    }


    test_insert_simulation(list)
    test_simualtions()
    test_filter_state()
    test_read_order()