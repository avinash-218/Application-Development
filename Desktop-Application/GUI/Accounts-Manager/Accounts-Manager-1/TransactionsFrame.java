import java.io.*;
import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.sql.*;
import javax.swing.table.DefaultTableModel;
import com.lowagie.text.Document;
import com.lowagie.text.pdf.PdfWriter;
import com.lowagie.text.pdf.PdfPTable;
import com.lowagie.text.pdf.*;

public class TransactionsFrame extends JFrame
{
	//required components
    DefaultTableModel tableModel;
    JTable table;
	JButton clear_filter,b_filter;
	JMenuItem print,clear,edit_trans,del_trans;
	JCheckBox by_accounts,by_date;
	JMenuBar menu_bar;
	JMenu edit,view,file;
	
	public TransactionsFrame()							//default constructor
	{
		setResizable(true);								//the frame is  resizable
		setTitle("Transactions");						//title is set
		Toolkit kit = Toolkit.getDefaultToolkit();	
		Image img=kit.getImage("transact.jpg");
		setExtendedState(JFrame.MAXIMIZED_BOTH);		//frame opens with maximized
		setIconImage(img);								//setting icon
		Dimension size=kit.getScreenSize();				//getting local machine monitor size
		setSize(size.width,size.height);				//setting size of the frame to the original sizde of the system
		buildComponents();
		setTable();										//set table entries
		designUI();										//design user interface
		setVisible(true);								//set the visibility of the frame to be true
		
		print.addActionListener(							//action listener to print table contents
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				DBHandler dbh=new DBHandler();
				int count = dbh.countTransactions("*","*",0);
				Document document=new Document();
				try
				{
					PdfWriter.getInstance(document,new FileOutputStream("Accounts Transaction.pdf"));
					document.open();
					PdfPTable tab=new PdfPTable(6);
					tab.addCell("No");
					tab.addCell("Accounts");
					tab.addCell("Date-Time");
					tab.addCell("Status");
					tab.addCell("Comments");
					tab.addCell("Balance");
					for(int i=0;i<count;i++)
					{
						for(int j=0;j<6;j++)
						{
							Object obj = GetData(table, i, j);
							String value = obj.toString();
							tab.addCell(value);
						}
					}
					document.add(tab);
					document.close();
				}
				catch (Exception e) 
				{
				  System.err.println(e.getMessage());
				}
				JOptionPane.showMessageDialog(null,"Transactions Printed Successfully");
			}
		});
		
		
		clear.addActionListener(							
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				DBHandler dbh=new DBHandler();
				if(dbh.clear("Transactions")==0)
				{
					JOptionPane.showMessageDialog(null,"Transactions Cleared");
					setTable();
				}
				else
					JOptionPane.showMessageDialog(null,"Error");
			}
		});
		
		edit_trans.addActionListener(							//action listener to edit particular transaction
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				int sno = Integer.parseInt(JOptionPane.showInputDialog("Enter The Serial Number of transaction to edit"));
				DBHandler dbh=new DBHandler();
				while(!(sno>0 && sno <= dbh.countTransactions("","",0)))
					sno = Integer.parseInt(JOptionPane.showInputDialog("Enter a Valid Serial Number"));
				try
				{
					ResultSet trans = dbh.getTransactions(dbh.countTransactions("","",0)-sno);
					EditTransactionFrame edit_trans_frame=new EditTransactionFrame(trans.getString(2).substring(0,19),trans
.getString(4),sno);
				}
				catch(Exception ex)
				{
					System.out.println(ex);
				}
				setVisible(false);
			}	
		});
		
		del_trans.addActionListener(							
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				int sno = Integer.parseInt(JOptionPane.showInputDialog("Enter The Serial Number of transaction to edit"));
				DBHandler dbh=new DBHandler();
				while(!(sno>0 && sno <= dbh.countTransactions("","",0)))
					sno = Integer.parseInt(JOptionPane.showInputDialog("Enter a Valid Serial Number"));
				try
				{
					int x=dbh.delete_a_transaction(sno-1);
				}
				catch(Exception ex)
				{
					System.out.println(ex);
				}
				setVisible(false);
			}
		});		
		
		clear_filter.addActionListener(							
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				setTable();
				by_accounts.setSelected(false);
				by_date.setSelected(false);
			}
		});
		
		b_filter.addActionListener(
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				String acc_name="",str_date="";
				java.sql.Date date;
				DBHandler dbh=new DBHandler();
				ResultSet temp;
				int flag=0;
				
				if(by_accounts.isSelected()==false && by_date.isSelected()==false)	//choosed none
				{
					JOptionPane.showMessageDialog(null,"Choose Filtering Options in Checkbox");
					flag=4;
				}
				else if(by_accounts.isSelected() && by_date.isSelected()==false)	//by account name
				{
					acc_name=JOptionPane.showInputDialog("Account Name?");
					flag=1;
				}				
				else if(by_date.isSelected() && by_accounts.isSelected()==false)	//by date
				{
					try
					{
						str_date=JOptionPane.showInputDialog("Enter Date in format 'yyyy-mm-dd'");
						date=java.sql.Date.valueOf(str_date);
					}
					catch(Exception ex)
					{
						by_date.setSelected(false);
						JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd'");		//prompting for a valid input
						return;
					}
					flag=2;
				}
				else															//by account name and date
				{
					acc_name=JOptionPane.showInputDialog("Account Name?");
					try
					{
						str_date=JOptionPane.showInputDialog("Enter Date in format 'yyyy-mm-dd'");
						date=java.sql.Date.valueOf(str_date);
					}
					catch(Exception ex)
					{
						by_date.setSelected(false);
						JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd'");		//prompting for a valid input
						return;
					}
					flag=3;
				}
				
				if(flag!=4)
				{
					int i,count=dbh.countTransactions(acc_name,str_date,flag);
					if(count==0)
					{
						JOptionPane.showMessageDialog(null,"No Such Transactions Found");	
						by_accounts.setSelected(false);
					}
					else
					{
						tableModel.setRowCount(0);
						try
						{
							for(i=0;i<count;i++)
							{
								temp=dbh.getTransactions(acc_name,str_date,flag,i);
								tableModel.insertRow(0, new Object[] {count-i,temp.getString(1),temp.getString(2),temp.getString(3),temp.getString(4),temp.getString(5) });
							}
						}
						catch(Exception e)
						{
							System.out.println(e);
						}
					}
				}
			}
		});
	}
			
	
	public void buildComponents()
	{
		tableModel = new DefaultTableModel();
		table = new JTable(tableModel);
		table.setFont(new Font("Soulmate",Font.ITALIC,17));
		table.setEnabled(false);
		//table.setBackground(Color.YELLOW);
		table.setRowHeight(table.getRowHeight() + 10);
		
		menu_bar=new JMenuBar();
		
		file=new JMenu("File");
		file.setFont(new Font("Soulmate",Font.ITALIC,17));
		edit=new JMenu("Edit");
		edit.setFont(new Font("Soulmate",Font.ITALIC,17));
		view=new JMenu("View");
		view.setFont(new Font("Soulmate",Font.ITALIC,17));

		print=new JMenuItem("Print Transactions");
		print.setFont(new Font("Soulmate",Font.ITALIC,17));
		edit_trans=new JMenuItem("Edit Transaction");
		edit_trans.setFont(new Font("Soulmate",Font.ITALIC,17));
		del_trans=new JMenuItem("Delete Transaction");
		del_trans.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		by_accounts=new JCheckBox("By Accounts");
		by_accounts.setFont(new Font("Soulmate",Font.ITALIC,17));
		by_date=new JCheckBox("By Date       ");
		by_date.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		clear=new JMenuItem("Clear Transactions");
		clear.setFont(new Font("Soulmate",Font.ITALIC,17));
		clear_filter=new JButton("Clear Filter ");
		clear_filter.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		b_filter=new JButton("Filter          ");
		b_filter.setFont(new Font("Soulmate",Font.ITALIC,17));

		//accelerator
		print.setAccelerator(KeyStroke.getKeyStroke(KeyEvent.VK_P, Event.CTRL_MASK));
	}
	
	public void setTable()							//set the table entries
	{
		int count,i;
		ResultSet temp;
		tableModel.setRowCount(0);		//setting no row
		tableModel.setColumnCount(0);	//setting no column
		tableModel.addColumn("Serial No.");
		tableModel.addColumn("Accounts");			//adding required columns in the table
		tableModel.addColumn("Date Time");
		tableModel.addColumn("Status");
		tableModel.addColumn("Comments");
		tableModel.addColumn("Balance");
		try
		{
			DBHandler dbh=new DBHandler();
			count=dbh.countTransactions("","",0);
			for(i=0;i<count;i++)
			{
				temp=dbh.getTransactions(i);
				tableModel.insertRow(0, new Object[] {count-i,temp.getString(1),temp.getString(2).substring(0,19),temp.getString(3),temp.getString(4),temp.getString(5) });
			}
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
	}
	
	public void designUI()
	{
		//panel
		JScrollPane scrollPane = new JScrollPane(table);
		add(scrollPane);
		
		//menu bar
		menu_bar.add(file);	//File menu
		file.add(print);	
		menu_bar.add(edit);	//edit menu
		edit.add(clear);
		edit.add(edit_trans);
		edit.add(del_trans);
		menu_bar.add(view);	//view menu
		view.add(by_accounts);
		view.add(by_date);
		view.add(b_filter);
		view.add(clear_filter);
		setJMenuBar(menu_bar);
	}
	
	public Object GetData(JTable table, int row_index, int col_index)
	{
		return table.getModel().getValueAt(row_index, col_index);
	}

}