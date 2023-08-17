import Adafruit_DHT
class AirHumidityAndTemperature:
    DHT_SENSOR = Adafruit_DHT.DHT22
    DHT_PIN = 4

    def get():
        return Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
