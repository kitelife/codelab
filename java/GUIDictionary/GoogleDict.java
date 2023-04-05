
import java.io.File;
import java.io.FileWriter;
import java.net.URI;

import org.apache.http.HttpEntity;
import org.apache.http.HttpResponse;
import org.apache.http.client.HttpClient;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.utils.URIUtils;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.util.EntityUtils;
import org.htmlparser.Node;
import org.htmlparser.NodeFilter;
import org.htmlparser.Parser;
import org.htmlparser.filters.OrFilter;
import org.htmlparser.filters.TagNameFilter;
import org.htmlparser.util.NodeList;
import org.htmlparser.visitors.TextExtractingVisitor;

class GoogleDict extends Thread
{
	private String searchterm=null;
	public GoogleDict(String input)
	{
		this.searchterm=input;
	}
	String result;
	public void run()
	{
		
		//http://www.google.com/dictionary?source=translation&hl=zh-CN&q=computer&langpair=en|zh-CN
		try
		{
		HttpClient httpclient = new DefaultHttpClient();
		String searchstring = "source=translation&hl=zh-CN&q=" + searchterm + "&langpair=en%7Czh-CN";
		URI	uri=URIUtils.createURI("http", "www.google.com", -1, "/dictionary", searchstring, null);
		HttpGet httpget = new HttpGet(uri);
		HttpResponse response = httpclient.execute(httpget);
		HttpEntity entity = response.getEntity();
		String text=null;
		if (entity != null) {
			Parser parser = new Parser(EntityUtils.toString(entity));
			parser.setEncoding("gb2312");

			//NodeFilter filter_tab_content =new OrFilter( new  TagNameFilter("div"),new TagNameFilter("span"));
			NodeFilter filter_tab_content=new TagNameFilter("div");
			//NodeFilter filter_tab_content=new TagNameFilter("span");
			NodeList nodelist_tab_content = parser.parse(filter_tab_content);
			int length = nodelist_tab_content.size();
			if(searchterm.getBytes().length==searchterm.length())
			{
				for (int i = 10; i < length-3; i++) {
					Node node_tab_content = nodelist_tab_content.elementAt(i);
					Parser parser_tab_content = new Parser(node_tab_content
						.toHtml());
					TextExtractingVisitor visitor_tab_content = new TextExtractingVisitor();
					parser_tab_content.visitAllNodesWith(visitor_tab_content);
					text = text+"\n"+visitor_tab_content.getExtractedText().trim();
				}
			}
			else
			{
				for (int i = 8; i < length-3; i++) {
					Node node_tab_content = nodelist_tab_content.elementAt(i);
					Parser parser_tab_content = new Parser(node_tab_content
						.toHtml());
					TextExtractingVisitor visitor_tab_content = new TextExtractingVisitor();
					parser_tab_content.visitAllNodesWith(visitor_tab_content);
					text = text+"\n"+visitor_tab_content.getExtractedText().trim();
				}
			}
			text=text.replaceAll("ĎŕšŘËŃË÷", "ĎŕšŘËŃË÷:");
			text=text.replaceAll("null", "");
			text=text.replaceAll("\n\n", "\n");
			text=text.replaceAll("\n\n", "\n");
			text=text.replaceAll("\n\n", "\n");
			
			//System.out.println("-----------------------------------------" +
					//"šČ¸čˇ­Ňë-------------------------------------------");
			//System.out.println(uri);
			
			//System.out.println(text);
			result=text;
			//File f = new File("D:\\study/Undergraduate/Java/GoogleDict/" + searchterm + ".txt");
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
