# closed_loop.py
import threading
import time
from sensors import Sensors
from sensor_simulation import SensorSimulation

def run_server(sensors_instance):
    sensors_instance.start()

def run_client(sensor_simulation_instance):
    sensor_data1 = {"MAC": "B4:32:a4:12", "value": 42}
    sensor_data2 = {"MAC": "B3:32:a4:12", "value": 20}
    sensor_data3 = {"MAC": "B2:32:a4:12", "value": 10}

    while True:
        sensor_simulation_instance.send_sensor_data1(sensor_data1)
        sensor_simulation_instance.send_sensor_data2(sensor_data2)
        sensor_simulation_instance.send_sensor_data3(sensor_data3)
        time.sleep(1)

if __name__ == "__main__":
    variable_value = "variableValue"

    sensors_instance = Sensors(host='', port=33333, variable=variable_value)
    sensor_simulation_instance = SensorSimulation(host='127.0.0.1', port=33333)

    server_thread = threading.Thread(target=run_server, args=(sensors_instance,))
    client_thread = threading.Thread(target=run_client, args=(sensor_simulation_instance,))

    server_thread.start()
    client_thread.start()
    time.sleep(3)
    new_host = '127.0.0.1'
    new_port = 33334
    sensors_instance.update_config(new_host, new_port)
    sensor_simulation_instance.update_config(new_host, new_port)

    print(f"Configuration updated. New host: {new_host}, New port: {new_port}")
    mac_to_query = "B4:32:a4:12"
    sensor_value = sensors_instance.get_sensor_value(mac_to_query)

    if sensor_value is not None:
        print(f"Sensor value for {mac_to_query}: {sensor_value}")
    else:
        print(f"No sensor value found for {mac_to_query}")

    server_thread.join()
    client_thread.join()
