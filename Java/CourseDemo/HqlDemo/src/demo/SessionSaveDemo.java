package demo;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class SessionSaveDemo {

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
			news.setTitle("ฤ๚บร");
			news.setContent("Java3E,Java Web, Struts2, Hibernate, Spring");
			sess.save(news);
			//sess.flush();
			tx.commit();
		}catch(HibernateException e){
			throw e;
		}finally{
			HibernateUtil.closeSession();
		}
	}

}
