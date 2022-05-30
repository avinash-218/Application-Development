#include<iostream>
#include<stdlib.h>
#include<fstream>
using namespace std;
class AirTick
{
 public:
	AirTick();	//default constructor
   	AirTick(string,string,string,int,int,string);	//parameterised constructor
   	AirTick(const AirTick&);	//copy constructor
   	~AirTick();	//destructor
   	virtual void computeFare()=0;	//to calc tick cost wrt flight type (virtual fn)
	void operator+(int);	//to add ticket cost by 99
	void set_obj_tick_id(int);	//setter for obj_tick
	void set_seat_num(int);	//setter for sear_num
	void set_count(int);	//setter for count
	void set_remTick(int);	//setter for remTick
	int get_count();	//getter for count	
	friend ostream &operator<<(ostream&,AirTick&);	//to print both object
	friend istream &operator>>(istream&,AirTick&);   //to get input for both object
 protected:
   	   string name,gender,email,source,dest,ph;	//details
   	   int age,type;				//details
	   float cost;					//details
	   static int count;				
	   int tick_id_obj,seat_num_obj,count_obj,rem_tick_obj;
};

class Domestic:public AirTick
{
 public:
	Domestic();	 //default constructor
	Domestic(string,string,string,int,int,string,string,string);	//parameterised constructor
	static void remTickCount();	 //to calc remaining ticket after booking
	int get_obj_tick_id();		 //getter for tick_id
	int get_seat_num();	 	 //getter for seat_num
	int get_remTick();		 //getter for remTick
	int gettick_id_search();	 //getter for tick_id_obj to search
	static void seatNum();		 //to calc starting seat number
	Domestic operator++();		 //to calc ticket id for each booking
	void computeFare();		 //to calc domestic cost (virtual fn)
 private:
	 static int tick_id,seat_num,remTick;				
};
class International:public AirTick
{
 public:
	 International();	//default constructor
	 International(string,string,string,int,int,string,string,string); //parameterised constructor
	 static void remTickCount(); 	//to calc remaining ticket after booking
	 int get_obj_tick_id();		//getter for tick_id
	 int get_seat_num();		//getter for seat_num
	 int get_remTick();		//getter for remTick
	 int gettick_id_search();       //getter for tick_id_obj to search
	 static void seatNum();         //to calc starting seat number
	 International operator++();    //to calc ticket id for each booking
	 void computeFare();		//to calc international cost (virtual fn)
 private:
	 static int tick_id,seat_num,remTick;
};

