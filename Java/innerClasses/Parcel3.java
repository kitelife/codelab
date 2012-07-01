package innerClasses;

public class Parcel3 {

	/**
	 * @param args
	 */
	
	class Contents {
		public int value(){ return 0; }
	}
	
	public Contents contents() {
		return new Contents() {
			private int i = 42;
			public int value() {
				return i;
			}
		};
	}
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Parcel3 p = new Parcel3();
		Contents c = p.contents();
		System.out.println(c.value());
	}

}
