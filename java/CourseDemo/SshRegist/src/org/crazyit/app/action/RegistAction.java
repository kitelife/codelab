package org.crazyit.app.action;

import com.opensymphony.xwork2.Action;

import org.crazyit.app.domain.*;
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
public class RegistAction
	implements Action
{
	//���������ڷ�װ�û��������������
	private Person person;
	//���ڷ�װ������������
	private String tip;
	//ϵͳ���õ�ҵ���߼����
	private LeeService leeService;
	//����ע��ҵ���߼�����������setter����
	public void setLeeService(LeeService leeService)
	{
		this.leeService = leeService;
	}

	//person���Ե�setter��getter����
	public void setPerson(Person person)
	{
		this.person = person;
	}
	public Person getPerson()
	{
		return this.person;
	}

	//tip���Ե�setter��getter����
	public void setTip(String tip)
	{
		this.tip = tip;
	}
	public String getTip()
	{
		return this.tip;
	}

	//�����û������execute����
	public String execute()
		throws Exception
	{
		//����ҵ���߼������regist��������������
		if (leeService.regist(person))
		{
			setTip("������ע��ɹ���");
			return SUCCESS;
		}
		else
		{
			return ERROR;
		}
	}
}