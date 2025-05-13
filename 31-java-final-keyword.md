# Java final Keyword
***
The `final` keyword is used to restrict us from modifying an entity like variable, method or class. For example, if a variable is declared as final, then we can’t change its value.

The entities which can be declared as final are variables, methods and classes.

Now, you might be wondering - “**Why would we want to prevent ourselves or others from modifying an entity?**”

Let’s try to answer that. We know that the value of **Pi** is 3.14. To store it in your program, you will declare a variable, say pi, with value equal to 3.14.

`int pi = 3.14;`

You will not want to change the value of the variable `pi` anywhere in your program (even by mistake) because the value of **Pi** is constant and equal to 3.14. This is when you will declare your variable `pi` as `final`.

Hope you understood the significance of the `final` keyword. An entity is declared as final by writing the `final` keyword at the beginning of its definition. So let’s how to declare variables, methods and classes as `final`.
***
## Java final Variable
If a variable is declared as final, its value can’t be changed.

We already saw an example of a use case where we might want to declare a variable as final. Let’s write a program and try to change the value of a final variable.

```java
class Test {

    public static void main(String[] args) {
        // defining a final variable
        final int AGE = 18;

        // trying to change the value of final variable
        AGE = 20;
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:7: error: cannot assign a value to final variable AGE
        AGE = 20;
        ^
1 error
</pre>
    </details>
</div>

In this example, we declared a final variable `AGE` with the value 18. When we tried to change its value, we got an error.

Note that a variable whose value can’t be changed in a program is called a **constant**. A constant name is written in uppercase. That is the reason we wrote `AGE` in uppercase in this program.

> If a variable is declared as final, it works as a constant.

### Blank final Variable
If a final variable is not initialized at the time of its declaration, then it is called a **blank final variable**.

For example, the following final variable is a blank final variable because it is not assigned any value when declared.

`int final AGE;`

A final blank variable must be initialized in the class constructor. Assigning a value to it anywhere else will result in an error.

#### What is the use of blank final variables?
Suppose you defined a class `Student` having an attribute `roll` for storing roll number. We declared this attribute as final because the roll number of a student will not be changed.

Assume there are 10 students in a class. Thus we need to make 10 objects of this class. Now, you will know the roll numbers of the students only when their objects will be created. Until then, you would not know the value of the `roll` attribute. Therefore, we will not initialize the `roll` attribute at the time of declaration.

Whenever an object of the `Student` class will be created, the constructor will get called and the roll number of the student (object) will be assigned to the `roll` attribute.

This example is implemented in the following program.

```java
class Student {

    // defining a blank final variable
    private final int roll;

    public Student(int r) {
        // initializing the blank final variable
        roll = r;
    }

    public void displayRoll() {
        System.out.println(roll);
    }
}

class Test {

    public static void main(String[] args) {
        Student s1 = new Student(1);
        Student s2 = new Student(2);

        s1.displayRoll();
        s2.displayRoll();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">1
2
</pre>
    </details>
</div>

In the above program, we created a class `Student` and a blank final variable `roll` as the attribute. Whenever an object of the class is created, its constructor gets called with an argument and the `roll` attribute gets initialized with the passed argument.

> All variables in an interface are by default final.
***
## Java final Method
In the topic [Method Overriding](https://web.archive.org/web/20240416081404/https://www.codesdope.com/course/java-method-overriding/), we read that the implementation of a method can be changed through method overriding.

Thus, if a method is declared as final, it can’t be overridden. 

Let’s try to override a final method.

```java
// superclass
class Animal {

    // defining a final method
    public final void display() {
        System.out.println("This is method of Animal class");
    }
}

// subclass
class Dog extends Animal {

    // trying to override a final method
    public void display() {
        System.out.println("This is method of Dog class");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        d.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Main.java:12: error: display() in Dog cannot override display() in Animal
 public void display() {
 ^
 overridden method is final
1 error
</pre>
    </details>
</div>

Here, we created a class `Animal` and its subclass `Dog`. In the `Animal` class, we defined a `final` method named `display()`.

When we tried to override this method by defining a method with the same name in the subclass `Dog`, we got an error.

> A constructor can’t be declared as final.
***
## Java final Class
Similar to variables and methods, a class can also be declared as final. If a class is declared as final, it can’t be inherited. Thus, we can’t create a subclass of a final class.

Let’s declare a class as final and try to create its subclass.

```java
// defining a final class
final class Animal {

    public void display() {
        System.out.println("This is method of Animal class");
    }
}

// trying to inherit a final class
class Dog extends Animal {

    public void display() {
        System.out.println("This is method of Dog class");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        d.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:9: error: cannot inherit from final Animal
class Dog extends Animal {
 ^
1 error
</pre>
    </details>
</div>

Here, we created a class `Animal` and declared it as `final`. As a result, when we tried to create a subclass of `Animal`, we got an error.

> To see what is right and not do it is a lack of courage.
>
> \- Confucius
***


<a href="32-java-errors-and-exceptions.md" class="next">Next</a>
