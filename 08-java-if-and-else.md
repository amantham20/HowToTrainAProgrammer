# Java If and Else

Till now, we have learned about printing something on screen, taking input from a user, different data types and operators. These were all the basics of Java, From this chapter onwards, we will look into more programmatic concepts of Java.

Many times, we need to check a condition to make a decision. For example, if it is raining, we will take an umbrella, otherwise not. Similarly, if a number is divisible by 2, it is even, otherwise, it is odd.

<img alt="If else in Java" src="https://web.archive.org/web/20220811203539im_/https://www.codesdope.com/pa-images-bucket/courses/java/if1.png" style="max-width:30%;height:auto;"/>

Such types of decisions are made in Java using **if...else**.

---
## Java if Statement

Again take the example of raining. If it is raining, a person will take an umbrella. This type of decision making is done using an `if` statement.

Let's have a look at the syntax of an *if* statement before looking at examples.

### Java if Syntax
```java
if(condition) {
    statements
}
```
First, `if(condition)` is written, where the **condition** written within parentheses `( )` is what affects the decision to be made.

The statements written inside the braces `{ }` following `if(condition)` constitute the body of *if*.

If the **condition** is true, then the statements inside the body of if are executed, otherwise they are not executed.

### Java if Examples

Let’s see an example.
```java
class Test {

    public static void main(String[] args) {
        int num1 = 10, num2 = 20;
        if (num1 < num2) {
            System.out.println("num2 is greater than num1");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">num2 is greater than num1
</pre>
    </details>
</div>

Here, the condition of *if* is `num1 < num2`.

The body of *if* contains the statement `System.out.println("num2 is greater than num1")`. This statement will get executed only if the condition of *if* is true.

Since the values of the variables `num1` and `num2` are 10 and 20 respectively, the condition `num1 < num2` became true and thus the statement in the body of if got executed and "*num2 is greater than num1*" got printed.

If the value of `num1` was more than `num2`, then the condition of *if* would have become false and the statement in its body would not have executed.

Try this case yourself.

It is a good practice to add indentation before the statements inside the body of if.

That was easy, right?

Look at another example.
```java
class Test {

    public static void main(String[] args) {
        int num1 = 10, num2 = 20;
        if (num1 < num2) {
            System.out.println("num2 is greater than num1");
        }

        System.out.println("This statement is outside the body of if");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">num2 is greater than num1
This statement is outside the body of if
</pre>
    </details>
</div>

In this example, we added a statement outside the body of *if*. Thus, this statement `System.out.println("This statement is outside the body of if")` will always get executed irrespective of whether the condition of *if* is true or false.

Let’s see one more example.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        System.out.println("Enter your age");

        Scanner s = new Scanner(System.in);
        int age = s.nextInt();

        if (age > 18) {
            System.out.println("Your age is 18+");
            System.out.println("You are eligible to vote");
        }

        System.out.println("This statement is outside the body of if");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your age 20
Your age is 18+
You are eligible to vote
This statement is outside the body of if
</pre>
    </details>
</div>

Here, the condition of *if* is `age > 18`.

The body of *if* consists of the statements `System.out.println("Your age is 18+")` and `System.out.println("You are eligible to vote")`.

In the program, we are assigning the age entered by the user to a variable `age`. Since the age entered by the user is 20, the condition `age > 18` became true and the statements inside the body of *if* got executed.

If the body of if or else consists of only one statement, then the braces { } enclosing the body can be omitted. (We will learn about else in the next section)

<img alt="first statement of if in Java" src="https://web.archive.org/web/20220811203539im_/https://www.codesdope.com/pa-images-bucket/courses/java/p11.png" style="max-width:80%;height:auto;"/>

If there is just one statement in the body of if, then it is not mandatory to put the braces `{ }` to enclose the body. For example, in the first and second programs we saw in this chapter, the body of *if* can be written without being enclosed within `{ }` as shown below.
```java
class Test {

    public static void main(String[] args) {
        int num1 = 10, num2 = 20;
        if (num1 < num2) System.out.println("num2 is greater than num1");

        System.out.println("This statement is outside the body of if");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">num2 is greater than num1
This statement is outside the body of if
</pre>
    </details>
</div>

In the above example, since we have not written braces `{ }` for marking the body of *if*, the first statement written after the `if(num1 < num2)`, i.e. `System.out.println("num2 is greater than num1")` is considered as the body of *if*.

Numbers like 1, 1.2, 3, etc except 0 are also evaluated as true if used as a condition. 0 is evaluated as false.

Let's look at one more example.
```java
class Test {

    public static void main(String[] args) {
        if (true) System.out.println("This will always execute!");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This will always execute!
</pre>
    </details>
</div>

We have directly written `true` for the condition. Hence, the condition is always true and the statement inside if - `System.out.println("This will always execute!");` is always executed.

So, it was this easy to check a condition and perform a task or print something if that condition is true. Wait, there is more that we can do by checking conditions. Let’s look at that in the next sections.

---
## Java if...else Statement

Now, consider the same example of raining. If it is raining, a person will take an umbrella, otherwise the person will wear a hat. Such decision making in which if the condition is true, then we perform some action, and if the condition is false, then we perform some other action is done using an **if...else** statement.

Let’s look at the syntax of an *if...else* statement.

### Java if...else Syntax
```java
if(condition) {
	statements
}
else {
	statements
}
```
The statements written inside the braces `{ }` following `if(condition)` constitute the body of *if*.

The statements written inside the braces `{ }` following `else` constitute the body of else.

If the **condition** is true, then the statements inside the body of *if* are executed, otherwise the statements inside the body of *else* are executed.

### Java if...else Examples

Let’s see an example.
```java
class Test {

    public static void main(String[] args) {
        int num1 = 20, num2 = 10;

        if (num1 < num2) {
            System.out.println("num2 is greater than num1");
        } else {
            System.out.println("num2 is less than num1");
        }

        System.out.println("This statement is outside the body of if and else");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">num2 is less than num1
This statement is outside the body of if and else
</pre>
    </details>
</div>

Since `num1` is greater than `num2`, the condition `num1 < num2` became false, and hence the statement in the body of else got executed.

If the condition was true, then the statement in the body of if would have got executed resulting in the following output.
```
num2 is greater than num1
This statement is outside the body of if and else
```
Look at another example.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        System.out.println("Enter your age");

        Scanner s = new Scanner(System.in);
        int age = s.nextInt();

        if (age > 18) {
            System.out.println("Your age is 18+");
            System.out.println("You are eligible to vote");
        } else {
            System.out.println("Your age is not 18+");
            System.out.println("You are not eligible to vote");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your age 15
Your age is not 18+
You are not eligible to vote
</pre>
    </details>
</div>

Since the age entered by the user is 15, the condition `age > 18` became false and the statements inside the body of else got executed.

Now let’s write a program to check if a number is even or odd.
```java
class Test {

    public static void main(String[] args) {
        int num = 12;

        if (num % 2 == 0) {
            System.out.println("Number is even");
        } else {
            System.out.println("Number is odd");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number is even
</pre>
    </details>
</div>

In the condition `num % 2 == 0`, we are checking if the remainder obtained by dividing `num` by 2 is 0. If it is 0 (`num` is perfectly divisible by 2), then the body of *if* gets executed, otherwise the body of else gets executed. In this program, the value of `num` is 12, hence the condition became true and the body of *if* got executed.

Since the body of *if* and *else* in the above example contains just one statement each, so we can remove the braces `{ }` enclosing the body as shown below.
```java
class Test {

    public static void main(String[] args) {
        int num = 12;

        if (num % 2 == 0) System.out.println(
            "Number is even"
        ); else System.out.println("Number is odd");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number is even
</pre>
    </details>
</div>

---
## Java else if Statement

Many times we fall in situations when only if and else are not sufficient. For example, if you have 5 rupees, then you will buy a candy, if you have 10 rupees, then a chocolate and if more than 100, then a cake. Java provides another tool **else if** to get this done.

Let’s look at its syntax.

### Java else if Syntax
```java
if(condition) {
	statements
}
else if(condition) {
	statements
}
else if(condition) {
	statements
}
...
...
else {
	statements
}
```
First, the condition of *if* is checked. If it is true, then the body of *if* is executed.

If the condition of *if* is false, then the condition of the first *else if* is checked. If the condition of the first *else if* is true, then its body is executed, otherwise the condition of the next *else if* is checked.

If the conditions of *if* and all the else *if* blocks are false, then the body of the *else* is executed.

### Java else if Examples

Look at the following example.
```java
import java.util.*;

class Test {

    public static void main(String[] args) {
        int x, y, z;
        Scanner s = new Scanner(System.in);

        System.out.println("Enter first number");
        x = s.nextInt();

        System.out.println("Enter second number");
        y = s.nextInt();

        System.out.println("Enter third number");
        z = s.nextInt();

        if ((x > y) && (x > z)) {
            System.out.println(x + " is the greatest integer");
        } else if ((y > x) && (y > z)) {
            System.out.println(y + " is the greatest integer");
        } else System.out.println(z + " is the greatest integer");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter first number
4
Enter second number
5
Enter third number
1
5 is the greatest integer
</pre>
    </details>
</div>

First, the condition of *if* is checked. If it is false, then the condition of *else if* is checked and if that is also false, then the body of else is executed.

In the above example, we are given three numbers `x`, `y` and `z` and we have to find the greatest among them. For that, first we will compare the first number with the other numbers i.e. `x` with both `y` and `z`. If the condition `(x>y && x>z)` of *if* is true (if both are true, means `x` is the greatest), then the body of *if* is executed.

If not, then the condition `(y>x && y>z)` of *else if* is checked. If this condition is true, then the body of else *if* will be executed. If this is also false, then the body of else will be executed.

In our case, since `x` is greater than `y` and `z`, therefore the condition of if became true and its body got executed.

Let’s see one more example.
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

First the condition of *if* is checked. If it is true, then only statements in the body of *if* are executed, otherwise the condition of the first *else if* is checked. If it is true, then its body is executed, otherwise the condition of the next *else if* is checked. If none of them are true, then the body of else is executed.

### Java Nested if...else Statements

We can use *if*, *if...else* or *if...else* *if...else* statements inside the body of other *if*, *if...else* or *if...else* *if...else* statements. This is called **nesting**.

Let’s see an example.
```java
class Test {

    public static void main(String[] args) {
        int rating = 8;

        if (rating < 5) {
            System.out.println("Bad rating");
        } else {
            if (rating < 8) {
                System.out.println("Average rating");
            } else {
                System.out.println("Good rating");
            }
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Good rating
</pre>
    </details>
</div>

Suppose the rating for a product can be from 1 to 10. If the rating is less than 5, then it is considered a *Bad rating*. Otherwise, if the rating is from 5 to 7 then it is an Average rating, and if the rating is from 8 to 10 then it is a *Good rating*.

<img alt="Nested if else in Java" src="https://web.archive.org/web/20220811203539im_/https://www.codesdope.com/pa-images-bucket/courses/java/p12.png" style="max-width:80%;height:auto;"/>

Here, we assigned the value 8 to the variable `rating`. In if...else, the condition `rating < 5` of the outer if is checked. Since the condition is false, the statements inside the body of the outer else are executed.

The following statements are inside the body of the outer *else*.
```java
if(rating < 8) {
    System.out.println("Average rating");
}
else {
    System.out.println("Good rating");
}
```
The first statement i.e., `if(rating < 8)` got executed first. Since its condition `rating < 8` is false, the statement `System.out.println("Good rating")` inside the body of the inner else got executed.

Now look at another example. The following program checks whether a number is the greatest among three numbers.
```java
class Test {

    public static void main(String[] args) {
        int x = 5, y = 2, z = 8;
        if (x> y) {
            if (x > z) System.out.println(
                "x is the greatest integer"
            ); else System.out.println("x is not the greatest integer");
        } else System.out.println("x is not the greatest integer");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">x is not the greatest integer
</pre>
    </details>
</div>

<img alt="Nested" else="" if="" in="" java"="" src="https://web.archive.org/web/20220811203539im_/https://www.codesdope.com/pa-images-bucket/courses/java/p13.png" style="max-width:80%;height:auto;"/>

Here, the following *if...else* statement is inside `if(x > y)`.
```java
if(x > z)
    System.out.println("x is the greatest integer");
else
    System.out.println("x is not the greatest integer");
```
Since the condition `x > y` of the outer *if* is true, the statements inside the body of *if* got executed. Inside the body of *if*, the first statement i.e., `if(x > z)` got executed first. Since its condition `x > z` is false, the statement `System.out.println("x is not the greatest number.")` in the body of the inner else got executed.

We can also do the same by using the `&&` operator.
```java
class Test{

    public static void main(String[] args){
        int x = 5, y = 2, z = 8;
        if ( (x > y) && (x > z) ){
            System.out.println( "x is the greatest integer" );
        }
    else
        System.out.println( "x is not the greatest integer" );
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">x is not the greatest integer
</pre>
    </details>
</div>

Here, the expression inside *if* is true only if both `(x > y)` and `(x > z)` are true. If that is the case, then `x` will be the greatest number, otherwise not.

---
## Java Ternary Operator

**Ternary operator** checks a condition and then returns a value depending on whether the condition is true or false.

Look at the following statements.

`int num = 10`

`String result = (num == 10) ? "num is equal to 10" : "num is not equal to 10";`

In the second statement, `? :` is a ternary operator. It takes three operands - `num == 10`, "`num is equal to 10`" and "`num is not equal to 10`".

The first operand is always a condition. If this condition is true, then the second operand is returned, otherwise the third operand is returned.

In our case, the condition `num == 10` is checked. If this condition is true, then "`num is equal to 10`" is assigned to the variable `result`, otherwise "`num is not equal to 10`" is assigned to `result`. Since the value of `num` is 10, the value of `result` becomes "`num is equal to 10`".

Let’s generalize the syntax of the ternary operator.

### Java Ternary Operator Syntax

`condition ? value1 : value2`

The **condition** is checked first. If it is true, then **value1** is returned, and if it is false, then **value2** is returned.

<img alt="ternary operator in Java" src="https://web.archive.org/web/20220811203539im_/https://www.codesdope.com/pa-images-bucket/courses/java/p14.png" style="max-width:50%;height:auto;"/>

### Java Ternary Operator Examples

Now look at the following example.
```java
class Test{

    public static void main(String[] args){
        int age = 20;
        String message = (age > 18) ? "You are eligible to vote" : "You are not eligible to vote";
        System.out.println(message);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">You are eligible to vote
</pre>
    </details>
</div>

In this example, the condition `age > 18` is true. Hence, the value "`You are eligible to vote`" is assigned to the variable `message`.

If the condition `age > 18` was false, then the value "`You are not eligible to vote`" would have been assigned to `message` and the output would be as shown below.

`You are not eligible to vote`

Look at another example which prints the maximum among two numbers.
```java
class Test{

    public static void main(String[] args){
        int num1 = 10, num2 = 20;
        int max = (num1 > num2) ? num1 : num2;
        System.out.println("The greater number is " + max);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">The greater number is 20
</pre>
    </details>
</div>

Here, the condition `num1 > num2` is false and hence `num2` is assigned to the variable `max`.

Note that both the examples discussed above can be written using *if..else* as well. Using a ternary operator shortened the code.

Now let’s look at a more advanced example. The following program prints the maximum among three numbers.
```java
class Test{

    public static void main(String[] args){
        int num1 = 10, num2 = 20, num3 = 30;
		
        int max = ((num1 > num2) && (num1 > num3)) ? num1 : ((num2 > num3) ? num2 : num3);
        System.out.println("The greatest number is " + max);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">The greatest number is 30
</pre>
    </details>
</div>

This is an example of a nested ternary operator. Try to understand the code yourself before looking at the explanation.

<img alt="Nested ternary operator in Java" src="https://web.archive.org/web/20220811203539im_/https://www.codesdope.com/pa-images-bucket/courses/java/p15.png" style="max-width:100%;height:auto;"/>

We are given three numbers `num1`, `num2` and `num3` and we have to assign the greatest number among them to the variable `max`.

First, the condition `(num1 > num2) && (num1 > num3)` is checked. If this condition is true (*which means `num1` is the greatest number*) (greater than `num2` and `num3` both), then `num1` is assigned to `max`.

However, if this condition is false (*which means `num1` is not the greatest number*), then the expression `(num2 > num3) ? num2 : num3` is evaluated and assigned to `max`. In this expression, the condition `num2 > num3` is checked. If this condition is true (*which means `num2` is the greatest*), then `num2` is assigned to `max`, else `num3` is assigned to `max`.

The equivalent if/else code for the same example would be:
```java
class Test{

    public static void main(String[] args){
        int num1 = 10, num2 = 20, num3 = 30;
        int max;
        if((num1 > num2) && (num1 > num3)) {
            max=num1;
        }
        else {
            if (num2 > num3)
                max = num2;
            else
                max = num3;
        }
        System.out.println("The greatest number is " + max);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">The greatest number is 30
</pre>
    </details>
</div>

Using nested ternary operators instead of if...else is not recommended because it increases the complexity of the code.

In this chapter, you learned about different ways you can perform some task based on some condition. Though you saw different examples explaining the concept, it is necessary that you [practice questions](https://web.archive.org/web/20220811203539/https://www.codesdope.com/practice/) because it is a new concept. In the next chapter, we will look at another approach to perform decision making which can reduce the complexity of code as compared to *if...else* in some cases.

> If something is important enough, even if the odds are stacked against you, you should still do it.
>
> \- Elon Musk

---
