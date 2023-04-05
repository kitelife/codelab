package org.crazyit.app.domain;

import java.util.List;
import java.util.ArrayList;

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
public class Person
{
	//��ʶ����
	private Integer id;
	//��ͨ����name
	private String name;
	//��ͨ����age
	private int age;
	//�������ԣ������ö��������ѧУ
	private List<String> schools = new ArrayList<String>();
	
	//id���Ե�setter��getter����
	public void setId(Integer id)
	{
		this.id = id;
	}
	public Integer getId()
	{
		return this.id;
	}
	
	//name���Ե�setter��getter����
	public void setName(String name)
	{
		this.name = name;
	}
	public String getName()
	{
		return this.name;
	}
	
	//age���Ե�setter��getter����
	public void setAge(int age)
	{
		this.age = age;
	}
	public int getAge()
	{
		return this.age;
	}
	
	//schools���Ե�setter��getter����
	public void setSchools(List<String> schools)
	{
		this.schools = schools;
	}
	public List<String> getSchools()
	{
		return this.schools;
	}
}