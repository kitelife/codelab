package demo;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class UniqueResultDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub

		Configuration conf = new Configuration().configure();

		SessionFactory sf = conf.buildSessionFactory();
		Session sess = sf.openSession();
		Transaction tx = sess.beginTransaction();
		Query query = sess.createQuery("from News where title=?");
		query.setString(0, "linux");
		News news = (News)query.uniqueResult();
		System.out.println(news.getId());
		System.out.println(news.getTitle());
		System.out.println(news.getContent());
		tx.commit();
	}

}
