
-- verify if database exist
DO
$$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_language
        WHERE lanname = 'plpgsql'
    ) THEN
        CREATE LANGUAGE plpgsql;
    END IF;
END
$$;


DO $$
BEGIN
  IF NOT EXISTS (SELECT 1 FROM pg_database WHERE datname = 'MachineSimulator') THEN
    CREATE DATABASE MachineSimulator;
  ELSE
    RAISE NOTICE 'La base de datos MachineSimulator ya existe.';
  END IF;
END $$;


-- entry to data base
\c MachineSimulator;



-- Create table for machines
CREATE TABLE machines (
    machine_id VARCHAR PRIMARY KEY,
    machine_name VARCHAR NOT NULL,
    type_machine VARCHAR
);

-- Create table for simulations 
CREATE TABLE simulations (
    simulation_id VARCHAR PRIMARY KEY,
    name VARCHAR NOT NULL,
    status VARCHAR NOT NULL ,
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    machine_id VARCHAR,
    FOREIGN KEY (machine_id) REFERENCES machines(machine_id) --Match FOREIGN Key machine with simulations
);



-- Insert data into the machines table
INSERT INTO machines (machine_id, machine_name , type_machine ) VALUES
('MACHINE_A', 'Machine A' , NULL),
('MACHINE_B', 'Machine B' , NULL),
('MACHINE_C', 'Machine C', NULL),
('MACHINE_D', 'Machine D', NULL),
('MACHINE_E', 'Machine E' , NULL),
('MACHINE_F', 'Machine F' , 'fixtures');


-- table to show in grafic data in real time o time finnished
CREATE TABLE data_simulations (
    data_id SERIAL PRIMARY KEY,           
    simulation_id VARCHAR(255) NOT NULL,  
    machine_id VARCHAR(255) NOT NULL,    
    seconds INT NOT NULL,               
    loss FLOAT NOT NULL                   
);




-- Insert data into the simulations table
INSERT INTO simulations (simulation_id, name, status, start_date, end_date, machine_id) VALUES
('SIM123', 'Airflow Test', 'Pending', NULL, NULL, NULL),
('SIM456', 'Structural Analysis', 'In Progress', '2024-08-02 10:00:00', NULL, 'MACHINE_A'),
('SIM789', 'Traffic Simulation', 'Completed', '2024-07-31 15:30:00', '2024-08-01 02:15:00', 'MACHINE_B'),
('SIM101', 'Thermal Analysis', 'Pending', NULL, NULL, NULL),
('SIM102', 'Fluid Dynamics', 'In Progress', '2024-08-01 09:00:00', NULL, 'MACHINE_C'),
('SIM103', 'Mechanical Stress Test', 'Completed', '2024-07-30 08:00:00', '2024-07-30 20:00:00', 'MACHINE_D'),
('SIM104', 'Electric Field Simulation', 'Pending', NULL, NULL, NULL),
('SIM105', 'Acoustic Analysis', 'In Progress', '2024-08-03 11:00:00', NULL, 'MACHINE_E'),
('SIM106', 'Radiation Pattern Test', 'Completed', '2024-07-29 14:00:00', '2024-07-29 18:00:00', 'MACHINE_A'),
('SIM107', 'Network Traffic Simulation', 'Pending', NULL, NULL, NULL);



INSERT INTO data_simulations (simulation_id, machine_id, seconds, loss) VALUES
-- Datos para SIM456 (Machine_A)
('SIM456', 'MACHINE_A', 10, 0.45),
('SIM456', 'MACHINE_A', 20, 0.40),
('SIM456', 'MACHINE_A', 30, 0.35),
('SIM456', 'MACHINE_A', 40, 0.30),
('SIM456', 'MACHINE_A', 50, 0.25),

-- Datos para SIM789 (Machine_B)
('SIM789', 'MACHINE_B', 10, 0.55),
('SIM789', 'MACHINE_B', 20, 0.50),
('SIM789', 'MACHINE_B', 30, 0.45),
('SIM789', 'MACHINE_B', 40, 0.40),
('SIM789', 'MACHINE_B', 50, 0.35),

-- Datos para SIM102 (Machine_C)
('SIM102', 'MACHINE_C', 10, 0.50),
('SIM102', 'MACHINE_C', 20, 0.45),
('SIM102', 'MACHINE_C', 30, 0.40),
('SIM102', 'MACHINE_C', 40, 0.35),
('SIM102', 'MACHINE_C', 50, 0.30),

-- Datos para SIM105 (Machine_E)
('SIM105', 'MACHINE_E', 10, 0.60),
('SIM105', 'MACHINE_E', 20, 0.55),
('SIM105', 'MACHINE_E', 30, 0.50),
('SIM105', 'MACHINE_E', 40, 0.45),
('SIM105', 'MACHINE_E', 50, 0.40);