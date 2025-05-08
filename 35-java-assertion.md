# Java Assertion

In the last chapter, we saw how to manually `throw` an exception using the throw keyword. Assertion is another way to throw an exception.

Note that by default, assertions are disabled. Therefore, we need to enable them in order to use them. So,  let’s first learn to enable assertions in Java.

***

## Enabling Assertions in Java

As mentioned above, assertions are disabled by default. To enable assertions, while running a program, write `java -ea` instead of `java` before the filename.

For example, if after compilation, you want to run the Test.java file, then write any one of the following commands instead of `java Test`.

`java -ea Test`

Or

`java -enableassertions Test`

So, whenever you want to use assertions in your program, run the program using one of the above commands.

We need to enable assertions to use them.

So this is how we can enable assertion when we run a program that uses it. Before understanding why we need assertion, let’s see how we can throw an exception using assertion.

Assertion is written using the `assert` keyword. It is used to check a condition. If the condition is true, then it does nothing and the program execution continues normally. However, if the condition is false, then it throws the `AssertionError` exception and the program gets terminated.

Let’s look at an example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter a positive number");
        int num = s.nextInt();

        assert num > 0;
        System.out.println("Number is positive");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter a positive number
5
Number is positive
</pre>
    </details>
</div>

Here `assert num > 0` is the assert statement. It checks if the condition `num > 0` is true. If the condition is true, then nothing happens and the next statement is executed. Here we gave the input as 5, thus the condition `num > 0` of the assert statement is true and so no exception was thrown.

Let’s see what would happen if we pass a negative number as input.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter a positive number");
        int num = s.nextInt();

        assert num > 0;
        System.out.println("Number is positive");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter a positive number
-5
Exception in thread "main" java.lang.AssertionError
	at Test.main(Test.java:9)
</pre>
    </details>
</div>

Here we gave the input as -5 which made the condition `num > 0` of the assert statement false. Thus, the assert statement threw an `AssertionError` exception.

The assert statement always throws the `AssertionError` exception which is a built-in exception in Java.

The condition of the assert statement must be given such that it always computes to true or false.

We can also add an error message for the `AssertionError` exception so that whenever this exception is thrown, the error message gets displayed. Let’s add an error message in the previous example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter a number");
        int num = s.nextInt();

        assert num > 0 : "Number is not positive";
        System.out.println("Number is positive");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter a positive number
-5
Exception in thread "main" java.lang.AssertionError: Number is not positive
	at Test.main(Test.java:9)
</pre>
    </details>
</div>

In this example, we added the error message for the exception in the assert statement by writing `assert num > 0: "Number is not positive"`, where `num > 0` is the condition to be checked and "Number is not positive" is the description or the error message. In the output, you can see the error message on giving an invalid input.

Note that if we don’t enable assertions, then the assert statements will never throw an `AssertionError` exception.

We have already seen how to enable assertions in the beginning of this chapter. We can also disable assertions in Java. Let’s see how.

***

## Disabling Assertions

Assertions are by default disabled. But still we can selectively disable them while running a program. For disabling assertions, while running a program, write `java -da` instead of `java` before the *filename*.

For example, if after compilation, you want to run the Test.java file, then write any one of the following commands instead of `java Test`.

`java -da Test`

Or

java -disableassertions Test

Now that we know what assertion is, let’s discuss where it can be used.

***

## Where is Assertion Used?

Assertions are mostly used for debugging or checking for any invalid values in a program. Normally, it is used for debugging and testing in large programs.

Let’s take a simplified example. Suppose you own a retail shop and want to get rid of all the products whose expiry date is less than 5 months. To do that, you can test whether the expiry date is greater than 5 months using assertion for each product and reject all the products for which the condition does not satisfy.

Consider another example in which you have a list of one thousand integer values. Now suppose your program is breaking because some values in the list might not be of type integer. In that case you can check the data type of those values using assertion in a loop.

In testing a software, we often use assert. Suppose, we have a list of test cases which should pass a particular function to ensure correct working of the program. In that case we use assert and if any of the test cases is not passed, then assert throws an error and we know that our program is not yet ready for production as it didn’t pass all test cases.

Now, you must have got an idea of where you can use assertions. So, let's move forward.

***

## More Examples of Assertion

We have already seen an example in which assertion was used to check the validity of user input. Let’s look at one more example.

```java
import java.util.Scanner;

class Test1 {

    // method to check if blood group entered by the user is valid
    public static boolean isValid(String bgroup) {
        String[] blood_group = {
            "A+",
            "A-",
            "B+",
            "B-",
            "O+",
            "O-",
            "AB+",
            "AB-",
        };
        for (String el : blood_group) {
            if (bgroup.equals(el)) {
                return true;
            }
        }
        return false;
    }

    // main method
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Enter your blood group");
        String bgroup = s.next();

        assert isValid(bgroup) : "You entered an incorrect blood group!";
        System.out.println("Your blood group is " + bgroup);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your blood group
AB++
Exception in thread "main" java.lang.AssertionError: You entered an incorrect blood group!
	at Test.main(Test1.java:22)
</pre>
    </details>
</div>

In the above example, we are asking the user to enter the blood group. Then we are using an assert statement to check if the entered blood group is valid. If the condition of the assert statement is false, then we are throwing `AssertionError` with the error message "You entered an incorrect blood group!".

Look at the assert statement below.

`assert isValid(bgroup): "You entered an incorrect blood group!";`

In this assert statement, the condition is `isValid(bgroup)`. This means that we are calling the `isValid()` method by passing the blood group entered by the user and the method returns either true or false depending on whether the blood group is valid or not.

Inside the `isValid()` method, we created a string array named `blood_group` storing all types of blood groups. We are checking if the blood group entered by the user stored in the variable `bgroup` is equal to any element of the array `blood_group`. If it is equal, then we are returning true, else we are returning false.

We can also handle `AssertionError` using try and catch blocks like all other exceptions.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        try {
            System.out.println("Please enter your roll number");
            int roll = s.nextInt();
            assert roll > 0 : "You entered an incorrect Roll Number!";
            System.out.println("You entered " + roll);
        } catch (AssertionError e) {
            System.out.println(e.getMessage());
        } catch (Exception e) {
            System.out.println("Some error occurred");
        }
    }
}
```

In this example, in the condition `roll > 0` of the assert statement, we are checking if the roll number entered by the user is greater than 0. Let’s check the output for different input values.

If the user enters 5, then the condition of the assert statement becomes true and no exception is thrown. We will get the following output.

```
Enter your roll number
5
You entered: 5
```

If the user enters -5, then the condition of the assert statement becomes false and the `AssertionError` exception is thrown. This exception gets handled by the first catch block. We will get the following output.

```
Enter your roll number
-5
You entered an incorrect Roll Number!
```

Exception handling becomes necessary when your program grows larger or more complex. Since the last few chapters, we learned about different types of exceptions and how to handle them. We also learned about the ways to throw new exceptions or create our own exceptions. So, start handling your exceptions elegantly.

Always make a total effort, even when the odds are against you.

- Arnold Palmer

