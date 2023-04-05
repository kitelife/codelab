package demo;

import java.util.AbstractList;
import java.util.ArrayList;
import java.util.Iterator;

import org.hibernate.Query;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;
import java.util.*;


public class QueryWithListArguments {

	/**
	 * @param args
	 */
	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub

		Configuration conf = new Configuration().configure();

		SessionFactory sf = conf.buildSessionFactory();
		Session sess = sf.openSession();
		Transaction tx = sess.beginTransaction();
		List titlelist = new ArrayList();
		titlelist.add("linux");
		titlelist.add("hello");
		Query query = sess.createQuery("from News where title in (:titlelist)");
		query.setParameterList("titlelist", titlelist);
		List list = query.list();
		for(Iterator pit = list.iterator(); pit.hasNext();){
			News news = (News)pit.next();
			System.out.println(news.getContent());
		}
		tx.commit();
		
	}

}
