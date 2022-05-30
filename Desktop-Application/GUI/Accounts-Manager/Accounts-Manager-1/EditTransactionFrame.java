import java.awt.*;
import javax.swing.*;
import java.awt.event.*;
import javax.swing.event.*;
import java.sql.Timestamp;
import java.util.Date;

public class EditTransactionFrame extends JFrame
{
	//required components
	JLabel l_comment,l_date_time;
	JTextField t_comment,t_date_time;
	JButton edit;
	JPanel row1,row2,row3,p;
	
	public EditTransactionFrame(String s_date,String comment,int index)	//default constructor
	{
		setResizable(false);							//the frame is not resizable
		setTitle("Edit Transaction");						//title is set
		setSize(400,400);								//size is set
		setLocation(520,175);							//default location of the frame is set
		setVisible(true);								//set the visibility of the frame to be true
		buildComponents(s_date,comment);	
		designUI();										//design user interface
		Toolkit kit = Toolkit.getDefaultToolkit();	
		Image img=kit.getImage("self.png");
		setIconImage(img);								//setting icon
	
		edit.addActionListener(						//action listener for transfer button
		new ActionListener()
		{
			public void actionPerformed(ActionEvent ae)
			{
				String comment=t_comment.getText();
				String new_date;
				try
				{
					new_date=java.sql.Timestamp.valueOf(t_date_time.getText()).toString();
				}
				catch(Exception ex)
				{
					JOptionPane.showMessageDialog(null,"Enter a Valid date in the format 'yyyy-mm-dd hh:mm:ss'");//prompting for a valid input
					return;
				}
				DBHandler dbh=new DBHandler();
				dbh.edit_transaction(index,new_date,comment);
				JOptionPane.showMessageDialog(null,"Edit Successfull");
				setVisible(false);
			}
		});
		
	}
	public void buildComponents(String s_date,String comment)	//building components
	{
		//Panels
		row1=new JPanel();
		row2=new JPanel();
		row3=new JPanel();
		p=new JPanel();
		
		//buttons
		edit=new JButton("Edit");
		edit.setFont(new Font("Soulmate",Font.ITALIC,17));
		
		//textFileds
		t_comment=new JTextField(23);
		t_date_time=new JTextField(23);
		t_date_time.setText(s_date);
		
		t_comment.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_date_time.setFont(new Font("Soulmate",Font.ITALIC,17));
		t_comment.setText(comment);
		
		//Labels
		l_comment=new JLabel("Comments");
		l_date_time=new JLabel("Date/Time");
		
		l_comment.setFont(new Font("Soulmate",Font.ITALIC,17));
		l_date_time.setFont(new Font("Soulmate",Font.ITALIC,17));
	}
	
	public void designUI()	//design UI
	{
		//row1
		row1.add(l_comment);
		row1.add(t_comment);
		
		//row2
		row2.add(l_date_time);
		row2.add(t_date_time);
		
		//row3
		row3.add(edit);
		
		p.setLayout(new BoxLayout(p,BoxLayout.Y_AXIS));
		p.add(row1);
		p.add(Box.createVerticalStrut(30));
		p.add(row2);
		p.add(Box.createVerticalStrut(30));
		p.add(row3);

		add(p);
	}
}