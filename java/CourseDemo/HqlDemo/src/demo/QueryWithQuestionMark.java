package demo;

import java.util.Iterator;
import java.util.List;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class QueryWithQuestionMark {

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
		List<News> list = query.list();
		/*
		for(Iterator pit = list.iterator(); pit.hasNext();){
			News news = (News)pit.next();
			System.out.println(news.getContent());
		}*/
		Iterator it = list.iterator();
		while(it.hasNext()){
			News news = (News)it.next();
			System.out.println(news.getContent());
		}
		tx.commit();
	}

}
