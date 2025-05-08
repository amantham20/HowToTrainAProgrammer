# Java Method Overriding
<hr/>
In the last chapter, we learned about inheritance. In this chapter, we will look at method overriding which is often used when dealing with inheritance.

Think of a case where the parent class and the child class have methods with the same name, say display. This feature is called **method overriding**.  Let’s first look at the use of method overriding before discussing it in detail.
<hr/>
## Why Method Overriding?
Suppose we created a class named `Animal` with a method named `printSound()` that prints the sound of an animal. Dog, cat and pig are different types of animals, so we created three subclasses named `Dog`, `Cat` and `Pig` of the class `Animal`.

Since different animals make different sounds, we can create different methods for returning the sound in the classes `Dog`, `Cat` and `Pig` as shown below.

```java
class Animal {

    public void printSound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {

    public void printDogSound() {
        System.out.println("Dogs bark");
    }
}

class Cat extends Animal {

    public void printCatSound() {
        System.out.println("Cats meow");
    }
}

class Pig extends Animal {

    public void printPigSound() {
        System.out.println("Pigs snort");
    }
}
```

Here, we defined different methods to print sound in different classes. Hence, we will have to remember the names of different methods to print different animal sounds. For example, the object of the class `Cat` will call the method named `printCatSound()` to print the sound of a cat and the object of the class `Pig` will call the method named `getPigArea()` to print the sound of a pig.

A better solution is to use method overriding, by creating methods in the subclasses having the same name as the method in the superclass as shown below.

```java
class Animal {

    public void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    public void printSound() {
        System.out.println("Dogs bark");
    }
}

class Cat extends Animal {

    public void printSound() {
        System.out.println("Cats meow");
    }
}

class Pig extends Animal {

    public void printSound() {
        System.out.println("Pigs snort");
    }
}
```

In this case, we defined methods in all the subclasses with the same name `printSound()`. Now, we will always call the method named `printSound()`.

For example, the object of `Cat` will call the `printSound()` method to print the sound of a cat and the object of `Pig` will also call the `printSound()` method to print the sound of a pig.

Hence, we gave the same name to the methods of different subclasses because they all implement the same functionality varying slightly for different subclasses and giving the same name makes code more organised, less complex and easier to debug.

Method overriding is useful when we want to implement a functionality based on the subclass. In other words, it is useful when a class has multiple subclasses and each subclass wants to use a parent class method. In such a case, method overriding allows each subclass to implement the parent class method according to its requirement without making any change in the actual parent class method.

Having looked at the need of method overriding, let’s understand it in detail with examples.
<hr/>
## Method Overriding
Let’s understand method overriding with the help of an example.

```java
class Animal {

    public void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    public void printSound() {
        System.out.println("Dogs bark");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        d.printSound();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Dogs bark
</pre>
    </details>
</div>

Here, the subclass `Dog` and the superclass `Animal` have methods with the same name `printSound()`. When the object `d` of the subclass `Dog` calls the `printSound()` method, the method of the subclass `Dog` gets called and not that of the superclass.

So, in this case, the `printSound()` method of the subclass overrides the `printSound()` method of the superclass. This is called **method overriding**.

When a subclass and the superclass have methods with the same name, parameters and return type, the method of the subclass overrides the method of the superclass.

### Conditions for Method Overriding in Java
Conditions for method overriding are -

1.  Methods in subclass and superclass must have the same name
2.  Method in subclass and superclass must have the same parameters
3.  Methods in subclass and superclass must have the same return type

Look at another example.

```java
class Animal {

    public void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    public void printSound() {
        System.out.println("Dogs bark");
    }
}

class Cat extends Animal {

    public void printSound() {
        System.out.println("Cats meow");
    }
}

class Pig extends Animal {

    public void printSound() {
        System.out.println("Pigs snort");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        Cat c = new Cat();
        Pig p = new Pig();

        d.printSound();
        c.printSound();
        p.printSound();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Dogs bark
Cats meow
Pigs snort
</pre>
    </details>
</div>

In this example, `Dog`, `Cat` and `Pig` are subclasses of the class `Animal`. The class Animal has a method `printSound()` to print the sound of the animal. Since the sound of dogs, cats and pigs are different, each subclass wants to implement the method `printSound()` differently.

As a result, each subclass has overridden the `printSound()` method of `Animal` to implement its own functionality.

### Role of Access Modifiers in Method Overriding
Apart from the 3 conditions required for method overriding to take place, there is also a fourth condition - access modifier of the overriding subclass method must not have a smaller access range than the access range of the access modifier of the overridden superclass method.

The order of access range of the access modifiers is - **public > default > protected > private**. (Note that when a method is not declared `public`, `protected` or `private`, then it is said to have `default` access modifier)

`public` has the largest access range because a public entity can be accessed at the most number of places and `private` has the smallest access range because a private entity can be accessed at the least number of places i.e. only within the class in which it is defined.

Therefore, the following points regarding the access modifiers of methods must be considered for method overriding.

*   If the superclass method is public, then the subclass method must be public.
*   If the superclass method is default, then the subclass method must be default or public.
*   If the superclass method is protected, then the subclass method must be protected, default or public.
*   The superclass method must not be private. (We already know this)

Look at the following example.

```java
class Animal {

    protected void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    public void printSound() {
        System.out.println("Dogs bark");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        d.printSound();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Dogs bark
</pre>
    </details>
</div>

In this example, when the object `d` of the subclass `Dog` calls the `printSound()` method, the method of the subclass `Dog` gets called. Thus, method overriding took place.

Notice that the `printSound()` method of the parent class `Animal` is declared as `protected`. So, the access modifier of the `printSound()` method of the child class can be `protected`, `default` or `public`. Since the method of the subclass `Dog` is declared as `public`, method overriding took place.

Now let’s try to give a smaller range access modifier to the subclass method.

```java
class Animal {

    protected void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    private void printSound() {
        System.out.println("Dogs bark");
    }
}

class Test {

    public static void main(String[] args) {
        Dog d = new Dog();
        d.printSound();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:8: error: printSound() in Dog cannot override printSound() in Animal
    private void printSound() {
           ^
  attempting to assign weaker access privileges; was protected
Test.java:16: error: printSound() has private access in Dog
            d.printSound();
             ^
2 errors
</pre>
    </details>
</div>

Here, the range of the access modifier of the `printSound()` method of the subclass `Dog` is smaller than the range of the access modifier of the printSound() method of the superclass `Animal`. This violates the condition necessary for method overriding and hence we got an error on running the program.
<hr/>
## Assigning Child Object to Parent Class Variable
This subtopic is not frequently used in Object Oriented Programming, but it is good to know the concept. Before discussing it, let’s see what stack and heap memories are.

### Stack Memory and Heap Memory
We know that everything in Java is stored in memory. For example, variables, objects, etc are all stored in memory. This memory is divided into two areas - stack memory and heap memory. Let’s discuss both these memory types briefly.

Stack memory and heap memory are not the same as the stack and heap data structures. They just have the same name.

The stack memory is used to store the data that is known to the compiler during compile time. It is a temporary memory because it stores the entities of the method that is currently getting executed. You know that local variables can be accessed inside the method in which they are defined and can’t be accessed outside that method. Thus, whenever a method gets called in a program, the local variables defined in it are allocated stack memory and when the method call is over, the memory assigned to the variables is deallocated. So, local variables and other temporary data in a program are stored in the stack memory.

Now let’s talk about heap. Unlike stack memory, the entities stored in heap memory are not removed. Hence, it is used to store global variables and all the objects. It is allocated at runtime. This means that after compilation, the heap memory gets allocated when execution starts.

Summing up, stack memory is assigned at compile time and stores the variables and temporary data of only the currently running method. On the other hand, heap memory is assigned at runtime and stores objects.

Having known the difference between these two types of memory, let’s proceed further.

### Memory Allocation to Reference Variables and Objects
Suppose there is a class named `MyClass`. Let’s create an object of this class.

`MyClass ref = new MyClass();`

Let’s understand how memory is allocated to this class object.

Here, `ref` is a variable of the class `MyClass`. Such variables of classes are called **reference variables**. These reference variables are mostly stored in the stack memory at compile time but can be stored in the heap memory as well in certain conditions. Let’s for now assume that `ref` is stored in the stack memory.

The statement `new MyClass()` created an object of `MyClass` at runtime in the heap memory. When this object is created, the reference variable `ref` points to the object i.e. it stores the address of the memory location in which the object is stored. We can also say that the reference variable `ref` is assigned the reference to the object of `MyClass`.

Now you must have understood how memory is assigned to objects in Java.

### Referencing Objects of Subclass
Do you know that a reference variable of a class can also be assigned the reference to its subclass object? Yes, it is possible. Let’s show how.

Suppose there is a parent class named `ParentClass` and its child class named `ChildClass`. Now look at the following statement.

`ParentClass ref = new ChildClass();`

In the above statement, we created a reference variable `ref` of `ParentClass` by writing `ParentClass ref` and an object of the `ChildClass` by writing `new ChildClass()`. The reference variable `ref` of `ParentClass` is pointing to the object of `ChildClass`.

Let’s implement this in an example.

```java
class Animal {

    public void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    public void printSound() {
        System.out.println("Dogs bark");
    }
}

class Test {

    public static void main(String[] args) {
        Animal a = new Dog();
        a.printSound();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Dogs bark
</pre>
    </details>
</div>

Notice that a reference variable `a` of the superclass `Animal` is referencing an object of the subclass `Dog`. When the object referenced by `a` calls the method `printSound()` which is present in both the classes, the method of the subclass `Dog` gets called. The program runs fine!

Now look at another example.

```java
class Animal {

    public void printSound() {
        System.out.println("Sound method of parent class");
    }
}

class Dog extends Animal {

    public void printDogSound() {
        System.out.println("Dogs bark");
    }
}

class Test {

    public static void main(String[] args) {
        Animal a = new Dog();
        a.printDogSound();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:16: error: cannot find symbol
            a.printDogSound();
             ^
  symbol:   method printDogSound()
  location: variable a of type Animal
1 error
</pre>
    </details>
</div>

We got a compilation error. This is because `a` is a reference variable of `Animal` but references an object of its subclass `Dog`. This means that you can't access the methods which are not defined in the superclass if your reference variable is of the superclass.

When a reference variable of a superclass is referencing an object of the subclass, then the object can only access the members (variables, methods, etc.) defined in the superclass.

Hope you understood the purpose of using method overriding.

The way to get started is to quit talking and begin doing.

- Walt Disney

<hr/>
