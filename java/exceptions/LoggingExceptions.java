package exceptions;
// An exception that reports through a Logger

import java.util.logging.*;
import java.io.*;

class LoggingException extends Exception {
	
	private static Logger logger = 
			Logger.getLogger("LoggingException");
	public LoggingException() {
		StringWriter trace = new StringWriter();
		printStackTrace(new PrintWriter(trace));
		logger.severe(trace.toString());
	}
}
public class LoggingExceptions {

	public static void main(String[] args) {
		try {
			throw new LoggingException();
		}catch(LoggingException e) {
			System.err.println("Caught " + e);
		}
		try {
			throw new LoggingException();
		}catch(LoggingException e) {
			System.err.println("Caught " + e);
		}
	}
}
// 静态的Logger.getLogger()方法创建了一个String参数相关联的Logger对象(通常与错误相关的包名和类名)，
// 这个Logger对象会将其输出发送到System.err。向Logger写入的最简单方式就是直接调用与日志记录消息的级别相关联的方法，
// 这里使用的是severe()