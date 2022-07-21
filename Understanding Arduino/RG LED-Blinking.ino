void setup() {
 
 // put your setup code here, to run once:
pinMode(13, OUTPUT);
pinMode(10,OUTPUT);
}

void loop() {
  delay(1000);
  digitalWrite(13,HIGH);
  // put your main code here, to run repeatedly:
  delay(1000);
  digitalWrite(13,LOW);
  delay(1000);
  digitalWrite(10,HIGH);
  // put your main code here, to run repeatedly:
  delay(1000);
  digitalWrite(10,LOW);
  

}
