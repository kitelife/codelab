package demo2;

import demo1.Axe;
import demo1.Person;

public class Chinese implements Person{


	private Axe axe;
	public Chinese(){
		
	}
	public Chinese(Axe axe){
		this.axe = axe;
	}
	
	public void useAxe(){
		System.out.println(axe.chop());
	}
}
