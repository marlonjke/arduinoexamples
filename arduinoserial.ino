int led =  13;
char valor_recebido = '0';
int x = 20;

void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

void loop(){
  if(valor_recebido == '3'){
    digitalWrite(led, HIGH);
    delay(x);
    digitalWrite(led, LOW);
    delay(x);
 }
}

void serialEvent (){
  valor_recebido = Serial.read(); 
 
  switch(valor_recebido){
  case '1':
    digitalWrite(led, HIGH);
    Serial.println("Led no pino 13 ligado!");
    break;
  case '2':
    digitalWrite(led, LOW);
    Serial.println("Led no pino 13 desligado!");
    break;
  case '3':
    Serial.println("Led no pino 13 itermitente!");
    break;
  case '4':
    x += 20;
    Serial.println("Menos Velocidade");
    valor_recebido = '3';
    break;
  case '5':
    if(x - 20 >= 0){
      x -= 20;
    }
    Serial.println("Mais velocidade");
    valor_recebido = '3';
    break;
   default:
     break;
  }
}
