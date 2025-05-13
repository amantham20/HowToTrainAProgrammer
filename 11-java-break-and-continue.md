# Java Break and Continue

In the last topics, you learned about loops which are used to repeat a certain process some number of times.

What if we can control the way our loop operates?

In Java, we can jump out of a loop or jump to the starting condition of a loop whenever we want. We do this with the help of `break` and `continue` statements respectively.

## Java break Statement

`break` is used to break or terminate a loop whenever we want.

Just type `break;` after the statement after which you want to break the loop.

### Java break Syntax
```java
break;
```
### Java break Examples
```java
class Test {

    public static void main(String[] args) {
        for (int n = 1; n <= 5; n++) {
            System.out.println("*");
            if (n == 2) {
                break;
            }
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">*
*</pre>
    </details>
</div>

**In the first iteration of the loop**, "*" gets printed and the condition `n == 2` of *if* is checked. Since the value of `n` is 1, the condition becomes false.

**In the second iteration of the loop**, '*' gets printed again and the condition of *if* is checked. This time the value of `n` is 2 and hence the condition of *if* becomes true. In the body of *if*, the `break` statement terminates the loop.

The same program using a `while` loop is written below.
```java
class Test {

    public static void main(String[] args) {
        int n = 1;

        while (n <= 5) {
            System.out.println("*");
            if (n == 2) {
                break;
            }
            n++;
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">*
*</pre>
    </details>
</div>

Let's look at one more example.
```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        int x;
        Scanner s = new Scanner(System.in);

        for (;;) {
            System.out.println("Enter 0 to stop");
            x = s.nextInt();
            if (x == 0) {
                break;
            }
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter 0 to stop
3
Enter 0 to stop
32
Enter 0 to stop
23
Enter 0 to stop
0</pre>
    </details>
</div>

This is an infinite loop. To terminate it, we are using the `break` statement. If the user enters 0, then the condition of *if* will get satisfied and the `break` statement will terminate the loop.

## Java continue Statement

While the `break` statement **terminates** the loop, the `continue` statement skips the remaining statements in the loop and starts the next iteration.

In short, it ends the execution of the current iteration without executing the rest of the statements in the loop. After that, the f<b>low proceeds to the next iteration as usual</b>.

![continue statement in Java](https://web.archive.org/web/20220811205712im_/https://www.codesdope.com/pa-images-bucket/courses/java/p17.png)

Let’s look at its syntax and examples to understand the working of continue.

### Java continue Syntax
```java
continue;
```
### Java continue Examples
```java
class Test {

    public static void main(String[] args) {
        for (int n = 1; n <= 10; n++) {
            if (n == 5) {
                continue;
            }
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
6
7
8
9
10</pre>
    </details>
</div>

Notice that **5** is not printed in the output. This is because in the fifth iteration when the value of `n` became 5, the condition of if became true and the `continue` statement in the body of *if* got executed. Thus the next statement `System.out.println(n)` didn’t get executed and the sixth iteration started.
```java
class Test {

    public static void main(String[] args) {
        int n = 1;

        while (n <= 10) {
            if (n == 5) {
                n++;
                continue;
            }
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
6
7
8
9
10</pre>
    </details>
</div>

> You can waste your lives drawing lines. Or you can live your life crossing them.
>
> \- Shonda Rhimes


<a href="12-java-methods.md" class="next">Next</a>
