# Java Constructor overloading
***
As we read in the [classes and objects](https://web.archive.org/web/20220811201850/https://www.codesdope.com/course/java-classes-and-objects/) topic, a constructor is just a method that doesn’t have a return type, has the same name as that of its class and is called implicitly at the time of object creation. As a result, all properties of methods are also shown by constructors.

We know that Java supports [method overloading](https://web.archive.org/web/20220811201850/https://stage.codesdope.com/course/java-method-overloading/) in which multiple methods with the same name but different parameters can be defined.

Similarly, it is also possible to define multiple constructors with the same name but different parameters. This is known as **constructor overloading**.

## Java Constructor Overloading
The one condition for constructor overloading is that constructors must have different parameters (either different number of parameters or different types of parameters).

Hence, two or more constructors are said to be overloaded if they have either a different number of parameters or parameters having different data types.

Let’s write a program that prints areas of rectangles.

```java
class Rectangle {

    private int length;
    private int breadth;

    public Rectangle(int side) {
        length = side;
        breadth = side;
    }

    public Rectangle(int l, int b) {
        length = l;
        breadth = b;
    }

    public int getArea() {
        return length * breadth;
    }
}

class Test {

    public static void main(String[] args) {
        Rectangle rect = new Rectangle(4, 5);
        Rectangle sq = new Rectangle(5);

        System.out.println(rect.getArea());
        System.out.println(sq.getArea());
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">20
25</pre>
    </details>
</div>

Here, we defined two constructors of the `Rectangle` class with different parameters.

In the main method,

`Rectangle rect = new Rectangle(4, 5)` → This statement creates an object named `rect` and calls the constructor having two parameters `(int l, int b)`. Inside the constructor, the attributes `length` and `breadth` of `rect` are assigned the values 4 and 5 respectively. Or, we can say that `rect` is a rectangle having length as 4 and breadth as 5.

`Rectangle sq = new Rectangle(5)` → This statement creates an object named `sq` and calls the constructor having one parameter `(int side)`. Inside the constructor, the attributes `length` and `breadth` of `sq` are assigned the same value i.e. 5. We can also say that `sq` is a rectangle having both length and breadth as 5.

So, based on the argument(s) passed while creating an object, the corresponding constructor gets called.

This is it in constructor overloading. Now move on to the next chapter to see what more you can do in Object Oriented Programming in Java.

> Failure Will Never Overtake Me If My Determination To Succeed Is Strong Enough.
> 
> \- Og Mandino
