# Java Errors and Exceptions

You must have got errors on running your programs when you made some mistakes in the programs. It is often frustrating to get errors especially when we can’t figure out their cause.

Whenever we write something wrong in our program, we get an error on running the program. For example, if we forget to write a semicolon after a statement, then on running the program, the program gets terminated (stopped) and an error message gets displayed.

Look at the following example.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("Java")
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:3: error: ';' expected<br/>
    System.out.println("Java")<br/>
                  ^<br/>
1 error
</pre>
    </details>
</div>

Basically, there are two separate terms **Errors** and **Exceptions**. We often use the word Error for both these terms.

So let’s understand the difference between errors and exceptions.

## Errors in Java

An error occurs when there is an irrecoverable problem like the system getting crashed, unavailability of memory, etc. A programmer doesn’t have control over these errors and can’t do much to remove them.

Errors are thrown when the program gets executed i.e. at runtime. (The time when the program gets executed is called runtime)

Examples of errors are OutOfMemoryError, StackOverflowError, VirtualMachineError, etc.

## Exceptions in Java

All the errors which are thrown when a programmer makes some mistake in the code are called exceptions. Exceptions can be eliminated by the programmer by making changes in the code. For example, missing a semicolon after a statement, assigning a string value to an int variable, etc. will throw exceptions.

Some exceptions are thrown when the program gets compiled and some exceptions are thrown when the program gets executed.

We know that a Java program is first compiled and then executed. When a program is compiled, that time is known as compile time, and when a program is executed, that time is known as runtime. Some types of exceptions are thrown at compile time and some are thrown at runtime.

Based on whether an exception is thrown at compile time or runtime, exceptions can be classified into two types.

*   Checked exceptions
*   Unchecked exceptions

### Checked Exceptions

Checked exceptions are the exceptions thrown at the compile time. At compile time, the compiler checks the syntax and semantics (semantics is whether the program is logically correct) of the program. So, whenever the syntax or the semantics of a program are incorrect, an exception is thrown at the compile time.

Take the following example.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("Java")
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:3: error: ';' expected<br/>
        System.out.println("Java")<br/>
                     ^<br/>
1 error
</pre>
    </details>
</div>

In this program, a semicolon `;` is missing at the end of the statement `System.out.println("Java")`. Hence, on compiling the program, this statement will throw an exception because the syntax is incorrect.

Let’s take another example of a compile time exception.

```java
class Test {

    public static void main(String[] args) {
        int a = 1, b = 2, c = 3;
        a * b = c;
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:4: error: unexpected type<br/>
        a*b = c;<br/>
            ^<br/>
  required: variable<br/>
  found:    value<br/>
1 error
</pre>
    </details>
</div>

Here, in the statement `a*b = c`, the value of the variable `c` is assigned to the product of the variables `a` and `b`, which does not make sense. Hence, this statement will throw an exception at the compile time because it is semantically incorrect.

Examples of checked exceptions are IOException, SQLException, etc.

### Unchecked Exceptions

Unchecked exceptions are the exceptions thrown at the runtime. If the syntax and semantics of a program are correct but there is some problem in the execution of a program, an exception is thrown at the runtime.

Examples of unchecked exceptions are ArithmeticException, ArrayIndexOutOfBoundsException, NullPointerException, IllegalArgumentException, NumberFormatException, etc.

Let’s take a look at some of these exceptions.

#### Java ArithmeticException

This exception is thrown due to wrong arithmetic expression or condition. For example, when a number is divided by 0.

```java
class Test {

    public static void main(String[] args) {
        int a = 10, b = 0;
        int c = a / b;
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception in thread "main" java.lang.ArithmeticException: / by zero<br/>
    at Test.main(Test.java:4)
</pre>
    </details>
</div>

The syntax and semantics of this program is correct and so it got compiled successfully. After compilation, ArithmeticException is thrown at the runtime because we are dividing a number by 0 in the statement `int c = a/b`.

#### Java ArrayIndexOutOfBoundsException

This exception is thrown when the index of an array does not exist. In other words, it is raised when the index is out of bounds.

```java
class Test {

    public static void main(String[] args) {
        int[] arr = new int[5];
        System.out.println(arr[10]);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception in thread "main" java.lang.ArrayIndexOutOfBoundsException: 10<br/>
        at Test.main(Test.java:4)
</pre>
    </details>
</div>

We got ArrayIndexOutOfBoundsException on printing `arr[10]` because there is no index 10 of the array `arr`.

So, now you know the difference between errors and exceptions. Note that it is not necessary to know the different types of exceptions and these are mentioned in this chapter just for better understanding.

#### Java Exception Hierarchy

All errors and exceptions are actually classes in Java. This means that **Error** is a class and **Exception** is also a class. Both **Error** and **Exception** are the subclasses of the root class named **Throwable**.

<p><img alt="types of errors and exceptions in Java" src="https://web.archive.org/web/20240416085645im_/https://www.codesdope.com/pa-images-bucket/courses/java/p36.png" style="max-width:100%;height:auto;"/></p>

Thus, **Throwable** class has two subclasses - **Error** and **Exception**.

**Exception** class has several subclasses - **IOException**, **RuntimeException**, **SQLException**, etc. Most common subclasses are **IOException** and **RuntimeException**.

**IOException** class has the subclasses **EOFException**, **FileNotFoundException**, **UnsupportedEncodingException**, etc. All IOException subclasses are checked exceptions, which means that all IOException exceptions are thrown at compile time.

**RuntimeException** class also has the subclasses **ArithmeticException**, **ArrayIndexOutOfBoundsException**, **NullPointerException**, **NumberFormatException**, **IllegalArgumentException**, etc. All RuntimeException subclasses are unchecked exceptions, which means that all RuntimeException exceptions are thrown at runtime.

That’s all for this chapter! Let’s finish this topic by summarizing the differences between errors and exceptions.

You don’t need to remember these exceptions, but it’s always good to have a rough idea of the types of error or exceptions while debugging. You can read about other built-in exceptions from [Java Built-in Exceptions](https://web.archive.org/web/20240416085645/https://docs.oracle.com/javase/7/docs/api/java/lang/Exception.html).

Apart from these built-in exceptions, we can also create our own exceptions and can also handle exceptions about which we will learn in the next chapters.

> When the going gets tough, the tough get going.
>
> Joe Kennedy


<a href="33-java-exception-handling.md" class="next">Next</a>
