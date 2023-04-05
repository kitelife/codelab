package demo;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class SessionLoadOverride {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Session sess = null;
		try{
			sess = HibernateUtil.currentSession();
			Transaction tx = sess.beginTransaction();
			News news = new News();
			news.setTitle("����");
			news.setContent("�ѵ���ע��Ҫ�����ǵ���ô?");
			sess.load(news, new Integer("2"));
			tx.commit();
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
