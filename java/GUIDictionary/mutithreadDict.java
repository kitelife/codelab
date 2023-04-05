//这个程序其实很需要进行重构，GoogleDict.java和IcibaDict.java相同的代码太多

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;

public class mutithreadDict {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub		
		EventQueue.invokeLater(new Runnable()
		{
			public void run()
			{
				TextComponentFrame frame = new TextComponentFrame();
				frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
				frame.setVisible(true);
			}
		});
		
	}
}

class TextComponentFrame extends JFrame
{
	String googleResult,icibaResult;
	public TextComponentFrame()
	{
		setTitle("MultithreadDict");
		setSize(DEFAULT_WIDTH,DEFAULT_HEIGHT);
	
		final JTextField textfield = new JTextField();
		JPanel northPanel = new JPanel();
		northPanel.setLayout(new GridLayout(1,1));
		northPanel.add(textfield);
		add(northPanel,BorderLayout.NORTH);
		
		JPanel southPanel = new JPanel();
		JButton OKButton = new JButton("OK");
		southPanel.add(OKButton);
		add(southPanel);
		
		final JTextArea textArea = new JTextArea(30,600);
		textArea.setEditable(false);
		JScrollPane scrollPane = new JScrollPane(textArea);
		add(scrollPane,BorderLayout.SOUTH);
		
		OKButton.addActionListener(new ActionListener(){
			public void actionPerformed(ActionEvent event)
			{
				GoogleDict google=new GoogleDict(textfield.getText());
				IcibaDict iciba=new IcibaDict(textfield.getText());
				try{
					google.start();
					google.sleep(2000);
					iciba.start();
					iciba.sleep(2000);
				}
				catch(Exception e)
				{
					e.printStackTrace();
				}
				googleResult = google.ReturnResult();
				icibaResult = iciba.ReturnResult();
				
				textArea.setFont(new Font("汉真广标",Font.BOLD,14));
				textArea.setBackground(Color.YELLOW);
				
				textArea.setText("谷歌翻译的结果：>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>" 
						+"\n"+googleResult+"\n"+"爱词霸翻译的结果：>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"
						+"\n"+icibaResult+"\n");
				textArea.setCaretPosition(0);
			}
		});
	}
	public static final int DEFAULT_WIDTH = 600;
	public static final int DEFAULT_HEIGHT = 650;
}
