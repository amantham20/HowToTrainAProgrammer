# Java Method Overloading
<hr/>
We have already seen how to define our own methods. Do you know we can also define multiple methods with the same name? Yes, that is possible. In Java, we can define more than one method with the same name. This feature is called **method overloading**.

Before learning about method overloading, let’s first understand how method overloading can be useful.
<hr/>
### Why Method Overloading?
Let’s take a very simple example. Suppose you want to find the area of some rectangles and squares. For that, you want to define a method that would take the dimensions of a rectangle or a square as arguments and calculate and return the area of the rectangle or the square.

Now, for calculating the area of a rectangle, we need to pass two arguments - length and breadth. Whereas, to calculate the area of a square, only one argument has to be passed - side of the square.

One way to accomplish this task is to create a different method for the area of a rectangle that would take two parameters and a different method for the area of a square that would take one parameter as shown below.

```java
// for area of rectangle
public static double getArea1(double length, double breadth) {
    return length*breadth;
}

// for area of square
public static double getArea2(double side) {  
    return side*side;
}
```

In this case, different methods are defined for different shapes. As a result, you will have to remember the names of different methods before calling them to return the area. For example, you have to call the method named `getArea1()` for a rectangle and the method named `getArea2()` for a square.

A better solution is to use method overloading, by creating both these methods with the same name as shown below.

```java
// for area of rectangle
public static double getArea(double length, double breadth) {
    return length*breadth;
}

// for area of square
public static double getArea(double side) {  
    return side*side;
}
```

Here, you will always call the method `printArea()` to print the area of a rectangle or a square. For example, to get the area of a rectangle having length 10 and breadth 5, you can call `getArea(10, 5)`. Similarly, to get the area of a square having each side 5, you can simply call `getArea(5)`.

In this way, the complexity of the code got reduced because we now no longer need to call different methods to get the area of different shapes. Whenever we need to get the area of a shape, we can just call the method `printArea()`.

Thus, method overloading is a feature that allows us to define multiple methods with the same name, provided their parameters are different. Let’s discuss more on this in this chapter.
<hr/>
## Method Overloading
Conditions for method overloading are -

1.  Methods must have the same name
2.  Methods must have different parameters (either different number of parameters or different types of parameters)

Hence, two or more methods are said to be overloaded if they have the same name and either different number of parameters or parameters having different data types.

The following example shows method overloading.

```java
class Test {

    public static void printArea(int x, int y) {
        System.out.println(x * y);
    }

    public static void printArea(int x) {
        System.out.println(x * x);
    }

    public static void printArea(int x, double y) {
        System.out.println(x * y);
    }

    public static void printArea(double x) {
        System.out.println(x * x);
    }

    public static void main(String[] args) {
        printArea(2, 4);
        printArea(2, 5.1);
        printArea(10);
        printArea(2.3);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">8
10.2
100
5.289999999999999</pre>
    </details>
</div>

Here, we defined four methods with the same name `printArea` but different parameters.

In the main method, the first statement calls the method `printArea()` with arguments 2 and 4. Since both 2 and 4 are integers, the method `printArea()` with both its parameters of type int `(int x, int y)` gets called.

The second statement calls the method with arguments 2 and 5.1. Since 2 is of type int and 5.1 is of type double, the method with the first parameter of type *int* and the second parameter of type *double* `(int x, double y)` gets called.

Similarly, the third statement calls the method having one parameter of type *int* and the fourth statement calls the method having one parameter of type *double*.

This is **method overloading**.

So, for method overloading, we need to create methods with the same name by changing either the number of parameters or the data types of the parameters. That’s it.

Hence, method overloading can help us reduce the complexity and increase the readability of the code. 

> No amount of money ever bought a second of time.
>
> \- Tony Stark

<hr/>
