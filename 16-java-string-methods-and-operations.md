# Java String Methods and Operations

In the last chapter, we learned about creating and using strings. Strings are very commonly used in programming and so it is good to know some string methods and operations which can make working with strings easier by returning string length, converting string to lowercase or uppercase, joining strings, etc.

## Java String Methods

Some useful string methods are given below.

| Method                                      | Description                                                                                                                                   |
| :------------------------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------- |
| char charAt(int index)                      | returns char value for particular index                                                                                                       |
| int length()                                | returns string length                                                                                                                         |
| String substring(int startIndex)            | returns substring for given start index                                                                                                       |
| String substring(int startIndex, int endIndex) | returns substring for given start index and end index                                                                                       |
| boolean equals(Object anotherObject)        | checks the equality of string with object                                                                                                     |
| boolean isEmpty()                           | checks if string is empty                                                                                                                     |
| String concat(String str)                   | joins two strings                                                                                                                             |
| String replace(char oldChar, char newChar)     | replaces old character with new character value in string                                                                                     |
| String replaceAll(String oldSubstring, String newSubstring) | replaces each substring that matches oldSubstring with a substring that matches newSubstring in string                     |
| String toLowerCase()                        | returns string in lowercase                                                                                                                   |
| String toUpperCase()                        | returns string in uppercase                                                                                                                   |
| int indexOf(char ch)                        | returns index of specified character                                                                                                          |
| int indexOf(char ch, int startIndex)        | returns index value of specified character starting with given index                                                                          |
| int indexOf(String substring)               | returns index of specified substring                                                                                                          |
| int indexOf(String substring, int startIndex) | returns index value of specified substring starting with given index                                                                         |
| boolean contains(CharacterSequence t)       | checks if string contains the specified character sequence                                                                                    |
| String trim()                               | omits leading and trailing white spaces                                                                                                       |
| boolean startWith(String str)               | checks if the string starts with the specified substring                                                                                      |
| boolean startWith(String str, int startIndex) | checks if the string starts with the specified substring starting from the specified index                                                 |
| boolean endsWith(String str)                | checks if the string ends with the specified substring                                                                                        |
| int compareTo(Object obj)                   | compares string with object                                                                                                                   |
| int compareTo(String anotherString)           | compares string with another string                                                                                                              |

Now let's quickly have a look at some examples.

### Java charAt()

It returns the character at the specified index in a string.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Hello";
        char ch = s1.charAt(1);
        System.out.println(ch);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">e</pre>
    </details>
</div>

The character at index 1 in `s1` is e. So, `s1.charAt(2)` returned e.

### Java length()

It returns the length (number of characters) in a string.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Hello World";
        int len = s1.length();
        System.out.println("String length is " + len);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">String length is 11</pre>
    </details>
</div>

### Java substring()

It returns the substring starting from the specified **start index** and ending at the specified **end index**. If no **end index** is given, then the substring starting from the **start index** is returned.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Umbrella";
        String s2 = s1.substring(2);
        String s3 = s1.substring(2, 6);
        System.out.println(s2);
        System.out.println(s3);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">brella
brel</pre>
    </details>
</div>

`s1.substring(2)` returned the substring starting from index 2 (2 is the start index).

`s1.substring(2, 6)` returned the substring starting from index 2 (2 is the start index) and ending at index 6 (6 is the end index).

### Java isEmpty()

It checks whether a string is NULL or not. If the string is NULL, it returns true, otherwise it returns false.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Umbrella";
        String s2 = "";
        System.out.println(s1.isEmpty());
        System.out.println(s2.isEmpty());
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">false
true</pre>
    </details>
</div>

### Java concat()

It concatenates or joins two strings.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Codes";
        String s2 = "Dope";
        s1 = s1.concat(s2);
        System.out.println(s1);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">CodesDope</pre>
    </details>
</div>

In this example, the string `s2` is concatenated to the string `s1`.

### Java replace()

It returns a string by replacing the specified character or substring with another specified character or substring.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Welcome to CodesDope";
        String s2 = s1.replace('o', 'D');
        System.out.println(s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">WelcDme tD CDdesDDpe</pre>
    </details>
</div>

In the above example, all occurrences of the character `'o'` got replaced by `'D'` in the string `s1`.

Look at another example.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Switch on the button";
        String s2 = s1.replace("on", "ui");
        System.out.println(s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Switch ui the buttui</pre>
    </details>
</div>

In this example, all occurrences of the substring `“on”` got replaced by `“ui”` in the string `s1`.

### Java toLowerCase()

It returns a string with all the characters in lowercase.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Welcome to Codesdope";
        String s2 = s1.toLowerCase();
        System.out.println(s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">welcome to codesdope</pre>
    </details>
</div>

### Java toUpperCase()

It returns a string with all the characters in uppercase.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Welcome to Codesdope";
        String s2 = s1.toUpperCase();
        System.out.println(s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">WELCOME TO CODESDOPE</pre>
    </details>
</div>

### Java indexOf()

It returns the index of the specified character or substring in a string.

If the specified character or substring occurs more than once in the string, then the index of its first occurrence is returned.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Switch on the button";
        int n1 = s1.indexOf('t');
        int n2 = s1.indexOf("on");
        System.out.println("n1 = " + n1);
        System.out.println("n2 = " + n2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">n1 = 3
n2 = 7</pre>
    </details>
</div>

`s1.indexOf('t')` returned the index of the character `'t'` in the string `s1`. Note that the character `'t'` occurs four times at indices 3, 10, 16 and 17, but only the index of the first occurrence, i.e. 3, is returned.

Similarly, `s1.indexOf("on")` returned the index of the first occurrence of the string `“on”` in the string `s1`.

We can also pass the **start index** from which we want the search to begin to the method.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Switch on the button";
        int n1 = s1.indexOf('t', 8);
        int n2 = s1.indexOf("on", 12);
        System.out.println("n1 = " + n1);
        System.out.println("n2 = " + n2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">n1 = 10
n2 = 18</pre>
    </details>
</div>

`s1.indexOf('t', 8)` returned the index of the character `'t'` after the 8<sup>th</sup> index and `s1.indexOf("on", 12)` returned the index of the string `“on”` after the 12<sup>th</sup> index.

### Java contains()

It checks if a string contains the specified character sequence. It returns true if the character sequence is present in the string, and returns false otherwise.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "My name is : Robert Brown";
        System.out.println(s1.contains("Robe"));
        System.out.println(s1.contains(":"));
        System.out.println(s1.contains("/"));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">true
true
false</pre>
    </details>
</div>

### Java compareTo()

It compares two strings lexicographically (in the dictionary order). It returns **0** if both the strings are the same, **a positive value** if the first string comes after the second string and **a negative value** if the first string comes before the second string in the dictionary order.

While comparing two strings, the Unicode values of their characters are compared. The character having the lower Unicode value is smaller.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Black";
        String s2 = "Brown";
        System.out.println(s1.compareTo(s2));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">-6</pre>
    </details>
</div>

Here the strings *“Black”* and *“Brown”* are compared.

First of all, the Unicode values of the first characters of both the strings are compared. Since the first characters are the same, their Unicode values are also the same. After that, the Unicode values of the second characters of both the strings are compared.

The Unicode value of *‘l’* is less than that of *‘r’*, and therefore the string “*Black*” is smaller than the string “*Brown*” lexicographically.

Since the string " *Black* " comes before " *Brown* " in the lexicographical order, `s1.compareTo(s2)` returned -1.

## Java String Operations

### Java Concatenation (+)

Two or more strings can be concatenated together using the `+` operator. We have already looked at examples of string concatenation before.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Codes";
        String s2 = "Dope";
        String s3 = s1 + s2;
        System.out.println(s3);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">CodesDope</pre>
    </details>
</div>

*s1* and *s2* are concatenated to form *s3*.

String concatenation can also be done using the `concat()` method.

### Java Comparison (==, !=)

Two strings can be compared using the `==` and `!=` operators.

Whenever two strings are compared, the Unicode values of their corresponding characters are compared. The character having the lower Unicode value is smaller.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Black";
        String s2 = "Black";
        System.out.println(s1 == s2);
        System.out.println(s1 != s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">true
false</pre>
    </details>
</div>

Since the values of the variables `s1` and `s2` are the same, `s1 == s2` returned true and `s1 != s2` returned false.

From the Unicode chart, we can see that the Unicode values of lowercase alphabets are smaller than the Unicode values of the uppercase alphabets. For example, the Unicode value of the character ‘*b*’ is smaller than that of the character ‘*B*’, and therefore these are not equal.

This is demonstrated in the following example.

```java
class Test {

    public static void main(String[] args) {
        String s1 = "Black";
        String s2 = "black";
        System.out.println(s1 == s2);
        System.out.println(s1 != s2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">false
true</pre>
    </details>
</div>

String concatenation can also be done using the `compareTo()` method.

### Difference between equals() method and ==

There is often confusion between choosing `equals()` and `==` to compare two strings. Let’s find out which one to use in which scenarios.

Whenever we create a new object, it is allocated some location in the memory. For example, if we write

`String s1 = new String("Welcome");`

Here, object `s1` is created and given some location in the memory. Its value is assigned as "Welcome".

When we create another object `s2`, it is also given some location in the memory (since it is also a new object). Its value is also assigned as "Welcome".

`String s2 = new String("Welcome");`

Thus, we have two objects with different memory locations and the same value "Welcome".

#### Java == operator compares two objects

```java
class Test {

    public static void main(String[] args) {
        String s1 = new String("Welcome");
        String s2 = new String("Welcome");
        if (s1 == s2) System.out.println(
            "Both objects are equal"
        ); else System.out.println("Objects are different");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Objects are different</pre>
    </details>
</div>

Since `s1` and `s2` are different objects having different memory locations, therefore the condition `s1 == s2` is false.

Consider another example.

```java
class Test {

    public static void main(String[] args) {
        String s1 = new String("Welcome");
        String s2 = s1;
        if (s1 == s2) System.out.println(
            "Both objects are equal"
        ); else System.out.println("Objects are different");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Both objects are equal</pre>
    </details>
</div>

In the above example, the object `s2` is created and assigned the same memory location as that of `s1`. So, the two objects are the same in this case.

#### Java equals() method

It compares the contents of two objects.

```java
class Test {

    public static void main(String[] args) {
        String s1 = new String("Welcome");
        String s2 = new String("Welcome");
        if (s1.equals(s2)) System.out.println(
            "Values of both objects are equal"
        ); else System.out.println("Values of both objects are not equal");
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Values of both objects are equal</pre>
    </details>
</div>

Though both the objects are different, because their values are the same, so the condition (`s1.equals(s2)`) is true.

With this, you just finished the first part of Java programming. So give yourself a pat and have a cup of coffee because you have achieved a milestone in programming. Believe us!

> Don’t Let Yesterday Take Up Too Much Of Today.
>
> \- Will Rogers


<a href="17-java-object-oriented-programming.md" class="next">Next</a>
