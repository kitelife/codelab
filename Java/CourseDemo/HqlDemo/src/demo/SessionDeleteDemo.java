package demo;
import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class SessionDeleteDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Session sess = null;
		try{
			sess = HibernateUtil.currentSession();
			Transaction tx = sess.beginTransaction();
			News news = (News)sess.get(News.class, new Integer("6"));
			sess.delete(news);
			sess.flush();
			tx.commit();
			System.out.println(news.getTitle());
		}catch(HibernateException e){
			throw e;
		}finally{
			HibernateUtil.closeSession();
		}
	}

}
