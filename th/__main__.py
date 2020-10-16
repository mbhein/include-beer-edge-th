# main script for Temperature Humidity package

import os
import importlib
import core.config.manager as cfg_mgr
import core.utils.logging as logger

# Set config object
config = cfg_mgr.ConfigManager()

# Set stats objects
stats_buffer = {}
stats_field_names = ['timestamp', 'temperature', 'humidity']
stats_dir = os.path.expanduser(config.stats_dir)
if not os.path.exists(stats_dir):
    os.mkdir(stats_dir)

# Set logging objects
log_buffer = []
log_dir = os.path.expanduser(config.log_dir)
if not os.path.exists(log_dir):
    os.mkdir(log_dir)
log_file = os.path.join(log_dir, 'include-beer-edge-th.log')
log_this = logger.load_logger(
    'include-beer-edge-th', log_file, config.debugging)

# Load ambient sensor module
ambient_sensor = config.ambient_sensor.type
log_this.debug('Set ambient sensor to: ' + ambient_sensor)
try:
    a_sensor = importlib.import_module(ambient_sensor)
except Exception as e:
    log_this.error('Error loading ambient sensor: ' +
                    ambient_sensor + ' exception: ' + str(e))

# Get ambient temperature and humidity
ambient_temp, ambient_humidity = a_sensor.read(config.ambient_sensor.pin)
print(ambient_temp)
log_this.debug('Ambient Temperature: ' + str(ambient_temp))
log_buffer.append('A/T: ' + str(ambient_temp))
log_this.debug('Ambient Humidity: ' + str(ambient_humidity))
log_buffer.append('A/H: ' + str(ambient_humidity))
