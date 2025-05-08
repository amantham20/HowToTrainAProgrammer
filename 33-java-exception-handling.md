# Java Exception Handling

In the last chapter, we looked at some of the built-in Exceptions in Java. We know that whenever an exception occurs in a program, the program gets terminated and an error message is displayed. This behaviour is often undesirable especially when the exception is raised due to some external factor (like due to some value entered by a user) and not due to some mistake in the code.

For example, take the following program.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.println("Please enter a number");
        int num1 = s.nextInt();

        int num2 = 10 / num1;
        System.out.println(num2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter a number 0
Exception in thread "main" java.lang.ArithmeticException: / by zero
       at Test.main(Test.java:10)</pre>
    </details>
</div>

Here, we are asking the user to enter a number which is assigned to `num1`. Then, `num1` is divided by 10 and the result of the division is assigned to `num2`.

In the above case, the user entered 0. Since we can’t divide 10 by 0, the statement `int num2 = 10/num1` threw `ArithmeticException`.

As you can see, this exception was raised because the user was expected to enter a non-zero number but instead gave the wrong input. In this case, the execution of the program was stopped. Wouldn’t it be nice to show the user a message and continue the normal execution of the program instead of terminating the program?

Doing this is possible in Java. In such scenarios, we can check if any (or a particular) exception is thrown and simply return a message informing the user that the input entered is incorrect without leading to the termination of the program. This handling of exceptions is called **Exception Handling**.

Now let’s see how we can handle exceptions in Java.

## Java try Block and catch Block

**try** and **catch** blocks are used to handle exceptions. The piece of code which is likely to throw an exception is placed inside the **try** block. It basically means that we want to **try** the execution of our code.

The statements which we want to execute if the code inside the try block throws an exception are placed inside the catch block.

So the flow is we write some code which we want to try for execution in the try block and if throws any exception, the catch block catches it and the code inside it is executed.

<img alt="try catch in Java" src="https://web.archive.org/web/20240416075436im_/https://www.codesdope.com/pa-images-bucket/courses/java/p34.png" style="max-width:80%;height:auto;"/>

### Java try catch Syntax

The syntax of try and catch blocks is shown below.

```java
try {
	// statements in try block
}

catch(Exception e) {
	// statements in catch block (executed when exception is thrown from try block)
}
```

### Java try catch Examples

Let’s handle the exception thrown in the first example of this chapter using try and catch blocks.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter a number");
        int num1 = s.nextInt();

        // try block
        try {
            int num2 = 10 / num1;
            System.out.println(num2);
        } // catch block
        catch (Exception e) {
            System.out.println("Please enter the correct input");
        }

        System.out.println("This statement is outside try-catch blocks.");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter a number 0
Please enter the correct input
This statement is outside try-catch blocks.</pre>
    </details>
</div>

The statements `int num2 = 10/num1` and `System.out.println(num2)` are placed inside the **try** block because they may throw an exception if the user enters the wrong input. The statement `System.out.println("This statement is outside try-catch blocks.")` is placed inside the **catch** block.

If the two statements inside the **try** block don't throw any exception, then the statement inside the **catch** block is not executed and the rest of the program after the **catch** block is executed as usual.

However, if a statement inside the **try** block throws an exception, the control gets transferred to the **catch** block and the statement inside the **catch** block is executed. After that, the rest of the program after the **catch** block is executed.

In the above example, the statement `int num2 = 10/num1` inside the try block threw an exception when the user entered a wrong input i.e. 0. As a result, without executing the second statement inside the try block, the control got transferred to the catch block and "Please enter the correct input" got printed.

So, in this way if any exception is thrown by the program, it will be handled gracefully without the termination of the program.

Let’s see what happens if the user gives the correct input in the above program.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter a number");
        int num1 = s.nextInt();

        // try block
        try {
            int num2 = 10 / num1;
            System.out.println(num2);
        } // catch block
        catch (Exception e) {
            System.out.println("Please enter the correct input");
        }

        System.out.println("This statement is outside try-catch blocks.");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter a number 2
5
This statement is outside try-catch blocks.</pre>
    </details>
</div>

The user entered 2. So, the statements inside the try block got executed without throwing any exception, and therefore the statement inside the catch block didn’t get executed.

> The catch block must be written immediately after the try block.

> In Java, we can have a try block without a catch block, but we can’t have a catch block without a try block.

So, put whatever code you doubt might throw an exception inside the try block and the code to be executed after an exception is thrown inside the catch block.

### Printing Thrown Exception While Handling

It
Let’s again look at the syntax of try and catch blocks.

```java
try {
	// statements in try block
}

catch(Exception e) {
	// statements in catch block (executed when exception is thrown from try block)
}
```

Did you notice `(Exception e)` written after the catch keyword? In the topic Errors and Exceptions, we saw that **Exception** is actually a class. Here, in `Exception e`, `e` is an object of the **Exception** class. This tells us that this catch block will handle all the exceptions thrown from the try block.

We can print an exception handled using a catch block. Let’s see how.

```java
class Test {

    public static void main(String[] args) {
        int arr[] = new int[10];

        try {
            arr[15] = 10;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception: " + e);
            System.out.println("Please enter the correct input");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception: java.lang.ArrayIndexOutOfBoundsException: Index 15 out of bounds for length 10
Please enter the correct input</pre>
    </details>
</div>

Inside the try block, we are assigning 10 to `arr[15]` but 15 is not an index in the array `arr`. Therefore, an exception is thrown from the try block. This exception is handled by the catch block. In the catch block, `e` is an object of the `Exception` class.

So, whenever the catch block catches an exception thrown from the try block, it gets stored in the `e` object. Thus, to print the thrown exception, simply print the value of `e` as done in the statement `System.out.println("Exception: " + e)`.

On printing `e`, the following exception stored in `e` got printed.

java.lang.ArrayIndexOutOfBoundsException: Index 15 out of bounds for length 10

Note that any variable can be used in place of `e`.

In the above example, the exception got printed on printing `e`. However, if we want to print just the exception message instead of the whole exception, we can do so using the `getMessage()` method on the exception object `e`. Let’s print just the exception message in the above example.

```java
class Test {

    public static void main(String[] args) {
        int arr[] = new int[10];

        try {
            arr[15] = 10;
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Exception: " + e.getMessage());
            System.out.println("Wrong index of array!");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception: Index 15 out of bounds for length 10
Wrong index of array!</pre>
    </details>
</div>

Here, on printing `e.getMessage()`, the following error message of the exception stored in `e` got printed.

`Index 15 out of bounds for length 10`

In this way, you can print the thrown exception message along with any other task you want to execute inside the catch block.

### Handling a Specific Exception

In all the previous examples, the catch block handled all types of exceptions thrown from the try block.

Now suppose we want to handle a specific type of exception (for example, ArithmeticException), then we need to write the class name of that exception in place of **Exception** in the above syntax.

For example, to handle only `ArithmeticException`, we have to define the catch block as `catch(ArithmeticException e)`.

Let’s try this out.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter a number");
        int num1 = s.nextInt();

        try {
            int num2 = 10 / num1;
            System.out.println(num2);
        } catch (ArithmeticException e) {
            System.out.println("Please enter the correct input");
        }

        System.out.println("This statement is outside try-catch blocks.");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter a number 0
Please enter the correct input
This statement is outside try-catch blocks.</pre>
    </details>
</div>

In the above example, we defined the catch block as `catch(ArithmeticException e)`, which means that our catch block will only handle `ArithmeticException` exceptions and will not handle any other type of exceptions. Since the try block threw an exception of type `ArithmeticException`, therefore it got handled by the catch block.

This is useful when we want to handle different exceptions differently. For example, suppose we are handling a file. In that case, we would want to execute some logic if a file doesn’t exist and different logic if the file type is different.

Let’s see another example.

```java
class Test {

    public static void main(String[] args) {
        int arr[] = new int[10];

        try {
            arr[15] = 10;
        } catch (ArithmeticException e) {
            System.out.println("Please enter the correct input");
        }

        System.out.println("This statement is outside try-catch blocks.");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 15
    at Test.main(Test.java:6)</pre>
    </details>
</div>

Inside the try block, we are assigning 10 to `arr[15]` but 15 is not an index in the array `arr`. Therefore, the `ArrayIndexOutOfBoundsException` exception is thrown from the try block. It is not handled by the catch block because it only handles `ArithmeticException` exceptions, and so our program terminated with an error message.

### Handling Multiple Exceptions

We know how to handle all types of exceptions or a specific exception using a catch block. Handling all types of exceptions by a single catch block is not a good idea when you want to take different actions or display different messages when different types of exceptions are thrown. For example, you might want to ask the user to enter a non-zero value if `ArithmeticException` is thrown or to check the index of an array element if `ArrayIndexOutOfBoundsException` is thrown.

This can be done by defining multiple catch blocks for a single try block as shown below.

```java
try {
	// statements in try block
}
 
catch(ArithmeticException e) {
	// handles ArithmeticException exceptions
}
 
catch(ArrayIndexOutOfBoundsException e) {
	// handles ArrayIndexOutOfBoundsException exceptions
}
 
catch(NullPointerException e) {
	// handles NullPointerException exceptions
}
```

Here we defined three except blocks, the first one handles `ArithmeticException` exceptions, the second handles `ArrayIndexOutOfBoundsException` exceptions and the third handles `NullPointerException` exceptions. All other types of exceptions will not be handled.

Note that only one catch block is executed for a try block. To handle an exception thrown from the try block, the first catch block is checked first, if the first catch block doesn’t handle it then the second catch block is checked, and so on.

Let’s see an example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter a number");
        int num = s.nextInt();

        int arr[] = new int[10];

        try {
            arr[num] = 10 / num;
            System.out.println(arr[num]);
        } catch (ArithmeticException e) {
            System.out.println("Please enter non-zero input");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Please enter the correct array index");
        }
    }
}
```

In this program, `ArithmeticException` exceptions are handled in the first catch block and `ArrayIndexOutOfBoundsException` exceptions are handled in the second catch block.

The number entered by the user is assigned to the variable `num`. Look at the following statement written inside the try block.

`arr[num] = 10/num;`

If the value of `num` is 0, then `ArithmeticException` will be thrown, and if its value is not between 0 and 9 (both included), then `ArrayIndexOutOfBoundsException` will be thrown.

If the user enters 2, no exception will be thrown and thus no catch block will get executed. We will get the following output.

```
Please enter a number 2
5
```

If the user enters 0, then the `ArithmeticException` exception will be thrown and the statements written inside the first catch block will get executed, giving the following output.

```
Please enter a number 0
Please enter non-zero input
```

If the user enters 0, then the `ArithmeticException` exception will be thrown and the statements written inside the first catch block will get executed, giving the following output.

```
Please enter a number
15
Please enter the correct array index
```

A **generic catch block** is a catch block which handles all types of exceptions. It is defined as `catch(Exception e)`. We can also give a **generic catch block** after all the catch blocks to handle all unhandled exceptions as shown below.

```java
try {
	// statements in try block
}
 
catch(ArithmeticException e) {
	// handles ArithmeticException exceptions
}
 
catch(ArrayIndexOutOfBoundsException e) {
	// handles ArrayIndexOutOfBoundsException exceptions
}
 
catch(NullPointerException e) {
	// handles NullPointerException exceptions
}
 
catch(Exception e) {
	// handles all other exceptions
}
```

Here the `ArithmeticException`, `ArrayIndexOutOfBoundsException` and `NullPointerException` exceptions are handled by the first three catch blocks. All other types of exceptions are handled by the last generic catch block.

Look at another example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        String s = null;
        try {
            System.out.println(s.charAt(1));
        } catch (ArithmeticException e) {
            System.out.println("Please enter non-zero input");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Please enter the correct array index");
        } catch (Exception e) {
            System.out.println("Some error occurred");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Some error occurred</pre>
    </details>
</div>

In this example, we assigned `null` to the string variable `s`. Inside the try block, `s.charAt(1)` threw the `NullPointerException` exception because we are trying to access the character at index 1 of `null`.

The first two catch blocks don’t handle `NullPointerException` and hence the third catch block handled it and printed “Some error occurred”.

> If a generic catch block is defined, then it must be defined after all the other catch blocks.

Whenever we define a generic catch block for a try block, it must be defined after all the other specific exception catch blocks for that try block. This is because if the generic catch block is defined at the first place, then the other catch blocks placed after it would not be able to catch the thrown exceptions.

If we don’t define it at the last, then we will get a compile time error as shown in the following example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        String s = null;
        try {
            System.out.println(s.charAt(1));
        } // generic catch block
        catch (Exception e) {
            System.out.println("Some error occurred");
        } catch (ArithmeticException e) {
            System.out.println("Please enter non-zero input");
        } catch (NullPointerException e) {
            System.out.println("Please enter the correct array index");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Main.java:14: error: exception ArithmeticException has already been caught
        catch(ArithmeticException e) {
        ^
Main.java:18: error: exception NullPointerException has already been caught
        catch(NullPointerException e) {
        ^
2 errors</pre>
    </details>
</div>

In this program, the try block throws the `NullPointerException` exception. We got the compilation error because the generic catch block is defined before the other catch blocks.

Now, suppose you want to perform the same task when three different types of exceptions are thrown. One way to do so is obvious - create three different catch blocks, one for handling each of the three exceptions, and perform the task in their respective catch blocks. Another way is to create a catch block that can handle all the three exceptions. Yes, in Java, we can also create catch blocks which can handle multiple exceptions as shown below.

```java
try {
	// statements in try block
}
 
catch(NullPointerException e) {
	// handles NullPointerException exceptions
}
 
catch(ArithmeticException | ArrayIndexOutOfBoundsException e) {
	// handles ArithmeticException and ArrayIndexOutOfBoundsException exceptions
}
 
catch(Exception e) {
	// handles all other exceptions
}
```

Notice the definition of the second catch block - `catch(ArithmeticException | ArrayIndexOutOfBoundsException e)`. Here it handles two types of exceptions - `ArithmeticException` and `ArrayIndexOutOfBoundsException`.

Look at the following example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        System.out.println("Please enter a number");
        int num = s.nextInt();

        int arr[] = new int[10];

        try {
            arr[num] = 10 / num;
            System.out.println(arr[num]);
        } catch (NullPointerException e) {
            System.out.println("NullPointerException error");
        } catch (ArithmeticException | ArrayIndexOutOfBoundsException e) {
            System.out.println("Please enter the correct input");
        } catch (Exception e) {
            System.out.println("Some error occurred");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Please enter a number 15
Please enter the correct input</pre>
    </details>
</div>

In this example, the second catch block handles both `ArithmeticException` and `ArrayIndexOutOfBoundsException`. Since we gave the input as 15, the statement `arr[num] = 10/num` in the try block threw `ArrayIndexOutOfBoundsException` which is handled by the third catch block.

Look at another example.

```java
class Test {

    public static void main(String[] args) {
        int arr[] = new int[10];

        try {
            arr[5] = 10 / 0;
        } catch (ArithmeticException e1) {
            System.out.println("Exception: " + e1.getMessage());
        } catch (ArrayIndexOutOfBoundsException e2) {
            System.out.println("Exception: " + e2.getMessage());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception: / by zero</pre>
    </details>
</div>

In this example, the `ArithmeticException` exception is thrown from the try block which is handled by the first catch block. In the catch block, the exception object  `e1` stores the thrown exception.

It is this easy to handle exceptions. We have a lot of flexibility in exception handling in Java like selecting which exceptions to handle or handling all the exceptions.

We know that a try block can have one or more **catch** blocks. A try block can also have another block - **finally**. Let’s read about it.

## Java finally Block

The **finally** block is executed after the execution of the **try** and **catch** blocks. If no exception is thrown inside the **try** block, then the **finally** block gets executed directly after the execution of the **try** block. If some exception is thrown inside the **try** block, then the **finally** block gets executed after the execution of the respective catch block. After the execution of the **finally** block, the rest of the program is executed.

We generally use the finally block to do clean-up before the execution of the rest of the program. Cleanup can be anything like assigning a default value to some variable, deleting something which we created inside the try or the excecatchpt block, closing an opened file (you will learn more about files in a later chapter).

> The finally block is always executed irrespective of whether an exception is raised or not inside the try block.

### Java finally Syntax

The syntax of finally block is shown below.

```java
try {
	// statements in try block
}
 
catch(Exception e) {
	// statements in catch block
}
 
finally {
	// statements in finally block
}
```

> The finally block is written after the try block and all the catch blocks (if defined).

### Java finally Examples

Let’s see an example of a finally block.

```java
class Test {

    public static void main(String[] args) {
        try {
            int num = 10 / 0;
            System.out.println(num);
        } catch (ArithmeticException e) {
            System.out.println("Number is divided by zero!");
        } catch (ArrayIndexOutOfBoundsException e) {
            System.out.println("Wrong index of array!");
        } catch (Exception e) {
            System.out.println("Some error occurred");
        } finally {
            System.out.println("finally");
        }

        System.out.println(
            "This statement is outside try-catch-finally blocks."
        );
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number is divided by zero!
finally
This statement is outside try-catch-finally blocks.</pre>
    </details>
</div>

In this example, the statement written inside the finally block got executed after the first catch block got executed.

Now let’s see an example in which there is no catch block.

```java
class Test {

    public static void main(String[] args) {
        try {
            int num = 10 / 0;
            System.out.println(num);
        } finally {
            System.out.println("finally");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">finally
Exception in thread "main" java.lang.ArithmeticException: / by zero
      at Test.main(Test.java:4)</pre>
    </details>
</div>

Here, an exception is thrown from the try block but still the finally block got executed.

In this chapter, we saw the different ways we can handle exceptions in Java. We can also create our own exceptions or throw built-in exceptions about which we will learn in the next chapter.

<div><span>Opportunities don’t happen, you create them.</span></div>
<div><span>- Chris Grosser</span></div>
