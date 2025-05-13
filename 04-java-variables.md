# Variables in Java

Till now, we know how to print anything on screen. Now, let’s learn about variables in Java which are somewhat similar to the variable we use in Mathematics.

## What are Variables?

A variable is used to store some value. You can think of a variable as a storage which has a name and stores some value.

<img alt="Variables in Java" src="https://web.archive.org/web/20220811202648im_/https://www.codesdope.com/pa-images-bucket/courses/java/p8.png" style="max-width:30%;height:auto;"/>

```java
class Test {

    public static void main(String[] args) {
        int n;
        n = 4;
        System.out.println(n);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">4
</pre>
    </details>
</div>

In this example, `n` is a variable and we stored a value of 4 in it.

`int n` → This statement declares that `n` is a variable that can store some integer value (because `int` is written before `n`). Whenever a variable is declared, it takes some space in the memory of the computer. With this declaration, a space is allocated to `n` in the memory of the computer to store an integer value.

<img alt="Variable declaration in Java" src="https://web.archive.org/web/20220811202648im_/https://www.codesdope.com/pa-images-bucket/courses/java/p9.png" style="max-width:70%;height:auto;"/>

`n = 4` → A value 4 is assigned to the variable `n`.

`System.out.println(n)` → The `System.out.println()` method prints the value of n on the screen.

Note that while printing, `n` is not written within double quotes ` " " `. This is because `n` written within double quotes ` " " ` would have printed simple `n` instead of the value of n.

Look at another example.

```java
class Test {

    public static void main(String[] args) {
        int n;
        n = 4;
        System.out.println(n);
        System.out.println("n");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">4
n
</pre>
    </details>
</div>

Here `System.out.println(n)` printed the value of the variable `n` whereas `System.out.println("n")` printed the character `n`.

<img alt="Variable VS string in Java" src="https://web.archive.org/web/20220811202648im_/https://www.codesdope.com/pa-images-bucket/courses/java/v2.png" style="max-width:70%;height:auto;"/>

In the above examples, we declared a variable and assigned a value to it in two separate statements as shown below.

`int n;`
`n = 4;`

We can do this in a single statement also as shown below.

`int n = 4;`

Look at the following example in which we have declared a variable and assigned a value to it in a single statement.

```java
class Test {

    public static void main(String[] args) {
        int n = 4;
        System.out.println(n);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">4
</pre>
    </details>
</div>

Let’s see some more examples.

```java
class Test {

    public static void main(String[] args) {
        int n = 4;
        System.out.println("The value of n is: " + n);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">The value of n is: 4
</pre>
    </details>
</div>

In this example, notice the following statement.

`System.out.println("The value of n is: " + n);`

The string ` "The value of n is: " ` is joined to the value of `n` using `+`, and the final string ` "The value of n is: 4" ` got printed.

We can also reassign value to a variable as shown below.

```java
class Test {

    public static void main(String[] args) {
        // declaring and assigning a value to variable num
        int num = 4;

        // reassigning value to the variable num
        num = 5;

        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">5
</pre>
    </details>
</div>

In the above example, a variable `num` is declared and assigned a value of 4. Then in the next statement, the variable `num` is reassigned a value of 5 making its value equal to 5.

## Declaring Multiple Variables

Let’s see a simple example in which two variables are declared.

```java
class Test {

    public static void main(String[] args) {
        int num1;
        int num2;

        num1 = 10;
        num2 = 20;

        System.out.println(num1);
        System.out.println(num2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10
20
</pre>
    </details>
</div>

Here, the statement int `num1` declares a variable `num1` and the statement int `num2` declares a variable `num2`. Then `num1` and `num2` are assigned the values 10 and 20 respectively.

We can also declare multiple variables in a single statement as shown below.

`int num1, num2;`

In the above statement, the variables `num1` and `num2` are declared in a single statement. This is demonstrated in the following program.

```java
class Test {

    public static void main(String[] args) {
        int num1, num2;

        num1 = 10;
        num2 = 20;

        System.out.println(num1);
        System.out.println(num2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10
20
</pre>
    </details>
</div>

We can also declare and initialize multiple variables in a single statement as shown below.

`int num1 = 10, num2 = 20;`

Here, the variable `num1` is declared and assigned a value 10 and the variable `num2` is declared and assigned a value 20 in a single statement. Let’s do this in a program.

```java
class Test {

    public static void main(String[] args) {
        int num1 = 10, num2 = 20;

        System.out.println(num1);
        System.out.println(num2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10
20
</pre>
    </details>
</div>

In the above example, by declaring and assigning values to multiple variables in a single statement, we saved so many lines of code.

So now you have understood what a variable is. We will be using variables in almost all the programs in future.

## Identifiers

An **identifier** is a name we give to entities like variables, methods, classes, etc. We will learn about all these entities in later chapters. For now, just remember that whenever we define an entity, we assign it a name which is called an identifier.

In the last example, `Hello` is an identifier because it is the name of a class, `main` is an identifier because it is the name of a method and `num1` and `num2` are also identifiers because they are the names of variables.

### Rules for writing Identifiers

1.  Identifiers can be a combination of lowercase (**a - z**) and uppercase (**A - Z**) letters, digits (**0 - 9**), dollar sign (**$**) or an underscore (\_). Special characters (\*, %, #, !, @, etc.) cannot be present in identifiers. Eg, *Message1*, *num\_max* are valid identifiers and *num@* is an invalid identifier.
2.  Identifiers cannot start with a digit. Eg, 2num is an invalid identifier.
3.  In Java, identifier names are **case-sensitive**, i.e. *num* and *Num* will be treated as different.
4.  Keywords cannot be used as identifiers (Keywords are explained in the [previous chapter](https://web.archive.org/web/20220811202648/https://www.codesdope.com/course/java-basics/)).
5.  Eg, class is an invalid identifier because it is a keyword.

### Good Practices to Name Identifiers

There are some good practices to name identifiers which should be followed but are not mandatory.

1.  Identifiers should be kept meaningful so that understanding code is easier. Therefore, instead of using names like *x*, *y*, *a*, *b*, etc. for identifiers, use some meaningful names. For example, if we are storing the product of two numbers in a variable, then the name of that variable should be kept as *product*.
2.  Names of variables and methods should contain only lowercase letters. For example, *name*, *display()*, etc.
3.  Class names should start with capital letters. For example, Person, Student, Books, etc.
4.  If you want to name a variable with multiple words, then name it as multiple words separated by underscores. For example, *first\_name*, *last\_name*, etc.
5.  If you want to name a method with multiple words, then name it in **CamelCase** format. For example, *getName()*, *printMessage()*, etc.
6.  If you want to name a class with multiple words, then name it in **CamelCase** format. For example, *StudentRecord*, *BookAuthor*, etc.

In this chapter, we learned about variables and also saw examples to define variables which can store integer values. However, we can also define variables which can store text or other types of values, which we will look at in the next chapter.

> All our dreams can come true, if we have the courage to pursue them.
>
> \- Walt Disney

<a href="05-java-data-types.md">Next Lesson</a>