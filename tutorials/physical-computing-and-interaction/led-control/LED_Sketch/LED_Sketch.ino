const int leds[8] = {2,3,4,5,6,7,8,9};

String inputString = "";

void setup() {
  Serial.begin(9600);

  for (int i = 0; i < 8; i++) {
    pinMode(leds[i], OUTPUT);
    digitalWrite(leds[i], LOW);
  }
}

void loop() {
  if (Serial.available()) {

    inputString = Serial.readStringUntil('\n');
    inputString.trim();

    if (inputString.length() == 8) {

      for (int i = 0; i < 8; i++) {

        if (inputString.charAt(i) == '1')
          digitalWrite(leds[i], HIGH);
        else
          digitalWrite(leds[i], LOW);
      }
    }
  }
}