# Java Data Types

We know that 2 is an integer, ‘<i>a</i>’ is a character and “<i>Let’s learn Java</i>” is a sentence. All these values require different amounts of space in the memory. For example, the space required to store an integer is different from that required to store a character.

In all the examples in the previous chapter, the variables were declared of type int and thus can store only integer values. However, we can also declare variables which can store a character, a sentence or other types of values.

Variables can be of different types depending on the type of data it can store. A variable which stores an integer value is of type `int`. Similarly, a variable which stores a character value is of type `char`.

We specify the type of a variable at the time of its declaration. For example, a character variable is declared as shown below.

`char ch;`

In the above declaration, `ch` is the name of a variable which is of type `char` i.e., it can store only character values.

Most commonly used data types in Java are **int** (integer), **char** (character), **float** (number having decimal), **double** (number having decimal), **String** (collection of characters) and **boolean** (true or false).

Let’s look at these data types.

## Data Types in Java

### int

The *int* data type is used to store integers. Integers are numbers which don’t have decimal. For example, -5, 0, 6, etc.

```java
class Test {

    public static void main(String[] args) {
        int num;
        num = 10;
        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

The variable `num` is declared of type int and is assigned an integer value 10.

### double

The *double* data type is used to store double-precision 64-bit floating point numbers. Floating point numbers are numbers which have decimal. In other words, the  double data type is used to store numbers having decimal. For example, -5.64, 10.228, etc.

```java
class Test {

    public static void main(String[] args) {
        double num;
        num = 10.5;
        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10.5</pre>
    </details>
</div>

The variable `num` is declared of type double and is assigned a floating point value 10.5.

Note that 8 is an int but 8.0 is a double.

### float

The float data type is used to store single-precision 32-bit floating point numbers. A float value should always end with `f` or `F`. For example, -5.64f, 10.228F, etc.

```java
class Test {

    public static void main(String[] args) {
        float num;
        num = 10.5f;
        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10.5</pre>
    </details>
</div>

In this example, we assigned the value 10.5f and not 10.5 to the variable `num` because 10.5 is a *double*. To tell the compiler to consider 10.5 as a *float*, we assigned 10.5f to the variable.

### char

The *char* data type is used to store a character. A character value must be written within single quotes `' '`. For example, ‘a’, ‘B’, ‘@’, etc.

```java
class Test {

    public static void main(String[] args) {
        char ch;
        ch = 'e';
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

Here, `ch` is the name of a variable of type *char* which is assigned a character value 'e'.

### String

The *String* data type is used to store a string. A string is a sequence of characters. For example, “Hello” is a string having characters ‘H’, ‘e’, ‘l’, ‘l’ and ‘o’.

A string value must be enclosed within double quotes `" "`. In fact, any value enclosed within double quotes `" "` is a string. Some examples of string are “Hello World”, “Hello123”, "123" and “Name: John”.

```java
class Test {

    public static void main(String[] args) {
        String msg;
        msg = "Let's learn Java";
        System.out.println(msg);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Let's learn Java</pre>
    </details>
</div>

In this example, the variable `msg` is declared of type String and is assigned the string "Let's learn Java".

As we know that any value enclosed within double quotes “ “ is a string, so values like “10” and “10+2” are also strings.

Note that 10 is an int but “10” is a String.

Look at the following example.

```java
class Test {

    public static void main(String[] args) {
        int a = 10 + 2;
        String b = "10 + 2";
        System.out.println(a);
        System.out.println(b);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">12
10 + 2</pre>
    </details>
</div>

In the above example, the integer variable `a` is assigned the expression `10 + 2`. This expression first gets evaluated to 12 and then 12 is assigned to `a`. On the other hand, the string variable `b` is assigned the string `"10 + 2"`.

We will learn more about String later in the topic [Strings](https://web.archive.org/web/20220811212956/https://www.codesdope.com/course/java-strings/).

### boolean

The *boolean* data type consists of two values - `true` and `false`.

```java
class Test {

    public static void main(String[] args) {
        boolean a, b;
        a = true;
        b = false;
        System.out.println(a);
        System.out.println(b);
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

The variables `a` and `b` are declared of type boolean and are assigned the values `true` and `false` respectively.

So these were all the basic data types. Now, let’s look at the range of values that different data types can take.

The following table states different data types along with the maximum and minimum value they can take.

| Data Type | Maximum Value | Minimum Value |
| --------- | ------------- | ------------- |
| int |  2,147,483,647  | - 2,147,483,648 |
| float | 3.4028235E38 | 1.4E-45 |
| double | 1.7976931348623157E308 | 4.9E-324 |
| char | 65,535 | 0 |
| short | 32767 | -32767 |
| long | 9223372036854775807 | -9223372036854775808 |

10E5 means 10<sup>5</sup> i.e. 100000.

Let's see an example of double, char and boolean values.

```java
class Test {

    public static void main(String[] args) {
        double b = 123.43555;
        char c = 'e';
        boolean d = true;
        System.out.println("Double: " + b);
        System.out.println("Character: " + c);
        System.out.println("Boolean: " + d);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Double: 123.43555
Character: e
Boolean: true</pre>
    </details>
</div>

You must have understood the code. While printing, + joined a string and the value of a variable in each  `System.out.println()` method.

In the first `System.out.println()` method, the string "Double: " and the value of `b` (because `b` is not inside `" "`) are combined and printed.

Look at another example.

```java
class Test {

    public static void main(String[] args) {
        int x = 1, y = 5;
        System.out.println("x");
        System.out.println("y");
        System.out.println("x" + "y");
        System.out.println(x);
        System.out.println(y);
        System.out.println(x + y);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">x
y
xy
1
5
6</pre>
    </details>
</div>

Here, whatever is written within `" "` got printed as it is, without getting evaluated. Whatever is not inside `" "` got evaluated first and then their values got printed. For example, `"x"+"y"` got printed as xy (without evaluation) but `x+y` got evaluated first as **1+5** i.e., **6** and then **6** got printed.

## Primitive and Non-Primitive Data types

Using data types is so easy, isn't it?

All the data types are broadly classified into primitive and non-primitive.

### Primitive Data type

**Primitive data types** are predefined (already defined) data types in Java.

There are eight predefined data types in Java, which are

**int**,   **float**,   **double**,   **short**,   **long**,   **char**,   **boolean**,   **byte**

### Non-Primitive Data type

**Non-primitive data types** are defined by the programmer. Some examples of non-primitive data types are Array, Class and Interface.

At present, there is no need to go into the details of non-primitive data types as we will learn about them later.

## Type Casting

Suppose we are writing a program and we have an integer variable having a value 10 (an integer) and at some point of time we want it to be a string i.e., “10”. Or a more practical case would  be to convert a double (10.2) to an integer (10). We can easily do so in Java using type casting.

**Type Casting** is the conversion of a value from one data type to another data type. For example, we can convert a double value to an int value or a char value to an int value.

Type Conversions are of two types - implicit and explicit.

### Implicit Conversion

Suppose we are adding two numbers. The first number is of type *int* and the second number is of type *double*. We cannot add an *int* and a *double* because both the numbers have to be of the same data type i.e. either both are *int* or both are *double*. Since *double* is a larger data type than *int*, therefore while adding, the *int* variable automatically gets converted into *double* and then both the *double* variables add up.

Order of size of data types:
double > float > long > int > char > short

From the above order, we can see that *double* is the largest data type and *short* is the smallest data type. Any smaller data type gets implicitly converted into a larger data type when performing arithmetic operations or in any such other expression.

For example, when adding a value of type *int* and a value of type *long*, the value of type *int* gets automatically converted to *long* and then both the values get added.

Similarly, a *char* variable gets converted into an int while performing some arithmetic operation.

```java
class Test {

    public static void main(String[] args) {
        int n = 10;
        char ch = 'h';
        int sum = n + ch;
        System.out.println(sum);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">114</pre>
    </details>
</div>

In the above program, when the variables `n` and `ch` are added, the integer value (ASCII value) of `ch` i.e. 104 is added to the value of `n` to produce a sum of 114. Note that every character has an ASCII value. You can get the ASCII chart from [here](https://web.archive.org/web/20220811212956/https://www.codesdope.com/media/pdf/ASCII.pdf).

### Explicit Conversion

We know that a smaller data type can be implicitly converted to a larger data type. But what if we want to convert a larger data type to a smaller data type?

We can also convert values from one data type to another as shown below:

`( data-type ) expression;`

For example, a *double* value 10.5 can be converted to *int* as shown below.

`(int)10.5;`

Consider an example.

```java
class D3 {

    public static void main(String[] args) {
        int sum = 23;
        int n = 7;
        double avg;
        avg = (double) sum / n;
        System.out.println("Average = " + avg);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Average = 3.2857142857142856</pre>
    </details>
</div>

In this example, since the variable `avg` is declared of type double, we are converting `sum/n` to type double by writing `(double)sum/n` (since **int**/ **int** gives **int** in Java).

You will understand many concepts only by practicing. So, solve questions from the [practice section](https://web.archive.org/web/20220811212956/http://codesdope.com/practice/).

> Everything you can imagine is real.
>
> \- Pablo Picasso


<!-- Next Chapter -->
<a href="06-java-input.md">Next Chapter</a>