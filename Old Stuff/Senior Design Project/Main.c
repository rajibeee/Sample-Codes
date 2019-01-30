//Author: Rajib Dey
#include <mega8.h> 
#include <stdio.h> 
#include <stdlib.h> 
#include <delay.h> 
// Alphanumeric LCD functions 
#include <alcd.h> 
 
#define sonarpin PORTD.4 
#define sonarpindata PIND.4 
 
// Declare your global variables here 
float distance=0,coefficient=0,temp=0,level=0; 
unsigned int timerCoefficient=0,i=0; 
//unsigned long int elapsedTime1=0; 
unsigned int elapsedTime=0; 
//unsigned long int elapsedTime=0; 
unsigned char buffer[5]; 
eeprom float threshold=20;  
 
// Timer 0 overflow interrupt service routine 
interrupt [TIM0_OVF] void timer0_ovf_isr(void) 
{ 
// Place your code here 
    timerCoefficient++; 
    TCNT0=0; 
} 
 
void TimerStart(); 
void TimerStop(); 
void TimerReset(); 
 
void main(void) 
{ 
 
unsigned char buffer1[10]; 
unsigned int level1=0; 
PORTB=0x00; 
DDRB=0x00; 
 
PORTC=0x00; 
DDRC=0x00; 
 
PORTD=0x00; 
DDRD=0xE0; 
 
// Timer/Counter 0 initialization 
// Clock source: System Clock 
// Clock value: 1000.000 kHz 
TCCR0=0x00; 
TCNT0=0x00; 
// Timer(s)/Counter(s) Interrupt(s) initialization 
TIMSK=0x01; 
// USART initialization 
// Communication Parameters: 8 Data, 1 Stop, No Parity 
// USART Receiver: Off 
// USART Transmitter: On 
// USART Mode: Asynchronous 
// USART Baud Rate: 9600 
UCSRA=0x00; 
UCSRB=0x08; 
UCSRC=0x86; 
UBRRH=0x00; 
UBRRL=0x33; 
 
// Alphanumeric LCD initialization 
// Connections are specified in the 
// Project|Configure|C Compiler|Libraries|Alphanumeric LCD menu: 
// RS - PORTB Bit 0 
// RD - PORTB Bit 1 
// EN - PORTB Bit 2 
// D4 - PORTB Bit 4 
// D5 - PORTB Bit 5 
// D6 - PORTB Bit 6 
// D7 - PORTB Bit 7 
// Characters/line: 8 
lcd_init(16); 
// Global enable interrupts 
#asm("sei") 
coefficient=73.74; 
temp=threshold; 
delay_ms(2000); 
while (1) 
    {  
        elapsedTime=0; 
        //elapsedTime1=0; 
        // Place your code here 
        TimerReset(); 
        //declare the pin as output pin 
        DDRD=0X10; 
        //make the pin logic high 
        sonarpin=1; 
        delay_us(5); 
        //make the pin logic low 
        sonarpin=0;  
        delay_us(500); 
 //Declare the pin here as input  
        DDRD=0x00;  
        delay_us(60);           
        //wait here as long as pin is logic 0 
        while(sonarpindata == 0 )  { }  
        //here count start         
        TimerStart(); 
        //wait here as long as pin is logic 1         
        while(sonarpindata == 1) {  } 
        //count stop when the signal is 0 
        TimerStop(); 
        elapsedTime= timerCoefficient*256+TCNT0;   
        elapsedTime=elapsedTime/2; 
        //elapsedTime=elapsedTime+elapsedTime1; 
        sonarpin=0; 
        delay_ms(20); 
        sonarpin=0;   
                      
        // elapsedTime=elapsedTime/5; 
 //Converting elapsed time into float , this is typecasting 
        distance=(float)elapsedTime/coefficient; 
      
         // Save the new threshold value onto eeprom                
        if(PINC.0 == 1) 
        {   
            threshold=distance; 
            lcd_clear(); 
            lcd_gotoxy(0,0); 
            lcd_putsf("Data stored");   
            delay_ms(2000);   
            temp=threshold;  
            lcd_gotoxy(0,0); 
            lcd_putsf("                "); 
            //lcd_gotoxy(0,1);  
            //lcd_putse("")        
        }  
 //To show the water level in percentage 
         
        level=100*distance; 
        level=level/temp; 
         
 //This is the code where we define when to turn the relay on or off,  
        if(level < 10.00) PORTD.6=1; 
        if(level > 90.00) PORTD.6=0; 
                         
        delay_ms(500);  
        lcd_gotoxy(0,0);//This will set the LCD display point to 0 Column and 0 Row 
        lcd_putsf("WATERLEVEL");//This will display the word "Water level" at 0,0 
        lcd_gotoxy(11,0);//This will set the LCD display point to 11 Column and 0 Row , and will show the threshold value ( Tank height ) to the display 
        ftoa(temp,2,buffer); 
        lcd_puts(buffer); 
        lcd_gotoxy(0,1);//This will set the LCD display point to 0 Column and 1 Row 
        ftoa(distance,2,buffer);//This will display the water height in the tank 
        lcd_puts(buffer); 
        lcd_gotoxy(8,1);//This will set the LCD display point to 8 Column and 1 Row 
        ftoa(level,2,buffer); 
        lcd_puts(buffer); 
        lcd_gotoxy(15,1); 
        lcd_putsf("%"); 
        delay_ms(500);  
 //The following lines are used to send data to computer 
 
        level1=(int)level; 
        sprintf(buffer1,"%d,2",level1); 
        puts(buffer1); 
        delay_ms(100);  
      
    } 
} 
void TimerStart() 
{ 
    TCNT0=0x00; 
    TCCR0=0x02; 
} 
void TimerStop() 
{ 
     TCCR0=0x00; 
} 
void TimerReset() 
{ 
    TCNT0=0x00; 
    TCCR0=0x00;  
    timerCoefficient=0; 
}