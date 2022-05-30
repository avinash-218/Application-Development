import java.awt.*;
import javax.swing.*;
import java.sql.*;
import javax.swing.table.DefaultTableModel;

public class AccountsFrame extends JFrame
{
	//required components
    DefaultTableModel tableModel;
    JTable table;
	JScrollPane scrollPane;

	public AccountsFrame()	//default constructor
	{
		setResizable(false);							//the frame is not resizable
		setTitle("Accounts");							//title is set
		Toolkit kit = Toolkit.getDefaultToolkit();	
		Image img=kit.getImage("transact.jpg");
		setIconImage(img);								//setting icon
		setSize(290,490);								//setting size of the frame
		setLocation(1635,200);							//set default location of the frame
		buildComponents();
		designUI();										//design user interface
		setVisible(false);								//initially the frame is not visible
		setDefaultCloseOperation(DO_NOTHING_ON_CLOSE);	//close button is disabled
	}
	
	public void buildComponents()		//to build the components of the frame
	{
		tableModel = new DefaultTableModel();
		table = new JTable(tableModel);
		table.setFont(new Font("Soulmate",Font.ITALIC,17));
		table.setEnabled(false);
		//table.setBackground(Color.YELLOW);
		table.setRowHeight(table.getRowHeight() + 10);
	}
	
	public void designUI()				//design user interface of the frame
	{
		scrollPane = new JScrollPane(table);
		add(scrollPane);
	}
	
	public void setTable()				//set table contents
	{
		tableModel.setRowCount(0);		//setting no row
		tableModel.setColumnCount(0);	//setting no column
		int count,i;
		ResultSet temp;
		tableModel.addColumn("No.");
		tableModel.addColumn("Accounts");	//add column Accounts
		tableModel.addColumn("Balance");	//add column Balance
		try
		{
			DBHandler dbh=new DBHandler();
			count=dbh.countAccounts();
			for(i=count-1;i>=0;i--)
			{
				temp=dbh.getAccounts(i);
				tableModel.insertRow(0, new Object[] {i+1,temp.getString(1),temp.getString(2)});
			}
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
	}
}