# Java static Keyword
***
The `static` keyword states that a member like variable or method defined in a class belongs to the class rather than the object of the class.

Before going forward, let us introduce two terminologies - **instance attributes** and **class attributes**.

Instance attributes are the attributes/variables defined in a class which belong to the objects of that class. Look at the following example.

```java
class Student {

    String name;

    public Student(String n) {
        name = n;
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John");
        Student st2 = new Student("Julie");

        System.out.println(st1.name);
        System.out.println(st2.name);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">John
Julie</pre>
    </details>
</div>

In this example, when the object `st1` of the class `Student` is created, the constructor gets called with the argument “John” making the parameter `n` equal to “John”. Inside the constructor, the statement `name = n` assigns the value “John” to the attribute `name`.

As a result, the name of the object `st1` is “John”. Similarly, the name of the object `st2` is assigned “Julie”. Here, the value of the attribute `name` is different for both the objects of the class. Therefore, here `name` is an **instance attribute** or **instance variable** (the term instance is used for object).

Till now, all the programs we saw in the previous chapters had instance variables.

On the other hand, suppose you want to define a variable in a class whose value is the same for all the objects of that class. Such a variable is a **class attribute**. Class attributes can be created using the `static` keyword.

Apart from creating a class attribute, there are other advantages also of static which we will discuss in this chapter.

The following members defined in a class can be declared as static.

1.  Variables
2.  Methods
3.  Blocks
4.  Classes

Let’s understand why and how these members are declared as static.

***
## Java static Variable
When a variable in a class is declared as static, it belongs to the class rather than the object. A static variable/attribute is also called class variable/attribute.

Let’s first try to create a class variable without using `static`. Suppose there are two students in a school. Both the students will have different names but the same college.

So, `name` must be an instance variable and `college` should be a class variable, as shown in the below example.

```java
class Student {

    String name;
    String college = "ABC";

    public Student(String n) {
        name = n;
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John");
        Student st2 = new Student("Julie");

        System.out.println("Name: " + st1.name);
        System.out.println("College: " + st1.college);
        System.out.println("Name: " + st2.name);
        System.out.println("College: " + st2.college);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: John
College: ABC
Name: Julie
College: ABC</pre>
    </details>
</div>

In this example, the class `Student` has two variables: `name` and `college`.

`String college = "ABC"` → This statement declares a variable `college` with the value “ABC”. Since this value is assigned outside all the methods and constructors, the value of `college` will be “ABC” for all the objects of the class.

In the code, you can see that whenever a new object is created, it is assigned a different `name` in the constructor. So, the value of the variable `name` is different but the value of the variable `college` is the same for both the objects.

Thus, the `college` variable works like a class variable without using `static`. Then why should we use `static` to create a class variable?

In the above example, `college` works like a class variable but it is an instance variable only. Whenever an object (instance) of a class is created, all the instance variables are allocated memory for that object. Different memories are provided for the `name` and `college` attributes for the two objects, even though the value of `college` is the same for both.

<img alt="space for variable in Java" src="https://web.archive.org/web/20240422031352im_/https://www.codesdope.com/pa-images-bucket/courses/java/p32.png" style="max-width:80%;height:auto;"/>

Suppose there are 100 students in the college. In that case, assigning different memory locations for the `college` attribute for different objects even though its value is the same for all objects doesn’t make much sense. This is where we will use `static`.

If a variable is declared `static`, it belongs to the class rather than the objects and takes a single memory location which is shared for all the objects.

<img alt="static variable space allocation in Java" src="https://web.archive.org/web/20240422031352im_/https://www.codesdope.com/pa-images-bucket/courses/java/p33.png" style="max-width:70%;height:auto;"/>

A static variable is also called a class variable.

To declare a variable as static, write the `static` keyword before the data type of the variable at the time of its declaration.

```java
class Student {

    String name;
    static String college = "ABC";

    public Student(String n) {
        name = n;
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John");
        Student st2 = new Student("Julie");

        System.out.println("Name: " + st1.name);
        System.out.println("College: " + st1.college);
        System.out.println("Name: " + st2.name);
        System.out.println("College: " + st2.college);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: John
College: ABC
Name: Julie
College: ABC</pre>
    </details>
</div>

Notice the following statement in the above program.

`static String college = "ABC";`

We declared the `college` variable as static. So, now it will just take a single memory location which will be common for all the objects of the class.

A static variable can be accessed directly by using the class name without creating any object of the class.

We know that a static variable belongs to a class. Thus, it can be accessed using the class name also.

```java
class Student {

    static String college = "ABC";
}

class Test {

    public static void main(String[] args) {
        System.out.println("College: " + Student.college);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">College: ABC</pre>
    </details>
</div>

In the above example, we accessed the static variable `college` of the `Student` class by writing `Student.college`.

We can’t access an instance variable by a class name. Let’s see what happens when we try to do that.

```java
class Student {

    String college = "ABC";
}

class Test {

    public static void main(String[] args) {
        System.out.println("College: " + Student.college);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:7: error: non-static variable college cannot be referenced from a static context
                System.out.println("College: " + Student.college);
                                                     ^
1 error</pre>
    </details>
</div>

Here, the variable `college` is not a static variable and so trying to access it directly using the class name by writing `Student.college` gave an error.

### Program of Counter
Let’s see another example in which a variable is used to count the number of objects of a class without using `static`.

```java
class Counter {

    int count = 0;

    Counter() {
        count++;
        System.out.println("No of objects: " + count);
    }
}

class Test {

    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
        Counter c4 = new Counter();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">No of objects: 1
No of objects: 1
No of objects: 1
No of objects: 1</pre>
    </details>
</div>

Here, an instance variable `count` is defined in the class `Counter`. This variable is incremented in the constructor.

Whenever an object of `Counter` is created, the instance variable `count` is allocated memory and assigned the value 0. In the constructor, its value is increased to 1 for that particular object. Thus, each object will have a different copy of the `count` variable. In other words, the value of `count` will be 1 for each object.

Let’s make `count` a static variable so that it belongs to the class and not objects.

```java
class Counter {

    static int count = 0;

    Counter() {
        count++;
        System.out.println("No of objects: " + count);
    }
}

class Test {

    public static void main(String[] args) {
        Counter c1 = new Counter();
        Counter c2 = new Counter();
        Counter c3 = new Counter();
        Counter c4 = new Counter();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">No of objects: 1
No of objects: 2
No of objects: 3
No of objects: 4</pre>
    </details>
</div>

In this example, we just made a change in the following statement from the previous example.

`static int count = 0;`

We declared the variable `count` as `static`. So, it belongs to the class and hence is allocated the memory only once.

Initially, the value of `count` is 0. When the first object `c1` is created, the constructor gets called and the value of `count` increases by 1 making it 1. Similarly, when the second object `c2` is created, the constructor gets called and the value of `count` is increased to 2. Thus, you can see that after the value of `count` got changed when the object `c1` was created, the updated value of `count` was available for the object `c2`.

Hope you understood how static variables (class variables) are different from instance variables.

***
## Java static Method
Like static variables, static methods can also be accessed without creating an object of the class in which they are defined. Thus, they belong to the class and not the objects of the class.

Static methods are mainly used to access or modify static variables (class variables).

A static method is also called a class method.

A static method can be accessed directly by using the class name without creating any object of the class.

To declare a method as static, write the `static` keyword before the return type of the method when defining it.

Static variables can be accessed from both static and non-static methods.

Static methods can access static variables but not non-static variables.

Look at the following example.

```java
class Student {

    // non-static variable
    String name;

    // static variable
    static String college = "ABC";

    public Student(String n) {
        name = n;
    }

    // static method
    public static void updateCollege() {
        college = "DEF";
    }

    // non-static method
    public void printDetails() {
        System.out.println("Name: " + name + ", College: " + college);
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John");
        Student st2 = new Student("Julie");

        // calling static method
        Student.updateCollege();

        st1.printDetails();
        st2.printDetails();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: John, College: DEF
Name: Julie, College: DEF</pre>
    </details>
</div>

In this example, the class `Student` has a non-static variable `name`, a static variable `college`, a non-static method `printDetails()` and a static method `updateCollege()`.

Inside the static method `updateCollege()`, the value of the static variable `college` is changed to “DEF”. In the regular method `printDetails()`, the values of the non-static variable `name` and the static variable `college` are printed.

Look at the following statement.

`Student.updateCollege();`

In this statement, the static method `updateCollege()` is directly accessed using the class name without requiring any object.

So, whenever you want to access or modify the value of a static variable without creating an object, a static method can be used.

As already mentioned, static methods can’t access non-static variables.

Let’s try to access an instance variable inside a static method.

```java
class Student {

    // non-static variable
    String name;

    // static method
    public static void printName() {
        System.out.println(name);
    }
}

class Test {

    public static void main(String[] args) {}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Main.java:7: error: non-static variable name cannot be referenced from a static context
                System.out.println(name);
                                   ^
1 error</pre>
    </details>
</div>

We got an error as expected.

Let’s look at some important points related to static methods.

*   Static methods belong to the class in which they are defined and not to the objects. As a result, they can be accessed using the class name without creating any object of the class.
*   Static methods can access static variables but can’t access non-static variables.
*   Static methods can be accessed from static as well as non-static methods.
*   Static methods can’t be overridden.
*   Abstract methods can’t be static.
*   We can’t use `this` or `super` keywords inside a static method.

So this was all about static methods. Let’s see the advantages of using static methods.

### Advantage of static Methods
The major advantage of using static methods is that they can be used to access or modify static variables and other static methods that don’t depend on objects.

***
## Java static Block
Before introducing static blocks, let’s see what blocks are in Java.

### Java Block
A block or block statement is a sequence of zero or more statements enclosed within braces in a program. A simple example of a block is given below.

```java
{  // block starts
	int num = 10;
	num++
}  // block ends
```

In the above example, we have a block having two statements. This block initializes a variable named `num` by assigning it 10 and then increments its value by 1.

Now let’s use this block in a program.

```java
class Test {

    public static void main(String[] args) {
        System.out.println("This is a random statement");

        // block
        {
            int num = 10;
            num++;
            System.out.println(num);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is a random statement
11</pre>
    </details>
</div>

In the above example, the first statement inside the main method gets executed first printing *This is a random statement*. After that, a block having three statements got executed printing 11. As you can see, here we have just clubbed three statements together creating a block.

Have we used blocks before in other forms too? Yes, we have used blocks to mark the body of methods, classes, if...else statements, etc. For example, look at the following program.

```java
class Test {

    public static void main(String[] args) {
        int num = 10;

        if (num == 10) {
            System.out.println("Number is 10");
        } else {
            System.out.println("Number is not 10");
        }
    }
}
```

Can you tell how many blocks are used in the above program?

Here 4 blocks are used.

*   One block to mark the body of the Test class
*   One block to mark the body of the main method
*   One block to mark the body of if
*   One block to mark of else

We know that we can’t access a variable or any other entity defined inside the body of a method outside its body. We also know that we can’t access a variable or entity defined inside the body of if or else outside its body. From this, we can conclude that an entity defined inside a block can’t be accessed outside it. This can be proved from the following example.

```java
class Test {

    public static void main(String[] args) {
        // block
        {
            int num = 10;
        }

        // trying to access num outside its block
        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Test.java:9: error: cannot find symbol
                System.out.println(num);
                                   ^
  symbol:   variable num
  location: class Test
1 error</pre>
    </details>
</div>

Here, we declared a variable named `num` inside a block. Hence, when we tried to access it outside the block in which it is declared, we got an error.

Cool, guess you understood blocks!

Blocks have one more characteristic. A block defined in a class gets called before its constructor, no matter in which order it is defined. This means that whenever an object of a class will be created, the block defined in the class will get called before its constructor.

A block gets called before the constructor of the class in which it is defined.

Let’s look at an example.

```java
class Student {

    // constructor
    public Student() {
        System.out.println("I am constructor");
    }

    // block
    {
        System.out.println("I am block");
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student();
        Student st2 = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">I am block
I am constructor
I am block
I am constructor</pre>
    </details>
</div>

In the above example, we defined a constructor and a block inside a class named `Student`. When an object `s1` of the class is created, its block gets called and after that its constructor gets called, though the constructor is defined before the block. Similarly, when the second object `s2` is created, the block gets called before the constructor.

Now that you know what blocks are, let’s proceed to static blocks in Java.

A static block is used to initialize static variables in a class. It gets executed exactly once when the class is loaded for the first time.

First of all, let’s talk about how static blocks are different from constructors.

A static block is called the first time its class is loaded and hence is used to initialize the static variables. Whereas, a constructor is called each time an object of the class is created, and hence is used to initialize the instance variables.

The following example will make the difference clear.

```java
class Student {
    // static block
    static {
        System.out.println("I am static block");
    }

    // constructor
    public Student() {
        System.out.println("I am constructor");
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student();
        Student st2 = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">I am static block
I am constructor
I am constructor</pre>
    </details>
</div>

Here, the static block got called only once when the class `Student` is loaded the first time and after that the constructor got called whenever an object of the class was created.

Now that you know what a static block is used for and when it gets called, let’s see an example.

```java
class Student {

    String name;
    static String college;

    static {
        college = "ABC";
    }

    public Student(String n) {
        name = n;
    }

    public void printDetails() {
        System.out.println("Name: " + name + ", College: " + college);
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John");
        Student st2 = new Student("Julie");

        st1.printDetails();
        st2.printDetails();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: John, College: ABC
Name: Julie, College: ABC</pre>
    </details>
</div>

In this example, look at the following code.

```java
static String college;
	
static {
    college = "ABC";
}
```

This piece of code is equivalent to writing the following statement.

```java
static String college = "ABC";
```

When the class `Student` is first loaded, the static block gets executed and assigns the value “ABC” to the static variable `college`.

### Advantage of static Blocks
Static blocks are used to initialize the static variables. Additionally, they can be used to run any code that you want to run when the in which they are defined is first loaded.

Now let’s move on to the last application of the `static` keyword.

***
## Java static Class
We can declare a class as static only if it is a nested class. Nested classes and static nested classes are explained in the chapter [Nested Classes](https://web.archive.org/web/20240422031352/https://www.codesdope.com/course/java-nested-classes/).

> Creativity Is Intelligence Having Fun.
>
> \- Albert Einstein

***
