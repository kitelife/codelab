package demo;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class noArgumentQuery {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Configuration conf = new Configuration().configure();

		SessionFactory sf = conf.buildSessionFactory();
		Session sess = sf.openSession();
		Transaction tx = sess.beginTransaction();
		//........
		List<News> list = sess.createQuery("from News").list();
		/*
		for(Iterator pit = list.iterator(); pit.hasNext();){
			News news = (News)pit.next();
			System.out.println(news.getContent());
		}
		*/
		Iterator<News> pit = list.iterator();
		while(pit.hasNext()){
			News n = pit.next();
			System.out.println(n.getId() + " "+n.getTitle() +" " + n.getContent());
		}
		tx.commit();
	}

}
