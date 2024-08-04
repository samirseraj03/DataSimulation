from fastapi import FastAPI  , Request 
from fastapi.responses import HTMLResponse , JSONResponse 
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.encoders import jsonable_encoder
from starlette.requests import Request

import QueryDatabase

 

app = FastAPI()

# Ruta para servir archivos estáticos como javascript y css
app.mount("/static", StaticFiles(directory="static"), name="static")
# para servir templates de html
templates = Jinja2Templates(directory="templates")
 
 
# Ruta para servir el index.html
@app.get("/", response_class=HTMLResponse)
async def read_index():
    index_file = Path("templates/index.html")
    return index_file.read_text(encoding="utf-8")



@app.get("/simulations", response_class=HTMLResponse)
async def get_simulations(request : Request):
    try:
        data = QueryDatabase.get_simulations()
        if data:
            return JSONResponse(content=jsonable_encoder(data), status_code=200)
        else:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)



    
@app.get("/simulations/{state}", response_class=HTMLResponse)
async def get_simulations( state: str , request : Request):
    try:
        data = QueryDatabase.filter_simulations_bystat(state)
        if data:
            return JSONResponse(content=jsonable_encoder(data), status_code=200)
        else:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)
    


@app.get("/order", response_class=HTMLResponse)
async def order_simulations(request : Request):
    
    try:
        data = QueryDatabase.OrderList()
        if not data:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
        else:
            return JSONResponse(content=jsonable_encoder(data), status_code=200)

    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)




@app.get("/machines/available", response_class=HTMLResponse)
async def get_machines_avaiable(request : Request):
    try:
        data = QueryDatabase.get_machines_available()
        if data:
            return JSONResponse(content=jsonable_encoder(data), status_code=200)
        else:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)



# class SimulationData(BaseModel):
#     simulation_id: str
#     name: str
#     status : str
#     start_date : str
#     end_date : str
#     machine_id : str



@app.post("/simulations", response_class=HTMLResponse)
async def create_simulations(request: Request):

    form_data = await request.form()  # Obtener datos del formulario
    data = {key: form_data.get(key) for key in form_data}
    
    try:
        data = QueryDatabase.post_simulation()
        if data:
            return JSONResponse(content=data, status_code=200)
        else:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)
    


@app.get("/simulations/detailed/{id_simulation}", response_class=HTMLResponse)
async def get_detailed_simulation(id_simulation: str , request : Request):
    try:
        data = QueryDatabase.get_detailed_simulation(id_simulation)
        if data:
            return JSONResponse(content=jsonable_encoder(data), status_code=200)
        else:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)
    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)




""" function check is machine running , if running , frontend  recive the machine is ruuning to do grafh in realtime
    else the frontend recive all data  """
@app.get("/simulations/data/{id_simulation}", response_class=HTMLResponse)
async def get_data_simulation(id_simulation: str , request : Request):

    try:     
        data = QueryDatabase.get_data_simulations_realtime(id_simulation)  
        if not data or len(data) == 0:
            return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

        data = data[0]
        if data[7] == 'running':
            return JSONResponse(content=jsonable_encoder(data), status_code=200)
        else:    
            # Cuando el estado ya no es 'running', obtenemos los datos completos de la simulación
            data = QueryDatabase.get_data_simulations(id_simulation)
            if not data or len(data) == 0:
                 return templates.TemplateResponse("404.html", {"request": request}, status_code=404)

            return JSONResponse(content=(data), status_code=200)

    except Exception as e:
        print(e)
        return templates.TemplateResponse("500.html", {"request": request}, status_code=500)




# Ejecutar la aplicación usando uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
