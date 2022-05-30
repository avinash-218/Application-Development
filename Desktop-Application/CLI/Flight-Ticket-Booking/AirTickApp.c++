#include"AirTickHdr.h"
int main()
{
 int ch;
 do
 {
  int count,age,type;
  string name,gender,email,ph,source,dest;
  cout<<"\nEnter 1 For Domestic Flight";
  cout<<"\nEnter 2 For International Flight";
  cout<<"\nEnter any other number to exit\n";
  cin>>type;
  if(type!=1 && type!=2)
   exit(0); 
  cout<<"\nEnter 1 to use default constructor";
  cout<<"\nEnter 2 to use parameterised constructor";
  cout<<"\nEnter 3 to use copy constructor";
  cout<<"\nEnter 4 for array of objects";
  cout<<"\nEnter any other number to exit\n";
  cin>>ch;
  AirTick *aptr;	//base class pointer
  Domestic *dptr;	//sub class pointer
  International *iptr;	//sub class pointer
  switch(ch)
  {
   case 1:
      	  {
	   if(type==1)
	   {
	    Domestic dom1;
	    aptr=&dom1;	//pointing sub class object
	    dptr=dynamic_cast<Domestic*>(aptr);
	    dptr->set_count(aptr->get_count());
	    dptr->computeFare();
	    dptr->operator+(99.0);
	    ++dom1;
	    dptr->set_obj_tick_id(dom1.get_obj_tick_id());
	    dptr->set_seat_num(dom1.get_seat_num());
	    Domestic::remTickCount();
	    dptr->set_remTick(dom1.get_remTick());
	    cout<<dom1;
	    Domestic::seatNum();
	   }
	   else
	   {
	    International inter1;
	    aptr=&inter1;
	    iptr=dynamic_cast<International*>(aptr);
	    iptr->set_count(inter1.get_count());
	    iptr->computeFare();
	    iptr->operator+(99.0);
	    ++inter1;
	    iptr->set_obj_tick_id(inter1.get_obj_tick_id());
	    iptr->set_seat_num(inter1.get_seat_num());
	    International::remTickCount();
	    iptr->set_remTick(inter1.get_remTick());
	    cout<<inter1; 
            International::seatNum();
	   }
	   break;
	  }
   case 2:
	  {
	   cout<<"\nEnter your details";
	   cout<<"\nName:";
	   cin>>name;
	   cout<<"\nGender:";
	   cin>>gender;
	   cout<<"\nEmail id:";
	   cin>>email;
	   cout<<"\nPhone Number:";
	   cin>>ph;
	   cout<<"\nAge:";
	   cin>>age;
	   cout<<"\nEnter the number of Passengers:";
	   cin>>count;
	   cout<<"\nBoarding Place:";
           cin>>source;
           cout<<"\nDestination:";
           cin>>dest;
	   if(type==1)
	   {
	    Domestic dom2(name,email,ph,age,count,gender,source,dest);
	    aptr=&dom2;
	    dptr=dynamic_cast<Domestic*>(aptr);
	    dptr->set_count(dom2.get_count());
            dptr->computeFare();
            dptr->operator+(99.0);
            ++dom2;
	    dptr->set_obj_tick_id(dom2.get_obj_tick_id());
            dptr->set_seat_num(dom2.get_seat_num());
            Domestic::remTickCount();
            dptr->set_remTick(dom2.get_remTick());
            cout<<dom2;
	    Domestic::seatNum();
	   }
	   else
	   {
	    International inter2(name,email,ph,age,count,gender,source,dest);
	    aptr=&inter2;
	    iptr=dynamic_cast<International*>(aptr);
            iptr->set_count(inter2.get_count());
            iptr->computeFare();
            iptr->operator+(99.0);
            ++inter2;
            iptr->set_obj_tick_id(inter2.get_obj_tick_id());
	    iptr->set_seat_num(inter2.get_seat_num());
            International::remTickCount();
            iptr->set_remTick(inter2.get_remTick());
            cout<<inter2;
            International::seatNum();
	   }
	   break;
	  }
   case 3:
	  {
	   if(type==1)
	   {
	    Domestic dom_temp;
	    cin>>dom_temp;
	    Domestic dom3=dom_temp;
	    dom3.set_count(dom3.get_count());
            aptr=&dom3;
	    dptr=dynamic_cast<Domestic*>(aptr);
	    dptr->computeFare();
            dptr->operator+(99.0);
            ++dom3;
            dptr->set_obj_tick_id(dom3.get_obj_tick_id());
	    dptr->set_seat_num(dom3.get_seat_num());
            Domestic::remTickCount();
            dptr->set_remTick(dom3.get_remTick());
            cout<<dom3;
	    Domestic::seatNum();
	   }
	   else
	   {
	    International inter_temp;
	    cin>>inter_temp;
	    International inter3=inter_temp;
	    aptr=&inter3;
	    iptr=dynamic_cast<International*>(aptr);
	    iptr->set_count(inter3.get_count());
            iptr->computeFare();
            iptr->operator+(99.0);
            ++inter3;
            iptr->set_obj_tick_id(inter3.get_obj_tick_id());
	    iptr->set_seat_num(inter3.get_seat_num());
            International::remTickCount();
            iptr->set_remTick(inter3.get_remTick());
            cout<<inter3;
            International::seatNum();
	   }
	   break;
	  }
   case 4:
	  {
	   if(type==1)
	   {  
	    int i,n,id,sch,flag=0;
	    cout<<"\nEnter number of objects\n\n";
	    cin>>n;
	    Domestic dom4[n];
	    for(i=0;i<n;i++)
	    {
	     cin>>dom4[i];
	     aptr=&dom4[i];
	     dptr=dynamic_cast<Domestic*>(aptr);
	     dptr->set_count(dom4[i].get_count());
	     dptr->computeFare();
	     dptr->operator+(99.0);
      	     ++dom4[i];
	     dptr->set_obj_tick_id(dom4[i].get_obj_tick_id());
	     dptr->set_seat_num(dom4[i].get_seat_num());
	     Domestic::remTickCount();
	     dptr->set_remTick(dom4[i].get_remTick());
	     cout<<dom4[i]; 
	     Domestic::seatNum();
	    }
	    ofstream ofs;	//file ptr
	    ofs.open("Domestic_Bills.bin",ios::out|ios::binary);	//
	    ofs.write((char *)dom4,n*sizeof(Domestic));	//write
	    ofs.close();	//write close
 	    do
	   {
	    cout<<"\n\nEnter 1 To Search Ticket";
	    cout<<"\nEnter any other number to exit searching\n";
	    cin>>sch;
	    if(sch==1)
	    {
	     cout<<"\nEnter Ticket Id to search\n";
	     cin>>id;
	     Domestic temp[n];	//temp objs for file transfers
	     ifstream ifs;	//file ptr
	     ifs.open("Domestic_Bills.bin",ios::in);	//
	     ifs.read((char *)temp,n*sizeof(Domestic));	//read
	     for(i=0;i<n;i++)
	     {	     
	      if(id==temp[i].gettick_id_search())
	      {
	       flag=1;
	       cout<<"\nSearched Id Details\n";
	       cout<<temp[i];
	       break;
	      }
	     }
	     ifs.close();		//read close
	     if(flag==0)
	      cout<<"\n\nNo Such Id Found\n";
	    }
	   }while(sch==1);	 
 	   break;
	  }
          else
	  {
           int i,n,id,sch,flag=0;
           cout<<"\nEnter number of objects\n\n";
           cin>>n;
           International inter4[n];
           for(i=0;i<n;i++)
           {
            cin>>inter4[i];
	    aptr=&inter4[i];
	    iptr=dynamic_cast<International*>(aptr);
	    iptr->set_count(inter4[i].get_count());
            iptr->computeFare();
            iptr->operator+(99.0);
            ++inter4[i];
            iptr->set_obj_tick_id(inter4[i].get_obj_tick_id());
	    iptr->set_seat_num(inter4[i].get_seat_num());
            International::remTickCount();
            iptr->set_remTick(inter4[i].get_remTick());
            cout<<inter4[i];
            International::seatNum();
           }
           do
           {
            cout<<"\n\nEnter 1 To Search Ticket";
            cout<<"\nEnter any other number to exit searching\n";
            cin>>sch;
            if(sch==1)
            {
             cout<<"\nEnter Ticket Id to search\n";
             cin>>id;
             for(i=0;i<n;i++)
             {
              if(id==inter4[i].gettick_id_search())
              {
               flag=1;
               cout<<"\nSearched Id Details\n";
               cout<<inter4[i];
               break;
              }
             }
             if(flag==0)
              cout<<"\n\nNo Such Id Found\n";
            }
           }while(sch==1);
           break;
	  }
	  } }
 }while(ch==1||ch==2||ch==3||ch==4);
 exit(0);
 return 0;
 }

