# Java Array of Objects
<hr/>
By now, you must have got a good hold over classes and objects. If not, you can go to the practice section to practice questions on classes and objects.

In the topic [classes and objects](https://web.archive.org/web/20220811214912/https://www.codesdope.com/course/java-classes-and-objects/), we saw an example in which the area of a rectangle is printed by making an object of the Rectangle class. Now suppose we want to display the area of two rectangles.

An obvious way to do this is by creating two objects of the Rectangle class, each representing a rectangle. This is a quite straightforward solution. Let’s write a program for this approach.

```java
class Rectangle {

    private int length;
    private int breadth;

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
        Rectangle rect1 = new Rectangle(2, 4); // 1st rectangle
        Rectangle rect2 = new Rectangle(4, 5); // 2nd rectangle

        System.out.println(rect1.getArea());
        System.out.println(rect2.getArea());
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">8
20</pre>
    </details>
</div>

In this example, two objects `rect1` and `rect2` of the `Rectangle` class are created. The first object `rect1` is created with length and breadth as 2 and 4 respectively and the second object `rect2` is created with length and breadth as 4 and 5 respectively. Both the objects then call the `getArea()` method to print the respective areas.

Now suppose you want to print the area of 50 rectangles. For that, with the above approach you need to create 50 objects of the `Rectangle` class, each representing a rectangle, and then make each object call the `getArea()` method separately. Using 50 different objects is not a good choice.

A better solution is to create an array of 50 objects. Yes, we can also create an array of objects of a class.

Let’s see how to create an array of objects.
<hr/>
## Creating Array of Objects in Java
We know that an array is declared as follows.

```java
type[] arrayName = new type[array_size];
```

Where **arrayName** is the name of the array, **type** is the data type of the values that the array will store and **array_size** is the number of values that the array will store.

An array to store 5 integers can be declared as:

`int[] arr = new int[5];`

Similarly, an array of 50 objects of the class `Rectangle` can be declared as:

`Rectangle[] arr = new Rectangle[50];`

It is this easy to create an array of objects.

For now, let’s write a program to display the area of two rectangles by creating an array of two objects.

```java
class Rectangle {

    private int length;
    private int breadth;

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
        // declaring array of objects
        Rectangle[] rect = new Rectangle[2];

        // initializing array
        rect[0] = new Rectangle(2, 4);
        rect[1] = new Rectangle(4, 5);

        for (int i = 0; i < 2; i++) {
            System.out.println(rect[i].getArea());
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">8
20</pre>
    </details>
</div>

Let’s go through the statements in the main method.

`Rectangle[] rect = new Rectangle[2]` → An array named `rect` with 2 elements is created. These 2 elements will store the objects of the `Rectangle` class. This means that the objects of the `Rectangle` class will be assigned to these two elements of the array.

`rect[0] = new Rectangle(2, 4)` → In this statement, `new Rectangle(2, 4)` creates a new object of `Rectangle` having `length` and `breadth` as 2 and 4 respectively. This object created is assigned to the first element `rect[0]` of the array.

`rect[1] = new Rectangle(4, 5)` → Again `new Rectangle(4, 5)` creates a new object having `length` and `breadth` as 4 and 5 respectively. This object is assigned to the second element `rect[1]` of the array.

Thus, the two objects of the class are assigned to the two elements of the array `rect`. After that, a `for` loop is run two times.

In the first iteration of the loop, the value of i is 0 and so `rect[i].getArea()` is `rect[0].getArea()`. The first object calls the `getArea()` method and its area is printed. Similarly in the second iteration of the loop, the area of the second object is printed.

![array of objects in Java](https://web.archive.org/web/20220811214912im_/https://www.codesdope.com/pa-images-bucket/courses/java/p23.png)

That was so cool!

Take another example in which the name and marks of 5 students are taken as input and stored using an array of objects.

```java
import java.util.Scanner;

class Student {

    private String name;
    private int marks;

    public void setDetails(String n, int m) {
        name = n;
        marks = m;
    }

    public void printDetails() {
        System.out.println("Name: " + name);
        System.out.println("Marks: " + marks);
    }
}

class Test {

    public static void main(String[] args) {
        // declaring array of objects
        Student[] st = new Student[5];

        // initializing array
        Scanner s = new Scanner(System.in);

        for (int i = 0; i < 5; i++) {
            System.out.println("Student " + (i + 1));
            System.out.println("Enter name");
            String name = s.next();
            System.out.println("Enter marks");
            int marks = s.nextInt();

            st[i] = new Student();
            st[i].setDetails(name, marks);
        }

        // printing details of the objects
        for (int i = 0; i < 5; i++) {
            st[i].printDetails();
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Student 1
Enter name
Jack
Enter marks
54
Student 2
Enter name
Marx
Enter marks
45
Student 3
Enter name
Julie
Enter marks
47
Student 4
Enter name
Peter
Enter marks
23
Student 5
Enter name
Donald
Enter marks
87
Student 1
Name : Jack
Marks : 54
Student 2
Name : Marx
Marks : 45
Student 3
Name : Julie
Marks : 47
Student 4
Name : Peter
Marks : 23
Student 5
Name : Donald
Marks : 87</pre>
    </details>
</div>

In this example,

`Student[] st = new Student[5]` → An array named `st` with 5 elements is defined which will store the objects of the `Student` class.

In the first `for` loop, objects of the `Student` class are created and assigned to the elements of the array.

In the first iteration of the `for` loop, `i` is 0. The name and marks of the first student entered by the user are assigned to the variables `name` and `marks` respectively. The statement `st[0] = new Student()` creates a new object and assigns it to the first element `st[0]` of the array. Then in the statement `st[0].setDetails(name, marks)`, the first object calls the `setDetails()` method to set the values of its `name` and `marks` attributes to the passed arguments.

So, in the 5 iterations of the loop, 5 objects are created and assigned to the elements of the array `st`.

In the second `for` loop, the objects call the `printDetails()` method to print their `name` and `marks`.

You are now ready to create arrays of objects!

> People Who Are Crazy Enough To Think They Can Change The World, Are The Ones Who Do.
>
> \- Rob Siltanen
<hr/>


<a href="20-java-constructor-overloading.md" class="next">Next</a>
