#include <VarSpeedServo.h> 
#include <math.h>

VarSpeedServo servoBase;
VarSpeedServo servoInferior; 
VarSpeedServo servoVertical; 
VarSpeedServo servoPinzas; 

double lastRadius = 7;
int direction = 1;

String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

const int pinBase = 11;//azul
const int pinInferior =10 ;// subir y bajar
const int pinVertical = 9;// brazo vertical
const int pinPinzas = 8;// pienzas

int lastBase = 0;//azul
int lastInferior = 0 ;// subir y bajar
int lastVertical = 0;// brazo vertical
int lastPinzas = 0;// pienzas


#define X_OFFSET  5.5
#define Y_OFFSET -2.75
#define X_SCALE 2
#define Y_SCALE 2.0

#define SCALE_ANGLE 0.8964143
#define OFFSET_ANGLE 4.322709

#define SERVO2 4.346707
#define SERVO3 2.594587
#define SERVO4 -5.011424

#define SERVO2_OFFSET 52.21554
#define SERVO3_OFFSET 56.27014
#define SERVO4_OFFSET 137.9164

struct polar{
  double radius;
  double angle;
};
struct servos{
  int servo1;
  int servo2;
  int servo3;
  int servo4;
};
double radius(int x,int y){
    return sqrt(x*x+ y*y);
}
double angle(int x,int y){
    return atan2(y,x);
}

struct polar toRadiusAngle(int xIn,int yIn){
    
   int x = X_SCALE * (xIn - X_OFFSET);
   int y = Y_SCALE *(yIn - Y_OFFSET);
    
   double rad = radius(x,y);
   double angulo = (angle(x,y) * 4068) / 71;

   struct polar res =  {rad, angulo};
   return res;
}
int servo02(double x){
//   double x2 = x*x;
//   double x3 = x*x*x;
//   double x4 = x*x*x*x;
//   double x5 = x*x*x*x*x;
//   int y = round(-1930.432 + 700.5934*x - 91.67013*x2 + 5.712748*x3 - 0.1708117*x4 + 0.00197525*x5);
    int y = round(SERVO2 * x + SERVO2_OFFSET);
    return y;
}
struct servos radiusToServos(double r){
    struct servos res;
    res.servo2 = servo02(r);
    res.servo3 = round(SERVO3 * r + SERVO3_OFFSET);
    res.servo4 = round(SERVO4 * r + SERVO4_OFFSET);

    return res;
}
struct servos toServos(int xIn,int yIn){
    struct polar p = toRadiusAngle(xIn,yIn);

    struct servos res  = radiusToServos(p.radius);
    res.servo1 = round(OFFSET_ANGLE+ (p.angle * SCALE_ANGLE));

    if(lastRadius < p.radius) direction = 1;
    else direction = 0;
    lastRadius = p.radius;
    
    
    return res;
}

void moveServos(struct servos angles, int speed)
{
    int extra1 = getValue(inputString,',',2).toInt();
    int extra2 = getValue(inputString,',',3).toInt();
    
    if(direction){ //alejandome
    
        servoVertical.write(50,speed,true);
        servoPinzas.write(angles.servo4,speed,true);
        servoInferior.write(70,speed,true);
        servoBase.write(angles.servo1,speed,true); 
        servoInferior.write(angles.servo2,speed,true);
        servoVertical.write(angles.servo3,speed,true);
    
    
    }

    else{ //acercandome
        servoVertical.write(50,speed,true);
        servoPinzas.write(angles.servo4,speed,true);
        servoInferior.write(angles.servo2,speed,true);
        servoBase.write(angles.servo1,speed,true); 
        servoVertical.write(angles.servo3,speed,true);
    
    }
}
void setup() {
  // initialize serial:
  Serial.begin(9600);
  pinMode(2, OUTPUT);  
  servoBase.attach(pinBase);  // attaches the servo on pin 9 to the servo object
  servoInferior.attach(pinInferior);
  servoVertical.attach(pinVertical);
  servoPinzas.attach(pinPinzas);

   struct servos angles = toServos(5,2);
   angles.servo3 = 55;
   moveServos(angles, 200);
    
  // reserve 200 bytes for the inputString:
  inputString.reserve(200);
}
String getValue(String data, char separator, int index)
{
  int found = 0;
  int strIndex[] = {0, -1};
  int maxIndex = data.length()-1;

  for(int i=0; i<=maxIndex && found<=index; i++){
    if(data.charAt(i)==separator || i==maxIndex){
        found++;
        strIndex[0] = strIndex[1]+1;
        strIndex[1] = (i == maxIndex) ? i+1 : i;
    }
  }

  return found>index ? data.substring(strIndex[0], strIndex[1]) : "";
}
void loop() {
  // print the string when a newline arrives:
  if (stringComplete) {
    Serial.println(inputString); 
    char option = inputString.charAt(0);
    inputString.remove(0,1);
    switch (option) {
        case 'm':
          struct servos anglesin = toServos(getValue(inputString,',',0).toInt(),getValue(inputString,',',1).toInt());
          moveServos(anglesin,15);
          break;
        case 'p':
          break;
        case 'd':
          break;
        default:
          break;
    }   
    
    // clear the string:
    inputString = "";
    stringComplete = false;
  }
}

/*
  SerialEvent occurs whenever a new data comes in the
 hardware serial RX.  This routine is run between each
 time loop() runs, so using delay inside loop can delay
 response.  Multiple bytes of data may be available.
 */
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read(); 
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag
    // so the main loop can do something about it:
    if (inChar == '\n') {
      stringComplete = true;
    } 
  }
}
