import java.sql.*;

public class DBHandler		//classs for database handler
{
	Connection con;
	Statement stmt;
	public DBHandler()			//default constructor
	{
		try
		{
			Class.forName("com.mysql.jdbc.Driver");
			con=DriverManager.getConnection("jdbc:mysql://localhost:3306/Accounts_Manager","root","");
			//con=DriverManager.getConnection("jdbc:mysql://192.168.1.5:3306/Accounts_Manager","root","");
			//odbc
			//Class.forName("oracle.jdbc.driver.OracleDriver");
			//con = DriverManager.getConnection("jdbc:oracle:thin:@localhost:1521:orcl","avinash","avinash");
			stmt=con.createStatement();
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
	}

	public int countAccounts()			//count the number of rows in the table Accounts
	{
		int x=0;
		try
		{
			String query="select count(Name) from Accounts";
			ResultSet rs=stmt.executeQuery(query);
			rs.next();
			x = rs.getInt(1);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int countTransactions(String acc_name,String date,int ch)			//count the number of rows in the table transactions
	{
		int x=0;
		String query;
		try
		{
			if(ch==0)
				query="select count(Accounts) from transactions";
			else if (ch==1)
				query="select count(Accounts) from transactions where accounts='"+acc_name+"'";
			else if (ch==2)
				query="select count(Accounts) from transactions where SUBSTRING(datetime, 1,10 )='"+date+"'";
			else
				query="select count(Accounts) from transactions where accounts='"+acc_name+"' and SUBSTRING(datetime, 1,10 )='"+date+"'";
				
			ResultSet rs=stmt.executeQuery(query);
			rs.next();
			x = rs.getInt(1);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public ResultSet getAccounts(int index)	//get the account in the index in the table Accounts
	{
		ResultSet row;
		try
		{
			String query="select * from Accounts order by Name ASC limit " + index + ",1";
			row=stmt.executeQuery(query);
			if(row.next())
				return row;
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return null;
	}
		
	public ResultSet getTransactions(int index)		//get the records sorted by datetime
	{
		ResultSet row;
		try
		{
			String query="select * from transactions order by DateTime DESC limit " + index + ",1";
			row=stmt.executeQuery(query);
			if(row.next())
				return row;
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return null;
	}
	
	public double getBalance(int index)	//get the balance of the account in the index in the table Accounts
	{
		double bal=0;
		try
		{
			String query="select * from Accounts order by Name limit " + index + ",1";
			ResultSet rs=stmt.executeQuery(query);
			if(rs.next())
				bal=Double.parseDouble(rs.getString(2));
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return bal;
	}
		
	public boolean checkUniqueName_accounts(String name)		//check if name is present in database already to prevent duplicate account names
	{
		boolean x=false;
		try
		{
			String query="select * from Accounts where Name='" + name + "'";
			ResultSet rs=stmt.executeQuery(query);
			x=rs.next();
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int insert_transaction(Accounts acc)			//insert transaction to the transaction table
	{
		int x=0;
		try
		{
			String query="insert into transactions values('" + acc.getName() + "','"+acc.getDate()+"','"+ acc.getStatus() + "','Account Opened',"+ acc.getBalance()+")";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int insert_accounts(String name,double bal)		//insert added account in Accounts table
	{
		int x=0;
		try
		{
			String query="insert into Accounts values('" + name + "'," + bal+")";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int delete_transactions(String name)			//insert 'account closed' transaction to transaction table
	{
		int x=0;
		try
		{
			String query="insert into transactions values('" + name +"',now(),'','" + "Account Closed" + "'," + 0.0 + ")";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int delete_accounts(String name)				//remove the account details with the given name from the Accounts table
	{
		int x=0;
		try
		{
			String query="delete from Accounts where Name='"+name+"'";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int rename_transactions(String oldName,String newName)		//rename every past entries in transaction table
	{
		int x=0;
		try
		{
			String query="update transactions set Accounts='" + newName + "'" + "where Accounts='" + oldName + "'";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int rename_accounts(String oldName,String newName)		//rename account name in Accounts table
	{
		int x=0;
		try
		{
			String query="update Accounts set Name='" + newName + "'" + "where Name='" + oldName + "'";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public String getBalance_accounts(String name)			//getter to get balance for an account
	{
		String x=null;
		try
		{
			String query="select * from Accounts where Name='" +name +"'";
			ResultSet rs=stmt.executeQuery(query);
			if(rs.next())
				x=rs.getString(2);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public double credit_debit_accounts(String name,double amnt)	//update balance for credit or debit in Accounts table
	{
		double x=0;
		try
		{
			String query1="select * from Accounts where Name='" +name +"'";
			ResultSet rs=stmt.executeQuery(query1);
			if(rs.next())
				x=Double.parseDouble(rs.getString(2));
			if(amnt<0 && -amnt>x)
				return -2;		//insufficient balance when debiting
			x=x+amnt;
			String query2="update Accounts set Balance="+x+"where Name='"+name+"'";
			x=stmt.executeUpdate(query2);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public double credit_debit_transactions(String name,double amnt,java.sql.Timestamp date,String comment)	//insert transaction in transaction table
	{
		int x=0;
		try
		{
			String query;
			if(amnt>0)
				query="insert into transactions values('" + name + "','"+date+"','Credited : " + amnt + "','" +comment+"',"+ getBalance_accounts(name) +")";
			else
				query="insert into transactions values('" + name + "','"+date+"','Debited : " + -amnt + "','" +comment+"',"+ getBalance_accounts(name) +")";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int clear(String tab)	//clear transactions or accounts
	{
		int x=0;
		try
		{
			String query="truncate table "+tab;
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public ResultSet getTransactions(String acc_name,String date,int choice,int index)		//get the records sorted by datetime
	{
		ResultSet row;
		String query;
		try
		{
			if(choice==1)
				query="select * from transactions where accounts='"+acc_name+"' order by DateTime DESC limit " + index + ",1";
			else if (choice==2)
				query="select * from transactions where SUBSTRING(datetime, 1,10 )='"+date+"'";
			else
				query="select * from transactions where accounts='"+acc_name+"' and SUBSTRING(datetime ,1,10)='"+date+"' order by DateTime DESC limit " + index + ",1";
				
			row=stmt.executeQuery(query);
			if(row.next())
				return row;
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return null;
	}
	
	public int edit_transaction(int ind,String new_date,String comment)
	{
		int x=0;
		ResultSet row;
		try
		{
			String query1="select DateTime from transactions order by Datetime ASC limit "+ind+",1";
			row=stmt.executeQuery(query1);
			row.next();
			String old_date=row.getString(1);	
			old_date = old_date.substring(0,19);
			String query2="update Transactions set DateTime='"+new_date+"',Comments='"+comment+"' where DateTime='"+old_date+"'";
			x=stmt.executeUpdate(query2);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
	public int delete_a_transaction(int ind)		//remove the transaction details in the index in transactions table
	{
		int x=0;
		ResultSet row;
		try
		{
			String query1="select DateTime from transactions order by Datetime ASC limit "+ind+",1";
			row=stmt.executeQuery(query1);
			row.next();
			String sch_date=row.getString(1);	
			sch_date = sch_date.substring(0,19);
			String query="delete from transactions where DateTime='"+sch_date+"'";
			x=stmt.executeUpdate(query);
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		return x;
	}
	
}