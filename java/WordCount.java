//package Test;

import java.io.*;
import java.util.*;

public class WordCount {
	static final Integer ONE = new Integer(1);
	
	public static void main(String args[]) throws IOException{
		Hashtable<String, Integer> map = new Hashtable<String, Integer>();
		FileReader fr = new FileReader(args[0]);
		BufferedReader br = new BufferedReader(fr);
		String line;
		while((line = br.readLine()) != null) {
			processLine(line,map);
		}
		Enumeration<String> en = map.keys();
		while(en.hasMoreElements()) {
			String key = (String) en.nextElement();
			System.out.println(key + " : " + map.get(key));
		}
	}

	static void processLine(String line, Map<String, Integer> map) {
		StringTokenizer st = new StringTokenizer(line);
		while(st.hasMoreTokens()) {
			addWord(map, st.nextToken());
		}
	}
	
	static void addWord(Map<String, Integer> map, String word) {
		Object obj = map.get(word);
		if (obj == null) {
			map.put(word,ONE);
		} else {
			int i = ((Integer)obj).intValue() + 1;
			map.put(word, new Integer(i));
		}
	}
}

