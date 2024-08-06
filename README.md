# SimulationOriginAI


     - preguntas
                    1. cuando se hace una solictud a la base de datos , solo se me devlovia una lista sin el nombre para cada variable y entonces accedia desde la posistion de la lista
                    como se puede conseguir que la lista sea un objeto json ?
                    
                    3. la orginizacion de los archivos/carpetas no los tengo del todo claro si esta bien organizado o no ? 


como utilizar la app. 

    simplemente desgarga docker y luego ejucuta docker compose up -d , recuerda modificar el env si es necesario aunque no deberia!

    puedes hacer test con test.py 
        docker exec -it simulationoriginai-python-1 /bin/bash
        luego python test.py

    casos de uso que puedes utilizar la app:
        - puedes acceder al /  desde el navegador
        - consulta las siguentes api
            - puede ser desde postman o fastapi docs 
                -metodo Get:
                    - /simulations
                        - devuelve todas las simulaciones
                    - /simulations/{state} pending , running or finished
                        - devuelve la simulaciones filtrado por estado
                    - /order
                        - devuelve lista ordenada de las simulaciones desde el nombre y la fecha
                    - /machines/available 
                        - devuelve maquinas disponibles
                    - /simulations/detailed/{id_simulation} 
                        - ejemplo  'SAM105'  devuelve detalles de la simulacion
                    - /simulations/grafic/{id_simulation} 
                        - ejemplo  'SAM105'  devulve una grafica en base64 
                    - /simulations/data/{id_simulation}   
                        - ejemplo  'SAM105' para obtener los datos sea en tiempo real o cuando ya se ha acabado
                - metodo Post
                    - /simulations 
                        para agregar nueva simulacion

                        siga esta lista y ponlo en el body:
                            {
                            'simulation_id' : 'SAM105',
                            'name' : 'For IA' ,
                            'status' : 'Pending',
                            'start_date' : today,
                            'end_date' : today,
                            'machine_id' : 'MACHINE_F' 
                            }

how use app:

    Simply download Docker and then run docker-compose up. Remember to modify the .env file if necessary, although it shouldn’t be required!

    you can test with test.py
        docker exec -it simulationoriginai-python-1 /bin/bash
        then python test.py


    Use cases for the app:

            You can access the root / from your browser to see graph example , this graph use api .
            Consult the following APIs:
                This can be done using Postman or FastAPI docs.
                    GET Method:
                        /simulations
                            Returns all simulations.
                        /simulations/{state} (pending, running, or finished)
                            Returns simulations filtered by state.
                        /order
                            Returns an ordered list of simulations by name and date.
                        /machines/available
                            Returns available machines.
                        /simulations/detailed/{id_simulation}
                            For example, 'SAM105' returns details of the simulation.
                        /simulations/grafic/{id_simulation}
                            For example, 'SAM105' returns a base64-encoded graphic.
                        /simulations/data/{id_simulation}
                            For example, 'SAM105' returns data, whether in real-time or once it has finished.
                    POST Method:
                            /simulations

                                To add a new simulation.
                                Follow this list and include it in the body:

                            {
                                'simulation_id': 'SAM105',
                                'name': 'For IA',
                                'status': 'Pending',
                                'start_date': today,
                                'end_date': today,
                                'machine_id': 'MACHINE_F'
                            }


Spanish : 

    El test se trata de gestionar simulaciones de herramientas para maquinas
    
        - para cada funcion explico lo que hace en ingles
        - cosas que he utilizado:

            - postgres:
                - He utilizado postgresSql para la base de datos.
                - He utilizado la libreria psycopg2 para connectar a la basede datos en python.
                        - separe las funciones de solicitud de postgres de la apis para hacer una simulacion de MVC.
                        - se hizo una classe de database , he incluido la connexion de base de datos y desconnexion automaticos para no repetir el mismo codigo.
                        - he incluido en la classe commit , rollback cuando se insertan nuevos datos
                        - se hizo funciones para cada probelma presentada , dejando el codigo sea lo mas bastante limpio

            - FastApi
                - He utilizado fastApi porque hice una busqueda que es lo que se utilizaba en la origen y opte por FastApi , espero que sea este framworks :) , la verdad nunca lo he utilizado pero me ha ido bien desarollar las Apis con fastApi aunque si que es verdad que me llevo un timepo por las dificultades.
                tambien tengo algunas preguntas


                - Lo mismo en la base de datos , hice las apis de fast api para cada consulta y he incluido las funcinoes de base de datos para cada api correspondiente 
                - simule cuando se manejan los errores poniendo htmls de 404 y 500 , aunque esten vacios.
                - puse que se devuelva estados de cada funcion 200 , 404 o 500

            - docker
                - he creado un docker compose para instalar dos contenedores para la base de datos y otro para el backend
                - he creado un dockerfile para instalar los requirimientos para que funciones las apis
                - el docker compose debe poder instalar los contendedors y insertar la informacion de base de datos y ejecutar fastApi automaticamente

            - test
                - utilize postman para hacer las comprobaciones que funcionban las apis , aunque mas tarde descubri fastApi docs
                - he creado test.py para comprobar las Apis funcionan bien



            Grafica de datos:
                - en tools he creado una funcion para crear una grafica que gestiona  los datos que obtenemos de la simulacion


english:

    The test is about managing tool simulations for machines

        For each function, I explain what it does in English

        Things I have used:

        PostgreSQL:

        - I used PostgreSQL for the database.
        - I used the library psycopg2 to connect to the database in Python.
        - I separated the PostgreSQL request functions from the APIs to simulate an MVC structure.
        - I created a database class, including automatic database connection and disconnection to avoid repeating the same code.
        - I included commit and rollback in the class when new data is inserted.
        - I created functions for each presented problem, keeping the code as clean as possible.
        FastAPI:

        - I used FastAPI because, after some research, I found it was being used initially, so I chose FastAPI. I had never used it before, but developing APIs with FastAPI went well, though it took some time due to difficulties. I also have some questions.
        Similarly to the database, I made FastAPI APIs for each query and included the database functions for each corresponding API.
        - I simulated error handling by including 404 and 500 HTMLs, even though they are empty.
        - I ensured that each function returns status codes 200, 404, or 500.
        Docker:

        - I created a Docker Compose file to set up two containers, one for the database and another for the backend.
        - I created a Dockerfile to install the requirements for the APIs to function.
            - The Docker Compose should be able to set up the containers, insert the database information, and automatically run FastAPI.
        test:

        - I used Postman to check if the APIs were working, although I later discovered FastAPI docs.
        - I have created test.py to check the APIs are working fine


        Data Graph:
        - In tools, I created a function to generate a graph that manages the data obtained from the simulation.

  





       