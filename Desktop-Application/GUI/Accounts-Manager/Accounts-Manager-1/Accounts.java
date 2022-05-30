import java.util.Date;

public class Accounts	
{
	private	 String name;	//account name
	private java.sql.Timestamp date;	//date of creation of account
	private String status;	//opening account status for a account
	private double bal;	//account balance
	
	public Accounts(String n,double b,String s,java.sql.Timestamp d)		//parameterised constructor
	{
		name=n;
		bal=b;
		status=s;
		date = d;
	}
		
	public String getName()		//gettter for account name
	{
		return name;
	}
	
	public double getBalance()		//getter for account balance
	{
		return bal;
	}
	
	public String getStatus()		//getter for account status
	{
		return status;
	}
	
	public java.sql.Timestamp getDate()	//getter for date
	{
		return date;
	}
}