# Java Access Modifiers

Access modifiers are used to limit the access of variables, methods, classes, etc., in a program. For example, we can prevent the use of a variable (like printing the value of the variable) outside of the class in which it is defined using the **private** access modifier.

To understand the need of access modifiers, take a real-life example of a washing machine.

A washing machine starts when we switch it on and stops when we switch it off. Thus, we have access to the power on and power off buttons but don’t have access to the internal working of the machine. Similarly in many cases, we want to limit the access of some entities in a program. This is where access modifiers are used.

In the chapter [Classes and Objects](https://web.archive.org/web/20240416070836/https://www.codesdope.com/course/java-classes-and-objects/), we declared class variables and class methods as private and public. **Private** and **public** are access modifiers. We will now learn more about access modifiers in this chapter.

**Access modifiers** are used to change the visibility and accessibility of variables, methods, classes and other entities. These are of four types.

1.  Public
2.  Private
3.  Protected
4.  Default

## Java Public Access Modifier

Declaring an entity like variable, method, class, etc., as `public` means that the entity can be accessed from anywhere in the program.

For example, we can print a variable (attribute) defined in a class anywhere outside the class.

An entity is declared as public by writing the `public` keyword at the beginning of its definition.

Take the following example.

```java
class Student {

    // public variable
    public String name;

    // constructor
    public Student(String n) {
        name = n;
    }

    // public method
    public void printDetails() {
        System.out.println("This is a public method");
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student("John");

        // accessing public variable
        System.out.println(st.name);

        // accessing public method
        st.printDetails();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">John
This is a public method</pre>
    </details>
</div>

Here, the variable `name` and the method `printDetails()` defined in the `Student` class are declared as `public` using the public keyword. So, they can be accessed from outside the class.

`st.name` → The public variable `name` is accessed from outside the `Student` class using its object.

`st.printDetails()` → The public method `printDetails()` is accessed from outside the `Student` class using its object.

Note that we will be able to access the variables and methods defined in a class from outside the class using its object even if they are not declared as public, as shown below.

```java
class Student {

    public String name;

    public Student(String n) {
        name = n;
    }

    public void printDetails() {
        System.out.println("This is a public method");
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student("John");

        System.out.println(st.name);
        st.printDetails();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">John
This is a public method</pre>
    </details>
</div>

In this example, we didn’t declare the class variable and class method as `public` but still we are able to access it outside the `Student` class. This is because it is the default behaviour also. However, it is better to declare entities as `public` if we want to use them outside the class in which they are defined.

## Java Private Access Modifier

Declaring an entity as `private` means that the entity can’t be accessed from outside the class in which it is defined. Thus, the private variables and methods defined in a class can be accessed from only within that class.

An entity is declared as `private` by writing the private keyword at the beginning of its definition.

Let’s declare a variable defined in a class as private and try to access it from outside the class.

```java
class Student {

    // private variable
    private String name;
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();

        // accessing private variable
        st.name = "John";
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:11: error: name has private access in Student
                st.name = "John";
                ^
1 error</pre>
    </details>
</div>

Here, we declared the variable `name` defined in the `Student` class as private by using the `private` keyword. Thus, it can be accessed from only within the `Student` class.

`st.name = “John”` → The object of the `Student` class tried to access the private variable `name` from outside the class. Hence, we got an error.

If a class variable is declared as private, then to modify it or print its value, a class method declared as public can be used. Let’s modify and print the value of the attribute `name` in the above example using public class methods.

```java
class Student {

    // private variable
    private String name;

    // public method
    public void setName(String n) {
        name = n;
    }

    // public method
    public String getName() {
        return name;
    }
}
 
class Test {
	public static void main (String[] args) {
		Student st = new Student();
		
		// accessing public method
		st.setName("John");
		
		// accessing public method
		System.out.println(st.getName());
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">John</pre>
    </details>
</div>

In this example, the object `st` of the `Student` class calls the public methods `setName()` and `getName()` of the class to modify and print the value of the private class variable `name`.

It is a good practice to declare class variables as private and class methods as public in normal conditions.

## Java Protected Access Modifier

Declaring an entity as `protected` means that the entity can only be accessed from the class in which it is defined and the subclasses of the class. We will learn about subclasses in a [later chapter](https://web.archive.org/web/20240416070836/https://www.codesdope.com/course/java-inheritance/).

The difference between `private` and `protected` modifiers is that entities declared as `private` can only be accessed from their class whereas entities declared as `protected` can only be accessed from class as well as the subclasses of that class.

An entity is declared as `protected` by writing the protected keyword at the beginning of its definition.

## Java Default Access Modifier

If we do not specify any modifier for a variable, method, class, etc., then by default it has the `default` modifier.

The `default` modifier is the same as the `public` modifier in normal conditions. It only differs from the `public` modifier when a **package** is used in the program. If packages are used, then a default variable, method, class, etc., defined in a package will be accessible from within that package and will not be visible outside that package or in other packages, whereas a public  variable, method, class, etc. can be accessed from anywhere.

For example, a variable defined in a class in package A can be accessed from all the classes present in the package A, but can’t be accessed from any class in package B.

If no package is used, then there is no difference between the `default` modifier and the `public` modifier.

For now, you can just focus on the private and public modifiers as we will be using only these in our programs.

> We May Encounter Many Defeats But We Must Not Be Defeated.
>
> -   Maya Angelou


<a href="22-java-inheritance.md" class="next">Next</a>
