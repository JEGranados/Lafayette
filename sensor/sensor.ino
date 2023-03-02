int PIN_SENSOR_1 = A0;
String NOMBRE_SENSOR_1 = "TEMP";
int DELAY = 1000;

void setup(){
  Serial.begin(9600);
  pinMode(PIN_SENSOR_1, INPUT);
}

void loop(){
    int data_sensor_1 = analogRead(PIN_SENSOR_1);
    Serial.print(NOMBRE_SENSOR_1);
    Serial.print(",");
    Serial.println(data_sensor_1);
    delay(DELAY);
}
