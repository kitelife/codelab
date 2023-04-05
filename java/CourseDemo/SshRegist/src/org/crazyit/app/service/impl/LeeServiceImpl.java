package org.crazyit.app.service.impl;

import org.crazyit.app.dao.*;
import org.crazyit.app.service.*;
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
public class LeeServiceImpl
	implements LeeService
{
	private PersonDao personDao;
	//����ע��DAO��������setter����
	public void setPersonDao(PersonDao personDao)
	{
		this.personDao = personDao;
	}
	//ע���û�
	public boolean regist(Person person)
	{
		//����DAO����ķ�����ʵ��ҵ���߼�
		int result = personDao.save(person);
		if (result > 0)
		{
			return true;
		}
		return false;
	}
}
