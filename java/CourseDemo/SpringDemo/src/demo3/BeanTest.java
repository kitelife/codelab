package demo3;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class BeanTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ApplicationContext ctx = new ClassPathXmlApplicationContext("bean.xml");
		System.out.println(ctx.getBean("p1") == ctx.getBean("p1"));
		System.out.println(ctx.getBean("p2") == ctx.getBean("p2"));
	}

}
