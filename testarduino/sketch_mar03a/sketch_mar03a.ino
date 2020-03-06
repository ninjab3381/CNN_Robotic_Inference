int ByteReceived;

void setup() {
  // put your setup code here, to run once:
pinMode(8,OUTPUT);
Serial.begin(9600);
while(!Serial.available())
{}
}

void loop() {
  char buffer[16];
  // if we get a command, turn the LED on or off:
  if (Serial.available() > 0) {
    int size = Serial.readBytesUntil('\n', buffer, 12);
    if (buffer[0] == 'Y') {
      digitalWrite(8,HIGH);
    }
    if (buffer[0] == 'N') {
      digitalWrite(8,LOW);
    }
  }
}
