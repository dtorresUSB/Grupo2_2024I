//1. configurar los puertos del arduino
//2. realizar el programa
long randomx;
void setup() {
  pinMode(LED_BUILTIN,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if(Serial.available()>0){
    char incoming=Serial.read();
    if(incoming=='H'){
      digitalWrite(LED_BUILTIN,HIGH);
      delay(500);
      randomx=random(1,100);
      Serial.println(randomx);
      digitalWrite(LED_BUILTIN,LOW);
      delay(500);
    }else if(incoming=='Q'){
      Serial.println("Cambio y fuera");
      delay(10);
    }else{
      Serial.println("Dato Incorrecto");
      delay(10);
    }
    
  }
}
