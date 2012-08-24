package demo;


import java.util.Iterator;
import java.util.List;

import org.hibernate.Session;
import org.hibernate.Transaction;

public class HqlQuery {

	public static void main(String[] args) throws Exception {
		HqlQuery mgr = new HqlQuery();
		String title="Hello";
		mgr.findNews(title);
	}

	public void findNews(String title) {
		Session sess = HibernateUtil.currentSession();
		Transaction tx = sess.beginTransaction();
		List pl = sess
				.createQuery("select news from News news where title = :title")
				.setString("title", title).list();
		for(Iterator pit = pl.iterator(); pit.hasNext();){
			News news = (News)pit.next();
			System.out.println(news.getContent());
		}
		tx.commit();
		HibernateUtil.closeSession();
	}
}