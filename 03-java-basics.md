# Java Basics

Now that you know how to print anything on screen, let’s look at some basics of Java.

## Whitespace

Whitespace refers to spaces, tabs and newlines. In some places in our code, whitespace is necessary, whereas in other places, it is given just to improve readability.

For example, while writing `class Hello`, it is necessary to give a space between class and Hello (as they are two different words).

`class Hello`

On the contrary, there is no need to give any space or newline in the following program after `{`.

`class Hello{public static void main(String[] args){System.out.print("Hello World");}}`

```java
class Hello{public static void main(String[] args){System.out.print("Hello World");}}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello World
                      </pre>
    </details>
</div>

Although we can give as many whitespaces as we want, the compiler ignores all the unnecessary whitespaces. The following code also runs just fine.

```java
class    Hello{
	
  public	static		void main(String[] args)   {
    		System.out.print("Hello World");
    		
    		
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

In this example, the compiler ignored the unnecessary spaces and the code ran fine.

In fact, apart from separating two different words, whitespaces doesn't hinder the functionality of our program i.e., we can give as many whitespaces as we want or we may even choose to give none.

<p><img alt="Java whitespace" src="https://web.archive.org/web/20220811201251im_/https://www.codesdope.com/pa-images-bucket/courses/java/im1.png" style="max-width:80%;height:auto;"/></p>

## Indentation

Indentation is a set of whitespaces at the beginning of the lines of code inside the body of a class, method, etc. It makes our code more readable. It is not compulsory to give indentation in a program in Java but giving it is a good practice.

To understand the need of indentation, look at the following two programs.

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

```java
class Hello {
public static void main(String[] args) {
System.out.println("Hello World");
}
}
```

Which one of the above two programs do you think is more readable? Correct, it is the first one.

In the first program, we gave indentation before the code (main method) inside the body of the `Hello` class. We also gave indentation before the code (System.out.println statement) inside the body of the main method. Giving indentation made the code more neat and clean. This is the significance of indentation.

<p><img alt="Indentation in Java" src="https://web.archive.org/web/20220811201251im_/https://www.codesdope.com/pa-images-bucket/courses/java/p7.png" style="max-width:70%;height:auto;"/></p>

It is preferred to give 2 or 4 spaces in indentation. It can also be given by tabs equivalent to 2 or 4 spaces. Indentation should be consistent throughout the program, which means that if an indentation of 4 spaces is given at one part of the program, then the same indentation should be given at other parts of the program.

A good programmer always indents the code. So, make it a habit of adding indentation to your code right from the start.

## Comments

Comment is some text written in a program and ignored by the compiler while compiling the code. Comments are for humans to read and not for computers. These are written to make our code more readable.

### Single Line Comments

Single line comments always start with `//`. The next line is not a part of the comment.

```java
//This is single line comment
//This is also a comment
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
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

### Multiline Comments

We can also write comments which extend upto multiple lines. Multiline comments are written within `/*  */`.

```java
/*Hello World code*/
/* Comments will not be compiled and will be ignored */
/* It is a
multiline
comment*/
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
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

Note that we can't put one comment inside another.For example, **/* This is a /*comment*/ */** is **invalid**.

### Why to use Comments?

As mentioned earlier, it makes your code more understandable. Assume that you have written a software and after releasing it, you hired a few good programmers for its maintenance. Without comments, it would be a very difficult job for them to understand your code. And most of the time it happens that the person who has written a code is not the one who is going to modify it. So, make a habit of writing good comments.

It is also not recommended to write too many comments. A clean and good code can be understood without comments.

## Java Keywords

There are few words which are used by Java itself. So, we can't use those words for the name of our classes, methods or variables (we will learn about variables in the next chapter) as they are reserved for Java. For example, the keyword `class` is used by Java to create a class and thus we can’t use it as the name of a class. Doing so will give us an error.

Here is the list of a few keywords reserved for Java.

| abstract | assert  | boolean | break  |
| ------- | ------- | ------- | ------ |
| byte   | case   | catch   | char   |
| class   | const   | continue | default |
| do     | double  | else    | enum   |
| extends | final   | finally | float  |
| for    | goto    | if     | implements |
| imports | instanceof | long    | native  |
| new    | package | private | protected |
| public  | return  | short   | static  |
| striptfp | super   | switch  | synchronized |
| this   | throw   | throws  | transient |
| try    | void    | volatile | while   |

Wooh! This had a lot of terminologies but it was just to introduce you to the basics of Java. We will look at variables in somewhat more detail in the next chapter.

> If you rely completely on protocol, you can become a robot.
>
> \- Margaret Trudeau
