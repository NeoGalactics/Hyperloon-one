/*
  RF_Sniffer
  
  Hacked from http://code.google.com/p/rc-switch/
  
  by @justy to provide a handy RF code sniffer
*/

#include <RCSwitch.h>
RCSwitch mySwitch = RCSwitch();

long startTime;
int nPackets = 0;
int dataSize = 0;
void setup() {
  Serial.begin(9600);
  mySwitch.enableReceive(0);  // Receiver on inerrupt 0 => that is pin #2
  startTime = millis();
}

boolean stopped = false;
void loop() {
  if(stopped) return;
  if (mySwitch.available()) {
    
    int value = mySwitch.getReceivedValue();
    
    if (value == 0) {
      Serial.print("Unknown encoding");
    } else {
      if(nPackets == 0)
        Serial.println("Beginning analysis...");
       nPackets++;
       dataSize += mySwitch.getReceivedBitlength();
      
     //Serial.print("Received ");
      //Serial.print(" / ");
      //Serial.print( mySwitch.getReceivedBitlength() );
      //Serial.print("bit ");
      //Serial.print("Protocol: ");
      //Serial.println( mySwitch.getReceivedProtocol() );
    }
    
    mySwitch.resetAvailable();
    
  }
  
  
   
   if(nPackets >= 1000){
     long time = millis() - startTime;
     Serial.println("Analysis finished.");
     Serial.print("Received ");
     Serial.print(nPackets);
     Serial.print(" packets with a total size of ");
     Serial.print(dataSize);
     Serial.print(" bits. (");
     Serial.print(dataSize/(time/1000.0)/1024.0);
     Serial.println(" kib/s)");
     startTime = millis();
     nPackets = 0;
     dataSize = 0;
   }

}


