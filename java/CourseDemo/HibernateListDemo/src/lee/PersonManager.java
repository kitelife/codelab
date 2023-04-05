package lee;

import org.hibernate.Transaction;
import org.hibernate.Session;

import java.util.Date;
import java.util.List;
import java.util.ArrayList;

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
public class PersonManager
{
	public static void main(String[] args)
	{
		PersonManager mgr = new PersonManager();
		mgr.createAndStorePerson();
		HibernateUtil.sessionFactory.close();
	}
	//����������Person����
	private void createAndStorePerson()
	{
		//���̰߳�ȫ��session����
		Session session = HibernateUtil.currentSession();
		//������
		Transaction tx = session.beginTransaction();
		//����Person����
		Person yeeku = new Person();
		//ΪPerson������������
		yeeku.setAge(29);
		yeeku.setName("crazyit.org");
		//����List����
		List<String> schools = new ArrayList<String>();
		schools.add("Сѧ");
		schools.add("��ѧ");
		//����List��������
		yeeku.setSchools(schools);
		session.save(yeeku);
		tx.commit();
		HibernateUtil.closeSession();
	}
}