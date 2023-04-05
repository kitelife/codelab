package org.crazyit.app.dao.impl;

import java.util.List;

import org.hibernate.SessionFactory;

import org.springframework.orm.hibernate3.HibernateTemplate;

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
public class PersonDaoImpl
	implements PersonDao
{
	//����һ��HibernateTemplate��������ִ�г־û�����
	private HibernateTemplate ht = null;
	//Hibernate�־û����������SessionFactory
	private SessionFactory sessionFactory;
	//����ע��SessionFactory��setter����
	public void setSessionFactory(SessionFactory sessionFactory)
	{
		this.sessionFactory = sessionFactory;
	}
	//��ʼ��HibernateTemplate�ķ���
	private  HibernateTemplate getHibernateTemplate()
	{
		if (ht == null)
		{
			ht = new HibernateTemplate(sessionFactory);
		}
		return ht;
	}

	/**
	 * ����Personʵ��
	 * @param id ��Ҫ���ص�Personʵ���ı�ʶ����ֵ
	 * @return ָ��id��Ӧ��Personʵ��
	 */ 
	public Person get(Integer id)
	{
		return getHibernateTemplate()
			.get(Person.class, id); 
	}
	
	/**
	 * ����Personʵ��
	 * @param person ��Ҫ�����Personʵ��
	 * @return �ոձ����Personʵ���ı�ʶ����ֵ
	 */   
	public Integer save(Person person)
	{
		return (Integer)getHibernateTemplate()
			.save(person);
	}
	
	/**
	 * �޸�Personʵ��
	 * @param person ��Ҫ�޸ĵ�Personʵ��
	 */
	public void update(Person person)
	{
		getHibernateTemplate().update(person);
	}	
	
	/**
	 * ɾ��Personʵ��
	 * @param id ��Ҫɾ����Personʵ���ı�ʶ����ֵ
	 */
	public void delete(Integer id)
	{
		getHibernateTemplate().delete(get(id));
	}
	
	/**
	 * ɾ��Personʵ��
	 * @param person ��Ҫɾ����Personʵ��
	 */
	public void delete(Person person)
	{
		getHibernateTemplate().delete(person);
	}
	
	/**
	 * �����û�������Person
	 * @param name ��ѯ������
	 * @return ָ���û�����Ӧ��ȫ��Person
	 */
	public List<Person> findByName(String name)
	{
		return (List<Person>)getHibernateTemplate()
			.find("from Person p where p.name = ?" , name);
	}
	
	/**
	 * ��ѯȫ��Personʵ��
	 * @return ȫ��Personʵ��
	 */
	public List findAllPerson()
	{
		return (List<Person>)getHibernateTemplate()
			.find("from Person");
	}
	
	/**
	 * ��ѯ���ݱ���Personʵ��������
	 * @return ���ݱ���Personʵ��������
	 */
	public long getPersonNumber()
	{
		return (Long)getHibernateTemplate().find
			("select count(*) from Person as p")
			.get(0);
	}
}