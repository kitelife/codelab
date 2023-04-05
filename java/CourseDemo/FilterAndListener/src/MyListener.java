import java.util.HashMap;

import javax.servlet.ServletContextEvent;
import javax.servlet.ServletContextListener;

// 监听器就是在服务启动之前做好保证服务正常运行的准备工作，服务结束的时候再善后一下
public class MyListener implements ServletContextListener {

    public void contextDestroyed(ServletContextEvent arg0) {
        BigBag.bag = null;
        System.out.println("回城了，让掉烂袋子吧");
    }

    public void contextInitialized(ServletContextEvent arg0) {
        BigBag.bag = new HashMap<String, Integer>();
        System.out.println("要进山了，准备好布袋子");
    }

}