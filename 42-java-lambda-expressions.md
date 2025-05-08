# Java Lambda Expressions

In Java, we can create methods known as **anonymous methods** which don't have a name. A **lambda expression** is a type of anonymous method that doesn’t belong to a class. Thus, a lambda expression is a method that doesn’t have a name and doesn’t belong to a class.

This might seem confusing for now. Don’t worry, you will understand the concept as we will move into the chapter.

**Lambda expression** is a new feature introduced in Java 8. Before understanding what a lambda expression is and why it is used, let’s introduce you to **functional interfaces**.

## Java Functional Interface

You must be familiar with interfaces. If not, you can read about it from [Java Interface](https://web.archive.org/web/20240416074021/https://www.codesdope.com/course/java-interface/).

We know that all methods of an interface are abstract by default. An abstract method is a method that doesn’t have a body. This means that the methods in an interface are declared but not implemented.

A Java interface that contains only one abstract method is called a **functional interface**.

Let’s see an example of a functional interface.

```java
interface Animal {
    void printSound();
}
```

Here, the interface `Animal` has only one abstract method `printSound()`. Hence, `Animal` is a functional interface.

Okay, so that means functional interface is just a terminology used for an interface having one method. Cool!

## Java Defining lambda Expressions

As mentioned earlier, a lambda expression is a method which doesn’t have a name and doesn’t belong to any class. It is used to implement a method defined in a functional interface.

Before learning to create lambda expressions, look at the following method.

```java
int identity(int x) {
    return x + 1;
}
```

The method `identity()` takes a parameter `x`, adds 1 to it and then returns it.

This method can be written in the form of a lambda expression as shown below.

```java
(x) -> {
    return x + 1;
};
```

This is a lambda expression which is actually a method that doesn’t have a name. It takes one parameter `x` and its body has one statement `return x + 1` which is executed. This statement in the body returns the value of `x + 1`. Thus, this lambda function will receive an argument `x`, add 1 to it and then return the result.

So, if we pass 2 as a parameter, then the lambda expression will return 3.

Using a lambda expression in place of the regular method made the code simpler and shorter.

Now let’s look at the syntax of a lambda expression.

Syntax

```java
(parameters) -> { body };
```

**parameters** are the same arguments which we pass to regular methods. There can be any number of parameters in lambda expressions.

**body** consists of some expressions or statements that are executed.

`->` is called an `arrow operator` or a `lambda operator`.

The parameters are written within parentheses `( )` and the body is written within braces `{ }`.

Now let’s look at some examples of lambda expressions.

### Lambda Expressions having No Parameter

If we don’t want to pass any parameter to a lambda expression, then just don’t pass anything in the parentheses `( )`.

```java
() -> {
    return 10;
};
```

The above lambda expression doesn’t take any parameter. In its body, 10 gets returned.

#### Lambda Expressions having One Parameter

If we want to pass exactly one parameter to a lambda expression, then just pass the parameter in the parentheses.

```java
(x) -> {
    return x + 1;
};
```

We talked about this example before also. Here, the above lambda expression takes `x` as the parameter. In its body, the statement `return x + 1` gets executed thus returning the value of `x + 1`.

#### Lambda Expressions having Multiple Parameters

To pass more than one parameter to a lambda expression, pass the comma separated set of parameters in the parentheses.

```java
(a, b) -> {
    return a + b;
};
```

The above lambda expression takes `a` and `b` as parameters. In its body, the statement `return a + b` gets executed thus returning the value of `a + b`.

#### Lambda Expressions having Body with a Single Statement

If a lambda expression has only one statement in its body, then we can also write it without enclosing it within braces `{ }`.

Look at the following lambda expression having a single expression in its body.

```java
() -> {
    System.out.println("This is body of lambda expression");
};
```

Since the body has a single statement, we can omit the braces enclosing the body as shown below.

```java
() -> System.out.println("This is body of lambda expression");
```

<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
If a lambda expression body has a single statement that returns a value, then on omitting the braces enclosing the body it is necessary to omit the <code>return</code> keyword as well.
</div>
</div>
</div>

If the body of a lambda expression has a single statement and that statement returns some value. In this case, if you want to remove the braces enclosing the body, then you must also remove the `return` keyword from the keyword.

Look at the following lambda expression.

```java
(a, b) -> {
    return a + b;
};
```

We can also write the above statement without enclosing the body in braces as shown below.

`(a, b) -> a + b;`

Note that in the above declaration, we wrote the body as `a + b` and not `return a + b`.

This means that all the examples of lambda expressions having a single statement that returns something in the body which we discussed in this chapter till now can be written without enclosing their bodies within braces as shown below.

`() -> 10;`

`(x) -> x + 1;`

Both the above lambda expressions have a single expression in their bodies, therefore the first expression returns `10` and the second expression returns `x + 1`.

#### Lambda Expressions having Body with Multiple Statements

If a lambda expression has more than one expression in its body, then it has to be enclosed within braces `{ }`.

Look at the following lambda expression.

```java
() -> {
    System.out.println("This is body of lambda expression");
    System.out.println("This is also body of lambda expression");
};
```

In the above lambda expression, there are two statements in the body.

Now look at another lambda expression.

```java
() -> {
	int num = 10;
	return num;
};
```

In the above lambda expression also, there are two statements in the body. The second statement returns an integer.

So these are the different types of lambda expressions that we can define in Java. Now let’s come to the main part - significance of lambda expressions and using them in our programs.

## When to Use lambda Expressions

Lambda expressions are mainly used because they can make code shorter and more readable. A shorter code is quite desirable when you have a program having thousands of lines of code.

There are two main cases in which lambda expressions can be helpful.

1.  Implementing the abstract method of a functional interface
2.  Passing as parameters to methods

We will cover the use of lambda expressions in both these use cases in detail in this chapter.

#### A lambda expression is used to implement the abstract method of a functional interface.

As we already know that a functional interface is just an interface with a single abstract method. It needs to be implemented. One way to implement it is by creating a class that implements it and provides definition to its abstract method, as shown below.

```java
interface Voting {
	public void getVotingAge(int age);
}

class Test {
	public static void main (String[] args) {
		// lambda expression
		Voting v = (age) -> {
			System.out.print("The age is ");
			System.out.println(age);
		};
		
		// calling abstract method
		v.getVotingAge(18);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">The age is 18</pre>
    </details>
</div>

In this example, the functional interface `Voting` has an abstract method `getVotingAge()`. The class `VotingClass` implements the interface `Voting` and provides definition (body) to the method `getVotingAge()`. Then in the main method, we created an object `v` of `VotingClass` and this object calls the method `getVotingAge()`.

Such a long code for calling the abstract method of the functional interface just once in the program!

If you want to call the method defined by the functional interface at only a few times (once or twice) in the code, then creating a class for implementing the functional interface and then creating an object of the class to call its abstract method will make the code unnecessarily long.

To make the program short and concise, we can use an **anonymous inner class** or a **lambda expression** to implement a functional interface. We discussed anonymous inner classes in the chapter Inner classes and we will see how a lambda expression is used to implement an interface in this chapter.

### Implementing Abstract Method of Functional Interface

A functional interface can be implemented without creating a class using the following ways.

**Pre Java 8**: Using anonymous inner classes. We saw how to do that in [Inner classes](https://web.archive.org/web/20240416074021/https://www.codesdope.com/course/java-nested-classes/).

**Post Java 8**: Using lambda expressions instead of anonymous inner classes. Lambda expression is a feature introduced in Java 8.

Using lambda expressions makes code shorter as compared to anonymous inner classes.

Let’s first see an example of implementing a functional interface using an anonymous inner class.

### Using Anonymous Inner Class

```java
interface Voting {
	public int getVotingAge();
}

class Test {
	public static void main (String[] args) {
		// anonymous inner class
		Voting v = new Voting() {
			public int getVotingAge() {
				return 18;
			}
		};
		
		// calling abstract method
		System.out.println(v.getVotingAge());
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">18</pre>
    </details>
</div>

In this example, a functional interface named `Voting` is defined with an abstract method  `getVotingAge()`.

Look at the following statement in the main method.

```java
Voting v = new Voting() {
	public int getVotingAge() {
		return 18;
	}
};
```

Here, `new Voting { … }` returns an object of an anonymous inner class that implements the functional interface `Voting`. This returned object of the anonymous inner class is assigned to the reference (variable) `v`. Thus, `v` is an object of the anonymous class.

Inside the anonymous class, the method `getVotingAge()` of the functional interface is defined with a body.

Now look at the following statement in the main method.

`System.out.println(v.getVotingAge());`

In the statement `v.getVotingAge()`, the object `v` of the anonymous class calls the method `getVotingAge()`.

Now let’s see how to implement a functional interface using a lambda expression.

### Using Lambda Expression

```java
interface Voting {
	public int getVotingAge();
}

class Test {
	public static void main (String[] args) {
		// lambda expression
		Voting v = () -> 18;
		
		// calling abstract method
		System.out.println(v.getVotingAge());
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">18</pre>
    </details>
</div>

In the main method, notice the following statement.

`Voting v = () -> 18;`

Here, `() -> 18` is a lambda expression that implements the functional interface `Voting` by implementing the abstract method defined in the functional interface. This returned lambda expression is assigned to `v`.

How does this lambda expression implement the abstract method `getVotingAge()`?

The method `getVotingAge()` in the functional interface `Voting` takes no parameter and returns an integer. As a result, the lambda expression `() -> 18` also takes no parameter and returns an integer 18. In this way, the lambda expression implements the abstract method of the interface `Voting`.

Now look at the following statement in the main method.

`System.out.println(v.getVotingAge());`

In this statement, the reference (variable) `v` storing the lambda expression calls the method `getVotingAge()`. On calling the method, the body of the lambda expression gets executed and 18 gets returned.

Didn’t the number of lines reduced and readability increased on using a lambda expression in place of an anonymous inner class for the functional interface implementation? This is one of the reasons we use lambda expressions in Java.

Let’s see another example.

```java
interface Voting {
	public void getVotingAge(int age);
}

class Test {
	public static void main (String[] args) {
		// lambda expression
		Voting v = (age) -> {
			System.out.println("The age is");
			System.out.println(age);
		};
		
		// calling abstract method
		v.getVotingAge(18);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">18</pre>
    </details>
</div>

In this example, the abstract method `getVotingAge()` defined in the functional interface `Voting` takes an integer parameter and doesn’t return anything (return type is `void`). Hence, the lambda expression implementing this method also takes a parameter age and doesn’t return anything. The body of the lambda expression has more than one statement and that’s why we enclosed the body within braces `{ }`.

### Passing as Parameters to Methods

In Java, we can’t normally pass a method as parameter to another method. So, if we want to pass a method as a parameter, we can use a lambda expression for that. Let’s see how we can do that.

Suppose you want to pass the following method as a parameter.

```java
public String myMethod(String name) {
	return "Hello " + name;
}
```

To do this, we can create a functional interface having this method as its abstract method and create a lambda expression to implement this method as shown below.

```java
// functional interface
interface myFuncInterface {
	public String myMethod(String name);
}

class Test {
	// defining printMessage() method
	public static void printMessage(String name, myFuncInterface exp) {
		String message = exp.myMethod(name);
		System.out.println(message);
	}
	
	public static void main (String[] args) {
		// lambda expressions
		myFuncInterface greet = (s) -> "Hello " + s;
		
		// calling printMessage() method by passing lambda expression
		printMessage("John", greet);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello John</pre>
    </details>
</div>

In the above example, `myFuncInterface` is a functional interface having an abstract method named `myMethod`.

In the main method, the lambda expression `(s) -> "Hello " + s` implements the functional interface `myFuncInterface` by implementing the abstract method defined in it. This lambda expression is assigned to the variable `greet` of the functional interface `myFuncInterface`.

We defined the following method named `printMessage`. We will be passing our lambda expression to this method while calling it.

```java
public static void printMessage(String name, myFuncInterface exp) {
	String message = exp.myMethod(name);
	System.out.println(message);
}
```

The method `printMessage()` takes two parameters: a string `name` and a lambda expression `exp` implementing the abstract method of the functional interface `myFuncInterface`.

`String message = exp.myMethod(name)` → The lambda expression `exp` calls the abstract method `myMethod()` by passing the string `name` as argument. On calling this method, the body of the lambda expression gets executed and the value returned is assigned to the variable `message`.

Look at the following statement in the main method.

`printMessage("John", greet);`

This statement calls the method `printMessage()` by passing a string “*John*” and a lambda expression `greet`. Inside the method, `exp.myMethod(name)` becomes equivalent to `greet.myMethod(“John”)`, thus executing the body of the lambda expression and returning the string “*Hello John*”. This string is assigned to the variable `message` and printed.

In this way, we were able to pass the method `myMethod()` as a parameter to the method `printMessage()`.

Let’s see another example.

```java
// functional interface
interface myFuncInterface {
	public String myMethod(String name);
}

class Test {
	// defining printMessage() method
	public static void printMessage(String name, myFuncInterface exp) {
		String message = exp.myMethod(name);
		System.out.println(message);
	}
	
	public static void main (String[] args) {
		// lambda expressions
		myFuncInterface greet = (s) -> "Hello " + s;
		myFuncInterface bye = (s) -> "Bye " + s;
		
		// calling printMessage() method by passing lambda expression
		printMessage("John", greet);
		printMessage("Julie", greet);
		printMessage("John", bye);
		printMessage("Julie", bye);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello John
Hello Julie
Bye John
Bye Julie</pre>
    </details>
</div>

In the above example, the lambda expressions `(s) -> "Hello " + s` and `(s) -> "Bye " + s` implementing the method `myMethod()` of the functional interface `myFuncInterface` are stored in the variables `greet` and `bye` respectively. The rest of the code is similar to the previous example.

`printMessage("Julie", greet)` prints *Hello John*, `printMessage("Julie", greet)` prints *Hello Julie*, `printMessage("John", bye)` prints *Bye John* and `printMessage("John", bye)` prints *Bye Julie*.

In this example also, we passed a lambda expression as parameter to a method.

In the above example, we could have also passed a lambda expression without assigning it to any variable. This is shown in the following example.

```java
// functional interface
interface myFuncInterface {
	public String myMethod(String name);
}

class Test {
	// defining printMessage() method
	public static void printMessage(String name, myFuncInterface exp) {
		String message = exp.myMethod(name);
		System.out.println(message);
	}
	
	public static void main (String[] args) {
		// calling printMessage() method by passing lambda expression
		printMessage("John", (s) -> "Hello " + s);
		printMessage("Julie", (s) -> "Hello " + s);
		printMessage("John", (s) -> "Bye " + s);
		printMessage("Julie", (s) -> "Bye " + s);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello John
Hello Julie
Bye John
Bye Julie</pre>
    </details>
</div>

Here, we wrote the following statement to call the method `printMessage()` by passing the lambda expression `(s) -> "Hello " + s`.

`printMessage("John", (s) -> "Hello " + s);`

This is the same as writing the following two statements of the previous example.

`myFuncInterface greet = (s) -> "Hello " + s;`

`printMessage("John", greet);`

So now you know how to pass a method as a parameter to another method in Java.
Let’s take another use case of lambda expressions. A lambda expression can be passed to the `forEach()` method of `ArrayList` to iterate through each element of the `ArrayList`. The `forEach()` method is used to perform the specified operation on each element in `ArrayList`.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		ArrayList<Integer> num = new ArrayList<Integer>();
		num.add(10);
		num.add(20);
		num.add(30);
		
		// forEach loop
		num.forEach( (n) -> {System.out.println(n*2);} );
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">20
40
60</pre>
    </details>
</div>

We created an Arraylist named num and added 10, 20 and 30 to it. We called the method forEach() on the Arraylist num by passing the lambda expression `(n) -> {System.out.println(n);}`. Hence, the lambda expression takes each element of num as parameter and then prints it after multiplying it with 2.

In the first iteration, in the lambda expression, the value of n is 10. So, the body of the lambda expression multiplied 10 by 2 and then printed it (20). Similarly, in the second and third iterations, 40 and 60 got printed respectively.

So this is how lambda expressions can help us make our code neat and more readable.

<div id="quote">
<div><span>The only limit is your imagination.</span></div>
<div><span>- Big Hero 6</span></div>
</div>
