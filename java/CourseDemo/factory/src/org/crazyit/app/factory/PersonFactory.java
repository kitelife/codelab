package org.crazyit.app.factory;

import org.crazyit.app.service.*;
import org.crazyit.app.service.impl.*;
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
public class PersonFactory
{
	/**
	 * ���Personʵ����ʵ����������
	 * @param ethnic ���������ĸ�Personʵ���Ĳ���
	 * @return ����Personʵ��
	 */
	public Person getPerson(String ethnic)
	{
		if (ethnic.equalsIgnoreCase("chin"))
		{
			return new Chinese();
		}
		else
		{
			return new American();
		}
	}
}
