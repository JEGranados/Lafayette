int PIN_SENSOR_1 = A1;
int PIN_SENSOR_2 = 2;
String NOMBRE_SENSOR = "IR";
int DELAY = 1000;

void setup(){
  Serial.begin(9600);
  pinMode(PIN_SENSOR_1, INPUT);
  pinMode(PIN_SENSOR_2, INPUT);
}

void loop(){
    int data_sensor_1 = analogRead(PIN_SENSOR_1);
    int data_sensor_2 = digitalRead(PIN_SENSOR_2);
    int mm_sensor_1 = data_sensor_1 / 2;
    Serial.print(NOMBRE_SENSOR);
    Serial.print(",");
    Serial.print(mm_sensor_1);
    Serial.print(",");
    Serial.println(data_sensor_2);
    delay(DELAY);
}
