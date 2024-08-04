# SimulationOriginAI


Spanish : 

    El test se trata de gestionar simulaciones de herramientas para maquinas
    
        - cosas que he utilizado:

            - postgres:
                - He utilizado postgresSql para la base de datos.
                - He utilizado la libreria psycopg2 para connectar a la basede datos en python.
                        - separe las funciones de solicitud de postgres de la apis para hacer una simulacion de MVC.
                        - se hizo una classe de database , he incluido la connexion de base de datos y desconnexion automaticos para no repetir el mismo codigo.
                        - he incluido en la classe commit , rollback cuando se insertan nuevos datos
                        - se hizo funciones para cada probelma presentada , dejando el codigo sea lo mas bastante limpio
            
            - FastApi
                - He utilizado fastApi porque hice una busqueda que es lo que se utilizaba en la empresa y opte por FastApi , espero que sea este framworks :) , la verdad nunca lo he utilizado pero me ha ido bien desarollar las Apis con fastApi aunque si que es verdad que me llevo un timepo por las dificultades.
                tambien tengo algunas preguntas

                    1. cuando se hace una solictud a la base de datos , solo se me devlovia una lista sin el nombre para cada variable y entonces accedia desde la posistion de la lista
                    como se puede conseguir que la lista sea un objeto json
                    2. debo crear alguna interfaz ?

                - Lo mismo en la base de datos , hice las apis de fast api para cada consulta y he incluido las funcinoes de base de datos para cada api correspondiente 

