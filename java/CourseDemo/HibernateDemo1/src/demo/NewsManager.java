package demo;

import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.Configuration;

public class NewsManager {

	public static void main(String[] args) throws Exception{
		/*
		 * Configuration实例的唯一作用是创建SessionFactory实例，所以它被设计成启动期间对象，一旦SessionFactory创建完成，它就被丢弃了。
		 * */
		Configuration conf = new Configuration().configure();
		
		SessionFactory sf = conf.buildSessionFactory();
		Session sess = sf.openSession();
		Transaction tx = sess.beginTransaction();
		News n = new News();
		n.setTitle("Hello");
		n.setContent("World");
		sess.save(n);
		tx.commit();
		sess.close();
		sf.close();
	}
}
