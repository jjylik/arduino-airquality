
#define CO2ZERO 55

void setup() {
  Serial.begin(9600);
}

void loop() {
  int airQualityMeasurements = 0;
  for (int i = 0; i < 10; i++) {
    airQualityMeasurements = airQualityMeasurements + analogRead(0);
    delay(200);
  }
  int airQualityAvg = airQualityMeasurements / 10;
  int airQualityComp = airQualityAvg - CO2ZERO;
  int airQualityPpm = map(airQualityComp, 0, 1023, 400, 5000);
  Serial.println(airQualityPpm, DEC);
  delay(58000);
} 
