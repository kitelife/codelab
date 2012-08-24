package demo4;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class ExampleTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ApplicationContext ctx = new ClassPathXmlApplicationContext("bean.xml");
		
		ExampleBean eb = ctx.getBean("examplebean", ExampleBean.class);
		System.out.println(eb.getIntegerProperty());
		System.out.println(eb.getDoubleProperty());
	}

}
