package org.crazyit.app.action;

import com.opensymphony.xwork2.Action;

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
public class LoginAction
	implements Action
{
	//���������ڷ�װ�û������������������
	private String username;
	private String password;
	//���ڷ�װ������������
	private String tip;
	//ϵͳ���õ�ҵ���߼����
	private MyService ms;
	//����ע��ҵ���߼�����������setter����
	public void setMs(MyService ms)
	{
		this.ms = ms;
	}
	//username���Ե�setter��getter����
	public void setUsername(String username)
	{
		this.username = username;
	}
	public String getUsername()
	{
		return this.username;
	}
	//password�����������setter��getter����
	public void setPassword(String password)
	{
		this.password = password;
	}
	public String getPassword()
	{
		return this.password;
	}
	//tip���Ե�getter��setter����
	public void setTip(String tip)
	{
		this.tip = tip;
	}
	public String getTip()
	{
		return this.tip;
	}
	//�����û������execute����
	public String execute() throws Exception
	{
		//����ҵ���߼������valid������
		//��֤�û�������û����������Ƿ���ȷ
		if (ms.valid(getUsername(), getPassword()))
		{
			setTip("���������ϳɹ���");
			return SUCCESS;
		}
		else
		{
			return ERROR;
		}
	}
}
