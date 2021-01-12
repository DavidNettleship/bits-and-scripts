package fizzBuzz;

public class FizzBuzz {

	public static void main(String[] args) {

		// The aim of this class is to count from 1-100.
		// For every multiple of 3, it should print "Fizz"
		// For every multiple of 5, it should print "Buzz"
		// If the number is a multiple of 3 and 5 it should print "Fizz-Buzz"

		for (int i = 1; i <= 100; i++) {

			if 	(i % 5 == 0 && i % 3 == 0) {
				System.out.println(i + "Fizz-Buzz");
			}

			else if (i % 5 == 0) {
				System.out.println(i + "Buzz");
			}

			else if (i % 3 == 0) {
				System.out.println(i + "Fizz");
			}

			else {
				System.out.println(i);
			}
		}
	}
}
