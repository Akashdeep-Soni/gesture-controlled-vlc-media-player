int trg1 = 2;
int echo1 = 3;
int trg2 = 4;
int echo2 = 5;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(trg1,OUTPUT);
  pinMode(echo1,INPUT);
  pinMode(trg2,OUTPUT);
  pinMode(echo2,INPUT);

}

void loop() {
  // put your main code here, to run repeatedly:
  int d,dl,dr;
  dl = get_dist(trg1,echo1);
  dr = get_dist(trg2,echo2);

  // Play/Pause
  if((dl>=40 && dl<=50) && (dr>=40 && dr<=50))
  {
   Serial.println("Play/Pause");
   delay(1000); 
  }
  else if(dl>=15 && dl<=25)
  {
    delay(100);
    while(dl<=40)
    {
      dl = get_dist(trg1,echo1);
      if(dl<=15)
      {
        Serial.println("VolumeDown");
        delay(100);
      }
      else if(dl>=25)
      {
        Serial.println("VolumeUP");
        delay(100);
      }
    }
  }
  else if(dr>=15 && dr<=25)
  {
    delay(100);
    while(dr<=40)
    {
      dr = get_dist(trg2,echo2);
      if(dr<=15)
      {
        Serial.println("Forward");
        delay(100);
      }
      else if(dr>=25)
      {
        Serial.println("Backward");
        delay(100);
      }
    }
  }

}

float get_dist(int trg, int echo)
{
  digitalWrite(trg, LOW);
  delayMicroseconds(2);
  digitalWrite(trg, HIGH);
  delayMicroseconds(10);
  digitalWrite(trg, LOW);

  int t,d;
  t = pulseIn(echo, HIGH);
  d = (t * 0.034)/2;
  return d;
  
}
