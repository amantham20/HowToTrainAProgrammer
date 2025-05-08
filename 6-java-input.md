# Java Input
We make computer programs for users. We solve real-world computer problems for users. So, it is necessary for our computer to interact with the users. This is what you will learn in this chapter.

There can be times when we want the user to enter the value which has to be assigned to a variable. Take an example of a calculator in which the user enters the values to be added or subtracted. So let's proceed to learn how to take input from a user.

In Java, we take input with the help of the `Scanner` class. Java has a number of predefined classes which we can use. We will learn more about classes [later](https://web.archive.org/web/20220811212753/https://www.codesdope.com/course/java-object-oriented-programming/).

Predefined classes are organized in the form of packages. This `Scanner` class is found in the `java.util` package. So to use the `Scanner` class, we first need to include the `java.util` package in our program.

We include a package in a program with the help of the `import` keyword. A package has many predefined classes. We can either import the `java.util.Scanner` class or the entire `java.util` package.

To import a class or a package, add one of the following lines to the very beginning of your code.

```java
import java.util.Scanner;   // This will import just the Scanner class
import java.util.*;   // This will import the entire java.util package
```

After importing, we need to write the following statement in our program.

`Scanner s = new Scanner (System.in);`

Here, by writing `Scanner s`, we are declaring `s` as an object of the `Scanner` class. `System.in` within the round brackets tells Java that this will be System Input i.e. input from a user will be given to the system.

If you have understood all that has been stated till now, that’s great. If you haven't, do not bother. Currently, you just need to know that we have to import the class or package at the beginning of the program and then include the above statement in the program.

## How to Input

Taking a value from the user is quite easy. You just have to write a statement and it is done!

Let's start with an integer. Consider the following code.

`Scanner s = new Scanner (System.in);
int n;
n = s.nextInt();      //   s is object of Scanner class`

The statement `n = s.nextInt()` is used to input an integer value from the user and assign it to the variable `n`.
Here, `nextInt()` is a method of the object `s` of the `Scanner` class.

Let's see an example in which we will input an integer value from the user.

```java
import java.util.*;

class I1 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("Enter an integer");
        int a;
        a = s1.nextInt();
        System.out.println("The entered integer is" + a);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter an integer
14
The entered integer is14
</pre>
    </details>
</div>

In this example, we created an object `s1` of the `Scanner` class. Then we took an integer input from the user using `s1.nextInt()` and the value entered by the user (14 in this case) is assigned to the variable `a`.

<p>
<img alt="Input in Java" src="https://web.archive.org/web/20220811212753im_/https://www.codesdope.com/pa-images-bucket/courses/java/p10.png" style="max-width:70%;height:auto;"/>
</p>

Wasn’t it easy?

In the last example, we used the `nextInt()` method to take integer input. Similarly, there are different methods to take input of different data types. For example, the `nextDouble()` method is used to take input of type double.

The table given below shows the methods used for taking input of different data types.

| Method      | Inputs        |
| ----------- | ----------- |
| nextInt()   | Integer     |
| nextFloat() | Float       |
| nextDouble()| Double      |
| nextLong()  | Long        |
| nextShort() | Short       |
| next()      | Single Word |
| nextLine()  | Line of Strings |
| nextBoolean() | Boolean |

Now let's see an example in which we will input values of different data types.

```java
import java.util.*;

class I2 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("Enter integer");
        int n = s1.nextInt();

        System.out.println("Enter double");
        double db = s1.nextDouble();

        System.out.println("Integer :" + n);
        System.out.println("Double :" + db);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter integer
45
Enter double
23.242
Integer :45
Double :23.242
</pre>
    </details>
</div>

Here, `s1.nextInt()` takes an integer input (45) and assigns it to the variable `n`, and `s1.nextDouble()` takes an input of type double (23.242) and assigns it to the variable `db`.

### Input Word
As we have seen in the above table, the method used to input a word is `next()`.

We know that 10 is an integer, in the same way a word is a string. A string is a collection of characters. Since a word consists of characters, therefore it is a string.

To input a word, we need to write

```java
String n;
n = s.next();      //   s is object of Scanner class
```

or simply

```java
String n = s.next();      //   s is object of Scanner class
```

Let's see an example.

```java
import java.util.*;

class I3 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("Enter your first name");
        String f = s1.next();
        System.out.println("Enter your last name");
        String l = s1.next();
        System.out.println("Your name is " + f + " " + l);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your first name
Robert
Enter your last name
Brown
Your name is Robert Brown
</pre>
    </details>
</div>

Here, the first `s1.next()` takes a word input (Robert) and assigns it to the variable `f`, and the second `s1.next()` takes another word input (Brown) and assigns it to the variable `f`.

```java
next() takes only the first word even if we try to give more than one word as input.
```

Let's see another example.

```java
import java.util.*;

class I3 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("Enter your first name");
        String f = s1.next();
        System.out.println("Your name is " + f);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your first name
Robert Brown
Your name is Robert
</pre>
    </details>
</div>

In the above example, the input that we gave (Robert Brown) has two words, but `s1.next()` took only the first word as input. Hence, the value of the variable `f` became equal to “Robert”.

### Input a Sentence
In the same way as a word is a string, a sentence is also a string. Therefore, we input a sentence in the same way as a word, the difference is that the method used to input a sentence is `nextLine()`.

`String st = s.nextLine();      //   s is object of Scanner class`

Look at the following example.

```java
import java.util.*;

class I4 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("Enter your name");
        String name = s1.nextLine();
        System.out.println("Your name is " + name);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your name
Robert Brown
Your name is Robert Brown
</pre>
    </details>
</div>

Here,  `s1.nextLine()` takes a sentence as input (Robert Brown) and assigns it to the variable `name`.

```java
The only difference between the methods nextLine() and next() is that nextLine() reads the entire input string including white spaces, whereas next() reads only upto the first white space and then stops.
```

An example will make the difference clear.

```java
import java.util.*;

class I5 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        System.out.println("Enter your name");
        String w = s1.next();
        System.out.println("Your name is " + w);
        System.out.println("Again enter your name");
        String st = s1.nextLine();
        System.out.println("Your name is " + st);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter your name
Robert Brown Jr.
Your name is Rober
Again enter your name
Your name is Brown Jr.
</pre>
    </details>
</div>

Here, `next()` read only the first word. After this first word has been read, `nextLine()`  read the rest of the words.

So this is how we can take input of values of any data type from the user. Before wrapping up, let’s look at an example in which we will take the length and breadth of a rectangle as input from the user and will then display the area of the rectangle.

```java
import java.util.*;

class I6 {

    public static void main(String[] args) {
        Scanner s1 = new Scanner(System.in);
        int l, b;
        System.out.println("Enter length of rectangle");
        l = s1.nextInt();

        System.out.println("Enter breath of rectangle");
        b = s1.nextInt();

        System.out.println("Area of rectangle is " + (l * b));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter length of rectangle
2
Enter breath of rectangle
4
Area of rectangle is 8
</pre>
    </details>
</div>
