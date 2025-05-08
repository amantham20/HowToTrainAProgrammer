# Java Nested Classes

Classes and objects are an integral part of programming. We looked at several concepts related to classes and objects in the previous topics. In this chapter, we will discuss nested classes in Java.

You know that a class can inherit another class. In Java, we can also have **nested classes**. In other words, we can define a class inside another class.

This sounds interesting. Let’s see how nesting classes can be useful.

## Need for Java Nested Classes

Let’s understand the need of nested classes by taking some real life examples.

Suppose there is a house. The house contains some bedrooms, some bathrooms and a kitchen. Now assume that someone decides to demolish (destroy) the house. If the house is demolished, then the bedrooms, bathrooms and kitchen will also be demolished.

In this scenario, we can say that the house contains the bedrooms, bathrooms and kitchen. Or we can also say that the bedrooms, bathrooms and kitchen are part of the house. If the house doesn’t exist, then they will also not exist. Programmatically, if the house object doesn’t exist, the objects of the bedroom, bathroom and kitchen also can’t exist.

Since bedrooms, bathrooms and kitchen are parts of the house, therefore it is better to define the `Bedroom` class, the `Bathroom` class and the `Kitchen` class inside the `House` class.

```java
class House {

    // code of House class

    class Bedroom {
        // code of Bedroom class
    }

    class Bathroom {
        // code of Bathroom class
    }

    class Kitchen {
        // code of Kitchen class
    }
}
```

Here, `Bedroom`, `Bathroom` and `Kitchen` are the nested classes.

Let’s take another example.

Suppose a university has several departments like Electrical, Mechanical, etc. If the university is closed, then the departments will also get closed. In this case also, departments are part of the university. So, we can define the Department class inside the University class.

```java
class University {

    // code of University class

    class Department {
        // code of Department class
    }
}
```

You must have now understood how making some classes as nested can be useful in some cases.

A class and its nested class follow the ‘has-a’ relationship.

A class is usually defined inside another class when the outer class follows the ‘**has-a**’ relation with the inner class. Let’s verify this from the above discussed examples.

*   House **has a** Bedroom, House **has a** Bathroom, House **has a** Kitchen
*   University has a Department

In Java, we can create two types of nested classes - **static** and **non-static**. Non-static nested classes are also called **inner classes**.

1.  Non-static nested classes (inner classes)

    a.  Inner classes
    b.  Method local inner classes
    c.  Anonymous inner classes
2.  Static nested classes.

Let’s learn about all these nested classes.

## Java Inner Class

An **inner class** is simply a class defined inside another class.

```java
class OuterClass {

    // code of OuterClass class

    class InnerClass {
        // code of InnerClass class
    }
}
```

In the above declaration, the `InnerClass` class is defined inside the `OuterClass` class. Thus, `InnerClass` is an inner class.

Note that an inner class is just like any other member of the outer class. For example, in the above declaration, the variables or methods defined inside `OuterClass` are its members. Similarly, the `InnerClass` class defined inside `OuterClass` is also its member.

### Creating Object of Inner Class

To create an object of the inner class, the object of the outer class is created first and then the object of the outer class is used to create the object of the inner class.

Let’s see how this is done using an example.

```java
class House {

    // nested class
    class Bedroom {

        int bedroom_count = 4;

        void printBedroom() {
            System.out.println("Number of bedrooms: " + bedroom_count);
        }
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of outer class House
        House house = new House();

        // creating object of inner class Bedroom
        House.Bedroom bd = house.new Bedroom();

        bd.printBedroom();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number of bedrooms: 4</pre>
    </details>
</div>

In the above example, the inner class `Bedroom` is defined inside the outer class `House`. The `Bedroom` class has two members - a variable named `bedroom_count` and a method named `printBedroom()`.

Now let’s come to the main method.

We first created an object `house` of the outer class `House`.

After that, we created an object `bd` of the inner class `Bedroom` using the object `house` of the outer class as shown below.

`House.Bedroom bd = house.new Bedroom();`

Thus, the syntax for creating an object of an inner class is shown below.

`OuterClass.InnerClass inner_class_object = outer_class_object.new InnerClass();`

Here, `OuterClass` is the outer class, `InnerClass` is the inner class, `inner_class_object` is the object of the inner class and `outer_class_object` is the object of the outer class.

This is how objects of an inner class are created.

Since an inner class acts like any other member of the outer class, it can have the access modifiers - `public`, `protected`, `private`, `final`, `static`, `abstract`.

In the following example, we declared a nested class as `protected`.

```java
class House {

    // nested class
    class Bedroom {

        int bedroom_count = 4;

        void printBedroom() {
            System.out.println("Number of bedrooms: " + bedroom_count);
        }
    }

    // nested class
    protected class Bathroom {

        int bathroom_count = 2;

        void printBathroom() {
            System.out.println("Number of bathrooms: " + bathroom_count);
        }
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of outer class House
        House house = new House();

        // creating object of inner class Bedroom
        House.Bedroom bd = house.new Bedroom();

        // creating object of inner class Bathroom
        House.Bathroom bt = house.new Bathroom();

        bd.printBedroom();
        bt.printBathroom();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number of bedrooms: 4
Number of bathrooms: 2</pre>
    </details>
</div>

Here, we declared two inner classes - `Bedroom` and `Bathroom`. We declared the inner class `Bathroom` as `protected`.

Look at the following statements from the above example.

`House.Bedroom bd = house.new Bedroom();`

`House.Bathroom bt = house.new Bathroom();`

In the above statements, we created the objects `bd` and `bt` of the inner classes `Bedroom` and `Bathroom` respectively.

### Accessing Members of Outer Class Within Inner Class

An inner class can access the members (variables, methods, etc.) of the outer class. Let’s show this with an example.

```java
class House {

    private String type;

    public House(String type) {
        this.type = type;
    }

    void printType() {
        System.out.println("House type: " + type);
    }

    // nested class
    class Bedroom {

        private int bedroom_count;

        public void printBedroom() {
            // accessing variable type of outer class
            if (type == "2bhk") {
                bedroom_count = 2;
            }
            if (type == "4bhk") {
                bedroom_count = 4;
            }

            // calling method printType() of outer class
            printType();

            System.out.println("Number of bedrooms: " + bedroom_count);
        }
    }
}

class Test {

    public static void main(String[] args) {
        // creating object 1 of outer class House
        House house1 = new House("2bhk");

        // creating object 1 of inner class Bedroom
        House.Bedroom bd1 = house1.new Bedroom();
        bd1.printBedroom();

        // creating object 2 of outer class House
        House house2 = new House("4bhk");

        // creating object 2 of inner class Bedroom
        House.Bedroom bd2 = house2.new Bedroom();
        bd2.printBedroom();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">House type: 2bhk
Number of bedrooms: 2
House type: 4bhk
Number of bedrooms: 4</pre>
    </details>
</div>

In the above example, we declared an inner class `Bedroom` inside the outer class `House`. The inner class `Bedroom` accesses the variable `type` and the method `printType()` of the outer class inside its method `printBedroom()`.

In the main method, notice the following statements.

```java
// creating object 1 of outer class House
House house1 = new House("2bhk");
		
// creating object 1 of inner class Bedroom
House.Bedroom bd1 = house1.new Bedroom();
bd1.printBedroom();
```

We created an object `house1` of the outer class by passing “2bhk” to its constructor. Inside the constructor, “2bhk” is assigned to the variable `type`. Then we created an object `bd1` of the inner class `Bedroom` which calls the `printBedroom()` method. Inside the `printBedroom()` method, 2 is assigned to the variable `bedroom_count` and a message is printed.

Now look at the following statements.

```java
// creating object 2 of outer class House
House house2 = new House("4bhk");
		
// creating object 2 of inner class Bedroom
House.Bedroom bd2 = house2.new Bedroom();
bd2.printBedroom();
```

Similarly, we created another object `house2` of the outer class by passing “4bhk” to its constructor making the value of the variable `type` equal to “4bhk”. Again, we created an object `bd2` of the inner class `Bedroom` which calls the `printBedroom()` method. Inside the `printBedroom()` method, 2 is assigned to the variable `bedroom_count` and again a message is printed.

From the above example, we can also say that `house1` is a house of type 2 bhk and has 2 bedrooms and `house2` is a house of type 4 bhk and has 4 bedrooms.

That was all in inner classes. Now let’s move on to the next type of nested class.

### Method Local Inner Class

Uptil now, we saw examples of classes defined inside an outer class, In Java, we can also define a class inside a method of the outer class.

A **method local inner class** is a class defined inside the method of another class. The name “Method Local Inner Class” means an inner class local to a method (defined in a method).

```java
class OuterClass {

    void localMethod() {
        // local method inner class
        class InnerClass {

            void display() {
                System.out.println(
                    "This class is defined inside outer class method"
                );
            }
        }
    }
}
```

In the above declaration, the `InnerClass` class is defined inside the method `localMethod()` of the `OuterClass` class. Thus, `InnerClass` is a local method inner class.

### Creating Object of Method Local Inner Class

If a class is defined inside a method, then its objects can be created and used only within that method. The following example will help you understand better.

```java
class OuterClass {

    private int num = 20;

    void localMethod() {
        // local method inner class
        class InnerClass {

            void display() {
                System.out.println(num);
            }
        }

        // creating object of InnerClass
        InnerClass ic = new InnerClass();
        ic.display();
    }
}

class Test {

    public static void main(String[] args) {
        OuterClass oc = new OuterClass();
        oc.localMethod();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">20</pre>
    </details>
</div>

In the above example, the `OuterClass` class has a method `localMethod()`. Inside the main method, an object `oc` of the `OuterClass` class is created and it calls `localMethod()`.

Look at the statements inside the `localMethod()` method.

```java
void localMethod() {
    // local method inner class
    class InnerClass {
        void display() {
            System.out.println(num);
        }
    }
	
    // creating object of InnerClass
    InnerClass ic = new InnerClass();
    ic.display();
}
```

Here, the `InnerClass` class having a method `display()` is defined. Then an object `ic` of the `InnerClass` class is created and it calls `display()`.

So, when the `localMethod()` method is called, the `InnerClass` class gets defined, its object gets created which calls the `display()` method defined in `InnerClass`.

A method local inner class can’t be instantiated outside the method in which it is defined.

Till JDK 1.7, a method local inner class can only access final local variables. After JDK 1.7, a method local inner class can also access non-final local variables.

If a variable is declared inside the method inside which a local inner class is also defined, then the local inner class can only access the local variable if it is declared `final` till JDK 1.7.

Let’s see another example.

```java
class OuterClass {

    void localMethod() {
        // local method inner class
        class InnerClass {

            int num = 10; // local variable (It must be declared final till jdk 1.7)

            void display() {
                System.out.println(num);
            }
        }

        // creating object of InnerClass
        InnerClass ic = new InnerClass();
        ic.display();
    }
}

class Test {

    public static void main(String[] args) {
        OuterClass oc = new OuterClass();
        oc.localMethod();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

Here, the `InnerClass` class declared inside the method `localMethod()` accesses the variable `num` declared inside the same method `localMethod()`. You must have understood the rest of the program.

## Java Anonymous Inner Class

An **anonymous class** is a nested class that doesn’t have a name. Yes, you read that right. We can define classes in Java which don’t have a name.

An anonymous class must be defined inside another class. That’s why it is called an anonymous inner class.

Since an anonymous class doesn’t have a name, we can’t create its objects separately. Hence, we define the anonymous class and create its objects in a single expression.

### Use of Anonymous Classes

We know that anonymous classes are local inner classes. Anonymous classes should be used if you want to use an inner class only once.

Anonymous classes are mostly if we want to override a method of a class of an interface without creating a class that extends (inherits) the class or implements the interface.

We will see how anonymous classes can help override methods of a class or an interface, but before that let’s look at its syntax.

### Syntax

```java
TypeName anonymous_class_object = new TypeName() {
	// body of anonymous class
};
```

Usually anonymous classes extend classes or implement interfaces.

In the above declaration, there is a single expression in which an anonymous class is defined and its object is created. Here, `TypeName` is the name of the class that the anonymous class extends or the interface that the anonymous class implements and `anonymous_class_object` is the name of the object of the anonymous class.

Whenever the above expression gets executed, an object named `anonymous_class_object` of the anonymous class extending/implementing a class/interface named `TypeName` is created at runtime.

Notice the semicolon at the end of the expression. Also note that this expression will be written inside a method of a class.

The syntax and the concept of anonymous classes will become more clear from some examples. The cases where an anonymous class extends a class and implements an interface are discussed below.

### Anonymous Class Extending a Class

Let’s first see an example without using an anonymous class. In the following example, a class defined inside a class extends another class.

```java
class ParentClass {

    public void display() {
        System.out.println("This is method of ParentClass");
    }
}

class OuterClass {

    // inner class
    class InnerClass extends ParentClass {

        public void display() {
            System.out.println("This is method of InnerClass");
        }
    }
}

class Test {

    public static void main(String[] args) {
        OuterClass oc = new OuterClass();
        OuterClass.InnerClass ic = oc.new InnerClass();
        ic.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is method of InnerClass</pre>
    </details>
</div>

Here, the class named `InnerClass` is defined inside the class named `OuterClass`. Hence, `InnerClass` is an inner class. The `InnerClass` class extends (inherits) another class named `ParentClass` and overrides its method `display()`.

In the main method, as usual we created an object named `ic` of `InnerClass` by creating an object of `OuterClass`.

This was a simple example.

Let’s make the code in the above example shorter by introducing an anonymous class.

```java
class ParentClass {

    public void display() {
        System.out.println("This is method of ParentClass");
    }
}

class OuterClass {

    public void createAnonymousClass() {
        // anonymous inner class
        ParentClass ic = new ParentClass() {
            public void display() {
                System.out.println("This is method of InnerClass");
            }
        };

        ic.display();
    }
}

class Test {

    public static void main(String[] args) {
        OuterClass oc = new OuterClass();
        oc.createAnonymousClass();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is method of InnerClass</pre>
    </details>
</div>

In the above example, the `OuterClass` class has a method `createAnonymousClass()`. Inside the main method, an object `oc` of the `OuterClass` class is created and it calls `createAnonymousClass()`.

The following statements are written inside the `createAnonymousClass()` method.

```java
// anonymous inner class
ParentClass ic = new ParentClass() {
    public void display() {
        System.out.println("This is method of InnerClass");
    }
};

// object ic of anonymous class calling display()
ic.display();
```

Here, an anonymous class is defined that extends the `ParentClass` class with `ic` as its object. Inside the anonymous class, a method `display()` is defined.

So, when the `createAnonymousClass()` method is called, the anonymous class gets defined and its object gets created which calls the `display()` method defined in the anonymous class.

With this example, you must have gotten more comfortable with anonymous classes. Now instead of extending a class, let’s define an anonymous class that implements an interface.

### Anonymous Class Implementing an Interface

The following example demonstrates an anonymous class implementing an interface.

```java
interface ParentInterface {
    public void display();
}

class OuterClass {

    public void createAnonymousClass() {
        // anonymous inner class
        ParentInterface ic = new ParentInterface() {
            public void display() {
                System.out.println("This is method of InnerClass");
            }
        };

        ic.display();
    }
}

class Test {

    public static void main(String[] args) {
        OuterClass oc = new OuterClass();
        oc.createAnonymousClass();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is method of InnerClass</pre>
    </details>
</div>

This example is similar to the previous example. Here, the anonymous class is implementing an interface named `ParentInterface`, instead of extending a class.

Summing up, an anonymous class is usually used to extend a class or implement an interface. It also makes the code short because we define the anonymous class and create its object in a single expression instead of separately defining the class and the object.

Note that anonymous classes should only be used when we want to override the method of a class or an interface only a few times, preferable one. In other cases, we should create a regular class instead of an anonymous class. This is because if we want to override a method five times, then we need to declare five anonymous classes, which is not a good choice.

## Java Static Nested Class

A **static nested class** is a static class defined inside another class.

```java
class OuterClass {

    // code of OuterClass class

    static class StaticNestedClass {
        // code of StaticNestedClass class
    }
}
```

In the above declaration, the `StaticNestedClass` class is defined inside the `OuterClass` class. Thus, `StaticNestedClass` is a static nested class.

Unlike inner classes, a static nested class can’t access the members (variables, methods, etc) of the class inside which it is defined.

### Creating Object of Static Nested Class

An object of a static nested class can be created without creating any object of the outer class i.e. the class inside which it is defined.

Static nested classes can’t access the members of the classes inside which they are defined.

Objects of static nested classes can be created without creating an object of the classes inside which they are defined.

Let’s see an example of a static nested class.

```java
class OuterClass {

    // static nested class
    static class StaticNestedClass {

        int num = 10;

        void display() {
            System.out.println(num);
        }
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of static inner class
        OuterClass.StaticNestedClass sc = new OuterClass.StaticNestedClass();

        sc.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

In this example, the static nested class `StaticNestedClass` is defined inside the outer class `OuterClass`. The `StaticNestedClass` class has a method named `display()`.

In the main method, we used the class name of the outer class to create an object `sc` of the static nested class `StaticNestedClass` without creating an object of the outer class as shown below.

`OuterClass.StaticNestedClass sc = new OuterClass.StaticNestedClass();`

Thus, the syntax for creating an object of a static nested class is shown below.

`OuterClass.StaticNestedClass nested_class_object = new`

`OuterClass.StaticNestedClass();`

Here, `OuterClass` is the outer class, `StaticNestedClass` is the static nested class and `nested_class_object` is the object of the static nested class.

We are almost done. Before wrapping up, let’s see what would happen if we try to access a member of the outer class inside the static nested class.

```java
class OuterClass {

    int num = 10;

    // static nested class
    static class StaticNestedClass {

        void display() {
            System.out.println(num);
        }
    }
}

class Test {

    public static void main(String[] args) {
        OuterClass.StaticNestedClass sc = new OuterClass.StaticNestedClass();

        sc.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:7: error: non-static variable num cannot be referenced from a static context
            System.out.println(num);
              ^
1 error</pre>
    </details>
</div>

As expected, we got an error. This is because we accessed the variable `num` of the `OuterClass` class inside the static nested class `StaticNestedClass`.

So we learned different types of nested classes and their significance. Nested classes are mainly useful in programs for organising classes with similar meaning together.

> Giving up is for rookies.
>
> \- Hercules
