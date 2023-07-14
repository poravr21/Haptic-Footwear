int ledpin=13;
void setup() {
  // put your setup code here, to run once:
pinMode(ledpin,OUTPUT);
}
int arr[]={5,4,3,2,1};
for(int i=0;i<5;i++){
  blinker(arr[i]);
  delay(1000);
  }

void blinker(int times ){
  for(int i=0;i<times;i++){
   digitalWrite(ledpin,HIGH);
   delay(500);
   digitalRead(ledpin,LOW);
   }
  }
