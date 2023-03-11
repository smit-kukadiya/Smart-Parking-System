#include <Servo.h> //includes the servo library
#include <Wire.h>
// #include <LiquidCrystal_I2C.h>
// LiquidCrystal_I2C lcd(0x27, 16, 2);

Servo myservo;

#define ir_enter 2
#define ir_back  4

#define ir_car1 5
#define ir_car2 6
#define ir_car3 7
#define ir_car4 8

int S1 = 0, S2 = 0, S3 = 0, S4 = 0;
int flag1 = 0, flag2 = 0;
int slot = 4;
int check = 1;

void setup() {
  Serial.begin(9600);

  pinMode(ir_car1, INPUT);
  pinMode(ir_car2, INPUT);
  pinMode(ir_car3, INPUT);
  pinMode(ir_car4, INPUT);

  pinMode(ir_enter, INPUT);
  pinMode(ir_back, INPUT);
  
  myservo.attach(9);
  myservo.write(100);
  /*
  lcd.init();
  lcd.backlight();
  lcd.setCursor (0, 0);
  lcd.print("Auto car Parking");
  lcd.setCursor (0, 1);
  lcd.print("    SYSTEM    ");
  delay (2000);
  lcd.clear();
   */
  Read_Sensor();
  
  int total = S1 + S2 + S3 + S4;
  slot = slot - total;
}

void loop() {

  Read_Sensor();
  delay(20);
  /*
  lcd.clear();
  if (S1 == 1) {
    lcd.print("P1:F");
  }
  else {
    lcd.print("P1:E");
  }

  lcd.setCursor (8, 0);
  if (S2 == 1) {
    lcd.print("P2:F");
  }
  else {
    lcd.print("P2:E");
  }

  lcd.setCursor (0, 1);
  if (S3 == 1) {
    lcd.print("P3:F");
  }
  else {
    lcd.print("P3:E");
  }

  lcd.setCursor (8, 1);
  if (S4 == 1) {
    lcd.print("P4:F");
  }
  else {
    lcd.print("P4:E");
  }
  */
  if (digitalRead (ir_enter) == 0 && flag1 == 0) {
    if (slot > 0) {
      flag1 = 1;
      if (flag2 == 0) {
        myservo.write(180);
        slot = slot - 1;
      }
    } else {
      //lcd.clear();
      //lcd.print("  Parking Full ");
      delay(1500);
    }
  }

  if (digitalRead (ir_back) == 0 && flag2 == 0) {
    flag2 = 1;
    if (flag1 == 0) {
      myservo.write(180);
      slot = slot + 1;
    }
  }

  if (flag1 == 1 && flag2 == 1) {
    delay (1000);
    myservo.write(90);
    flag1 = 0, flag2 = 0;
  }

  delay(1);
  
  if (check == 30)
  {
    if (S1 == 0)
      Serial.print(0);
    else
      Serial.print(1);
    if (S2 == 0)
      Serial.print(0);
    else
      Serial.print(1);
    if (S3 == 0)
      Serial.print(0);
    else
      Serial.print(1);
    if (S4 == 0)
      Serial.print(0);
    else
      Serial.print(1);
      Serial.println();
    check = 0;
  }
  else
  {
    check += 1;
  }

}

void Read_Sensor() {

  if (digitalRead(ir_car1) == 0) {
    S1 = 1;
  }
  if (digitalRead(ir_car2) == 0) {
    S2 = 1;
  }
  if (digitalRead(ir_car3) == 0) {
    S3 = 1;
  }
  if (digitalRead(ir_car4) == 0) {
    S4 = 1;
  }
}
