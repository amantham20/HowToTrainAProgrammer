# Java Interface

In the [last chapter](https://web.archive.org/web/20240416071824/https://www.codesdope.com/course/java-abstract-class/), we discussed abstraction and abstract classes. As a quick recap, abstraction is the process of reducing complexity by hiding unnecessary information from the user. It can be achieved using abstract classes and interfaces. Abstract classes can be used to achieve only partial abstraction.

In this chapter, we will go through the second method to achieve abstraction i.e., interface.

## Need for Interfaces

Interfaces are mainly used for the following reasons.

1.  The most important use of an interface is that **it provides full abstraction**.
2.  Interfaces are useful if we need to inherit multiple classes (or interfaces to be precise). In Java, we normally can't inherit multiple classes but we can achieve a similar functionality using interfaces.

We will see how an interface helps achieve full abstraction and how it can be useful in a program  as we will go through the chapter.

## What is an Interface?

Interfaces are similar to abstract classes. While abstract classes can contain both abstract and non-abstract methods, interfaces can contain only abstract methods. Like abstract class, we can’t create objects of an interface. We will look at more differences between interfaces and abstract classes later.

To create an interface, the `interface` keyword is used.

For example, an interface named `Walk` can be defined as shown below.

```java
interface Walk {
    // attributes and methods
}
```

Let’s read about the methods and variables defined inside an interface.

## Java Interface Methods

As stated earlier, all methods inside an interface are abstract methods. Thus, the methods defined inside an interface don't have a body.

 All methods defined in an interface are public and abstract by default.

Since all methods inside an interface are by default public and abstract, there is no need to explicitly declare them as `public` or `abstract`. If we try to define a non-public or non-abstract method inside an interface, we will get an error.

For example, an interface named `Walk` with an abstract method named `walk()` can be defined as follows.

```java
interface Walk {
    void walk();
}
```

## Java Interface Variables

We can also declare variables inside an interface. However, it is advised not to declare variables in interfaces.

 All variables declared in an interface are public, static and final by default.

Since all variables defined in an interface are by default `public`, `static` and `final`, there is no need to explicitly declare them as public, static or final. If we try to define a non-public, non-static or non-final method inside an interface, then we will get an error.

For example, an interface named `Walk` with an abstract method named `walk()` and a variable named `hours` can be defined as follows.

```java
interface Walk {
    int hours = 10;  // number of hours walked in a day
    void walk();
}
```

Now you know how to create an interface with methods and/or variables. So let’s see how to use interfaces in Java.

## Implementing an Interface

In the last chapter, we saw that a class **inherits** an abstract class to define the methods of the abstract class. However, a class **implements** an interface to define the methods of the interface. An interface is implemented using the `implements` keyword.

 When a class implements an interface, it must implement all the methods inside the interface. (It is not mandatory to use variables defined in an interface in the class implementing the interface)

Any number of classes can implement an interface.

```java
interface A {
    // code
}

class B implements A {
    // code
}
```

In the above code, class B implements the interface A. Therefore, it must implement all the abstract methods of the interface.

```java
// interface
interface Walk {
    void walk();
}

// class Dog implements interface Walk
class Dog implements Walk {

    public void walk() {
        System.out.println("A dog walks for 10 hours in a day");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        d.walk();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">A dog walks for 10 hours in a day
</pre>
    </details>
</div>

In the above example, an interface named `Walk` has an abstract method named `walk()`. A class named `Dog` implements the interface and thus implements the method `walk()` by providing it a body.

An object `d` of the class `Dog` is created and calls the method `walk()`.

Note that we defined the `walk()` method in the class `Dog` as `public` because this method is by default `public` in the interface.

Let’s see what would happen if the class `Dog` implementing the interface `Walk` doesn’t implement the method `walk()` defined in the interface.

```java
// interface
interface Walk {
    void walk();
}

// class Dog implements interface Walk
class Dog implements Walk {}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:7: error: Dog is not abstract and does not override abstract method walk() in Walk
class Dog implements Walk {
^
1 error
</pre>
    </details>
</div>

Since a class implementing an interface must override all the methods of the interface, therefore we got an error on running this program because the class `Dog` doesn’t implement the method defined in the interface `Walk`.

## A Real Life Example of Interface

We know that all vehicles (including cars and bikes) need servicing from time to time. Suppose we want to create two classes named **Car** and **Bike** having a method that returns the time after which servicing is required for the vehicle. Here, we can create an interface named **Servicing** having an abstract method named **getServiceTime()** and can make the classes Car and Bike implement the interface Servicing and thus implement its method **getServiceTime()**.

Note that when a class implements an interface, it must implement all the methods of the interface. Therefore, in our example, the interface **Servicing** acts as a base or a prototype for both theclasses. Thus, all the classes implementing the **Servicing** interface must define the **getServiceTime()** method.

This is implemented in the following program.

```java
// interface
interface Servicing {
    // abstract method
    int getServiceTime();
}

// class implements interface
class Car implements Servicing {

    //implementing abstract method
    public int getServiceTime() {
        return 2;
    }
}

// class implements interface
class Bike implements Servicing {

    //implementing abstract method
    public int getServiceTime() {
        return 3;
    }
}

class Test {

    public static void main(String[] args) {
        Car c = new Car();
        Bike b = new Bike();

        System.out.println(c.getServiceTime());
        System.out.println(b.getServiceTime());
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">2
3
</pre>
    </details>
</div>

As you can see, the interface `Servicing` is like a prototype which tells us that any class of a vehicle must contain the `getServiceTime()` method that returns the time after which servicing is required for the vehicle. Thus, all the two classes of vehicles implementing it have this method.

That was interesting! Don’t you think using an interface made our code much more organised?

Now let’s talk about the two main advantages of using an interface - full abstraction and multiple inheritance.

## Interface Helps Achieve Full Abstraction

In the last example, the interface `Servicing` has the `getServiceTime()` method without any definition (body) of the method. Thus, `Servicing` acts like a prototype that just tells us that a vehicle class has the `getServiceTime()` method that returns the servicing period of the vehicle without telling us any implementation details (like how the servicing period is calculated and returned) of the method.

Since an interface can contain only abstract methods, it provides full abstraction.

## Interface Helps Achieve Multiple Inheritance

In the Inheritance topic, we saw that multiple inheritance is not possible because a single class is not allowed to inherit more than one class in Java. A similar functionality, however, can be possible using an interface.

In Java, a single class can implement more than one interface. This is how multiple inheritance can be achieved.

![multiple inheritance in Java](https://web.archive.org/web/20240416071824im_/https://www.codesdope.com/pa-images-bucket/courses/java/p35.png)

```java
interface A {
    // code
}

interface B {
    // code
}

class C implements A, B {
    // code
}
```

In the above code, class C implements both interface A and interface B. As a result, it will implement the abstract methods of both the interfaces.

Let’s see an example in which a class inherits multiple interfaces.

Most of the birds can fly as well as walk. However, there are some birds like Humming Bird and Loon that can fly but can’t walk. Here, we can create an interface named *Fly* having a method *fly()* and an interface named Walk having a method named *walk()*. Now, we can make the classes of birds that can fly and walk implement both the interfaces, whereas the classes of birds that can only fly implement only the first Fly interface, as shown below.

```java
// interface Fly
interface Fly {
    void fly();
}

// interface Walk
interface Walk {
    void walk();
}

// class Sparrow implements interfaces Fly and Walk
class Sparrow implements Fly, Walk {

    public void fly() {
        System.out.println("Sparrows can fly");
    }

    public void walk() {
        System.out.println("Sparrows can walk");
    }
}

// class HummingBird implements interface Fly
class HummingBird implements Fly {

    public void fly() {
        System.out.println("Humming Birds can fly");
    }
}

class Test {

    public static void main(String[] args) {
        Sparrow s = new Sparrow();
        HummingBird hb = new HummingBird();

        s.fly();
        s.walk();
        hb.fly();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Sparrows can fly
Sparrows can walk
Humming Birds can fly
</pre>
    </details>
</div>

In the above program, the class Sparrow implements the interfaces Fly and Walk whereas the class HummingBird implements the interface Fly only.

Let’s see another example.

```java
// interface 1
interface Frontend {
    void displayFrontend();
}

// interface 2
interface Backend {
    void displayBackend();
}

// class implements interface 1 and interface 2
class Developer implements Frontend, Backend {

    public void displayFrontend() {
        System.out.println("I code in React");
    }

    public void displayBackend() {
        System.out.println("I code in Django");
    }
}

class Test {

    public static void main(String[] args) {
        Developer dev = new Developer();

        dev.displayFrontend();
        dev.displayBackend();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">I code in React
I code in Django
</pre>
    </details>
</div>

In this example, the interface `Frontend` has an abstract method `displayFrontend()` and the interface `Backend` has an abstract method `displayBackend()`. A class named `Developer` implements both the interfaces and hence adds definitions to their methods.

Here, we have implemented a case that a developer both frontend as well as backend.

## Extending an Interface

Till now we know that **a class extends a class** and **a class implements an interface**.

What if we want an interface to implement (use) another interface?

Well, we can do that also in Java - **an interface extends an interface**.

```java
interface A {
    // code
}

interface B {
    // code
}

interface B extends A {
    // code
}
```

In the above code, interface B extends interface A. As a result, the class implementing the interface B must define the methods of both the interface B and its parent interface A.

Let’s see an example. Suppose you want to draw two shapes, each shape is made up of rectangles, triangles and lines. So, we can make three interfaces named Rectangle defining a method drawRectangle(), Triangle defining a method named drawTriangle() and Line defining a method named drawLine(). We can further structure these interfaces by making the interfaces Rectangle and Triangle extend the interface Line. We did this because a rectangle and a triangle both are made up of lines and so we were able to show a relationship between these interfaces. Moreover, any shape class implementing Rectangle or Triangle will also have to implement Line.

Then we can make two classes Shape1 and Shape2 implementing the Rectangle and Triangle interfaces. This is demonstrated in the following program

```java
// parent interface
interface Line {
    void drawLine();
}

// child interface Rectangle
interface Rectangle extends Line {
    void drawRectangle();
}

// child interface Triangle
interface Triangle extends Line {
    void drawTriangle();
}

// class Shape1 implements interfaces Rectangle, Triangle
class Shape1 implements Rectangle, Triangle {

    void drawLine() {
        // code
    }

    void drawRectangle() {
        // code
    }

    void drawTriangle() {
        // code
    }
}

// class Shape2 implements interfaces Rectangle, Triangle
class Shape2 implements Rectangle, Triangle {

    void drawLine() {
        // code
    }

    void drawRectangle() {
        // code
    }

    void drawTriangle() {
        // code
    }
}
```

An interface can extend any number of interfaces and any number of interfaces can extend from an interface.

As you already know, interfaces are just prototypes or base models upon which classes are built. You can play around with interfaces and classes making your code more and more organised.

For example, you can extend multiple interfaces from a single interface and implement multiple classes for each extended interface. There are many more combinations which you can try based on your use case.

## Abstract Classes vs Interfaces

So you have read about abstract classes as well as interfaces. Though both might seem to perform similar tasks, they are not so similar. Let’s look at their differences and discuss when to use an abstract class and when to use an interface.

One basic difference between abstract classes and interfaces is that interfaces are not technically classes like abstract classes.

Another difference is that abstract classes provide partial abstraction and interfaces provide full abstraction. Let’s talk about some more concrete differences.

An abstract class is used to create functionality (methods) that subclasses can implement/override (for abstract methods). It is designed to be inherited by other classes. We normally use an abstract class when the subclasses have some common functionality that must be implemented by them. That common functionality (methods) is defined as the methods inside the abstract class.

For example, since all types of cars have brake and accelerator functionalities. So we can make an abstract class named Car having `getBrake()` and `getAccelerator()` methods and make all car models as its subclasses, as shown below.

```java
// abstract class
abstract class Car {

    abstract void getBrake();

    abstract void getAccelerator();
}

// class Ford extends Car
class Ford extends Car {

    public void getBrake() {
        // implement it
    }

    public void getAccelerator() {
        // implement it
    }
}

// class Honda extends Car
class Honda extends Car {

    public void getBrake() {
        // implement it
    }

    public void getAccelerator() {
        // implement it
    }
}
```

On the other hand, an interface is used to implement a functionality over many classes rather defining an entire class. It means an interface is a small functionality which can be common between many unrelated classes. For example, the functionality of remote control will be common in TV, AC, DVD Player, etc. So, it makes more sense to make RemoteControl an interface and all these TV, AC and DVD classes will implement RemoteControl class to have the functionality.

We know that extending or inheriting means that the subclass is also a superclass. Now think of a case where RemoteControl is a class (not interface) and TV, AC and DVD are inheriting it. Weird, isn’t it that even TV, AC and DVD are RemoteControl. So, we can have an interface of it and whatever class needs the functionality can implement the interface.

```java
// interface
interface class Brake {
    void getBrake();
}

// class Car implements Brake
class Car implements Brake {
    public void getBrake() {
        // implement it
    }
}

// class Bike implements Brake
class Bike implements Brake {
    public void getBrake() {
        // implement it
    }
}
```

From the above explanation and examples, we can conclude the following points.

*   When similar classes have similar functionalities, we can make them extend an abstract class providing the similar functionalities, provided that the classes follow the is-a relationship with the abstract class. For example, classes Honda and Ford extending the abstract class Car.
*   When some similar or non-similar classes have similar functionalities, then we can make them implement an interface providing that functionality. For example, classes Car and Bike implementing the interface Brake.
*   A class can extend only one abstract class (any class in general) but can implement multiple interfaces. So, structure your code accordingly.
*   An abstract class should be created with minimum functionality (methods) so that we don’t need to change its functionality in future. This is because other classes will extend the abstract class and thus a large structure will get built on top of it. In that case, if we do any significant modification (like changing the return type) in any method of the abstract class anytime in future, then the classes extending that abstract class will throw errors and the code will break. Hence, **prefer using interfaces instead of abstract classes if you think that you might modify the methods in future**.
*   An interface should also be created with minimum functionality (methods). For example, suppose an interface has methods getBrake() (for defining brake system) and getMusicSystem() (for defining music system), and a car class and a bike class implement the interface. In that case, both the classes will be forced to implement both the methods. Here, even if a bike class doesn’t want to implement the getMusicSystem(), it will be forced to do so which is not desirable. Hence, what we can do is create an interface that defines the getBrake() method and another interface that defines the getMusicSystem() method, and make the car class implement both the interfaces while make the bike class implement only the first interface.

> Turn your wounds into wisdom.
>
> \- Oprah Winfrey


<a href="28-java-encapsulation.md" class="next">Next</a>
