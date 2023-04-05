package ObjectOriented;

class Fruit {
    private String fruitName;
    private String shape;
    private String smell;
    private String taste;
    // private String fruitName, shape, smell, taste;
    Fruit(){

    }

    Fruit(String fruitName, String shape, String smell, String taste){
        this.fruitName = fruitName;
        this.shape = shape;
        this.smell = smell;
        this.taste = taste;
    }

    public void howToEat(){
        System.out.println("怎样吃" + this.fruitName + "啊?");
    }

    public void aboutThisFruit(){
        System.out.println("名称：" + this.fruitName +"    形状：" +
            this.shape + "  气味：" + this.smell + "   味道：" + this.taste);
    }
}

public class Constructor {
	
    public static void main(String[] args){
        Fruit f1 = new Fruit("苹果", "圆形", "有点清香", "甜甜的");
        f1.howToEat();
        f1.aboutThisFruit();
        Fruit f2 = new Fruit();
        f2.howToEat();
        f2.aboutThisFruit();
    }
}