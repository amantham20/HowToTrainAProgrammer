# Java Methods
***
Methods are used to perform specific tasks. Java provides some methods which we can use to perform different tasks. For example, The println from System.out (`System.out.println()`) which we have been using is a method which is used to print something.

Do you know we can also create our own methods? Yes, we can create our own methods for performing different tasks like returning the sum of two numbers, checking if a number is positive or negative, etc.

## Why Do We Need Methods?
Method is a set of statements written together and given a name. We can call that set of statements at any place in our program by just calling its name and without writing the whole set of statements again.

![method in Java](https://web.archive.org/web/20220412013007im_/https://www.codesdope.com/pa-images-bucket/courses/java/f1.jpg)

Suppose we need to check whether a number is even or not multiple times in our program. Instead of writing the same logic again and again, we can write a method and call it whenever we need to check if a number is even or not.

So let’s see how to define and use a method.
## Defining Methods in Java
Let's start by first looking at the `main` method, which we have defined in all our programs.

`public static void main(String[] args)` - 
When we run a Java program, the main method is executed first. So to execute a program in Java, there must be a main method.

Here, `public` is a **modifier**. You will learn about modifiers in a later chapter.

`static` means we can access this method without making any object of the class (classes and objects will also be taught later).

For now, just keep in mind that we are going to use this structure i.e., we will write public static ... to make our own method. You will learn the exact significance of public and static in later chapters.

`void` means that the method does `not return` anything. For the first few examples, we will use void and we will learn about returning something from a method later in this chapter itself.

Now let’s define a simple method which will help you understand all that we have discussed above.
```java
class Test {

    // method definition
    public static void sum() {
        System.out.println("This is a method");
        System.out.println(5 + 6);
    }

    public static void main(String[] args) {
        // method calling
        sum();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is a method
11</pre>
    </details>
</div>

We defined a method named `sum`. We can give any name to a method.
The **body of the method** consists of the statements `System.out.println("This is a method")` and `System.out.println(5 + 6)`.
Inside the `main` method, we called the method by writing `sum()`. When the method was called, its body got executed, printing *This is a method* and the value of *5 + 6*, i.e. 11.

Note that we defined the method `sum()` as `public`, `static` and `void`. As said earlier, these will be discussed later. (Keep in mind that because the `main` method is `static`, so to call our method from the `main` method, our method must also be `static`.)

> A static method can call only those methods that are static and can’t call methods that are not static. Therefore, since the main method is always declared as static, it can call only static methods.

Now let’s call this method more than once.
```java
class Test {

    // method definition
    public static void sum() {
        System.out.println("This is a method");
        System.out.println(5 + 6);
    }

    public static void main(String[] args) {
        System.out.println("Calling method first time");
        // calling method
        sum();

        System.out.println("Calling method second time");
        // calling method
        sum();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Calling method first time
This is a method
11
Calling method second time
This is a method
11</pre>
    </details>
</div>

Here, we called the method `sum()` two times inside the `main` method.

So, by now you must have understood how to define and call a method in Java.

We can also pass values to a method. Think of a situation where you want to get the area of a rectangle printed on the screen and you want to do it many times for different rectangles. Writing the same code again and again will do the job but there is an easier solution.
```java
class Test {

    // method definition
    public static void printArea(int x, int y) {
        System.out.println(x * y);
    }

    public static void main(String[] args) {
        printArea(2, 4);
        printArea(4, 8);
        printArea(100, 23);
        printArea(1221, 32);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">8
32
2300
39072</pre>
    </details>
</div>

`printArea(int x, int y)` → We defined a method named `printArea`. We also defined two parameters `x` and `y` of type `int`. This means that whenever we call this method, we have to pass two integers to it.

Inside the main method, the first statement is `printArea(2, 4`. This statement calls the `printArea()` method by passing two integers 2 and 4. Whenever a value is passed to a method, the respective parameter takes that value. In this case, the parameters `x` and `y` take the values 2 and 4 respectively. So, we have *x = 2* and *y = 4*.

Similarly, when the second statement `printArea(4, 8)` calls the method, the parameters `x` and `y` take the values 4 and 8 respectively.

In this way, we are able to display the areas of different rectangles by calling the same method by passing different values of length and breadth.

## Java Parameters and Arguments
Parameters are the variables we use in the method definition whereas arguments are the values we pass in the method call. These two terms are often used interchangeably.

![parameters and arguments in Java](https://web.archive.org/web/20220412013007im_/https://www.codesdope.com/pa-images-bucket/courses/java/p18.png)

Let’s again look at the previous example.
```java
class Test {

    // method definition
    public static void printArea(int x, int y) {
        System.out.println(x * y);
    }

    public static void main(String[] args) {
        // calling method
        printArea(2, 4);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">8</pre>
    </details>
</div>

Here, the variables `x` and `y` are the parameters and the values 2 and 4 passed in the method call are the arguments.

Look at another example.
```java
class Test {

    // method definition
    public static void printArea(int x, double y) {
        System.out.println(x * y);
    }

    public static void main(String[] args) {
        // calling method
        printArea(2, 4.5);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">9.0</pre>
    </details>
</div>

In this example, the parameter `x` is of type int and `y` is of type double. Thus, while calling the `printArea()` method, the first argument passed is of type int and the second argument of type *double*.

We can define any number of parameters in a method.

Let's look at one more example.
```java
class Test {

    public static void printSum(int x, int y) {
        System.out.println(x + y);
    }

    public static void main(String[] args) {
        printSum(2, 5);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">7</pre>
    </details>
</div>

As discussed in the beginning of this chapter, we can also define methods which return some value. Let’s see how.

## Java return
We can return something from a method using the `return` statement. Whenever a `return` statement is executed in a method, it terminates the method and returns some value to the place from where the method was called.

Let’s understand this through an example.
```java
class Test {

    // method definition
    public static int getArea(int x, int y) {
        int z = x * y;
        return z;
    }

    public static void main(String[] args) {
        // calling method
        int area = getArea(2, 4);
        System.out.println("Area: " + area);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Area: 8</pre>
    </details>
</div>

`getArea(int x, int y)` → The method `getArea()` takes two parameters `x` and `y` of type int.

`int getArea(int x, int y)` → Writing `int` before the method name means that the method returns an integer value. Thus, we will get some integer value whenever we call this method.

`return z` → This statement terminates the method and returns the value of `z`. Note that in this example, the value of `z` must be an integer because we have declared the return type of the method as `int`. If it is not an integer, then we will get an error on running the program.

Now, `getArea(2, 4)` calls the method `getArea()` by passing 2 and 4. Thus, the value of the variable `z` becomes 8 (because x = 2 and y = 4) and `return z` returns the value 8. This returned value is assigned to the variable `area`.

![calling method in Java](https://web.archive.org/web/20220412013007im_/https://www.codesdope.com/pa-images-bucket/courses/java/p19.png)
```java
class Test {

    // method definition
    public static boolean isEven(int x) {
        if (x % 2 == 0) {
            return true;
        } else {
            return false;
        }
    }

    public static void main(String[] args) {
        int num = 4;
        System.out.println("Is number even? " + isEven(num));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Is number even? true</pre>
    </details>
</div>

Here, the method `isEven()` returns a `boolean` (true or false). Inside the method, if the condition `x%2 == 0` is true, then the method returns *true*, otherwise it returns *false*.

## Calling a Method Inside Another Method
Yes, a method can be called inside another method. We have been doing this already. In this chapter, we have called all our methods inside the `main` method.

Now look at an example in which there are two user-defined methods, and one of them is called inside another.
```java
class Test {

    // method div_2() definition
    public static int div_2(int a) {
        if (a % 2 == 0) {
            return 1;
        } else {
            return 0;
        }
    }

    // method div_6() definition
    public static void div_6(int b) {
        if (div_2(b) == 1 && b % 3 == 0) {
            System.out.println("Yes, the number is divisible by 6.");
        } else {
            System.out.println("No, the number is not divisible by 6.");
        }
    }

    public static void main(String[] args) {
        div_6(12);
        div_6(25);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Yes, the number is divisible by 6.
No, the number is not divisible by 6.</pre>
    </details>
</div>

For a number to be divisible by 6, it must be divisible by both 2 and 3.

In this example, the `div_2()` method checks if a number is divisibility by 2. The `div_6()` method calls `div_2()` inside itself to check the number's divisibility by both 2 and 3. Let's see how:

The `div_2()` method returns 1 if the number is divisible by 2, and returns 0 if not. Thus, in the div_6() method, the condition `div_2(b) == 1 && b % 3 == 0` of if will be true only if both the sub conditions `div_2(b) == 1` and `b % 3 == 0` are true. This means that this condition will be true if the number is divisible by both 2 and 3, or divisible by 6.

> If a variable is defined inside a method, then it is available only inside that method and not outside the method.
```java
class Test {

    public static int getSum(int x, int y) {
        return x + y;
    }

    public static int getProduct(int x, int y) {
        return x * y;
    }

    public static int getSumOfProduct(int x, int y, int a, int b) {
        int firstProduct = getProduct(x, y);
        int secondProduct = getProduct(a, b);
        int sumOfProduct = getSum(firstProduct, secondProduct);
        return sumOfProduct;
    }

    public static void main(String[] args) {
        System.out.println(getSumOfProduct(1, 2, 3, 4));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">14</pre>
    </details>
</div>

In this example, we are calling methods `getSum` and `getProduct` inside the method `getSumOfProduct`.

## Recursion
Recursion is the process of calling a method within the same method. Before going into its detail, let's learn some mathematics.

We will calculate the factorial of a number. Factorial of any number n is (n)*(n-1)*(n-2)*....*1 and written as (n!) and read as 'n factorial'. For example,

4! = 4*3*2*1 = 24

3! = 3*2*1 = 6

2! = 2*1 = 2

1! = 1

Also, 0! = 1

The following program calculates the factorial of a number.
```java
import java.util.Scanner;

class Test {

    // method definition
    public static int factorial(int a) {
        if (a == 0 || a == 1) {
            return 1;
        } else {
            return a * factorial(a - 1);
        }
    }

    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);

        System.out.println("Enter number");
        int n = s.nextInt();
        int fact = factorial(n);

        System.out.println("Factorial of " + n + " is " + fact);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter number
4
Factorial of 4 is 24</pre>
    </details>
</div>

Let's go through this code.
If we give 0 or 1, our method `factorial()` will return 1 because the values of both 0! and 1! are 1. It is straightforward up till here.

Now, if we pass 2 to our method, the following block of code gets executed.
```java
else {
    return a*factorial(a - 1)
}
```

`factorial(a - 1)` → When `a` is 2, `factorial(a - 1)` is factorial(1) and it will be equal to 1. (This is called recursion, the `factorial()` function is called inside itself). So, the result is 2*factorial(1) = 2*1 i.e. 2.

Therefore, the method will finally return 2.
 
Now let's see for 3:

a*factorial(a - 1)

3*factorial(2)

Then factorial(2) will be called and it will return **2*factorial(2-1)** i.e.,

**2*factorial(1)**:

3*2*factorial(1)

3*2*1

So, it will return 6.

For 4

4*factorial(3)

4*3*factorial(2)

4*3*2*factorial(1)

4*3*2*1
![recursion in Java](https://web.archive.org/web/20220412013007im_/https://www.codesdope.com/pa-images-bucket/courses/java/m5.png)

If you have understood this chapter, then pat yourself because many programmers find methods difficult to understand initially.

Now you can create methods to perform different tasks like checking if a number is even or odd, returning the factorial of a number, or for any other task. Since this is an important topic in programming, practice questions on methods in the [practice section.](https://web.archive.org/web/20220412013007/https://www.codesdope.com/practice/) 

> Nothing will work unless you do.
> - Maya Angelou
