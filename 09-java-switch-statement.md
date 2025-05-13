# Java Switch Statement

We have already seen how to make decisions based on some condition in the previous chapter. In this chapter, we will look at the **switch** statement which can be used to replace the *if...else* statements in some cases to reduce the complexity and improve the readability of the code.

Normally, if we have to choose one case among many choices, nested *if-else* or *else if* is used. But if the number of choices is large, `switch..case` is a better option as it makes code neat and easier to understand. Let’s see how.

Consider a case in which we want to print a message based on the grade of a student. We can write a program for such a case using nested *if...else* or *else if* as shown below.

```java
class Test {

    public static void main(String[] args) {
        char grade = 'A';
        if (grade == 'A') {
            System.out.println("Excellent !");
        } else if (grade == 'B') {
            System.out.println("Outstanding !");
        } else if (grade == 'C') {
            System.out.println("Good !");
        } else if (grade == 'D') {
            System.out.println("Can do better");
        } else if (grade == 'E') {
            System.out.println("Just passed");
        } else if (grade == 'F') {
            System.out.println("You failed");
        } else {
            System.out.println("Invalid grade");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Excellent !
                      </pre>
    </details>
</div>

Here, we can see that if the grade of the student is ‘A’, then we are printing " *Excellent !*", if the grade is ‘B’, then we are printing " *Outstanding !*", and so on.

We can make this program more readable by using `switch..case` instead of `else if`.

Let’s have a look at the syntax of `switch...case`.

### Java switch Syntax

```java
switch(expression) {
    case value1:
        statement(s)
        break;
		
    case value2:
        statement(s)
        break;
		
	/* you can give any number of cases */
	
    default:
        statement(s)
}
```

In `switch(expression)`, the value of the **expression** is compared with the values of all the cases. If the value of the **expression** matches the **value** of a **case**, then the **statement(s)** corresponding to that case are executed.

If the **expression** doesn’t match the **value** of any case, then the **statement(s)** corresponding to **default** are executed.

For example, if the value of the **expression** is equal to **value2**, then the **statement(s)** corresponding to the second case are executed.

### Java switch Examples

```java
class Test {

    public static void main(String[] args) {
        char grade = 'B';

        switch (grade) {
            case 'A':
                System.out.println("Excellent !");
                break;
            case 'B':
                System.out.println("Outstanding !");
                break;
            case 'C':
                System.out.println("Good !");
                break;
            case 'D':
                System.out.println("Can do better");
                break;
            case 'E':
                System.out.println("Just passed");
                break;
            case 'F':
                System.out.println("You failed");
                break;
            default:
                System.out.println("Invalid grade");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Outstanding !
                      </pre>
    </details>
</div>

In this example, the value of the variable `grade`, i.e. ‘**B**’, is compared with the values of all the cases.

Since the value of the first case is not ‘*B*’, the first case is not executed. Now, since the value of the second case is ‘*B*’, `case 'B'` is executed and 'Outstanding !' gets printed. Then the `break` statement will terminate the flow without checking the rest of the cases. This is how it works.

This was more readable than the first program written using *if/else* statements.

No need to write the *break* statement in the default case because the flow automatically terminates once default statements are executed.

Note that we added the `break` statement after each case so that the flow terminates once a case is executed.

Now let's see what happens when we don't add `break` after the cases.

```java
class Test {

    public static void main(String[] args) {
        char grade = 'B';

        switch (grade) {
            case 'A':
                System.out.println("Excellent !");
            case 'B':
                System.out.println("Outstanding !");
            case 'C':
                System.out.println("Good !");
            case 'D':
                System.out.println("Can do better");
            case 'E':
                System.out.println("Just passed");
            case 'F':
                System.out.println("You failed");
            default:
                System.out.println("Invalid grade");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Outstanding !
Good !
Can do better
Just passed
You failed
Invalid grade
                      </pre>
    </details>
</div>

In the above example, the value of `grade` is ' **B**', so the control jumps to `case 'B'`. Since there is no `break` statement after any case, all the cases after `case 'B'` are also executed.

If you want to execute only that case whose value equals the value of the expression of the switch statement, then use the break statement.

Always enclose character values within  ` '   '`.

Let's see another example in which the value of the expression is an integer.

```java
class Test {

    public static void main(String[] args) {
        int i = 2;

        switch (i) {
            case 1:
                System.out.println("Number is 1");
                break;
            case 2:
                System.out.println("Number is 2");
                break;
            default:
                System.out.println("Number is greater than 2");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number is 2
                      </pre>
    </details>
</div>

You have now learned about the switch statement. Try to implement the basic functionality of a calculator like addition, subtraction, etc. using this technique. You can find the solution to this problem and more problems to practice in the [practice section](https://web.archive.org/web/20220811195841/https://www.codesdope.com/practice/).

<div><span>Hold the vision, trust the process.</span></div>

<a href="10-java-loops.md" class="next">Next</a>