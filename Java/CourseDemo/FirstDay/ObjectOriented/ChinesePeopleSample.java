package ObjectOriented;

class ChinesePeople {
	// 属性
	private String name;
	private int age;
	private String gender;

	// 行为，或者说方法
	ChinesePeople(String name, int age, String gender){
		this.name = name;
		this.age = age;
		this.gender = gender;
	}
	
	String getPeopleName(){
		return name;
	}
	
	int getPeopleAge(){
		return age;
	}
	
	String getPeopleGender() {
		return gender;
	}
	
}

public class ChinesePeopleSample {
	public static void main(String[] args){
		// 实例化类ChinesePeople为cp1
		ChinesePeople cp1 = new ChinesePeople("张三", 30, "男");
		System.out.println("姓名: " + cp1.getPeopleName() + "\n" + "年齡: " + cp1.getPeopleAge() + "\n" + "性別： " + cp1.getPeopleGender() + "\n");
		// 实例化类ChinesePeople为cp2
		ChinesePeople cp2 = new ChinesePeople("Hebe", 26, "女");
		System.out.println("姓名: " + cp2.getPeopleName() + "\n" + "年齡: " + cp2.getPeopleAge() + "\n" + "性別： " + cp2.getPeopleGender());
	}
}
