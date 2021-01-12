package pallindrome;

import java.util.Scanner;

public class isPallindrome {

	public static void main(String[] args) {
		// The aim of this class is to check if a word is a pallindrome.
		// The class takes user input and then checks if the string is the same backwards and forwards
		// Example pallindromes: racecar, madam
		
		System.out.println("-- David's Pallindrome Tester --");
		
		@SuppressWarnings("resource")
		Scanner input = new Scanner(System.in);
    	
    	System.out.print("Enter a phrase: ");
    	String phrase = input.next();
    	
    	int i = 0;
    	int j = phrase.length();
    	
    	while (i < phrase.length()) {
    		char a = phrase.charAt(i);
    		char b = phrase.charAt(j-1);
    		
    		if(a != b) {
    			System.out.println("\"" + phrase + "\"" + " is not a pallindrome!");
    			break;
    		}
    		
    		if(i == phrase.length()-1) {
    	    	System.out.println("\"" + phrase + "\"" + " is a pallindrome!");
    		}
    		
    		i++;
    		j--;
    		
    		}
	}
}
