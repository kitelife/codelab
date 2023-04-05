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
			// �����ȷ���Ƿ���ƥ����м�¼���ڣ�Ӧ��ʹ��get()�������������̷������ݿ⣬
			// ���û�ж�Ӧ���У��򷵻�null
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
