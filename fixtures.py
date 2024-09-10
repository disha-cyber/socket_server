import pytest
import threading
import time


class Sensors:
    def __init__(self, data):
        self.sensor_values = data
    def get_sensor_value(self, sensor_name):
        return self.sensor_values.get(sensor_name, None)
def inner_fixture():
    initial_sensor_data = {'sensor1': 10, 'sensor2': 20, 'sensor3': 30}
    sensors = Sensors(initial_sensor_data)
    return {'sensors': sensors}
def closed_loop(inner_fixture):
    sensors = inner_fixture['sensors']
    while True:
       
        new_sensor_data = {
            'sensor1': 15,
            'sensor2': 25,
            'sensor3': 35
        }
        sensors.sensor_values = new_sensor_data
        updated_sensor_data = sensors.sensor_values
        print(f"Updated sensor data: {updated_sensor_data}")

        time.sleep(2)  # Simulate some delay between updates

def test_sensor_data_update(inner_fixture):
    closed_loop_thread = threading.Thread(target=closed_loop, args=(inner_fixture,)) 
    closed_loop_thread.start()
    time.sleep(10)
    closed_loop_thread.join()
if __name__ == "__main__":
    pytest.main()
