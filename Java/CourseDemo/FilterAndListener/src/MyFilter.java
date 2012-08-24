import java.io.IOException;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

//过滤器就是针对服务器的请求，加以过滤限制；
public class MyFilter implements Filter {

	public void destroy() {

	}

	public void doFilter(ServletRequest request, ServletResponse response,
			FilterChain chain) throws IOException, ServletException {
		HttpServletRequest req = (HttpServletRequest) request;
		HttpServletResponse rsp = (HttpServletResponse) response;
		if (req.getRequestURI().toString().endsWith("money.jsp")) {
			// 什么时候有过钱啊？打回北京去
			rsp.sendRedirect("gohome.jsp");
			System.out.println("什么时候有过钱啊，滚回家去！");
			return;
		} else if (req.getRequestURI().toString().endsWith("hongshu.jsp")) {
			if (BigBag.bag.containsKey("hongshu")) {
				int num = BigBag.bag.get("hongshu") + 1;
				BigBag.bag.put("hongshu", num);
				System.out.println("得到第" + num + "个红薯");
			} else {
				BigBag.bag.put("hongshu", 1);
				System.out.println("得到第1个红薯");
			}
			// 村长同意了，下面就是到村民家中拿了。。
			chain.doFilter(request, response);
		} else {
			// 只要不要钱就行，放行
			chain.doFilter(request, response);
		}
	}

	public void init(FilterConfig filterConfig) throws ServletException {

	}

}