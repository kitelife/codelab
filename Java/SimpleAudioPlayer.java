import javax.media.*; 
import java.io.File; 
import java.io.IOException; 
import java.net.URL; 
import java.util.Scanner;
public class SimpleAudioPlayer {
	private Player audioPlayer=null;
	
	public SimpleAudioPlayer(URL url)throws IOException,NoPlayerException,CannotRealizeException
	{
		audioPlayer=Manager.createRealizedPlayer(url);
	}
	
	public SimpleAudioPlayer(File file)throws IOException,NoPlayerException,CannotRealizeException
	{
		this(file.toURI().toURL());
	}
	
	public void play()
	{
		audioPlayer.start();
	}
	
	public void stop()
	{
		audioPlayer.stop();
		audioPlayer.close();
	}
	
	public Player get()
	{
		return audioPlayer;
	}
	
	public static void main(String[] args) throws NoPlayerException, CannotRealizeException, IOException, InterruptedException
	{
		File audioFile=new File(args[0]);
		SimpleAudioPlayer player=new SimpleAudioPlayer(audioFile);
		player.play();
		
		Player p=player.get();
		Scanner s=new Scanner(System.in);
		String enter=s.next();
		if(p==null||enter.equals("q"))
		{
			player.stop();
		}
		return ;
	}
}