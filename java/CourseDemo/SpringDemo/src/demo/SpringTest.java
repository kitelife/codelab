package demo;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class SpringTest {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		ApplicationContext ctx = new ClassPathXmlApplicationContext("bean.xml");
		System.out.println(ctx);
		//PersonService ps = new PersonService();
		//ps.setName("wawa");
		PersonService ps = ctx.getBean("personService", PersonService.class);
		ps.info();
	}

}
