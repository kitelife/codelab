import java.util.Stack;

public class StackExample {
	public static void main(String args[]){
		Stack<String> s = new Stack<String>();
		s.push("Autumnal Tints");
		s.push("A week on the Concord and Merrimack Rivers");
		s.push("The Maine Woods");

		System.out.println("Next: "+s.peek());
		s.push("Civil Disobedience, Solitude and Life without Principle");

		System.out.println(s.pop());
		s.push("Walden");
		s.push("The Natural Man");

		int count = s.search("The Maine Woods");
		while(count != -1 && count > 1){
			s.pop();
			count--;
		}

		System.out.println(s.pop());
		System.out.println(s.empty());
	}
}
