# Java Annotations

Java Annotations are used to add additional information about our program.

You know what comments are. Comments are written in a program to give information about the different parts of the program so that a person can understand what the program does by reading the comments. Similarly, we have annotations in Java. They are also used to give information about the different parts of a program.

#### Then what is the difference between comments and annotations?

Both comments and annotations are just used to give information about a program and don't interfere with the working of the program. In fact, both are not part of the program itself.

The major difference between comments and annotations is that comments are used to give information about the code for the programmer or someone reading the code to understand, whereas annotations are used to give detailed information about the code for the compiler to understand. This means that the compiler understands the information provided by an annotation in a program.

Comments start with `//` whereas annotations start with `@`.

Let’s see an example of an annotation.

Suppose we want to define a functional interface (We read about functional interface in [Lambda Expressions](https://web.archive.org/web/20240222021053/https://www.codesdope.com/course/java-lambda-expressions/)). Functional interface is an interface which has only one abstract method. If by mistake, we define two abstract methods in the interface, then the compiler would not throw an error or warning because the compiler simply doesn’t know that we want to make the interface as a functional interface, as shown below.

```java
interface MyInterface {
    public void MethodOne();

    public void MethodTwo();
}

class Test {

    public static void main(String[] args) {}
}
```

In the above program, we wanted the interface named `MyInterface` to be a functional interface. But since we defined two methods `MethodOne()` and `MethodTwo()` inside it, it is not a functional interface.

The program got compiled successfully because the compiler didn’t know that we wanted a functional interface.

So let’s tell the compiler that we want the interface to be a functional interface by using the `@FunctionalInterface` annotation. `@FunctionalInterface` is a predefined annotation in Java which is used to tell the compiler that an interface is a functional interface. Look at the following program.

```java
@FunctionalInterface
interface MyInterface {
    public void MethodOne();

    public void MethodTwo();
}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:1: error: Unexpected @FunctionalInterface annotation<br/>
@FunctionalInterface<br/>
^<br/>
  MyInterface is not a functional interface<br/>
    multiple non-overriding abstract methods found in interface MyInterface<br/>
1 error</pre>
    </details>
</div>

In this program, we defined the interface named `MyInterface` as a functional interface by writing the `@FunctionalInterface` annotation above the interface definition. This annotation tells the compiler that `MyInterface` is a functional interface. So, when we defined two methods inside `MyInterface`, the compiler threw an error.

This means that if a programmer defines more than one abstract method inside the interface or violates any other rule of a functional interface, the compiler will throw an error. So this solved our problem.

That was so cool!

Let’s learn more about annotations.

---

## Placement of Annotations

An annotation can be placed above a declaration. In the previous example, we placed the annotation above the declaration of the interface.

However, from Java 8 onwards, an annotation can also be placed before a declaration.

### Above Declarations

As already mentioned, annotations can be placed above the declaration of program elements (entities) like class, interface, method, etc. Let’s again take the same example using the `@FunctionalInterface` annotation.

```java
@FunctionalInterface
interface MyInterface {
    public void MethodOne();

    public void MethodTwo();
}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:1: error: Unexpected @FunctionalInterface annotation<br/>
@FunctionalInterface<br/>
^<br/>
  MyInterface is not a functional interface<br/>
&amp;nbsp-&amp;nbsp-&amp;nbsp-&amp;nbsp-multiple non-overriding abstract methods found in interface MyInterface<br/>
1 error</pre>
    </details>
</div>

Here, the `@FunctionalInterface` annotation is placed above the interface `MyInterface` to specify that it is a functional interface. Since we defined two methods inside the interface, we got an error on compilation.

### Before Declarations

From Java 8, we can also place annotations before an entity.

```java
@FunctionalInterface
interface MyInterface {
    public void MethodOne();

    public void MethodTwo();
}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Main.java:1: error: Unexpected @FunctionalInterface annotation
@FunctionalInterface interface MyInterface {<br/>
^<br/>
  MyInterface is not a functional interface<br/>
    multiple non-overriding abstract methods found in interface MyInterface<br/>
1 error</pre>
    </details>
</div>

As you can see in the above example, we placed the annotation @FunctionalInterface before the declaration of the interface `MyInterface` to specify that it is a functional interface.

Annotations are interesting. Let’s look at some more predefined annotations.

---

## Predefined Annotations

### @Override

The `@Override` annotation specifies that a method in a class is overriding a method in the superclass. Note that when a method overrides another method, it must have the same name, parameters and return type.

```java
// parent class
class ParentClass {

    public void myMethod() {
        System.out.println("This is method of parent class");
    }
}

// child class
class ChildClass extends ParentClass {

    @Override
    public void myMethod(int n) {
        System.out.println("This is method of child class");
    }
}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:10: error: method does not override or implement a method from a supertype<br/>
    @Override<br/>
    ^<br/>
1 error</pre>
    </details>
</div>

In this example, the class `ChildClass` inherits the class `ParentClass`. We want to override the method `myMethod()` of the parent class in the child class. As a result, we applied the `@Override` annotation above the declaration of the method in the child class.

But while defining the method `myMethod()` in the child class, we gave an int as a parameter whereas the method in the parent class doesn’t take a parameter. This violates the overriding rule. Therefore, we got an error on compilation because the `@Override` annotation specified to the compiler that the method in the child class will override the parent class method, but it is not overriding.

### @Deprecated

If an entity is deprecated, it means that the entity was once used but now it is not important and should no longer be used.

The `@Deprecated` annotation specifies that an entity like class, method, variable, etc. has been replaced by another entity and thus should no longer be used. In other words, it tells the compiler that the entity is deprecated.

When we use an entity that has been declared deprecated using the annotation, we will get a warning but will not get any compilation error.

```java
class MyClass {

    @Deprecated
    public static void myMethod() {
        System.out.println("This is a deprecated method");
    }
}

class Test {

    public static void main(String[] args) {
        MyClass.myMethod();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Note: Test5.java uses or overrides a deprecated API.<br/>Note: Recompile with -Xlint:deprecation for details.<br/>This is a deprecated method</pre>
    </details>
</div>

In this example, we declared the static method `myMethod()` inside the class `MyClass` as deprecated using the `@Deprecated` annotation above its definition. Hence, we should not use this method anywhere in our program.

Since the method `myMethod` is static, we called it inside the main method of the class `Test` by writing `MyClass.myMethod()`. On compiling the program, we got a warning because we called a deprecated method inside the main method.

<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
             The compiler doesn’t throw a compilation warning if a deprecated entity is used within the same class.
          </div>
</div>
</div>

If a deprecated entity is accessed somewhere within the same class inside which it is defined, then we wouldn’t get any compilation warning. Let’s see an example supporting this fact.

```java
class Test {

    @Deprecated
    public static void myMethod() {
        System.out.println("This is a deprecated method");
    }

    public static void main(String[] args) {
        myMethod();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is a deprecated method</pre>
    </details>
</div>

In the above example, the method `myMethod()` inside the class `Test` is declared as deprecated using the `@Deprecated` annotation above its definition. We called this deprecated method inside the main method.

We didn’t get a warning on compilation even when we called a deprecated method because the deprecated method `myMethod()` is defined inside the class `Test` and it is called inside the main method which is also defined inside the class `Test`.

### @SuppressWarnings

The `@SuppressWarnings` annotation tells the compiler to suppress if any warning comes while executing the program.

There are two types of warnings - **deprecated** and **unchecked**. We can specify the type of warning we want to suppress by passing the warning type as an argument to the `@SuppressWarnings()` annotation, as shown in the following syntax.

`@SuppressWarnings("WarningType")`

Here, `WarningType` is the type of warning.
For example, to suppress the **deprecated** warnings, write the annotation as shown below.

`@SuppressWarnings("deprecated")`

We can also suppress multiple warnings using this annotation by using the following syntax.

`@SuppressWarnings({"WarningType1", "WarningType2"})`

Here, `WarningType1` and `WarningType2` are the types of warning.
For example, to suppress both the **deprecated** and **unchecked** warnings, write the annotation as shown below.

`@SuppressWarnings({"deprecated", "unchecked"})`

Note let’s see an example in which unchecked warnings are thrown without using the `@SuppressWarnings()` annotation.

```java
import java.util.*;

class Test {

    public static void main(String args[]) {
        ArrayList mylist = new ArrayList();
        mylist.add("one"); // this statement throws an unchecked warning
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Note:<br/>Test.java uses unchecked or unsafe operations.<br/>Note: Recompile with -Xlint:unchecked for details.</pre>
    </details>
</div>

This program got compiled and executed successfully but we got an unchecked warning on compilation. We got this warning on compiling the statement `mylist.add("one")` because we haven’t specified the type of the array list in the following statement.

`ArrayList mylist = new ArrayList();`

We can remove the warning by modifying the above statement to specify the type String of the arraylist as shown below.

`ArrayList<string> mylist = new ArrayList<>();`

Suppose we don’t want to modify the above statement. Then to prevent our program from throwing unchecked warnings, we can use the `@SuppressWarnings()` annotation as done below.

```java
import java.util.*;

class Test {

    @SuppressWarnings("unchecked")
    public static void main(String args[]) {
        ArrayList mylist = new ArrayList();
        mylist.add("one");
    }
}
```

In the above example, we wrote `@SuppressWarnings("unchecked")` above the main method because we got the warning on executing a statement in the body of the main method. We could have also written this annotation above the class `Test` because we got the warning on executing a method of this class. Writing this annotation prevented our program from throwing any unchecked warning on compilation.

### @FunctionalInterface

We have already seen an example using this interface. Let’s discuss it again. The `@FunctionalInterface` annotation specifies that an interface is a functional interface. An interface is a functional interface when it has a single abstract method.

```java
@FunctionalInterface
interface MyInterface {
    public void MethodOne();

    public void MethodTwo();
}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:1: error: Unexpected @FunctionalInterface annotation<br/>
@FunctionalInterface<br/>
^<br/>
  MyInterface is not a functional interface<br/>
    multiple non-overriding abstract methods found in interface MyInterface<br/>
1 error</pre>
    </details>
</div>

We defined an interface named `MyInterface` as a functional interface using the `@FunctionalInterface` annotation above its definition. So, when we defined two methods inside `MyInterface`, the compiler threw an error.

It is a good practice to include predefined annotations in your code so that the compiler understands when you need to define a functional interface, override a method, etc. So start including annotations in your code.

<div id="quote">
<div><span>Be yourself; everyone else is already taken.</span></div>
<div><span>- Oscar Wilde</span></div>
</div>

---
