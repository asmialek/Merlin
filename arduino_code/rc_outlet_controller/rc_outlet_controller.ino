/* Simple Serial ECHO script : Written by ScottC 04/07/2012 */
/* Stage 2 : Delimiters */

/* Use a variable called byteRead to temporarily store
   the data coming from the computer */
#include <RCSwitch.h>

const byte COMMAND_SIZE = 8;

byte byteRead;
byte cmd[COMMAND_SIZE];

RCSwitch mySwitch = RCSwitch();

void setup() {                
  // Turn the Serial Protocol ON
  Serial.begin(9600);
  
  mySwitch.setPulseLength(196); // Przepisujemy wartość sczytaną z serial monitora
  mySwitch.enableTransmit(10); // Przepisujemy wartość sczytaną z serial monitora

  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.println("Connection made.");
}

void read_cmd() {
  int i = 0;
  // read till Newline character
  while (byteRead!=10) {
    if (Serial.available()) {
      byteRead = Serial.read();
//      Serial.write(byteRead);
      cmd[i] = byteRead;
      i++;
    }
  }
  process_cmd();
//  Serial.println("Command processed.\n");
}

void process_cmd() {
  switch (cmd[0]) {
    // a
    case 97: control_led(cmd[1]); break;
    // d
    case 100: rc_outlet(cmd[1], cmd[2]); break;
  }
}

// RC outlet on/off control
void rc_outlet(byte outlet, byte state) {
  switch (outlet) {
    // a
    case 97:
      // a
      if (state == 97) { mySwitch.send("010001000101010111001100"); }
      // b
      if (state == 98) { mySwitch.send("010001000101010111000011"); }
      //
      break;
  }
}

// LED pin control, for connection test
void control_led(byte state) {
  switch (state) {
    // a
    case 97: digitalWrite(LED_BUILTIN, HIGH); Serial.println("LED on."); break;
    // b
    case 98: digitalWrite(LED_BUILTIN, LOW); Serial.println("LED off."); break;
  }
}

void loop() {
  // check if data has been sent from the computer:
  if (Serial.available()) {
    // read the most recent byte
    byteRead = Serial.read();
    // listen for a # char which equals byte code 35
    if (byteRead==35) {
//      Serial.println("Getting into command mode.");
      read_cmd();
    } else {
      Serial.write(byteRead);
    }
  }
}
