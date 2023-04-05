package lee;

import org.springframework.context.*;
import org.springframework.context.support.*;

import org.crazyit.service.impl.*;
/**
 * Description:
 * <br/>��վ: <a href="http://www.crazyit.org">���Java����</a> 
 * <br/>Copyright (C), 2001-2012, Yeeku.H.Lee
 * <br/>This program is protected by copyright laws.
 * <br/>Program Name:
 * <br/>Date:
 * @author  Yeeku.H.Lee kongyeeku@163.com
 * @version  1.0
 */
public class BeanTest
{
	public static void main(String[] args)throws Exception
	{
		ApplicationContext ctx = new
			ClassPathXmlApplicationContext("bean.xml");
		//��ȡ������Bean�������÷�����
		Person p = ctx.getBean("chinese" , Person.class);
		p.test();
		p.readMap();
	}
}