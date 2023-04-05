package org.crazyit.app.dao.impl;

import org.springframework.orm.hibernate3.support.HibernateDaoSupport;

import java.util.*;

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
public class PersonDaoHibernate
	extends HibernateDaoSupport implements PersonDao
{
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
			.find("from Person p where p.name like ?" , name);
	}
	
	/**
	 * ��ѯȫ��Personʵ��
	 * @return ȫ��Personʵ��
	 */
	public List<Person> findAllPerson()
	{
		return (List<Person>)getHibernateTemplate()
			.find("from Person");
	}
}