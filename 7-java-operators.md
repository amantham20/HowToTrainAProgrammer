# Java Operators
***
Do you know we can perform mathematical operations like addition, subtraction, multiplication, etc. in Java also? Yes, in this chapter, we will be looking at how we can perform different operations in Java.

In Maths, we add two numbers using the **+** symbol. In Java, such symbols are known as **operators**. For example, the + operator is used for doing addition and the *** operator is used for doing multiplication.

Java provides a rich set of built-in operators which can be categorized as follows.
*   Arithmetic Operators
*   Relational Operators
*   Logical Operators
*   Assignment Operators
*   Increment and Decrement Operators

***
## Java Arithmetic Operators
Arithmetic Operators are used to perform arithmetic operations. They take numerical values as their operands and return a single numerical value as result.

Let's take two variables `a` and `b` having values 3 and 2 respectively.

| Operator | Description                                                | Example          |
| :------- | :--------------------------------------------------------- | :--------------- |
| +        | Adds operands                                              | a + b = 5        |
| -        | Subtracts right operand from left operand                  | a - b = 1        |
| *        | Multiplies both operands                                   | a * b = 6        |
| /        | Quotient of division of left operand by right operand      | a / b = 1.5      |
| %        | Remainder of division of left operand by right operand    | a % b = 1        |

```java
class Test {

    public static void main(String[] args) {
        int a = 9, b = 2;
        System.out.println("a + b = " + (a + b));
        System.out.println("a - b = " + (a - b));
        System.out.println("a * b = " + (a * b));
        System.out.println("a / b = " + (a / b));
        System.out.println("a % b = " + (a % b));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">a + b = 11
a - b = 7
a * b = 18
a / b = 4
a % b = 1</pre>
    </details>
</div>

In the above example, the variables `a` and `b` are assigned the values 9 and 2 respectively. Now look at the following statement in the example.

`System.out.println("a + b = " + (a + b));`

Here, `a + b =` got printed as it is because it is a string enclosed within `" "`. After that, the expression (a + b) got evaluated and its value (9 + 2 = 11) got printed. Similarly, other statements also got executed.

We can also use a third variable to store the result of an operation as done in the following example.

```java
class Test {

    public static void main(String[] args) {
        int a = 9, b = 2; // declaring variables a and b
        int c = a + b; // storing sum of a and b in c
        System.out.println("a + b = " + c);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">a + b = 11</pre>
    </details>
</div>

When an integer is divided by another integer, the answer is rounded off to the nearest lower integer.

When we divide an integer by another integer, the result is rounded off to the lower integer. For example, 3/2 returns 1 instead of 1.5, and ⅔ returns 0 instead of 0.67.

If at least one of the numerator or denominator has decimal, then the result is the actual answer having decimal. For example, all 3/2.0, 3.0/2 and 3.0/2.0 return 1.5.

This is shown in the following example.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("3 / 2     = " + (3 / 2));
        System.out.println("3 / 2.0   = " + (3 / 2.0));
        System.out.println("3.0 / 2   = " + (3.0 / 2));
        System.out.println("3.0 / 2.0 = " + (3.0 / 2.0));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">3 / 2 = 1
3 / 2.0 = 1.5
3.0 / 2 = 1.5
3.0 / 2.0 = 1.5</pre>
    </details>
</div>

Now imagine a case where you are using two integer variables in your program and at some point of time you are dividing one variable from another. Since both variables store integers, you will get a rounded off integer output. If you still want to get the actual result of division including decimal point, then that can be achieved by type casting either the numerator or the denominator.

```java
class Test {

    public static void main(String[] args) {
        int x = 10, y = 3;

        System.out.println(x / y);
        System.out.println((double) x / y);
        System.out.println(x / (double) y);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">3
3.3333333333333335
3.3333333333333335</pre>
    </details>
</div>

In this example, `x / y` returned the rounded off result 3 because both are integers. On writing `(double)x / y`, the numerator `x` got converted into a double and thus the division of a double by an integer returned the actual quotient. Similarly, `x / (double)y` first converted the denominator `y` into a double and then the division of an integer by a double returned the actual quotient.

***
## Java Relational Operators
Relational Operators check the relationship between two operands. They return `true` if the relationship is true and `false` if it is false.

The relational operators in Java are listed below.

Again, take two variables `a` and `b` having values 3 and 2 respectively.

| Operator | Description                 | Example              |
| :------- | :-------------------------- | :------------------- |
| ==       | Equal to                    | (a == b) is false    |
| !=       | Not equal to                | (a != b) is true     |
| \>       | Greater than                | (a > b) is true      |
| <        | Less than                   | (a < b) is false     |
| >=       | Greater than or equal to    | (a >= b) is true     |
| <=       | Less than or equal to       | (a <= b) is false     |

Let's look at an example to see the use of these.

```java
class Test{

    public static void main(String[] args){
        int a = 10, b = 25;
    
        System.out.println("a == b = " + (a == b));
        System.out.println("a != b = " + (a != b));
        System.out.println("a > b = " + (a > b));
        System.out.println("a < b = " + (a < b));
        System.out.println("b >= a = " + (b >= a));
        System.out.println("b <= a = " + (b <= a));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">a == b = false
a != b = true
a > b = false
a < b = true
b >= a = true
b <= a = false</pre>
    </details>
</div>

In this example, the value of `a` is not equal to that of `b`, therefore `(a == b)` (equal to) returned false and `(a !=b)` (not equal to) returned true.

Also, the value of `a` is greater than that of `b`, therefore `(a > b)` (greater than) and `(a >= b)` (greater than or equal to) returned true whereas `(a < b)` (less than) and `(a <= b)` (less than or equal to) returned false.

### Difference Between = and ==
We know about `=` as well as `==`. They might seem similar but are completely different. `=` is called the **assignment operator** and `==` is called the **equality operator**.

`=` assigns values from its right operand to its left operand whereas `==` compares the values of both its operands.

```java
class Test {

    public static void main(String[] args) {
        int a = 10;
        System.out.println(a == 10);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">true</pre>
    </details>
</div>

In this example, `a = 10` assigns 10 to the variable `a`, whereas `a == 10` checks if the value of `a` is equal to 10.

```java
class Test {

    public static void main(String[] args) {
        int a = 10, b = 10;
        System.out.println("Are a and b equal?" + (a == b));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Are a and b equal? true</pre>
    </details>
</div>

In this example, we assigned the value 10 to the variables `a` and `b` by writing `a = 10` and `b = 10` respectively. Then we checked if the values of `a` and `b` are equal by writing `a == b`.

<img alt="Difference in = and == in Java" src="https://web.archive.org/web/20220811215131im_/https://www.codesdope.com/pa-images-bucket/courses/java/o2.png" style="max-width:60%;height:auto;"/>

***
## Java Logical Operators
Logical Operators are used to check if an expression is true or false.

In English, if we say “*Summer is a season **and** Winter is a season*”, then this statement is true because both the sub-statements “*Summer is a season*" and "*Winter is a season*” are true. However, if we say “*Summer is a season **and** Winter is not a season*”, then this statement is false because one of the sub- statements “*Winter is not a season*” is false. Therefore, the statement is true only if the sub-statements on both sides of **and** are true.

The `&&` operator in Java is similar to *and* in English. In Java, the `&&` operator returns true if both its operands are true. In all other cases, it returns false. For example, the expression *(2 > 3) && (6 > 5)* is false because one of the operands *(2 > 3)* is false.

Again, in English, if we say “*Summer is a season **or** Winter is a season*”, then this statement is true because at least one of the sub-statements out of “*Summer is a season*" and "*Winter is a season*” is true. Hence, the statement “*Summer is a season **or** Winter is not a season*” is also true because one of the sub-statements “*Summer is a season*” is true.

Similar to or in English, we have the `||` operator in Java which returns true if atleast one of its operands is true. In all other cases, it returns false. For example, the expression (`2 > 3) || (6 > 5)` is true because one of the operands `(6 > 5)` is true.

In English,

A and B - Both A and B.

A or B - Either A or B.

In programming also,

A && B - Both A and B.

A || B - Either A or B or both.

Now let’s look at the three logical operators in Java. Assume the values of two variables `a` and `b` as true and false respectively.

| Operator | Description                                                                                                                                                                                                                                                        | Example           |
| :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :---------------- |
| &&       | Logical AND. It returns true if both the operands are true. Otherwise, it returns false.                                                                                                                                                                         | (a && b) is false  |
| \|\|     | Logical OR. It returns true if either one or both the operands are true. Otherwise, it returns false.                                                                                                                                                           | (a \|\| b) is true |
| !        | Logical NOT. It is used to reverse a condition. So, if a condition is true, ! makes it false and vice versa.                                                                                                                                                     | !a is false, !b true |

```java
class Test{

    public static void main(String[] args){
        // both operands true
        System.out.println((2 < 3) && (5 < 6)); // prints true
        System.out.println((2 < 3) || (5 < 6)); // prints true
    
        // one operand true
        System.out.println((2 < 3) && (5 > 6)); // prints false
        System.out.println((2 < 3) || (5 > 6)); // prints true
    
        // both operands false
        System.out.println((2 > 3) && (5 > 6)); // prints false
        System.out.println((2 > 3) || (5 > 6)); // prints false
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">true
true
false
true
false
false</pre>
    </details>
</div>

In the above example, `(2 < 3)` is true and `(5 < 6)` is also true, thus `(2 < 3) && (5 < 6)` returns true and `(2 < 3) || (5 < 6)` also returns true.

`(2 < 3)` is true but `(5 > 6)` is false, thus `(2 < 3) && (5 > 6)` returns false and `(2 < 3) || (5 > 6)` returns true.

Both `(2 > 3) and (5 > 6)` are false, thus `(2 > 3) && (5 > 6)` returns false and `(2 > 3) || (5 > 6)` also returns false.

Look at another example.

```java
class Test{

    public static void main(String[] args){
        int a = 5, b = 10;
  	
        System.out.println(a > b); // prints false
        System.out.println(!(a > b)); // prints true
        System.out.println((a == b) && (a == 5)); // prints false
        System.out.println((a != b) && (a == 5)); // prints true
        System.out.println(!((a != b) && (a == 5))); // prints false
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">false
true
false
true
false</pre>
    </details>
</div>

You must have understood the program. The `!` operator reverses the condition, and thus `!(a > b)` returns true. Similarly, all the other expressions are evaluated.

***
## Java Assignment Operators
Assignment Operators are used to assign values of the right operands to the left operands.

= is also an assignment operator. Look at the following statement.

`num = 10;`

In this statement, 10 (right operand) is assigned to the variable num (left operand).
Now look at another statement.

`num = num + 1;`

This statement is different from what we do in normal Mathematics. Suppose the value of `num` before the above statement is 10. So in the above statement, the right operand `num + 1` gets evaluated to 11 (= 10 + 1) first and then gets assigned to the left operand `num`, making **num = 11**. Hence, the final value of `num` becomes equal to 11.

This is because in Java each operator has an order precedence. And the precedence of `+` operator is higher than that of `=` operator. So, `num+1` will be evaluated first making the statement - `num = 11` and then the value of the `num` will be changed to 11.

Before looking at other assignment operators, see this example:

```java
class Test {

    public static void main(String[] args) {
        int a = 10;
        System.out.println(a);

        a = a + 2;
        System.out.println(a);

        a = a * 2;
        System.out.println(a);

        a = a - 2;
        System.out.println(a);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10
12
24
22</pre>
    </details>
</div>

`int a = 10` → 10 is assigned to the variable `a`

`a = a + 2` → Remember we discussed that `=` assigns the value of the right operand to the left operand? The right operand `a + 2` gets evaluated to 12 because the current value of `a` is 10 and then the `=` operator assigns 12 (right operand) to the variable `a` (left operand), making **a = 12**.

`a = a * 2` → The right operand gets evaluated to 24 because the current value of `a` is 12. Then the `=` operator assigns 24 (right operand) to `a` (left operand), making **a = 24**.

`a = a - 2` → The right operand gets evaluated to 22 because the current value of `a` is 24, and then the `=` operator assigns 22 (right operand) to `a` (left operand), making **a = 22**.

The list of all assignment operators is given below.

| Operator | Description                                                                                                                                                                | Example                |
| :------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :--------------------- |
| =        | Assigns value of right operand to left operand                                                                                                                             | C = A + B              |
| +=       | Adds the value of right operand to left operand and assigns the final value to the left operand                                                                           | C += A is same as C = C + A |
| -=       | Subtracts the value of right operand from left operand and assigns the final value to left operand                                                                        | C -= A is same as C = C - A |
| *=       | Multiplies the value of right operand to left operand and assigns the final value to left operand                                                                         | C *= A is same as C = C * A |
| /=       | Divides the value of left operand by right operand and assigns the quotient to left operand                                                                               | C /= A is same as C = C / A |
| %=       | Divides the value of left operand by right operand and assigns the remainder to left operand                                                                             | C %= A is same as C = C % A |

Suppose the value of an integer variable `num` is 5. Then the expression `num += 1` is equivalent to the expression `num = num + 1`, making the value of `num` as 6.

Let’s write the last example using different assignment operators.

```java
class Test {

    public static void main(String[] args) {
        int a = 10;
        System.out.println(a);

        a += 2; // equivalent to a = a+2
        System.out.println(a);

        a *= 2; // equivalent to a = a*2
        System.out.println(a);

        a -= 2; // equivalent to a = a-2
        System.out.println(a);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10
12
24
22</pre>
    </details>
</div>

Here, `a += 2` is evaluated as `a = a + 2`, `a *= 2` is evaluated as `a = a * 2` and `a -= 2` is evaluated as `a = a - 2`.

We cannot assign any value to a constant. For example, 4 = num will give an error.

Writing *4 = num* will try to make 4 equal to the value *num*, but that is not possible.

***
## Java Increment and Decrement Operators
`++` and `--` are called increment and decrement operators respectively.

`++` adds 1 to the operand whereas `--` subtracts 1 from the operand.

**a++** increases the value of a variable a by 1 and **a--** decreases the value of a by 1.

Similarly, **++a** increases the value of a by 1 and **--a** decreases the value of a by 1.

In **a++** and **a--**, ++ and -- are used as **postfix** whereas in **++a** and **--a**, ++ and -- are used as **prefix**.

For example, suppose the value of a is 5, then *a++* and *++a* will change the value of a to 6. Similarly *a--* and *--a* will change the value of *a* to 4.

### Difference between Prefix and Postfix operators
While both a++ and ++a increases the value of a, the only difference between these is that a++ returns the value of a before the value of a is incremented and ++a first increases the value of a by 1 and then returns the incremented value of a.

Similarly, a-- first returns the value of a and then decreases its value by 1 and --a first decreases the value of a by 1 and then returns the decreased value.

An example will make the difference clear.

```java
class Test {

    public static void main(String[] args) {
        int a = 10, b = 10, c = 10, d = 10;

        System.out.println("value of a++ = " + (a++));
        System.out.println("a = " + a);
        System.out.println("value of ++b = " + (++b));
        System.out.println("value of c-- = " + (c--));
        System.out.println("value of --d = " + (--d));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">value of a++ = 10
a = 11
value of ++b = 11
value of c-- = 10
value of --d = 9</pre>
    </details>
</div>

`System.out.println("value of a++ = " + (a++))` → The initial value of the variable `a` is 10. On printing `a++`, first the value of `a`, i.e. 10, gets printed and after that it is incremented by 1 making **a = 11**.

`System.out.println("a = "+ a)` → The value of `a`, i.e. 11, gets printed.

`System.out.println("value of ++b = " + (++b))` → The initial value of the variable `b` is 10. On printing `++b`, the value of `b` is first incremented by 1 making **b = 11** and after that it is printed.

Similarly, the other values are printed.

***
## Precedence of Operators in Java
Consider an expression 2 * 5 + 6, which contains more than one operator. This expression can be evaluated by first doing multiplication and then addition, or by first doing addition and then multiplication. In Maths, the BODMAS rule is applied to evaluate expression. However, expressions with more than one operator don’t use BODMAS and are evaluated in Java in a different way.

In Java, **expressions inside parentheses ( )** are evaluated first. After that, precedence order of the operators mentioned in the following table is followed, with the operator at the top having the highest precedence and that at the bottom having the least precedence.

| Operator                | Associativity   |
| :---------------------- | :-------------- |
| ++ -- !                 | Right to left   |
| * / %                   | Left to right   |
| + -                     | Left to right   |
| \>  >=  <  <=           | Left to right   |
| == !=                   | Left to right   |
| &&                      | Left to right   |
| \|\|                    | Left to right   |
| = += -= *= /= %=        | Right to left   |

Again consider the equation

x = 2 * 5 + 6

From the table, we can see that the priority of the `*` operator is greater than that of the `+` operator, therefore first 2 will get multiplied with 5 and after that the product will get added to 6, making the value of the expression on the right side equal to 16. This will make the equation as follows.

x = 16

At last, the `=` operator will assign 16 to the variable `x`.

Did you notice that the equation `x = 2 * 5 + 6` has three operators - `*`, `+` and `=`? Among them, the priority of * is the highest and so `2 * 5` will get evaluated first, and the priority of `=` is the least and so x = 16 will get evaluated at the last.

In the above example, all the operators have different precedence. Suppose we have an expression which has two operators having the same precedence. In that case, if the associativity of the operators is from left to right, then the operator written left in the expression is evaluated first, and if the associativity is from right to left, then the operator written right in the expression is evaluated first first.

Let’s understand this by evaluating the following expression.

10 / 2 - 4 * 5 + 6

The priorities of / and * are greater than those of - and +, and so / and * will be evaluated first. But / and * have the same priority, so which among them will get evaluated first?

Since / and * have association from left to right, so first / will get evaluated and after that * will get evaluated, because in the expression, / is written at the left and * at the right. Evaluation of / will result in the following expression.

5 - 4 * 5 + 6

After this, * will get evaluated further simplifying the expression as follows.

5 - 20 + 6

Now, again - and + have the same priority. Since their associativity is from left to right, so first - will get evaluated because it is written at the left in the expression, resulting in the following expression.

-15 + 6

Finally, -15 and 6 are added to result in -9.

If you don't want to remember these rules, then just put the expression you want to execute first in brackets. E.g.- If you want to divide the product of (2+2) and 444 by the quotient of (999/5), then write the expression as - ((2+2)*444)/(999/5). This will get evaluated as (4*444)/(999/5) and finally get simplified to 1776/199 (because 999/5 is 199 and not 199.8).

We discussed the different types of operators in this chapter. It is important that you keep practicing questions before starting a new chapter so that you have a good command over all the concepts you have learnt before starting it.

> Whatever you are, be a good one.
>
> - Abraham Lincoln

***
