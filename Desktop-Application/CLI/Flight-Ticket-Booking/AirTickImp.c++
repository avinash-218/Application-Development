#include"AirTickHdr.h"

Domestic::Domestic()    //default constructor for Domestic
{
 source="Madurai";
 dest="Chennai";
}

International::International()  //default constructor for International
{
 source="Chennai";
 dest="USA";
}

AirTick::AirTick()              //default constructor of AirTick
{
 name="Avinash";
 email="ravinash218@gmail.com";
 ph="9629149765";
 age=20;
 count=3;
 gender="Male";
}

Domestic::Domestic(string str,string mail,string phno,int yrs,int cnt,\
string gend,string src,string desti):AirTick(str,mail,phno,yrs,cnt,gend)
{ //parameterised constructor for Domestic
 source=src;
 dest=desti;
}

International::International(string str,string mail,string phno,int yrs,\
int cnt,string gend,string src,string desti):AirTick(str,mail,phno,yrs,cnt,gend)
{	//parameterised constructor for International
 source=src;
 dest=desti;
}

AirTick::AirTick(string nam,string mail,string phno,int yrs,int cnt,string gend)
{	//parameterised constructor for AirTick
 name=nam;
 email=mail;
 ph=phno;
 age=yrs;
 count=cnt;
 gender=gend;
}

istream &operator>>(istream &is,AirTick &inp) 
{ //overloaded input operator of Domestic to get input for copy constructor
 cout<<"\nEnter the Details";
 cout<<"\nName:";
 is>>inp.name;
 cout<<"\nGender:";
 is>>inp.gender;
 cout<<"\nEmail id:";
 is>>inp.email;
 cout<<"\nPhone Number:";
 is>>inp.ph;
 cout<<"\nAge:";
 is>>inp.age;	
 cout<<"\nBoarding Place:";
 is>>inp.source;
 cout<<"\nDestination:";
 is>>inp.dest;
 cout<<"\nEnter the Number Of Passengers:";
 is>>inp.count;
 return is;
}

AirTick::AirTick(const AirTick &obj)//copy constructor
{
 name=obj.name;
 source=obj.source;
 dest=obj.dest;
 age=obj.age;
 count=obj.count;
}

AirTick::~AirTick()        //destructor
{
 cout<<"\nDestructor Is Invoked\n";
}

/*getter and setter to copy static members to objs' members*/
/*remtick*/
int Domestic::get_remTick()
{
 return remTick;
}
int International::get_remTick()
{
 return remTick;
}
void AirTick::set_remTick(int remTick)
{
 rem_tick_obj=remTick;
}

/*count*/
int AirTick::get_count()
{
 return count;
}
void AirTick::set_count(int cnt)
{
 count_obj=cnt;
}

/*seat_num*/
int Domestic::get_seat_num()	
{
 return seat_num;
}
int International::get_seat_num()
{
 return seat_num;
}
void AirTick::set_seat_num(int seat_num)
{
 seat_num_obj=seat_num;
}

/*tick_id*/	
int Domestic::get_obj_tick_id()	
{
 return tick_id;
}
int International::get_obj_tick_id()
{
 return tick_id;
}
void AirTick::set_obj_tick_id(int tick_obj_id)
{
 tick_id_obj=tick_obj_id;
}

int Domestic::gettick_id_search() //getter for tick_id_obj to search
{
 return tick_id_obj;
}
int International::gettick_id_search() //getter for tick_id_obj to search
{
 return tick_id_obj;
}


ostream &operator<<(ostream &os,AirTick &out)	
{	 //overloaded output operator to print every details
 os<<"---------------------------------------------------------------------------------------------------------";
 os<<"\n\n\t\t\tTicket Details\n";
 os<<"---------------------------------------------------------------------------------------------------------";
 os<<"\nName : "<<out.name;
 if(out.count_obj>1)
  os<<"\nSeat : "<<out.seat_num_obj<<" - "<<out.seat_num_obj+out.count_obj-1;
 else
  os<<"\nSeat : "<<out.seat_num_obj;	//static
 os<<"\nGender : "<<out.gender;
 os<<"\nSource : "<<out.source;
 os<<"\nDestination : "<<out.dest;
 os<<"\nAge : "<<out.age;
 os<<"\nTicket ID : "<<out.tick_id_obj;	//static
 os<<"\n\nContact Details :-";
 os<<"\nEmail : "<<out.email;
 os<<"\nPhone Number : "<<out.ph;
 os<<"\nTotal Fare : "<<out.cost;
 os<<"\n---------------------------------------------------------------------------------------------------------";
 os<<"\nRemaining Tickets : "<<out.rem_tick_obj;	//static
 return os;
}

Domestic Domestic::operator++()
{ 	 //overloaded pre-increment operator to calc ticket id of each booking
 ++tick_id;
 return *this;
}

International International::operator++()
{        //overloaded pre-increment operator to calc ticket id of each booking
 ++tick_id;
 return *this;
}

void AirTick::operator+(int n)	//overloaded binary addition operator
{
 cost+=n;
}

void Domestic::remTickCount()  //static function to calculate remaining tickets
{
 remTick-=count;
}

void International::remTickCount()  //static function to calculate remaining tickets
{
 remTick-=count;
}

void Domestic::seatNum()	//static function to calculate starting seat number
{
 seat_num+=count;
}

void International::seatNum()  //static function to calculate starting seat number
{
 seat_num+=count;
}

	/*static members*/	
int Domestic::tick_id=1111;		//for ticket id
int International::tick_id=111111;    
int Domestic::remTick=450;		//for remaining tickets
int International::remTick=450;
int Domestic::seat_num=1;		//for starting seat_num
int International::seat_num=1;
int AirTick::count=0;			//for number of passengers(no use for static)

void Domestic::computeFare()		//to calc domestic cost(virtual fn)
{
 cost=7800*count;
}
void International::computeFare()	//to calc international cost
{
 cost=15000*count;
}

