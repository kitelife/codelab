package AccessControl;

import Hello.HelloDate;
import ObjectOriented.SpaceShipDelegation;
import ObjectOriented.ChinesePeopleSample;
//import ObjectOriented.*;

public class PublicAccess {

	public static void main(String[] args){
		HelloDate.main(new String[2]);
		SpaceShipDelegation ssd = new SpaceShipDelegation("World");
		ssd.forward(100);
		ChinesePeopleSample.main(new String[1]);
	}
}
