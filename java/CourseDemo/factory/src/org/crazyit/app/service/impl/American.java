package org.crazyit.app.service.impl;

import org.crazyit.app.service.*;
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
public class American
	implements Person
{
	//ʵ��Person�ӿڱ���ʵ��������������	
	public String sayHello(String name)
	{
		return name + ",Hello!";
	}
	public String sayGoodBye(String name)
	{
		return name + ",Good Bye!";
	}
}