# Java Inheritance

Inheritance is an important topic in Object Oriented Programming. To understand inheritance, you need to understand what a subclass is. So let’s get started.

## What is Subclass in Java?

A rectangle has a length and a breadth and a square also has a length and a breadth. We know that a square is a rectangle having the same length and breadth.

Since a square is a rectangle, square is said to be a **subclass** of rectangle.

![subclass and class in Java](https://web.archive.org/web/20240422024544im_/https://www.codesdope.com/pa-images-bucket/courses/java/p24.png)

A class can have any number of subclasses.

Let’s take some other examples of subclasses. A class ‘Vehicle’ can have ‘Car’ and ‘Bicycle’ as its subclasses. A class ‘Bird’ can have ‘Sparrow’, ‘Crow’ and ‘Parrot’ as its subclasses.

A subclass is also called a **child class** and a class whose subclass is made is called a **superclass** or **parent class**. The process of creating a subclass of a class is called **inheritance**. Thus, in the Square-Rectangle example, Rectangle is the superclass and Square is the subclass.

In inheritance, subclass and superclass follow the ‘**is-a**’ relationship.

A subclass should be created such that it follows the ‘**is-a**’ relation with its superclass. Let’s verify this from the above discussed examples.

*   Square is a Rectangle
*   Car is a Vehicle, Bicycle is a Vehicle
*   Sparrow is a Bird, Crow is a Bird, Parrot is a Bird

Creating subclasses helps us understand the relationship between classes better and makes our program structure more organised.

A subclass can access the attributes and methods of its superclass (if not private).

Normally, an object of a class can access the members (attributes and methods) of only its class. However, a subclass inherits the attributes and methods of its superclass. In other words, the objects of a subclass can access the attributes and methods of its class as well as of its superclass.

Okay, enough of the introduction, now let’s quickly create a subclass.

A subclass is defined by using the extend keyword as shown below.

`class ChildClass extends ParentClass { }`

Where **ChildClass** is the name of the child class and **ParentClass** is the name of the parent class.

```java
// superclass
class Person {

    public void print1() {
        System.out.println("I am superclass");
    }
}

// subclass
class Student extends Person {

    public void print2() {
        System.out.println("I am subclass");
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of subclass
        Student st = new Student();

        st.print1();
        st.print2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">I am superclass
I am subclass</pre>
    </details>
</div>

In this example, two classes `Person` and `Student` are created. Look at the following statement.

`class Student extends Person`

This definition makes `Student` a subclass of `Person`. Thus, `Student` inherits the method `print1()` of `Person`. As a result, the objects of the subclass `Student` can also access this inherited method of the parent class `Person`.

Now notice the following two statements.

`st.print1();`

`st.print2();`

In the first statement, the object `st` of the subclass `Student` calls the method `print1()` of the parent class and in the second statement, it calls the method `print2()` of its own class.

This was a demonstration showing the object of a subclass accessing the method of its parent class.

We just read that the objects of a subclass can access the attributes and methods of the superclass (if they are not declared as `private`). However, the reverse is not true, which means that the objects of a superclass can’t access the attributes or members of its subclass. This is proved below.

```java
// superclass
class Person {

    public void print1() {
        System.out.println("I am superclass");
    }
}

// subclass
class Student extends Person {

    public void print2() {
        System.out.println("I am subclass");
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of superclass
        Person p = new Person();

        p.print1();
        p.print2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:21: error: cannot find symbol
        p.print2();
        ^
  symbol:   method print2()
  location: variable p of type Person
1 error</pre>
    </details>
</div>

We created an object `p` of the parent class `Person`. When this object tried to call the method `print2()` of its subclass, we got an error. This is because an object of a parent class can’t access the members of its child class.

## Using protected Modifier

In the topic [Access Modifiers](https://web.archive.org/web/20240422024544/https://www.codesdope.com/course/java-access-modifiers/), we learned the following points.

*   Declaring a class attribute or a class method as `public` means that it can be accessed from anywhere in the program.
*   Declaring it as `private` means that it can only be accessed from within the class in which it is defined.
*   Declaring it as `protected` means that it can be accessed from the class in which it is defined and the subclasses of this class.

These points are summarized in the following table.

| Can be accessed in | Its Class             | Its Subclass          | Other Classes                                    |
| ------------------- | --------------------- | --------------------- | ------------------------------------------------ |
| public              | Yes (directly)        | Yes (directly)        | Yes (using object of its class or subclasses)    |
| private             | Yes (directly)        | No                    | No                                               |
| protected           | Yes (directly)        | Yes (directly)        | Yes (using object of its class or subclasses)    |

Here is an example showing the same.

```java
// superclass
class C1 {

    public void m1() {}

    protected void m2() {}

    private void m3() {}
}

// subclass
class C2 extends C1 {

    public void m4() {
        m1(); // a subclass C2 can access all public methods of superclass
        m2(); // a subclass C2 can access all protected methods of superclass
        //m3(); // uncommenting this line will give an error because the private method 'm3' can't be accessed outside its class C1
    }
}

// Main class
class Test {

    public static void main(String[] args) {
        // creating object of superclass
        C1 a1 = new C1();

        a1.m1();
        a1.m2();
        //a1.m3(); // uncommenting this line will give an error because the private method 'm3' can't be accessed outside its class C1
        //a1.m4(); // uncommenting this line will give an error because an object 'a1' of superclass can't access a method 'm4' of subclass

        // creating object of subclass
        C2 a2 = new C2();

        a2.m1(); // an object 'a2' of subclass can access all public methods of superclass
        a2.m2(); // an object 'a2' of subclass can access all protected methods of superclass
        //a2.m3(); // uncommenting this line will give an error because the private method 'm3' can't be accessed outside its class C1
        a2.m4();
    }
}
```

On going through the code and the comments in the above program, we can conclude that if the members (variables and methods) of a class are not `private`, then they can be directly accessed from its own class (`C1` in this program) and its subclasses (`C2` in this program). In any other class (`Test` in this program), they can be accessed using the objects of its class or its subclasses.

Let’s see another example.

```java
// superclass
class Person {

    protected String name;

    protected void display() {
        System.out.println("This is a superclass method");
    }
}

// subclass
class Student extends Person {

    public void printName() {
        System.out.println("Name: " + name); // accessing protected variable of superclass in subclass
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of subclass
        Student st = new Student();

        // accessing protected variable and method of superclass using object of subclass
        st.name = "John";
        st.printName();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: John</pre>
    </details>
</div>

Try to understand what is happening in this program.

We created a class `Person` having a protected attribute `name` and a protected method `display()`. Then we created a subclass `Student` of this class.

Notice the following statement inside a method of the subclass.

`System.out.println("Name: " + name);  // accessing protected variable of superclass in subclass`

Here, since protected members of a class can be accessed from its subclass, the protected variable `name` of the `Person` class is accessed in the `printName()` method of its subclass `Student`.

Now notice the following two statements in the main method.

`st.name = "John";`

`st.printName();`

Since the protected members of a class can be accessed by the objects of its class or the objects of its subclass, the object `st` of the subclass `Student` accesses the `name` attribute and calls the `display()` method of the parent class.

## Java Subclass with Constructor

The constructor of a subclass can call the constructor of its superclass, but the reverse is not true. Let’s see how the constructor of a superclass is called from the constructor of its subclass.

We know that whenever an object of a class is created, its constructor automatically gets called. But there is more to it.

When the constructor of a class is called, the constructor of its parent class automatically gets called, even if we do not explicitly call it.

Look at the following example.

```java
// superclass
class Person {

    public Person() {
        System.out.println("Constructor of parent class");
    }
}

// subclass
class Student extends Person {

    public Student() {
        System.out.println("Constructor of child class");
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of subclass
        Student st = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Constructor of parent class
Constructor of child class</pre>
    </details>
</div>

In this example, when the object `st` of the `Student` class is created, the constructor of `Student` gets called. Inside the constructor of `Student`, first the constructor of its parent class `Person` gets automatically called and after that the code inside the constructor of `Student` gets executed.

```java
public Student() {
    // constructor of parent class gets implicitly called here
    System.out.println("Constructor of child class");
}
```

Look at the above code. In the constructor of `Student`, the constructor of the parent class `Person` automatically gets called (even when we didn’t call it in our program) as the first statement.

This is the reason *Constructor of parent class* got printed before *Constructor of child class*.

![animatic calling of parent constructor in Java](https://web.archive.org/web/20240422024544im_/https://www.codesdope.com/pa-images-bucket/courses/java/p25.png)

When the constructor of a class is called, the compiler first calls the constructor of its parent class implicitly.

However, unlike constructors having no parameter, a constructor having parameters of the parent class doesn’t get automatically called in the child class constructor.
Take the following example.

```java
// superclass
class Person {

    protected String name;

    public Person() {
        System.out.println("Constructor 1 of parent class");
    }

    public Person(String n) {
        System.out.println("Constructor 2 of parent class");
        name = n;
    }
}

// subclass
class Student extends Person {

    public Student() {
        System.out.println("Constructor of child class");
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of subclass
        Student st = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Constructor 1 of parent class
Constructor of child class</pre>
    </details>
</div>

In this example, when the constructor of the `Student` class gets called, the constructor of the parent class `Person` having no parameter gets called and the constructor having parameters doesn't get called.

So that was all you need to know about inheritance. Now let’s look at a practical example of subclasses.

## Java Examples of Inheritance

Till now, we saw examples in which a class inherits another class. Now let’s look at some more examples of inheritance.

In the following example, a class `Shape` has a subclass `Rectangle` and the class `Rectangle` has a subclass `Square`. Here, `Rectangle` will inherit the properties of `Shape` whereas `Square` will inherit the properties of both `Shape` and `Rectangle`.

```java
class Shape {

    public void m() {
        System.out.println("This is a Shape");
    }
}

class Rectangle extends Shape {

    public void m1() {
        System.out.println("This is a Rectangle");
    }
}

class Square extends Rectangle {

    public void m2() {
        System.out.println("This is a Square");
    }
}

class Test {

    public static void main(String[] args) {
        Rectangle r = new Rectangle(); // creating object r of Rectangle
        Square s = new Square(); // creating object s of Square

        r.m();
        r.m1();

        System.out.println("****");

        s.m();
        s.m1();
        s.m2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is a Shape
This is a Rectangle
****
This is a Shape
This is a Rectangle
This is a Square</pre>
    </details>
</div>

![inheritance in Java](https://web.archive.org/web/20240422024544im_/https://www.codesdope.com/pa-images-bucket/courses/java/p26.png)

In this example, `Rectangle` is a subclass of `Shape` and `Square` is a subclass of Rectangle. As a result, the object of `Rectangle` can access its method `m1()` and the method `m()` of its parent class `Shape`. Further, `Rectangle` also has a subclass `Square` and so the object of `Square` can access its method `m2()` as well as the methods of its ancestor classes `Rectangle` and `Shape`.

![Accessing of parent method in Java](https://web.archive.org/web/20240422024544im_/https://www.codesdope.com/pa-images-bucket/courses/java/p27.png)

In the next example, a class `Shape` has `Rectangle` and `Circle` as subclasses. So, both `Rectangle` and `Circle` will inherit the properties of `Shape`.

```java
class Shape {

    public void m() {
        System.out.println("This is a Shape");
    }
}

class Rectangle extends Shape {

    public void m1() {
        System.out.println("This is a Rectangle");
    }
}

class Circle extends Shape {

    public void m2() {
        System.out.println("This is a Circle");
    }
}

class Test {

    public static void main(String[] args) {
        Rectangle r = new Rectangle(); // creating object r of Rectangle
        Circle c = new Circle(); // creating object c of Circle

        r.m();
        r.m1();

        System.out.println("****");

        c.m();
        c.m2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is a Shape
This is a Rectangle
****
This is a Shape
This is a Circle</pre>
    </details>
</div>

In the above example, the class `Shape` has two subclasses `Rectangle` and `Circle`. Therefore, the object of `Rectangle` can access its method `m1()` and the method `m()` of its parent class `Shape`. The object of `Circle` can access its method `m2()` and the method `m()` of its parent class Shape.

In Java, a class can’t inherit more than one class.

## A Real Life Example of Inheritance

Suppose we want to make a school system to store information about students and teachers. In this system, we want to store the name, age and marks of students and the name, age and salary of teachers.

We can make such a system in Java using classes and objects. Notice that name and age have to be stored for both students and teachers and we also know that students as well as teachers are persons.

Therefore, we can make **Person** as a class with **name** and **age** as attributes, and can make **Student** and **Teacher** as the subclasses of **Person** (a class can have any number of subclasses). In the **Student** class, we can define an additional **marks** attribute and in the **Teacher** class an additional **salary** attribute.

Don’t you think this structure is better and more organised than creating just two classes **Student** and **Teacher**, each having 3 attributes?

Try to implement this structure in the form of a Java program yourself before looking at the program below.

```java
// superclass
class Person {

    protected String name;
    protected int age;

    public void setPersonDetails(String p_name, int p_age) {
        name = p_name;
        age = p_age;
    }

    public void getPersonDetails() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// subclass 1
class Student extends Person {

    private int marks;

    public void setStudentDetails(String s_name, int s_age, int s_marks) {
        setPersonDetails(s_name, s_age);
        marks = s_marks;
    }

    public void getStudentDetails() {
        System.out.println("#### Details of student ####");
        getPersonDetails();
        System.out.println("Marks: " + marks);
    }
}

// subclass 2
class Teacher extends Person {

    private int salary;

    public void setTeacherDetails(String t_name, int t_age, int t_salary) {
        setPersonDetails(t_name, t_age);
        salary = t_salary;
    }

    public void getTeacherDetails() {
        System.out.println("#### Details of teacher ####");
        getPersonDetails();
        System.out.println("Salary: " + salary);
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of subclass Student
        Student st = new Student();
        st.setStudentDetails("John", 20, 84);
        st.getStudentDetails();

        // creating object of subclass Teacher
        Teacher tch = new Teacher();
        tch.setTeacherDetails("Julie", 40, 200000);
        tch.getTeacherDetails();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">#### Details of student ####
Name: John
Age: 20
Marks: 84
#### Details of teacher ####
Name: Julie
Age: 40
Salary: 200000</pre>
    </details>
</div>

So let’s understand this program.

As discussed in the approach, we created two subclasses `Student` and `Teacher` of the `Person` class.

In the main method, an object `st` of the subclass `Student` is created. This object calls the `setStudentDetails()` method by passing the values “John”, 20 and 84. These passed values are assigned to the parameters `s_name`, `s_age` and `s_marks`. In the `setStudentDetails()` method, the value of `s_marks` (i.e. 84) is assigned to the `marks` attribute for the object `st`, and the `setPersonDetails()` method of the parent class is called by passing `s_name` and `s_age` as the arguments. In the `setPersonDetails()` method of the parent class, the attributes `name` and `age` becomes “John” and 20 respectively for the object `st`.

After this, in the main method, the object `st` of the subclass `Student` calls the `getStudentDetails()` method. In the `getStudentDetails()` method, the value of the `marks` attribute for the object `st` is printed and the `getPersonDetails()` method of the parent class is called. In the `getPersonDetails()` method, the values of the attributes name and age for the object `st` are printed.

A similar process is carried out for the subclass `Teacher`.

This finishes our explanation. If you understood this program, then you have understood the core of inheritance and you can start implementing this concept in your programs.

Before wrapping up, let’s look at the `instanceof` operator which is used to check if an object belongs to a class.

## Java instanceof Operator

The `instanceof` operator is used to check whether an object is an instance of a class. In other words, it checks whether an object belongs to a particular class.

If the specified object is an instance of the specified class, then the operator returns **true**, otherwise it returns **false**.

### Java instanceof Syntax

```
objectName instanceof className
```

Here, **objectName** is the name of the object and **className** is the name of the class.

### Java instanceof Example

```java
// superclass
class Rectangle {}

// subclass
class Square extends Rectangle {}

class Test {

    public static void main(String[] args) {
        // creating object of superclass
        Rectangle rect = new Rectangle();

        // creating object of subclass
        Square sq = new Square();

        System.out.println(rect instanceof Rectangle);
        System.out.println(sq instanceof Square);
        System.out.println(sq instanceof Rectangle);
        System.out.println(rect instanceof Square);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">true
true
true
false</pre>
    </details>
</div>

In this example, `rect` is an object of the superclass `Rectangle` and `sq` is an object of the subclass `Square`. Therefore, `rect` belongs only to `Rectangle`, whereas `sq` belongs to both `Square` and `Rectangle`.

`rect instanceof Rectangle` checks if the object `rect` belongs to the class `Rectangle`. Since it belongs to this class, the operator returned true.

Inheritance is a new and an important concept in Object Oriented Programming. So practice questions from our [practice section](https://web.archive.org/web/20240422024544/https://www.codesdope.com/practice/).

It is very important in real projects to organise different classes in a program as superclasses and subclasses based on the relationship between them. So, whenever you create multiple classes in a program, try to figure out if there is a possibility to introduce inheritance to make the code more organised.

> Whether You Think You Can Or Think You Can’t, You’re Right.
>
> \- Henry Ford


<a href="23-java-method-overriding.md" class="next">Next</a>
