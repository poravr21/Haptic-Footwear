#include <SoftwareSerial.h>
#define FORCE_SENSOR_PIN A0
int count=0;
SoftwareSerial BTSerial (10,11);
void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  BTSerial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int analogReading = analogRead(FORCE_SENSOR_PIN);
  if(analogReading>=200){count++;}
  Serial.print("Analog Reading:");
  Serial.println(analogReading);
  Serial.println("Count:");
  Serial.println(count);
  BTSerial.print("Count");
  BTSerial.println(count);
    delay(1000);
}
