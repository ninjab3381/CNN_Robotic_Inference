
#include "MeccaBrain.h"
#include <stdio.h>
// defines pins numbers

#define CHAIN_SVL         8
MeccaBrain mecaChainSVL(CHAIN_SVL);


//bool curtainIsUp = true;
void setup() {
  // setup all the module init callbacks

  pinMode(CHAIN_SVL, OUTPUT);
  Serial.begin(9600);

  for (int j = 0; j < 50; j++)
  {
    mecaChainSVL.communicate();

  }

  //Servo1 is green
  mecaChainSVL.setServoColor(0, 0xF2);
  //mecaChainSVL.communicate();
  //Servo2 is red
  mecaChainSVL.setServoColor(1, 0xF1);
  //mecaChainSVL.communicate();
  //  mecaChainSVL.setServoColor(2, 0xF5);
  //  mecaChainSVL.setServoColor(3, 0xF3);
  mecaChainSVL.communicate();
  delay(500);
    mecaChainSVL.setServoPosition(0, 120);
    mecaChainSVL.communicate();
    delay(500);
    mecaChainSVL.setServoPosition(1, 10);
    mecaChainSVL.communicate();
    delay(500);
  while(!Serial.available())
  {}
}

void loop() {
  char buffer[16];

  // if we get a command, turn the LED on or off:
  if (Serial.available() > 0) {
    int size = Serial.readBytesUntil('\n', buffer, 12);
    if (buffer[0] == 'Y') {
      mecaChainSVL.setServoPosition(0, 190);
      mecaChainSVL.communicate();
      delay(2000);
      mecaChainSVL.setServoPosition(1, 220);
      mecaChainSVL.communicate();
      delay(3000);
      mecaChainSVL.setServoPosition(0, 50);
      mecaChainSVL.communicate();
      delay(1000);
 
  }
  if (buffer[0] == 'N') {
     mecaChainSVL.setServoPosition(0, 50);
      mecaChainSVL.communicate();
      delay(2000);
      mecaChainSVL.setServoPosition(1, 220);
      mecaChainSVL.communicate();
      delay(3000);
      mecaChainSVL.setServoPosition(0, 190);
      mecaChainSVL.communicate();
      delay(1000);

    }

    mecaChainSVL.setServoPosition(0, 120);
    mecaChainSVL.communicate();
    delay(500);
    mecaChainSVL.setServoPosition(1, 10);
    mecaChainSVL.communicate();
    delay(500);
  }
}
