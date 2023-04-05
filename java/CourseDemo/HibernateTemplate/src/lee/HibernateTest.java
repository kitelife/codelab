package lee;

import org.springframework.context.*;
import org.springframework.context.support.*;

import org.crazyit.app.dao.*;
import org.crazyit.app.domain.*;
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
public class HibernateTest
{
	public static void main(String[] args)
	{
		//����Spring����
		ApplicationContext ctx = 
			new ClassPathXmlApplicationContext("bean.xml");
		//��ȡDAO���
		PersonDao pdao = (PersonDao)ctx.getBean("personDao");
		//ѭ������10����¼
		for (int i = 0 ; i < 10  ; i++ )
		{
			pdao.save(new Person(i + "" , i + 10));
		}
		//����DAO����ķ���
		System.out.println(pdao.getPersonNumber());
	}
}