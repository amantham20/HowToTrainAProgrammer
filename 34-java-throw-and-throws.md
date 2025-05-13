# Java Throw and Throws
We know that exceptions are thrown when there is some problem in the code. For example, ArithmeticException is thrown when a number is divided by zero and ArrayIndexOutOfBoundsException is thrown when the index of an array does not exist. In Java, we can also throw an exception on our own.

But why would we throw an exception explicitly?

Consider a scenario where we are asking the user to enter their roll number as input. We know that a roll number can only be a positive number. So, if the user enters a non-positive value as their roll number, we might want to throw an exception.

There can be more such cases where the values entered by the user or some piece of code are considered invalid for our program. In those cases, we can manually raise an exception.

Seems interesting, right? We can throw an exception explicitly using the `throw` keyword.

---
## Java throw
The `throw` keyword is used to throw an exception explicitly.

Let’s write a program which throws an error if the user enters a non-positive roll number.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter your roll number");
        int roll = s.nextInt();

        if (roll < 0) {
            throw new ArithmeticException("Roll number can't be negative");
        } else {
            System.out.println("Valid roll number");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter your roll number
-5
Exception in thread "main" java.lang.ArithmeticException: Roll number can't be negative
    at Main.main(Main.java:10)
</pre>
    </details>
</div>

Here, the roll number entered by the user is assigned to the variable `roll`. If the value of `roll` is negative, then we are manually raising the `ArithmeticException` exception with the error message "*Roll number can't be negative*" by writing `throw new ArithmeticException("Roll number can't be negative")`.

Note that in the above example, we have thrown an exception of type `ArithmeticException`. However, we can throw any other type of exception as well if the entered value is not positive. We chose to throw `ArithmeticException` because normally `ArithmeticException` is thrown when some value is incorrect. So, it is advisable to choose the exception type that best matches the reason you are throwing it.

Similarly, an ArrayIndexOutOfBoundsException exception can be raised by writing `throw new ArrayIndexOutOfBoundsException()`.

This explicitly thrown exception behaves like any other exception which is thrown implicitly in Java. So let’s handle this exception using try...catch.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter your roll number");
        int roll = s.nextInt();

        try {
            if (roll < 0) {
                throw new ArithmeticException(
                    "The number entered is not positive"
                );
            } else {
                System.out.println("Valid roll number");
            }
        } catch (ArithmeticException e) {
            System.out.println("An exception is thrown");
            System.out.println(e.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter your roll number
-5
An exception is thrown
The number entered is not positive
</pre>
    </details>
</div>

In this example, we transferred the code that is likely to throw an exception inside the try block. When the user enters a negative roll number, the `ArithmeticException` exception is thrown using the `throw` keyword. This exception is handled by the catch block.

We can throw any number of exceptions from a try block.

Let’s take another example. Suppose we are hosting a webinar in which only the students of the age group of 5 to 20 years are allowed. If any student who is not in this age group tries to register, then we will throw an exception.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter your age");
        int age = s.nextInt();

        try {
            if (age < 5) {
                throw new ArithmeticException(
                    "Not allowed! Your age is less than 5"
                );
            } else if (age > 20) {
                throw new ArithmeticException(
                    "Not allowed! Your age is greater than 20"
                );
            } else {
                System.out.println("Welcome!");
            }
        } catch (ArithmeticException e) {
            System.out.println("An exception is thrown");
            System.out.println(e.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter your age
26
An exception is thrown
Not allowed! Your age is greater than 20
</pre>
    </details>
</div>

In this example, we are asking the user to enter the age. If the entered age is less than 5, we are throwing an `ArithmeticException` exception with the error message "*Not allowed! Your age is less than 5*", and if the age is greater than 20, then we are throwing another `ArithmeticException` exception with another error message "*Not allowed! Your age is greater than 20*". Run this program and check the results for different inputs of age.

We can throw both checked exceptions like IOException, SQLException, etc and unchecked exceptions like ArithmeticException, ArrayIndexOutOfBoundsException, NullPointerException, etc. using the throw keyword.

While throwing an exception, if we are not sure about which type of exception we should throw, then we can throw a generic exception `Exception` as shown below.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter your roll number");
        int roll = s.nextInt();

        try {
            if (roll < 0) {
                throw new Exception("The number entered is not positive");
            } else {
                System.out.println("Valid roll number");
            }
        } catch (Exception e) {
            System.out.println("An exception is thrown");
            System.out.println(e.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter your roll number
-5
An exception is thrown
The number entered is not positive
</pre>
    </details>
</div>

You must have understood this example. We are throwing a generic Exception when the entered value is not positive.

Thus, we can throw either a generic Exception or specific built-in exceptions like ArithmeticException, ArrayIndexOutOfBoundsException, IOException, etc.

Apart from try...catch, there is one more way of handling exceptions - using the `throws` keyword.

---
## Java throws
The `throws` keyword is used to specify the type of exceptions that can be thrown by a method.

Suppose there is a method named `func` whose statements can throw `ArithmeticException`, as shown below.
```java
class Test {

    public static void func() {
        int num = 10 / 0;
    }

    public static void main(String[] args) {
        func();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception in thread "main" java.lang.ArithmeticException: / by zero
    at Test.func(Test.java:3)
    at Test.main(Test.java:7)
</pre>
    </details>
</div>

In the above example, the statement `int num = 10/0` inside the `func()` method threw `ArithmeticException`.

Let’s use the `throws` keyword to declare the type of exception that the `func()` method can throw.
```java
class Test {

    public static void func() throws ArithmeticException {
        int num = 10 / 0;
    }

    public static void main(String[] args) {
        func();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception in thread "main" java.lang.ArithmeticException: / by zero                                                                   
    at Test.func(Test.java:3)
    at Test.main(Test.java:7)
</pre>
    </details>
</div>

Notice the following method definition (method signature) in the above example.

`public static void func() throws ArithmeticException`

In this method definition, the `throws` keyword states that the statements inside the method might throw `ArithmeticException`.

You can see that the exception is still getting thrown and the output is also the same as the previous example.

**So the `throws` keyword is just used to specify the type of exceptions that a method can throw?**

Yes. Sounds weird?

Well, there are some advantages of using `throws` like exception handling.

#### What is the need to use throws when we can handle exceptions using try-catch?
This is a valid question. We know that we can use [try-catch](https://web.archive.org/web/20240221235352/https://www.codesdope.com/course/java-exception-handling/) to handle exceptions in Java. The `throws` keyword is also used to handle exceptions. However, there are some cases where we would prefer to use `throws` over try-catch. Let’s see an example of such a case.

Suppose there is a method named `func` whose statements might throw `ArithmeticException` or `ArrayIndexOutOfBoundsException`. To handle these exceptions, we can use try-catch inside the method as shown below.
```java
public void func() {
	try {
		// statements in try block
	}
	catch(ArithmeticException e) {
		// handles ArithmeticException exceptions
	}
	catch(ArrayIndexOutOfBoundsException e) {
		// handles ArrayIndexOutOfBoundsException exceptions
	}
}
```
Now suppose there are 10 or 20 such methods inside which the statements can throw `ArithmeticException` or `ArrayIndexOutOfBoundsException`. Wouldn’t it be hectic to write the catch blocks for `ArithmeticException` or `ArrayIndexOutOfBoundsException` separately for all the 10 or 20 methods?

In such cases, we can use `throws` to handle exceptions. Let’s see how.
```java
class Test {

    public static void func()
        throws ArithmeticException, ArrayIndexOutOfBoundsException {
        // statements which might throw ArithmeticException, or ArrayIndexOutOfBoundsException
    }

    public static void main(String[] args) {
        try {
            func();
        } catch (ArithmeticException e) {
            // handles ArithmeticException exceptions
        } catch (ArrayIndexOutOfBoundsException e) {
            // handles ArrayIndexOutOfBoundsException exceptions
        }
    }
}
```
Here, instead of handling exceptions using try-catch inside the method `func()`, the exceptions which are likely to be thrown are declared in the method definition (method signature) using the `throws` keyword.

`public void func() throws ArithmeticException, ArrayIndexOutOfBoundsException`

In the above method definition, the `throws` keyword states that the statements inside the method might throw `ArithmeticException` or `ArrayIndexOutOfBoundsException`. The `throws` keyword can declare any number of exceptions.

The method `func()` is called inside the main method. Therefore, in the main method, `func()` is called inside the try block and the catch blocks to handle `ArithmeticException` and `ArrayIndexOutOfBoundsException` are defined.

So, whenever `ArithmeticException` or `ArrayIndexOutOfBoundsException` is thrown from the method `func()`, it gets thrown from the try block in the main method and gets handled by the relevant catch block.

This prevents so much of our manual code writing because we no longer need to define try and catch blocks separately inside each method if multiple methods are called from the same method (main method in the above example). This also makes our code more organised and clean. So many benefits!

So let’s see an example.

### Java throws Examples
```java
class Test {

    public static void calculate()
        throws ArithmeticException, ArrayIndexOutOfBoundsException {
        int num = 10 / 0;
        // some code that might throw ArrayIndexOutOfBoundsException
    }

    public static void main(String[] args) {
        try {
            calculate();
        } catch (ArithmeticException e) {
            System.out.println("Arithmetic Exception thrown");
            System.out.println(e.getMessage());
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("ArrayIndexOutOfBounds Exception thrown");
            System.out.println(e.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Arithmetic Exception thrown
/ by zero
</pre>
    </details>
</div>

In this example, the method `calculate()` can throw two exceptions - `ArithmeticException` or `ArrayIndexOutOfBoundsException`. Therefore, these two exceptions are declared by the `throws` keyword in the method definition.
When the statement `int num = 10/0` inside the method is executed, the `ArithmeticException` exception is thrown. This thrown exception is also thrown from the try block in the main method where this method is called and is then handled by the catch block handling the `ArithmeticException` exceptions.

This is how `throws` can be used to handle exceptions thrown by methods. Now let’s handle a checked exception.
```java
import java.io.*;

class Test {

    public static void calculate() throws IOException {
        throw new IOException("IOException occurred");
    }

    public static void main(String[] args) {
        try {
            calculate();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">IOException occurred
</pre>
    </details>
</div>

Here, a checked exception `IOException` is thrown from the method `calculate()` using the `throw` keyword and is handled in the main method.

#### What if we don’t handle the exceptions defined by the throws keyword?
Apart from preventing us from writing the same piece of code again and again and making the code cleaner, there is one more advantage of using `throws`. All the exceptions which are declared using `throws` must be handled from where we are calling the method. If they are not handled, then we will get a compilation error. In this way, we are forced to handle the exceptions.

Let’s see what would happen if we don’t handle all the exceptions defined by `throws`.
```java
import java.io.*;

class Test {

    public static void func() throws IOException, ClassNotFoundException {
        // statements which might throw IOException or ClassNotFoundException
    }

    public static void main(String[] args) {
        try {
            func();
        } catch (IOException e) {
            System.out.println(e.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:10: error: unreported exception ClassNotFoundException; must be caught or declared to be thrown
        func();
        ^
1 error
</pre>
    </details>
</div>

Since we didn’t handle the `ClassNotFoundException` exception declared by the throws keyword using a catch block in the main method, we got a compile error.

So, this was all about the `throw` and `throws` keywords. Let’s summarize the difference between the two in a table.

| throw | throws |
| --- | --- |
| Used to throw an exception. | Used to declare the types of exceptions which might be thrown by a method. |
| Can throw one exception at a time. | Can declare multiple exceptions at a time. |
| While throwing an exception, it actually throws an exception object.<br/>For example, in the statement `throw new ArithmeticException`, **new** | While declaring an exception, it actually declares the class of the exception.<br/>For example, in `throws ArithmeticException`, |
| **ArithmeticException** is an object of the `ArithmeticException` class. | **ArithmeticException** is the class name of an exception. |

---
## Which Exceptions Should We Handle?
We know that there are two types of exceptions - Checked and Unchecked. Let’s see which of them we should handle.

### Handling Checked Exceptions
These are the exceptions that the compiler checks at compile time. Checked exceptions should be handled. Thus, whenever an exception occurs in a method, the method should handle it using try-catch inside it or declare it using the `throws` keyword.

### Handling Unchecked Exceptions
These are the exceptions that are checked at runtime. This means that we only get to know that an unchecked exception has been thrown when the program gets executed after getting compiled.

So, if the programmer knows beforehand that an unchecked exception can be thrown, then she should remove the cause of that exception.

For example, like giving the wrong array index in the program leads to `ArrayIndexOutOfBoundsException`. This can be corrected by correcting the array index.

Let’s take another example. Suppose we want to divide two numbers and if the denominator is 0, then `ArithmeticException` is thrown. This can be prevented by checking if the denominator is greater than 0 before dividing by it as shown below.
```java
// divide only when denominator > 0
if (denominator > 0) {
    int quotient = numerator/denominator;
}
```
But if the programmer doesn’t know beforehand that an unchecked exception can be thrown, then there is no use of handling the exception because she doesn’t know that an exception can be thrown.

Hence, it depends on the programmer whether she wants to handle unchecked exceptions or not.

> We are what we repeatedly do. Excellence, then, is not an act, but a habit.
>
> - Aristotle

---


<a href="35-java-assertion.md" class="next">Next</a>
