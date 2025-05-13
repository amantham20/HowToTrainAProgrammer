# Java Loops

Before you try to understand loop, you should be thorough with all the previous topics of Java. If not, practice a considerable number of problems of all the previous topics.

Loops are used to repeat a piece of code. Suppose we have to print the first 10 natural numbers.

One way to do this is to print the first 10 natural numbers individually using `System.out.println()`. But what if you were asked to print the first 100 natural numbers? You can easily do this with the help of a loop by repeating the print statement 100 times.

There are three types of loops in Java:

1.  while loop
2.  for loop
3.  do...while loop

All these loops do the same thing just different by their syntax. Let’s learn about them.

***

## Java while Loop

The syntax of the `while` loop is given below.

### Java while Loop Syntax

```java
while(condition) {
    statement(s)
}
```

The **body of the while loop** consists of the statements written inside the braces `{ }` following `while(condition)`.

`while` loop checks if the **condition** written within parentheses `( )` is true or false.

If the **condition** is true, then the statements inside the body of the `while` loop are executed. After that **again the condition is checked**, and if found true again, the statements inside the body of the `while` loop are executed again. This process continues until the **condition** becomes false.

Therefore, the `while` loop keeps executing the statements inside its body till the **condition** becomes false.

Now let’s look at some examples.

### Java while Loop Examples

The following program prints the first 10 natural numbers using a `while` loop.

```java
class Test {

    public static void main(String[] args) {
        int n = 1;

        while (n <= 10) {
            System.out.println(n);
            n++;
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">1
2
3
4
5
6
7
8
9
10</pre>
    </details>
</div>

In this example, the condition of the `while` loop is `n <= 10`.

The body of the loop consists of the statements `System.out.println(n)` and `n++`.

First, 1 is assigned to a variable `n`.

`while(n <= 10)` → The condition `n <= 10` of the loop is checked. If the condition is true, then the statements of the loop are executed.

The first statement `System.out.println(n)` prints the value of `n` i.e. **1**. The second statement `n++` increases the value of `n` by **1**, making n equal to **2**.

Now, again the condition is checked. This time also the condition `n <= 10` is true because the value of `n` is 2. So, again the value of `n` i.e. **2** is printed and the value of `n` is increased to **3**.

Going on, when the value of n becomes 10, again the condition `n <= 10` is true. So, again the value of `n` i.e. **10** is printed and the value of `n` is increased to **11**.

Now, this time the condition `n <= 10` becomes false and the loop gets terminated.

In this way, we printed the first 10 natural numbers without printing them separately one by one. Similarly, you can also print the first 1000 natural numbers using the same number of lines of code. Cool, right?

Checking of the condition and executing the body of the loop makes one iteration. In the above example, there were ten iterations.

![](https://web.archive.org/web/20220811214058im_/https://www.codesdope.com/pa-images-bucket/courses/java/l1.png)

The following animation will also help you to understand the working of the `while` loop.

![](https://web.archive.org/web/20220811214058im_/https://www.codesdope.com/pa-images-bucket/courses/java/l2.gif)

The next program prints the multiplication table of 12 using a `while` loop.

```java
class Test {

    public static void main(String[] args) {
        int i = 1;

        while (i <= 10) {
            System.out.println(i * 12);
            i++;
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">12
24
36
48
60
72
84
96
108
120</pre>
    </details>
</div>

Here, the condition of the `while` loop is `i <= 10` and initially `i` is equal to **1**.

**In the first iteration**, the condition of the loop is true (1 is less than 10). Therefore, the statements in the body of `while` are executed - `12*i` ( 12*1 = 12 ) gets printed and then `i++` increases the value of `i` to **2**.

**In the second iteration**, again the condition of the loop is true (2 is less than 10).  Therefore, the statements in the body of the loop are again executed - `12*i` ( 14*2 = 28 ) gets printed and then `i++` increases the value of `i` to **3**.

Similarly, **in the tenth iteration**, when `i` is **10**, 140 gets printed and `i++` makes the value of `i` equal to **11**.

Now, since the value of `i` is 11, the condition of the `while` loop becomes false and the loop gets terminated.

Let's see one more example.

```java
import java.util.*;

class Test {

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        int choice = 1;
        while (choice == 1) {
            int a;

            System.out.println("Enter a number to check odd or even");
            a = s.nextInt();

            if (a % 2 == 0) {
                System.out.println("Your number is even");
            } else {
                System.out.println("Your number is odd");
            }

            System.out.println("Want to check more 1 for yes 0 for no");

            choice = s.nextInt();
        }

        System.out.println("I hope you checked all your numbers.");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter a number to check odd or even
4
Your number is even
Want to check more 1 for yes 0 for no
1
Enter a number to check odd or even
3
Your number is odd
Want to check more 1 for yes 0 for no
0
I hope you checked all your numbers.</pre>
    </details>
</div>

Since the condition of the loop is `choice == 1`, the loop will run until the value of `choice` becomes something other than 1.

**In each iteration**, if the condition of the loop is true, the statements in the body of the loop are executed. In the body of the loop, it is checked if the number entered by the user is even or odd and the corresponding message is printed. After this, the user is again asked to enter a number - 1 if he wants to check more and 0 otherwise, and this entered number is assigned to the variable `choice`.

**In the first iteration**, the condition of the loop is true because the value of `choice` is 1, and hence the statements in the body of the loop get executed. The user first entered 4, which is even and so the message “Your number is even” gets printed. After that, on asking the value of `choice`, the user entered 1, making `choice` equal to 1.

**In the second iteration**, again the condition is true because  the value of `choice` is 2. So, again the body of the loop is executed, but this time the user entered the value of `choice` as 0, making `choice` equal to 0.

Thus, on checking the third time, the condition of the loop becomes false leading to the termination of the loop.

So, now you know that we use loops to repeat a task multiple times. Playing with loops is really fun!

Now let’s move on to another loop.

***

## Java for Loop

Let's go to our first example in which we printed the first 10 natural numbers using a `while` loop. We can also do that with a `for` loop.

The syntax of the `for` loop is given below.

### Java for Loop Syntax

```java
for(initialization; condition; propagation) {
    statement(s)
}
```

This syntax might seem confusing. Don’t worry, let’s understand it with the help of examples.

### Java for Loop Examples

The following program prints the first 10 natural numbers using a `for` loop.

```java
class Test {

    public static void main(String[] args) {
        int n;

        for (n = 1; n <= 10; n++) {
            System.out.println(n);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">1
2
3
4
5
6
7
8
9
10</pre>
    </details>
</div>

Now let's see how a `for` loop works.

`for(n = 1; n <= 10; n++)`

`n = 1` → This step is used to **initialize** a **variable** and is executed first and only once. Here, the variable `n` is assigned the value **1**.

`n <= 10` → This is a **condition** which is checked. If the condition is true, the statements written in the body of the loop are executed. If it is false, the loop gets terminated. This is similar to the condition we use in a `while` loop which gets checked again and again.

`n++` → This is executed after the code in the body of the `for` loop has been executed. In this example, the value of `n` increases by 1 every time the code in the body of the `for` loop executes. There can be any expression here which you want to run after every iteration.

In the above example, initially `n = 1` assigns the value **1** to `n`.

**In the first iteration**, the condition `n <= 10` is checked. Since the value of `n` is 1, the code in the body of the `for` loop is executed and thus the current value of `n` i.e. 1 gets printed.

Once the statements in the body of the `for` loop are executed, step `n++` is executed which increases the value of `n` by 1, making `n` equal to **2**.

**In the second iteration**, again the condition `n <= 10` is checked. This time also it is true because the value of `n` is 2. Therefore, again the statements in the body of the `for` loop are executed and 2 gets printed, and then the value of `n` is again incremented to **3**.

When the value of `n` becomes 10, the condition `n <= 10` becomes true and 10 gets printed. Now, when `n++` increases the value to `n` to 11, the condition `n <= 10` becomes false and the loop gets terminated.

Look at the following piece of code from the above example.

```java
int n;
		
for(n = 1; n <= 10; n++) {
    System.out.println(n);
}
```

It can also be written as:

```java
for(int n = 1; n <= 10; n++) {
    System.out.println(n);
}
```

And it performs the same task as the following piece of code having a `while` loop.

```java
int n = 1;
		
while(n <= 10) {
    System.out.println(n);
    n++;
}
```

![](https://web.archive.org/web/20220811214058im_/https://www.codesdope.com/pa-images-bucket/courses/java/p0.png)

So, this is how we can perform a task repeatedly using a `while` loop or a `for` loop. 

Now let’s print the first 10 natural numbers in reverse order.

```java
class Test {

    public static void main(String[] args) {
        for (int n = 10; n > 0; n--) {
            System.out.println(n);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10
9
8
7
6
5
4
3
2
1</pre>
    </details>
</div>

Here, initially the value of `n` is 10. The condition of the loop is` n > 0`, which means that the body of the loop will get executed as long as the value of `n` is greater than 0.

**In the first iteration**, the condition `n > 0` is true because the value of `n` is 10. Therefore, the body of the loop gets executed and 10 gets printed. After that, the step `n--` gets executed reducing the value of n to 9.

**In the second iteration**, again the condition is true and so 9 gets printed. After that, again `n--` reduces the value of `n` to **8**.

This goes on till the value of `n` is 1. On further reducing its value, the condition becomes false and the loop gets terminated.

Look at another example in which the sum of 10 numbers entered by the user is printed.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        int sum = 0;

        for (int n = 1; n <= 10; n++) {
            System.out.println("Enter a number");
            Scanner s = new Scanner(System.in);
            int num = s.nextInt();

            sum += num; // same as sum = sum + num
        }

        System.out.println("Sum is " + sum);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter number
4
Enter number
3
Enter number
10
Enter number
3
Enter number
5
Enter number
5
Enter number
1
Enter number
8
Enter number
9
Enter number
2
Sum is 50</pre>
    </details>
</div>

In this example, we initialized the variable `sum` with 0. We will use this variable to store the sum of all values entered by the user.

Coming to the loop, the variable `n` is assigned the value 1. We are running the loop from **n = 1** till **n = 10**, thus having 10 iterations. In each iteration, the value entered by the user is assigned to the variable `num` and then the statement `sum += num` adds that value to `sum`.

For example, in the first iteration, `sum` is 0 and `num` is 4 (user entered 4). So, `sum += num` makes **sum = 4** (sum = 0 + 4).

Similarly, in the second iteration, `sum` is 4 and `num` is 3 (user entered 3). So, `sum += num` makes **sum = 7** (sum = 4 + 3).

There are other ways also to write a program of a `for` loop.

The first example of for loop in which we printed the first 10 natural numbers can also be written in other ways which are:

```java
int n = 1;
for(; n <= 10; n++) {
    System.out.println(n);
}
```

Another way is as follows.

```java
for(int n = 1; n <= 10;) {
    System.out.println(n);
    n++;
}
```

There is also another form of for loop which is discussed in the chapter [Array](https://web.archive.org/web/20220811214058/https://www.codesdope.com/course/java-array/).

***

## Java do...while Loop

`do...while` is another type of loop. This is just like `while` and `for` loops but the only difference is that the code in its body is executed once before checking the conditions.

### Java do...while Syntax

```java
do {
    statement(s)
}
while(condition);
```

The **body of the do...while loop** consists of the statements written inside the braces `{ }` following `do`.

Here, the body of the loop is executed first and then the **condition** is checked for any iteration. So, the body will be executed at least once even if the condition is false.

Let’s look at an example to understand how this loop works.

### Java do...while Examples

In the following example, the first 10 natural numbers are printed using a `do...while` loop.

```java
class Test {

    public static void main(String[] args) {
        int n = 1;

        do {
            System.out.println(n);
            n++;
        } while (n <= 10);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">1
2
3
4
5
6
7
8
9
10</pre>
    </details>
</div>

In this example, the condition of the `do...while` loop is `n <= 10`.

The body of the loop consists of the statements `System.out.println(n)` and `n++`.

**In the first iteration**, the statements in the body of the loop are executed. The first statement prints the value of  `n` i.e. 1, and the second statement increments its value by 1 making `n` equal to **2**. After the body is executed, the condition `n <= 10` is checked. Since the value of `n` is 2, the condition gets satisfied and so there will be another iteration.

**In the second iteration**, the body again gets executed, printing 2 and incrementing the value of `n` to **3**. After that, the condition is checked again and is satisfied because `n` is equal to 3.

Moving on, **in the tenth iteration**, the value of `n` is 10. The body of the loop is executed printing 10 and incrementing the value of `n` to **11**. Now, on checking the condition, it doesn’t get satisfied and so the loop gets terminated.

So, you can see that we can perform the same task using any of the three loops in Java.

***

## Nesting of Loop in Java

You already know that we can create an if...else statement inside another if..else statement. Similarly, we can create a loop inside another loop. If one loop is created inside another loop, then the inner loop is called a **nested loop**.

Let’s see an example of a nested loop.

```java
class Test {

    public static void main(String[] args) {
        for (int i = 12; i <= 14; i++) {
            System.out.println("Table of " + i);
            for (int j = 1; j <= 10; j++) {
                System.out.println(i + "*" + j + "=" + (i * j));
            }
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Table of 12
12*1=12
12*2=24
12*3=36
12*4=48
12*5=60
12*6=72
12*7=84
12*8=96
12*9=108
12*10=120
Table of 13
13*1=13
13*2=26
13*3=39
13*4=52
13*5=65
13*6=78
13*7=91
13*8=104
13*9=117
13*10=130
Table of 14
14*1=14
14*2=28
14*3=42
14*4=56
14*5=70
14*6=84
14*7=98
14*8=112
14*9=126
14*10=140</pre>
    </details>
</div>

We are printing the tables of 12, 13 and 14 in this program.

![](https://web.archive.org/web/20220811214058im_/https://www.codesdope.com/pa-images-bucket/courses/java/p16.gif)

**In the first iteration of the outer for loop**, the value of `i` is 12. In its body, “*Table of 12*” gets printed and the inner `for` loop gets executed.

**In the first iteration of the inner `for` loop**, the value of  `i` is 12 and that of  `j` is 1, and so in its body, *12*1=12* gets printed.

**In the second iteration of the inner for loop**, the value of  `i` is 12 and that of  `j` is 2, and so in its body, *12*2=24* gets printed.

This goes till the tenth iteration of the inner `for` loop in which *12*10=120* gets printed.

This completes the first iteration of the outer `for` loop.

In the second and third iterations of the outer loop, the same process is repeated with `i` as 13 and 14 respectively.

In short, there is nothing new in nesting of loops. Inner loop is like all the other statements in the body of the outer loop, after the execution of which, the rest of the statements in the body of the outer loop are executed.

***

## Java Infinite Loop

An **infinite loop** is a loop whose condition is always true. As a result, it keeps executing its body forever, and hence got its name.

Look at the following example.

```java
class Test {

    public static void main(String[] args) {
        for (int i = 12; i > 0; i++) {
            System.out.println(i);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
…</pre>
    </details>
</div>

This is an infinite loop and will keep on executing. The condition `i > 0` of this loop will always be true because the value of i started from 12 and is getting incremented in each iteration.

Now look at the next example.

```java
class Test {

    public static void main(String[] args) {
        for (int i = 12; true; i++) {
            System.out.println(i);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36</pre>
    </details>
</div>

Here also, the condition of the loop is true and hence it will keep on executing.

We can also create an infinite loop by leaving its conditional expression empty. When the conditional expression is empty, it is assumed to be true. Let's see another example on how to make a `for` loop infinite.

```java
class Test {

    public static void main(String[] args) {
        for (int i = 12;; i++) {
            System.out.println("This loop will never end");
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
This loop will never end
...</pre>
    </details>
</div>

To terminate an infinite loop, press Ctrl + C.

Looping is an important concept in programming. So it is advisable to [practice questions of loops](https://web.archive.org/web/20220811214058/https://www.codesdope.com/practice/practice_java/).

>Invest in your dreams. Grind now. Shine later.



<a href="11-java-break-and-continue.md" class="next">Next</a>
