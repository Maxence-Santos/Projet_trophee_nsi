int pirPin = 7; // Input for HC-S501

int pirValue; // Place to store read PIR Value

bool flag = false;

void setup() {
  pinMode(pirPin, INPUT);
  Serial.begin(9600);
}

void loop() {
  pirValue = digitalRead(pirPin);
  if (!pirValue) {
    flag = false;
  }
  if (pirValue) {
    if (!flag) {
      Serial.println("Détecté");
      flag = true;
    }
    
  }

}
