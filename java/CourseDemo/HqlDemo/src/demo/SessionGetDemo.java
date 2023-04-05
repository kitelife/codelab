package demo;

import org.hibernate.HibernateException;
import org.hibernate.Session;
import org.hibernate.Transaction;

public class SessionGetDemo {

	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Session sess = null;
		try{
			sess = HibernateUtil.currentSession();
			Transaction tx = sess.beginTransaction();
			// 如果不确定是否有匹配的行记录存在，应该使用get()方法，它会立刻访问数据库，
			// 如果没有对应的行，则返回null
			News news = (News)sess.get(News.class, new Integer("16"));
			if(news == null){
				news = new News();
				sess.save(news);
			}
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
