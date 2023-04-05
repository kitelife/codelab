package demo;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class SessionLoadDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Session sess = null;
		try{
			sess = HibernateUtil.currentSession();
			Transaction tx = sess.beginTransaction();
			// ������ݿ�û��ƥ������ݿ��¼��load()�������ܻ��׳��޷��ָ����쳣
			News news = (News)sess.load(News.class, new Integer("2"));
			//tx.commit();
			System.out.println(news.getId());
			System.out.println(news.getTitle());
			System.out.println(news.getContent());
			
		}catch(HibernateException e){
			throw e;
		}finally{
			HibernateUtil.closeSession();
		}
	}

}
