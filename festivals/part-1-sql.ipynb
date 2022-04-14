import pandas as pd
from sqlalchemy import create_engine

db_config = {} # settings were hidden by artemtu

connection_string = 'postgresql://{}:{}@{}:{}/{}'.format(db_config['user'],
 db_config['pwd'],
 db_config['host'],
 db_config['port'],
 db_config['db'])

engine = create_engine(connection_string, connect_args={'sslmode':'require'})

def sql_result(query):
  return pd.io.sql.read_sql(query, con = engine)

query = \
'''
SELECT
    COUNT(flight_id) as flights_amount,
    aircrafts.model as model
    
FROM
    flights 
    INNER JOIN aircrafts ON aircrafts.aircraft_code = flights.aircraft_code 
    
WHERE
   EXTRACT(MONTH FROM flights.departure_time) = 9

GROUP BY
    aircrafts.model

'''
sql_result(query)
# flights_aircrafts september 2019

df = sql_result(query)
df.to_csv('flights_aircrafts.csv')

from google.colab import files
files.download("flights_aircrafts.csv")



query = \
'''
SELECT
    SUBQ.city AS city,
    AVG(SUBQ.flights_amount) AS average_flights
FROM (
        SELECT
            airports.city,
            EXTRACT(DAY FROM arrival_time) AS day_number,
            COUNT(flights.flight_id) AS flights_amount
        FROM
            flights
            INNER JOIN airports ON flights.arrival_airport = airports.airport_code 
        WHERE
            EXTRACT(MONTH FROM arrival_time) = 8
            AND 
            EXTRACT(YEAR FROM arrival_time) = 2018
        GROUP BY
            airports.city,
            day_number
    ) AS SUBQ
GROUP BY
    city;
'''
sql_result(query) # cities august 2018

df = sql_result(query)
df.to_csv('cities.csv')

from google.colab import files
files.download("cities.csv")
