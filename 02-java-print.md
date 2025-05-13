# Printing in Java

Let's take the first step in the journey of learning how to code. In this chapter, we will learn how to print something on the screen. Printing is the first step in learning any programming language.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hello World");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello World</pre>
    </details>
</div>

The above program printed "Hello world" on the screen. Basically, we have written a program to print any message on the screen. Let's try this out with a different message.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hey, I am a Silly Goose!");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hey, I am a Silly Goose!</pre>
    </details>
</div>

Yes, it worked. We just printed a different message on the screen. Now it's time to understand the working of the program. Let’s do this by understanding each line of the code.

**But Before that, could you change the message to "Hello World" to Say "Hello" and your name? For example, "Hello Aman".**





## Working of a Java Program

You won't be able to understand the entire code thoroughly in this first chapter, but gradually, with the progress of the course, you will understand everything. This makes sense because programming is all about consistency and practice. However, you will have enough understanding after this chapter to start writing and understanding different programs.

Let’s try to understand the structure of the first program in this chapter.

### class Hello

This is the class definition (you will learn about classes in a later chapter). For now, just keep in mind that we need to have a class in our code and we write like this. `Hello` is the name of the class. We can give any other **name of the class** like FirstProgram, MyCode, etc.

The curly braces `{ }` following `class Hello` represent the body of the class. All the statements written inside these curly braces are inside the body of the class named Hello.

<img alt="Java Hello World explanation" src="https://web.archive.org/web/20220811210445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p1.png" style="max-width:80%;height:auto;"/>

### public static void main(String[] args)

This is the **main method** (you will learn about methods also later). Its significance is that whenever we run our code, the main method gets executed first. It means that the code written inside this is executed first when a Java program is run. So, you won't be able to execute your code without the main method.

Similar to a class, the curly braces `{ }` following `public static void main(String[] args)` represent the body of the main method.

<img alt="Java Hello World main method explanation" src="https://web.archive.org/web/20220811210445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p2.png" style="max-width:80%;height:auto;"/>

### System.out.print("Hello World");

<img alt="Java print explanation" src="https://web.archive.org/web/20220811210445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p3.png" style="max-width:80%;height:auto;"/>

This is the **statement** which printed the message on the screen. The semicolon `;` at the end marks the end of the statement. We end our statements with a semicolon in Java. `print()` is a method which basically printed the message "Hello World". `print()` method is available in the `System` directory. It is used to display something on the screen.

Thus, the format of a Java program is as shown below.

```java
class CLASSNAME{

  public static void main(String[] args){
    Statement
    Statement
    Statement
    ....
  }
}
```

The body of the class contains the main method, and the body of the main method contains statements.

In the first example, you can see that the main method is inside the class `Hello` and the statement `System.out.print("Hello World");` is inside the main method.

<img alt="Body of method in Java" src="https://web.archive.org/web/20220811210445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p4.png" style="max-width:80%;height:auto;"/>

As mentioned earlier, when we run a program, the main method (hence the statements inside the main method) gets executed first.

## Printing in Java

We have already seen how to print something on screen. Let’s again look at the first example given in this chapter.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hello World");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello World</pre>
    </details>
</div>

This program prints Hello World. Thus, to print any message, we write it within double quotes ` " "` inside `System.out.print()`.

<img alt="printing message in Java" src="https://web.archive.org/web/20220811210445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p5.png" style="max-width:70%;height:auto;"/>

Look at another example.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hello");
        System.out.print("World");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">HelloWorld</pre>
    </details>
</div>

Here the first statement prints Hello and the second statement prints World.

Now let’s print a number.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("10");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

We printed 10 on screen.

Now suppose we want to print Hello and World in different lines. For that, we can use the `println()` method instead of the `print()` method as shown below.

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello");
        System.out.print("World");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello
World</pre>
    </details>
</div>

The `println()` method changes the line after printing its content.

In the above example, `System.out.println("Hello")` printed Hello and then moved to a new line. After that, `System.out.print("World")` printed World.

### Joining Strings while Printing

If we have two words and we want to print them together, we can join them using `+`. Let’s see how with the help of an example.

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello " + "World");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello World
                      </pre>
    </details>
</div>

*"Hello "* and *"World"* are two different words here, and `+` joins them together to make a single string "Hello World".

Try one more example

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Codes" + "Dope");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">CodesDope
                      </pre>
    </details>
</div>

So now you know how to print anything on screen. This was a good start.

In Java, there are some special characters which when printed prints something special. Let’s look at them.

## Using Special Characters

There are several special characters in Java which will be discussed in a later chapter. For now, let’s talk about the two most commonly used special characters - \n and \t.

### \n

`\n` is called the **newline character**. When we print it, a new line gets printed.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hello\nWorld");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello
World</pre>
    </details>
</div>

In the above example, after printing *Hello*, printing `\n` printed a new line. After that, *World* got printed.

Let's use `\n` at the end.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hello World\nNew Line\n");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello World
New Line
                      </pre>
    </details>
</div>

Yes you guessed it right, `\n` does the same job as the `println()` method. Therefore, `System.out.println("Hello")` and  `System.out.print("Hello\n”)` will give the same output.

<img alt="New line in Java" src="https://web.archive.org/web/20220811210445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p6.png" style="max-width:90%;height:auto;"/>

Let’s see another example.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Good morning\n\nAll set?\nLet's learn Java");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Good morning
All set?
Let's learn Java
                      </pre>
    </details>
</div>

From the output, you can see that each time `\n` is printed, the line gets changed (a new line is printed).

### \t

`\t` is called the **tab character**. When we print it, a new tab gets printed.

```java
class Hello {

    public static void main(String[] args) {
        System.out.print("Hello\tWorld");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello     World
                      </pre>
    </details>
</div>

In the above example, after printing Hello, printing `\t` printed a tab space, and after that, *World* got printed.

In this chapter, we learned how to print something in Java. Coding is all about practice and solving questions. So, solve questions as much as you can. Solve questions after completing every chapter and then only go to the next chapter.

> The best way to predict future is to create it.
>
> \- Alan Kay


<!-- next chapter -->
<a href="03-java-basics.md">Next Chapter</a>