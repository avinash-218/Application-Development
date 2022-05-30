//Feature Removed : Insert transactions when all accounts are deleted
//All colours removed
//Changed : Accounts frame displays accounts in ascending order

import java.text.*;
import java.util.Date;
import java.sql.Timestamp;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;

class MyFrame extends JFrame
{
	//required components
	JPanel p,row1,row2,row3,row4,row5;
	JButton delete,add,credit,debit,transfer,transaction,rename,delete_all_accounts;
	JToggleButton view_accounts;
	JTextField t_openBal,t_accBal,t_amnt,t_totBal,t_accName,t_comments,t_date_time1,t_date_time2;
	JComboBox accounts;
	JLabel l_accounts,l_openBal,l_accBal,l_amnt,l_totBal,l_accName,l_comments,l_date_time1,l_date_time2;

	public MyFrame()										//default constructor
	{
		
		setResizable(true);									//the frame is resizable
		setTitle("Accounts Manager");						//title is set
        setExtendedState(JFrame.MAXIMIZED_BOTH);
		Toolkit kit = Toolkit.getDefaultToolkit();	
		Dimension size=kit.getScreenSize();					//getting local machine monitor size
		Image img=kit.getImage("bg.jpg");			
		setIconImage(img);									//setting icon
		setSize(size.width,size.height);					//setting size of the frame to the original sizde of the system
		AccountsFrame accounts_frame=new AccountsFrame();
		buildComponents();
		setComboBox();										//setting combobox values to the values in database
		setTotalBalance();									//setting total balance of all accounts
		designUI();											//design user interface
		setVisible(true);									//visibility is true for the frame
		setTime();
		
		
		add.addActionListener(				//action listener for add button to add new account
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTime();
				String name=t_accName.getText();
				java.sql.Timestamp date;
				double bal=0;
				if(name.isEmpty())																
				{
					JOptionPane.showMessageDialog(null,"Enter Account or Wallet Name");			//prompting for account name
					return;
				}
				try			//amount should be of type double
				{
					String bal_str=t_openBal.getText();
					bal=Double.parseDouble(bal_str);
					if(bal_str.contains("d") || bal_str.contains("f") || bal_str.contains("e") || bal<0)
						throw new UserExceptions("Invalid Opening Amount");
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid Opening Balance");		//prompting for a valid input
					return;
				}
				try
				{
					date=java.sql.Timestamp.valueOf(t_date_time1.getText());
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd hh:mm:ss'");		//prompting for a valid input
					return;
				}
				Accounts acc = new Accounts(name,bal,"Opened With Balance "+bal,date);
				DBHandler dbh=new DBHandler();
				int flag=0;
				if(dbh.checkUniqueName_accounts(name)==false)									//check if the entered name is not duplicate
				{
					if(dbh.insert_transaction(acc)>0)		//add to databases
						flag++;
					if(dbh.insert_accounts(name,bal)>0)
						flag++;
				}
				else
				{
					JOptionPane.showMessageDialog(null,"Duplicate Account Names Not Allowed");	//prompting to enter non-duplicate account name
					return;
				}
				
				if(flag==2)
					JOptionPane.showMessageDialog(null,"Account Added");
				else
					JOptionPane.showMessageDialog(null,"Can't Add the Account");
				setComboBox();
				setTotalBalance();	
			}
		});
		
		delete.addActionListener(													//action listener for delete button to delete an account
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTime();
				String name=String.valueOf(accounts.getSelectedItem());
				if(name=="---Select An Account---")												//check if any account is selected
				{
					JOptionPane.showMessageDialog(null,"Select Any Account To Delete");			//prompting to select an account
					return;
				}	
				accounts.removeItem(name);														//remove from combobox
				DBHandler dbh=new DBHandler();
				int flag=0;
				if(dbh.delete_transactions(name)>0)												//remove from databases
					flag++;
				if(dbh.delete_accounts(name)>0)
					flag++;
				if(flag==2)
					JOptionPane.showMessageDialog(null,"Deletion Successful");
				else
					JOptionPane.showMessageDialog(null,"Deletion Not Possible");
				setComboBox();
				setTotalBalance();
			}
		});
		
		rename.addActionListener(				//Action Listener for rename button to rename account name
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTime();
				String oldName=String.valueOf(accounts.getSelectedItem());
				if(oldName=="---Select An Account---")										//check if an account is selected
				{
					JOptionPane.showMessageDialog(null,"Select Any Account To Rename");		//prompting to select any account to rename
					return;
				}	
				String newName= JOptionPane.showInputDialog("Enter The New Name");			//prompting for new name
				if(newName.isEmpty())																
				{
					JOptionPane.showMessageDialog(null,"Enter The New Account or Wallet Name");			//prompting for account name
					return;
				}
				accounts.removeItem(oldName);												//remove from combobox
				DBHandler dbh=new DBHandler();
				int flag=0;
				if(dbh.rename_transactions(oldName,newName)>0)								//renaming in databases
					flag++;
				if(dbh.rename_accounts(oldName,newName)>0)
					flag++;
				if(flag==2)
					JOptionPane.showMessageDialog(null,"Rename Successful");
				else
					JOptionPane.showMessageDialog(null,"Rename Not Possible");
				setComboBox();	
			}
		});
		
		delete_all_accounts.addActionListener(							//action listener for delete_all_accounts button to delete all accounts created
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTime();
				DBHandler dbh=new DBHandler();
				if(dbh.clear("Accounts")==0)
				{
					JOptionPane.showMessageDialog(null,"All Accounts Deleted");
					setComboBox();
					if(view_accounts.isSelected()==true)
					{
						view_accounts.setSelected(false);
						view_accounts.setSelected(true);
					}
				}
				else
					JOptionPane.showMessageDialog(null,"Error");					
				setTotalBalance();
			}
		});
		
		accounts.addItemListener(		//item listener for combo box to set the account balance in text field when an account is selected
		new ItemListener()
		{
			public void itemStateChanged(ItemEvent e)
			{
				setTime();
				String name=String.valueOf(accounts.getSelectedItem());
				if(name=="---Select An Account---")								//check if any account is selected
					t_accBal.setText("-");
				else
				{
					DBHandler dbh=new DBHandler();
					String bal=dbh.getBalance_accounts(name);
					if(bal!=null)
						t_accBal.setText(bal);									//setting the balance of the selected account in textfield
				}
			}
		});
		
		credit.addActionListener(					//action listener for credit button to credit amount
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				int flag=0;
				Double amnt;
				String name=String.valueOf(accounts.getSelectedItem());
				java.sql.Timestamp date;
				String comment=t_comments.getText();
				if(name=="---Select An Account---")												//check if any account is selected
				{
					JOptionPane.showMessageDialog(null,"Select Any Account For Transaction");	//prompting to select an account
					return;
				}	
				DBHandler dbh=new DBHandler();
				try																				//checking if the amount is valid or not
				{
					String amnt_str=t_amnt.getText();
					amnt=Double.parseDouble(amnt_str);
					if(amnt_str.contains("d") || amnt_str.contains("f") || amnt_str.contains("e") || amnt<=0)
						throw new UserExceptions("Invalid Amount");
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid Amount");					//prompting for valid amount
					return;
				}
				try
				{
					date=java.sql.Timestamp.valueOf(t_date_time2.getText());
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd hh:mm:ss'");		//prompting for a valid input
					return;
				}				
				if(dbh.credit_debit_accounts(name,amnt)>0)										//editing databases
					flag++;
				if(dbh.credit_debit_transactions(name,amnt,date,comment)>0)
					flag++;
				if(flag==2)
					JOptionPane.showMessageDialog(null,"Transaction Successful");
				else
					JOptionPane.showMessageDialog(null,"Transaction Failed");
				setComboBox();
				setTotalBalance();
				setTime();
			}
		});
		
		debit.addActionListener(					//action listener for debit button to debit amount from the account selected
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				int flag=0;
				Double amnt;
				String name=String.valueOf(accounts.getSelectedItem());
				java.sql.Timestamp date;
				String comment=t_comments.getText();
				if(name=="---Select An Account---")												//check if any account is selected
				{
					JOptionPane.showMessageDialog(null,"Select Any Account For Transaction");	//prompting to select an account
					return;
				}	
				DBHandler dbh=new DBHandler();
				try		//checking if the amount is valid or not
				{
					
					String amnt_str=t_amnt.getText();
					amnt=Double.parseDouble(amnt_str);
					if(amnt_str.contains("d") || amnt_str.contains("f") || amnt_str.contains("e") || amnt<=0)
						throw new UserExceptions("Invalid Amount");
					if(dbh.credit_debit_accounts(name,-amnt)==-2)									//editing databases
					{
						JOptionPane.showMessageDialog(null,"Insufficient Balance");					//prompting for valid amount
						return;
					}
					else
						flag++;
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid Amount");						//prompting for valid amount
					return;
				}
				try
				{
					date=java.sql.Timestamp.valueOf(t_date_time2.getText());
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd hh:mm:ss'");		//prompting for a valid input
					return;
				}	
				if(dbh.credit_debit_transactions(name,-amnt,date,comment)>0)
					flag++;
				if(flag==2)
					JOptionPane.showMessageDialog(null,"Transaction Successful");
				else
					JOptionPane.showMessageDialog(null,"Transaction Failed");
				setComboBox();
				setTotalBalance();
				setTime();
			}
		});
		
		transfer.addActionListener(							//action listener for transfer button to self transfer amount bettween accounts
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTime();
				TransferFrame transfer_frame=new TransferFrame();
			}
		});
		
		transaction.addActionListener(							//action listener for transaction button to view past transactions made
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTime();
				TransactionsFrame transaction_frame=new TransactionsFrame();	
			}
		});
		
		view_accounts.addItemListener(							//action listener for view accounts toggle button to view accounts details'
		new ItemListener()
		{
			public void itemStateChanged(ItemEvent ae)
			{
				setTime();
				accounts_frame.setTable();			
				if(view_accounts.isSelected())
					accounts_frame.setVisible(true);
				else
					accounts_frame.setVisible(false);
			}
		});
		
	}

	public void buildComponents()	//building components
	{
		//Panels
		row1=new JPanel();
		row2=new JPanel();
		row3=new JPanel();
		row4=new JPanel();
		row5=new JPanel();
		p=new JPanel();

		//combobox
		accounts=new JComboBox();
		accounts.setFont(new Font("Soulmate",Font.ITALIC,17));

		//buttons
		delete=new JButton("Delete Account");
		//delete.setBackground(Color.RED);
		rename=new JButton("Rename Account");
		add=new JButton("Add Account");
		//add.setBackground(Color.GREEN);
		credit=new JButton(" Credit Amount ");
		//credit.setBackground(Color.GREEN);
		debit=new JButton(" Debit Amount ");
		//debit.setBackground(Color.RED);
		transfer=new JButton("Self Transfer");
		transaction=new JButton("View Transactions");
		delete_all_accounts=new JButton("Delete Accounts");
		
		delete.setFont(new Font("Soulmate",Font.ITALIC,17));
		rename.setFont(new Font("Soulmate",Font.ITALIC,17));
		add.setFont(new Font("Soulmate",Font.ITALIC,17));
		credit.setFont(new Font("Soulmate",Font.ITALIC,17));
		debit.setFont(new Font("Soulmate",Font.ITALIC,17));
		transfer.setFont(new Font("Soulmate",Font.ITALIC,17));
		transaction.setFont(new Font("Soulmate",Font.ITALIC,17));
		delete_all_accounts.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		//toggle button
		view_accounts=new JToggleButton("View Accounts");
		//view_accounts.setBackground(Color.GREEN);
		view_accounts.setFont(new Font("Soulmate",Font.ITALIC,17));	
		
		//textFileds
		t_accName=new JTextField(20);
		t_openBal=new JTextField(15);
		t_accBal=new JTextField(30);
		t_accBal.setText("-");
		t_accBal.setEditable(false);
		t_amnt=new JTextField(15);
		t_totBal=new JTextField(30);
		t_totBal.setEditable(false);
		t_comments=new JTextField(20);
		t_date_time1=new JTextField(15);
		t_date_time2=new JTextField(15);
		Timestamp ts=new Timestamp(System.currentTimeMillis());
		Date today=ts;
		t_date_time1.setText(today.toString().substring(0,19));
		t_date_time2.setText(today.toString().substring(0,19));
		
		t_accName.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_openBal.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_accBal.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_amnt.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_totBal.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_comments.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_date_time1.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_date_time2.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		//Labels
		l_accName=new JLabel("Account / Wallet Name");
		l_accounts=new JLabel("Accounts");
		l_openBal=new JLabel("Opening Balance");
		l_accBal=new JLabel("Account Balance");
		l_amnt=new JLabel("Amount");
		l_totBal=new JLabel("Total Balance");
		l_comments=new JLabel("Comments");
		l_date_time1=new JLabel("Date/Time");
		l_date_time2=new JLabel("Date/Time");
		
		l_comments.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_accName.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_accounts.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_openBal.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_amnt.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_totBal.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_accBal.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_date_time1.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_date_time2.setFont(new Font("Soulmate",Font.ITALIC,17));
	}


	public void setComboBox()											//setting combobox with items in the database
	{
		accounts.removeAllItems();
		accounts.addItem("---Select An Account---");
		int count,i;
		DBHandler dbh=new DBHandler();
		count=dbh.countAccounts();
		try
		{
			for(i=0;i<count;i++)
				accounts.addItem(dbh.getAccounts(i).getString(1));
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
	}
	
	public void setTotalBalance()					//setting total balance in textfield
	{
		int count,i;
		double total=0;
		DBHandler dbh=new DBHandler();
		count=dbh.countAccounts();
		for(i=0;i<count;i++)
			total+=dbh.getBalance(i);
		t_totBal.setText(String.valueOf(total));
	}
	
	public void setTime()	//update time
	{
		Timestamp ts=new Timestamp(System.currentTimeMillis());
		Date today=ts;
		t_date_time1.setText(today.toString().substring(0,19));
		t_date_time2.setText(today.toString().substring(0,19));
	}
	
	public void designUI()							//design UI
	{

		//row 1 panel
		row1.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row1.add(l_accName);
		row1.add(Box.createHorizontalStrut(70));
		row1.add(t_accName);
		row1.add(Box.createHorizontalStrut(70));
		row1.add(l_openBal);
		row1.add(Box.createHorizontalStrut(70));
		t_openBal.setText("0.0");
		row1.add(t_openBal);
		row1.add(Box.createHorizontalStrut(70));
		row1.add(l_date_time1);
		row1.add(Box.createHorizontalStrut(70));
		row1.add(t_date_time1);
		row1.add(Box.createHorizontalStrut(70));
		row1.add(add);

		//row 2 panel
		row2.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row2.add(l_accounts);
		row2.add(Box.createHorizontalStrut(170));
		accounts.setPreferredSize(new Dimension(300,25));
		row2.add(accounts);
		row2.add(Box.createHorizontalStrut(150));
		row2.add(delete);
		row2.add(Box.createHorizontalStrut(150));
		row2.add(rename);
		row2.add(Box.createHorizontalStrut(150));
		row2.add(delete_all_accounts);
		
		
		//row 3 panel
		row3.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row3.add(l_accBal);
		row3.add(Box.createHorizontalStrut(125));
	    t_accBal.setMaximumSize(new Dimension(100,50));
		row3.add(t_accBal);

		//row 4 panel
		row4.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row4.add(l_amnt);
		row4.add(Box.createHorizontalStrut(50));
		t_amnt.setText("0.0");
		row4.add(t_amnt);
		row4.add(Box.createHorizontalStrut(50));
		row4.add(l_comments);
		row4.add(Box.createHorizontalStrut(50));
		row4.add(t_comments);
		row4.add(Box.createHorizontalStrut(50));
		row4.add(l_date_time2);
		row4.add(Box.createHorizontalStrut(50));
		row4.add(t_date_time2);
		row4.add(Box.createHorizontalStrut(55));
		row4.add(credit);
		row4.add(Box.createHorizontalStrut(55));
		row4.add(debit);

		//row 5 panel
		row5.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row5.add(l_totBal);
		row5.add(Box.createHorizontalStrut(130));
	    t_totBal.setMaximumSize(new Dimension(100,50));
		row5.add(t_totBal);
		row5.add(Box.createHorizontalStrut(150));
		row5.add(transfer);
		row5.add(Box.createHorizontalStrut(150));
		row5.add(transaction);
		row5.add(Box.createHorizontalStrut(125));
		row5.add(view_accounts);

		p.setLayout(new BoxLayout(p,BoxLayout.Y_AXIS));
		p.add(Box.createVerticalStrut(50));
		p.add(row1);
		p.add(Box.createVerticalStrut(50));
		p.add(row2);
		p.add(Box.createVerticalStrut(50));	
		p.add(row3);
		p.add(Box.createVerticalStrut(50));	
		p.add(row4);
		p.add(Box.createVerticalStrut(50));	
		p.add(row5);

		add(p);
		
		/*
		p.setBackground(Color.cyan);
		row1.setBackground(Color.cyan);
		row2.setBackground(Color.cyan);
		row3.setBackground(Color.cyan);
		row4.setBackground(Color.cyan);
		row5.setBackground(Color.cyan);*/
	}
}

public class MyFrameTest
{
	public static void main(String str[])
	{
		MyFrame f=new MyFrame();
		f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);		//setting default close operation (exit when close)
	}
}