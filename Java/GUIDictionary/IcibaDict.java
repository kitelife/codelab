
import java.io.File;
import java.io.FileWriter;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.htmlparser.Node;
import org.htmlparser.NodeFilter;
import org.htmlparser.Parser;
import org.htmlparser.filters.AndFilter;
import org.htmlparser.filters.HasAttributeFilter;
import org.htmlparser.filters.TagNameFilter;
import org.htmlparser.util.NodeList;
import org.htmlparser.visitors.TextExtractingVisitor;


class IcibaDict extends Thread
{
	private String searchterm=null;
	public IcibaDict(String input)
	{
		this.searchterm=input;
	}
	String result;
	public void run()
	{
		String text=null,webContent=null;
		try
		{
			HttpClient httpclient = new DefaultHttpClient();
			String searchstring = "http://www.iciba.com/" + searchterm + "/";

			HttpGet httpget = new HttpGet(searchstring);
			
			HttpResponse response = httpclient.execute(httpget);
			HttpEntity entity = response.getEntity();
			if (entity != null) {
				String content=EntityUtils.toString(entity);
				content=content.replaceAll("<a href", "  <a href");
				Parser parser = new Parser(content);
				parser.setEncoding("gb2312");

				NodeFilter filter_tab_content = new AndFilter(new TagNameFilter(
						"div"), new HasAttributeFilter("class", "tab_content"));
				NodeList nodelist_tab_content = parser.parse(filter_tab_content);
				int length = nodelist_tab_content.size();
				for (int i = 0; i < length; i++) {
					Node node_tab_content = nodelist_tab_content.elementAt(i);
					Parser parser_tab_content = new Parser(node_tab_content
						.toHtml());
					TextExtractingVisitor visitor_tab_content = new TextExtractingVisitor();
					parser_tab_content.visitAllNodesWith(visitor_tab_content);
					text = text+"\n"+visitor_tab_content.getExtractedText().trim();
				}
				parser.reset();

				NodeFilter filter_web = new AndFilter(new TagNameFilter(
						"div"), new HasAttributeFilter("class", "content_block"));

				NodeList nodelist_web = parser.parse(filter_web);
				Node node_web = nodelist_web.elementAt(0);
				if(node_web!=null)
				{
					Parser parser_web = new Parser(node_web.toHtml());
					TextExtractingVisitor visitor_web = new TextExtractingVisitor();
					parser_web.visitAllNodesWith(visitor_web);
					webContent=visitor_web.getExtractedText().trim();
				}
				text=text+webContent;
				text=text.replaceAll("						", "");
				text=text.replaceAll("				", "");
				text=text.replaceAll("		", "\n");
				text=text.replaceAll("\n\n\n", "\n");
				text=text.replaceAll("\n\n", "\n");
				text=text.replaceAll("\n\n", "\n");
				text=text.replaceAll("	", "");
				text=text.replace("null", "");
				text=text.replace("ĎŕšŘËŃË÷", "");
				text=text.replace("žäżâ","");
				text=text.replace("Î¤ĘĎ´Ęľä","");
				text=text.replace("Dictionary", "");
				
				//System.out.println("*************************************" +
				//		"°Ž´Ę°Ôˇ­Ňë*************************************");
				//System.out.println(searchstring);
				
				//System.out.println(text);
			    result=text;
				//File f = new File("D:\\study/Undergraduate/Java/IcibaDict/" + searchterm + ".txt");
				//FileWriter fw = new FileWriter(f);
				//fw.write(text);
				//fw.flush();
				//fw.close();
			}
		}
		catch(Exception e)
		{
			e.printStackTrace();
		}
	}
	public String ReturnResult()
	{
		return result;
	}
}
