
bool ok = false;

void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    if (ok == true) {
      delay(200);  // wait for a second
      char incoming = Serial.read();
      digitalWrite(LED_BUILTIN, HIGH);  // turn the LED on (HIGH is the voltage level)
      //Serial.print("enviado");
      delay(200);  // wait for a second
      //while (Serial.available() > 0) Serial.read();
      Serial.print(incoming);
      digitalWrite(LED_BUILTIN, LOW);  // turn the LED off by making the voltage LOW
    } else {
      ok = true;
      Serial.print("");
      delay(10);
    }
  }
}