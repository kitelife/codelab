package ObjectOriented;

interface Instrument {
	void giveSound();
}

class GiTa implements Instrument {
	String whose;
	GiTa(String whose){
		this.whose = whose;
	}
	
	public void giveSound(){
		System.out.println("DangDiDong.....");
	};
}

class DiZi implements Instrument {
	String fromWhere;
	DiZi(String fromWhere){
		this.fromWhere = fromWhere;
	}
	
	public void giveSound(){
		System.out.println("Di....Wu");
	}
}

class SomePerson{
	String name;
	SomePerson(String name){
		this.name = name;
	}
	public void playInstrument(Instrument inst){
		inst.giveSound();
	}
}
public class PlayInstruments {

	public static void main(String[] args){
		SomePerson sp = new SomePerson("王五");
		GiTa gt = new GiTa("张三");
		sp.playInstrument(gt);
		DiZi dz = new DiZi("云南");
		sp.playInstrument(dz);
	}
}
