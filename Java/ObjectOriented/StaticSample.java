package ObjectOriented;

public class StaticSample {
	static int count = 0;
	public void incrementCount(){
		count++;
		System.out.println(count);
	}
	public static void main(String[] args) {
		StaticSample ss1 = new StaticSample();
		ss1.incrementCount();
		StaticSample ss2 = new StaticSample();
		ss2.incrementCount();
		ss2.incrementCount();
		ss1.incrementCount();
	}

}
