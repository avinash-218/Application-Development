import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.sql.Timestamp;
import java.util.Date;
import java.util.concurrent.TimeUnit;

public class TransferFrame extends JFrame
{
	//required components
	JLabel l_from,l_to,l_amount,l_comment,l_date_time;
	JComboBox c_from,c_to;
	JTextField t_amount,t_comment,t_date_time;
	JButton transfer;
	JPanel row1,row3,row5,row6,row7,row8,p;
	
	public TransferFrame()	//default constructor
	{
		setResizable(false);							//the frame is not resizable
		setTitle("Self Transfer");						//title is set
		setSize(600,700);								//size is set
		setLocation(520,175);							//default location of the frame is set
		setVisible(true);								//set the visibility of the frame to be true
		buildComponents();	
		setComboBox();
		designUI();										//design user interface
		Toolkit kit = Toolkit.getDefaultToolkit();	
		Image img=kit.getImage("self.png");
		setIconImage(img);								//setting icon
	
		transfer.addActionListener(						//action listener for transfer button
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				int flag=0;
				double amount=0;
				String from=String.valueOf(c_from.getSelectedItem());
				String to=String.valueOf(c_to.getSelectedItem());
				String comment=t_comment.getText();
				java.sql.Timestamp date;
				if(from=="---Select An Account---" || to=="---Select An Account---" || from.equals(to))		//accounts to be selected for transfer
				{
					JOptionPane.showMessageDialog(null,"Select Two Different Accounts");					//prompting to select different accounts
					return;
				}
				try					//amount should be of type double
				{
					String amount_str=t_amount.getText();
					amount=Double.parseDouble(amount_str);
					/* Since in java d denotes decimal f denotes floating point numbers and so on, input should not be accepted if such values 
					   entered in textField
					*/
					if(amount_str.contains("d") || amount_str.contains("f") || amount_str.contains("e") || amount<=0)
						throw new UserExceptions("Invalid Amount");
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid Amount");								//prompting for a valid input
					return;
				}
				
				try
				{
					date=java.sql.Timestamp.valueOf(t_date_time.getText());
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd hh:mm:ss'");		//prompting for a valid input
					return;
				}	
				
				
				DBHandler dbh=new DBHandler();
				if(dbh.credit_debit_accounts(from,-amount)>0)												//editing databases
					flag++;
				else
				{
						JOptionPane.showMessageDialog(null,"Insufficient Balance");							//prompting for valid amount
						return;
				}
				//editing databases and ensuring if all edit is successfull
				if(dbh.credit_debit_accounts(to,amount)>0)													
					flag++;
				if(dbh.credit_debit_transactions(from,-amount,date,comment)>0)
					flag++;
				date.setTime(date.getTime() + 1000);
				if(dbh.credit_debit_transactions(to,amount,date,comment)>0)
					flag++;
				if(flag==4)
					JOptionPane.showMessageDialog(null,"Transaction Successful");
				else
					JOptionPane.showMessageDialog(null,"Transaction Failed");
				Timestamp ts=new Timestamp(System.currentTimeMillis());
				Date today=ts;
				t_date_time.setText(today.toString().substring(0,19));
				try
				{
					TimeUnit.SECONDS.sleep(1);
				}
				catch(Exception e)
				{
					System.out.println(e);
				}
			}
		});
		
	}
	public void buildComponents()	//building components
	{
		//Panels
		row1=new JPanel();		
		row3=new JPanel();	
		row5=new JPanel();
		row6=new JPanel();
		row7=new JPanel();
		row8=new JPanel();
		p=new JPanel();
		/*
		row1.setBackground(Color.YELLOW);
		row3.setBackground(Color.YELLOW);
		row5.setBackground(Color.YELLOW);
		row6.setBackground(Color.YELLOW);
		row7.setBackground(Color.YELLOW);
		row8.setBackground(Color.YELLOW);
		p.setBackground(Color.YELLOW);*/
		
		
		//combobox
		c_from=new JComboBox();
		c_to=new JComboBox();
		
		c_from.setFont(new Font("Soulmate",Font.ITALIC,17));
		c_to.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		//buttons
		transfer=new JButton("Transfer");
		transfer.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		//textFileds
		t_amount=new JTextField(23);
		t_comment=new JTextField(23);
		t_date_time=new JTextField(23);
		Timestamp ts=new Timestamp(System.currentTimeMillis());
		Date today=ts;
		t_date_time.setText(today.toString().substring(0,19));
		
		t_amount.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_comment.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_date_time.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		//Labels
		l_from=new JLabel("Transfer From");
		l_to=new JLabel("Transfer To");
		l_amount=new JLabel("Amount");
		l_comment=new JLabel("Comments");
		l_date_time=new JLabel("Date/Time");
		
		l_amount.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_to.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_from.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_comment.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_date_time.setFont(new Font("Soulmate",Font.ITALIC,17));
	}

	public void setComboBox()										//setting combobox with items in the database
	{
		c_from.removeAllItems();									//remove all items from combobox
		c_from.addItem("---Select An Account---");
		c_to.removeAllItems();
		c_to.addItem("---Select An Account---");
		int count,i;
		DBHandler dbh=new DBHandler();
		count=dbh.countAccounts();
		for(i=0;i<count;i++)
		{
		try
		{
				c_from.addItem(dbh.getAccounts(i).getString(1));
				c_to.addItem(dbh.getAccounts(i).getString(1));
		}
		catch(Exception ex)
		{
			System.out.println(ex);
		}
		}
	}
	
	public void designUI()	//design UI
	{
		//row1 panel
		row1.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row1.add(l_from);
		
		//row3 panel
		row3.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row3.add(l_to);
		
		//row5 panel
		row5.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		l_amount.setMaximumSize(new Dimension(100,30));
		row5.add(l_amount);
		row5.add(Box.createHorizontalStrut(50));
		t_amount.setMaximumSize(new Dimension(50,30));
		row5.add(t_amount);
		
		//row6
		row6.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		l_comment.setMaximumSize(new Dimension(100,30));
		row6.add(l_comment);
		row6.add(Box.createHorizontalStrut(25));
		t_comment.setMaximumSize(new Dimension(50,30));
		row6.add(t_comment);
		
		//row7
		row7.setLayout(new FlowLayout(FlowLayout.LEFT,20,20));
		row7.add(l_date_time);
		row7.add(Box.createHorizontalStrut(32));
		row7.add(t_date_time);
		
		
		//row8
		row8.setLayout(new FlowLayout(FlowLayout.CENTER,20,20));
		row8.add(transfer);
		
		p.setLayout(new BoxLayout(p,BoxLayout.Y_AXIS));
		p.add(row1);
		c_from.setMaximumSize(new Dimension(250,30));
		p.add(c_from);
		p.add(Box.createVerticalStrut(30));
		p.add(row3);
		c_to.setMaximumSize(new Dimension(250,30));
		p.add(c_to);
		p.add(Box.createVerticalStrut(30));
		p.add(row5);
		p.add(Box.createVerticalStrut(30));
		p.add(row6);
		p.add(Box.createVerticalStrut(30));
		p.add(row7);
		p.add(Box.createVerticalStrut(30));
		p.add(row8);

		add(p);
	}

}