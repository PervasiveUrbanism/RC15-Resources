void setup() {
  Serial.begin(9600);  //Start the Serial connection
}

void loop() {
  int sensorValue = analogRead(A0);
  Serial.println(sensorValue);
  delay(200);
}