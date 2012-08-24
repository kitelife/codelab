package demo2;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

import demo1.Person;

public class BeanTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ApplicationContext ctx = new ClassPathXmlApplicationContext("bean.xml");
		Person p = ctx.getBean("chinese2", Person.class);
		p.useAxe();
	}

}
