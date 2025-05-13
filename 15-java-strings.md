# Java Strings

We have already introduced strings in the topic [Data Types](https://web.archive.org/web/20220811195025/https://www.codesdope.com/course/java-data-types/) and have used them in the previous chapters.

As stated earlier, a string is a sequence of characters. Examples of string are “*Hello, let’s learn Java*”, “*John*”, “*1 + 2 = 3*”, etc.

Let’s again discuss what characters and strings are and what all we can do with strings in Java.

## Java Characters

You must be knowing about characters. The **_char_** data type is used to represent characters.

Characters are always written within single quotes `' '`. Examples of characters are ‘a’, ‘A’, ‘%’, ‘_’, ‘2’, etc. So, a '2' (inside single quotes) is a character and 2 (without quotes is an integer).

In Java, characters are represented using **Unicode**. Unicode is an international character set representing all the characters. As a result, the char data type ranges from **0 to 65,535**. For example, the Unidecode value of the character ‘*A*’ is 65 and that of ‘*Z*’ is 90.

```java
class Test {

    public static void main(String[] args) {
        char mychar = 'p';
        System.out.println(mychar);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">p</pre>
    </details>
</div>

In this example, the character 'p' is stored in a variable `mychar`.

## Java Strings

A string is a sequence of characters. In simpler words, it is an array of characters. For example, “Hello World” is a string and is a sequence of 11 characters - ‘H’, ‘e’, ‘l’, ‘l’, ‘o’, ‘ ‘, ‘W’, ‘o’, ‘r’, ‘l’, ‘d’. Yes, space is also a character.

Strings are always written within double quotes `" "`. We have already seen a lot of examples of strings in the previous chapters.

In Java programming, strings are objects of the `String` class (We will learn about classes and objects later). So let’s see how to declare a string.

```java
String mystring = "Hello";
```

In the above statement, the string "Hello" is assigned to `mystring`. Note that here `mystring` is not a variable but is an object of the class `String`. Thus, `mystring` is a `String` object having the value "Hello".

Don’t focus much on classes and objects as of now. In the above statement, `mystring` will behave like any other variable.

We can also declare it as shown below.

```java
String mystring = {'H', 'e', 'l', 'l', 'o'};
```

In the above statement, the string is declared as an array of characters.

We can also create `String` objects using the `new` keyword. In the following statement, the `new` keyword creates an object `mystring` of the `String` class having the value "Hello".

```java
String mystring = new String("Hello");
```

Hence, we can also declare it as shown below.

```java
char[] charArray = {'H', 'e', 'l', 'l', 'o'};
String mystring = new String(charArray);
```

The following example assigns and prints the values of two strings, one using the `new` keyword and the other without it.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "String and Characters";
        String s2 = new String("String and Characters");
        System.out.println(s1);
        System.out.println(s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">String and Characters
String and Characters</pre>
    </details>
</div>

### Using Quotes in String

Consider a string " _This is "Java" course_ ". This string contains another set of double quotes inside it. Let’s print this string.

```java
class Test {

    public static void main(String[] args) {
        String mystring = "This is "Java" course";
        System.out.println(mystring);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:3: error: ';' expected
		String mystring = "This is "Java" course";
		                        ^
Test.java:3: error: ';' expected
		String mystring = "This is "Java" course";
		                                ^
2 errors</pre>
    </details>
</div>

On printing the string, we got an error. The reason is that a string is enclosed within double quotes. So, if we use another set of double quotes in the string, then it will be misunderstood by the compiler.

#### But what if we want to use double quotes in a string?

Double quotes can be added in a string by using `\"` instead of `"`. Here, `\"` is called an **escape sequence**. We will look at more escape sequences in the next section.

```java
class Test {

    public static void main(String[] args) {
        String mystring = "This is \"Java\" course";
        System.out.println(mystring);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is "Java" course</pre>
    </details>
</div>

In the above example, the escape sequence `\"` got replaced by `"` in the output.

## Escape Sequence

An **escape sequence** consists of a backslash `\` followed by a **special character**. Special characters are the characters having special meaning like `'` (encloses a character), `"` (encloses a string), etc. Escape sequences get interpreted when placed inside a string.

For example, as seen in the previous example, `\"` is an escape sequence which tells the compiler that `"` is not an opening or closing quote of a string but just a simple “ character. Similarly, `\'` is another escape sequence which tells the compiler that `'` is not an opening or closing quote of a character but a simple ‘ character.

The escape sequences supported by Java are shown in the following table.

| Escape Sequence | Description                  |
| --------------- | ---------------------------- |
| \\              | Backslash (\)                |
| \'              | Single Quote (')             |
| \"              | Double Quote (")             |
| \n              | ASCII Line Feed              |
| \t              | ASCII Horizontal Tab         |
| \b              | ASCII Backspace              |
| \f              | ASCII Form Feed              |
| \r              | ASCII Carriage Return        |

Let’s look at some examples.

### \\

This escape sequence inserts a backslash `\` in its place in the string.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("C:\\Documents\\Folder");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Output<p>C:\Documents\Folder
                      </p></pre>
    </details>
</div>

In this example, the escape sequence `\\` got replaced by `\`.

### \'

This escape sequence inserts a single quote `'` in its place in the string.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("This is \'Java\' course");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is 'Java' course</pre>
    </details>
</div>

The escape sequence `\'` got replaced by `'`.

### \"

This escape sequence inserts a double quote `"` in its place in the string.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("This is \"Java\" course");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is "Java" course</pre>
    </details>
</div>

In this example, the escape sequence `\"` got replaced by `"`.

### \n

This escape sequence inserts a new line in its place in the string.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("First line\nSecond line");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">First line
Second line</pre>
    </details>
</div>

Here, a new line got inserted in place of `\n`.

### \t

This escape sequence inserts a horizontal tab in its place in the string.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("Before horizontal tab\tAfter horizontal tab");
        System.out.println("Before horizontal tab\t\tAfter horizontal tab");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Before horizontal tab    After horizontal tab
Before horizontal tab        After horizontal tab</pre>
    </details>
</div>

In the first string, a tab got inserted in place of `\t`, and in the second string, two tabs got inserted in place of `\t\t`.

In this chapter, we learned about how to create and work with strings in Java. In the next chapter, we will go through string operations and some of the useful methods which can be used on strings.

> It’s an imperfect world but it’s the only one we got.
>
> \- Tony Stark


<a href="16-java-string-methods-and-operations.md" class="next">Next</a>
