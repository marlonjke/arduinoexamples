/* TODOS:
  1 - Modificar os nomes dos valores recebidos para algo mais sugestivos...
  2 - Adicionar função de potenciômetro para 'meia luz'...
  3 - Have a lot of fun...
*/

int led =  13; // led será conectado no pino 13.
char valor_recebido = '0'; // valor recebido via serial.
int x = 20; // tempo para delay.

void setup(){
  Serial.begin(9600);
  pinMode(led, OUTPUT);
}

// loop principal, caso tenha recebido o valor 3, itermitente...
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
    break;
  case '2':
    digitalWrite(led, LOW);
    Serial.println("Led no pino 13 desligado!");
    break;
  default:
    break;
  }
}
