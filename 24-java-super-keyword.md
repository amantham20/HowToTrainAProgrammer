# Java super Keyword
***
Before starting this chapter, make sure you know about [inheritance](https://web.archive.org/web/20240416075755/https://www.codesdope.com/course/java-inheritance/) and [method overriding](https://web.archive.org/web/20240416075755/https://www.codesdope.com/course/java-method-overriding/).

The `super` keyword refers to the object of the parent class. Therefore, it can be used to access attributes, methods and constructors of the immediate parent class from the child class. `super` is mostly used to call overridden methods and non-parameterized constructors of the superclass from the subclass.

Let’s discuss some uses of `super`.
***
## Calling Parent Class Methods
<br/>

To understand the use of `super`, look at the following example.

```java
// superclass
class Person {

    public void message() {
        System.out.println("I am a Person");
    }
}

// subclass
class Student extends Person {

    public void message() {
        System.out.println("I am a Student");
    }

    public void display() {
        message();
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();
        st.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">I am a Student
</pre>
    </details>
</div>

In this example, the parent class `Person` and the child class `Student` have methods with the same name i.e. `message()`. Thus, the `message()` method of the child class `Student` overrides the `message()` method of the parent class `Person`.

In the main method, the object `st` of `Student` calls the `display()` method.

```java
public void display() {
	message();
}
```

Inside the  `display()` method, `message()` is called. Due to method overriding, the `message()` method of `Student` gets called and *I am a Student* gets printed.

Now suppose in this example, you want the overridden `message()` method of the parent class `Person` to get called.

To call a method of the parent class from a method in a child class, the `super` keyword is used. For example, writing *super.m()* will call the *m()* method of the parent class and writing *super.abc()* will call the *abc()* method of the parent class.

Let’s rewrite the above program using `super` to call the method of the parent class from a method in the child class.

```java
// superclass
class Person {

    public void message() {
        System.out.println("I am a Person");
    }
}

// subclass
class Student extends Person {

    public void message() {
        System.out.println("I am a Student");
    }

    public void display() {
        super.message();
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();
        st.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">I am a Person
</pre>
    </details>
</div>

Here, again the object `st` of `Student` calls the `display()` method.

```java
public void display() {
	super.message();
}
```

Inside the `display()` method of the `Student` class, the statement `super.message()` calls the `message()` method of its parent class `Person` and hence *I am a Person* gets printed.

So, you can now call any method of the superclass using the `super` keyword.

**Can we also call non-overridden methods of the parent class using super?**

Yes, all superclass methods can be called using the `super` keyword. However, non-overridden superclass methods can be accessed without the `super` keyword also, so no need to use `super` in this case.
***
## Accessing Parent Class Attributes
<br/>

Similar to methods, an attribute of the parent class can be accessed from the child class using the `super` keyword.

Let’s first look at an example without using `super`.

```java
// superclass
class Person {

    protected String name = "John";
}

// subclass
class Student extends Person {

    private String name = "Julie";

    public void display() {
        System.out.println(name);
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();
        st.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Julie
</pre>
    </details>
</div>

The parent class `Person` and the child class `Student` have an attribute with the same name i.e. `name`. 

In the main method, the object `st` of `Student` calls the `display()` method.

```java
public void display() {
	System.out.println(name);
}
```

Inside the  `display()` method, the value of `name` is printed. Since the object of the `Student` class calls the `display()` method, the value of the `name` attribute of `Student` i.e. *Julie* gets printed.

Now, to access an attribute of the parent class from a child class, `super` is used. For example, writing *super.name* will access the name attribute of the parent class and writing *super.age* will access the age attribute of the parent class.

Let’s rewrite the above program to print the value of the `name` attribute of the parent class, instead of the child class.

```java
// superclass
class Person {

    protected String name = "John";
}

// subclass
class Student extends Person {

    private String name = "Julie";

    public void display() {
        System.out.println(super.name);
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();
        st.display();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">John
</pre>
    </details>
</div>

Look at the `display()` method in this program.

```java
public void display() {
    System.out.println(super.name);
}
```

Inside the `display()` method of the `Student` class, we replaced `name` by `super.name` to access the `name` attribute of the parent class `Person`. As a result, *John* got printed.

**Can we also access attributes of the parent class which don’t have the same name as the attributes of the child class using super?**

Yes, all superclass attributes can be called using the `super` keyword. However, they can also be accessed without the `super` keyword also, so no need to use `super` in this case.
***
## Calling Parent Class Constructor
While methods and attributes of the parent class can be accessed from a subclass using the `super` keyword, the constructor of the parent class can be accessed using `super()`.

```java
super()``` is written inside the constructor of the subclass and must be the first statement inside the constructor.

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
        super(); // calls the default constructor of the superclass
        System.out.println("Constructor of child class");
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Constructor of parent class
Constructor of child class
</pre>
    </details>
</div>

When the object `st` of the `Student` class is created, the constructor of the Student class gets called.

```java
public Student() {
    super();  // calls the default constructor of the superclass
    System.out.println("Constructor of child class");
}
```

Inside the constructor of `Student`, the statement `super()` calls the constructor of the parent class `Person` and executes the statements inside it. As a result, *Constructor of parent class* gets printed.

After that, the second statement of the constructor of `Student` is executed and hence *Constructor of child class* gets printed.

However, we know that whenever the constructor of a class is called, the non-parameterized constructor of the parent class automatically gets called.

Compiler automatically calls the non-parameterized parent class constructor whenever a child class constructor is called.             

Let’s rewrite the above program without writing `super()` in the constructor of `Student`.

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
        Student st = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Constructor of parent class
Constructor of child class
</pre>
    </details>
</div>

In this example, inside the constructor of `Student`, we didn’t call the parent class constructor using `super()` and still we are getting the same output. This is because the non-parameterized constructor of the parent class automatically gets called whenever the child class constructor is called, as shown below.

```java
public Student() {
    // compiler implicitly calls super()
    System.out.println("Constructor of child class");
}
```

**Then why should we explicitly use super() to call the constructor of parent class when the compiler automatically calls it?**

`super()` is useful when we want to call a parameterized constructor of the parent class, because parameterized constructors of the parent class are not implicitly called by the compiler.

Take the following example.

```java
// superclass
class Person {

    protected String name;

    public Person() {
        System.out.println("Default constructor of parent class");
    }

    public Person(String n) {
        name = n;
        System.out.println("name: " + name);
    }
}

// subclass
class Student extends Person {

    public Student() {
        super("John"); // calls the parameterized constructor of the superclass
        System.out.println("Constructor of child class");
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">name: John
Constructor of child class
</pre>
    </details>
</div>

In this example, inside the constructor of the `Student` class, the first statement `super("John")` calls the constructor of the parent class `Person` which has one parameter of type *String* i.e. `public Person(String n)`. You must have understood the rest of the code.

Note that since we explicitly called the non-parameterized parent class constructor, the compiler didn’t call the default parent class constructor.

Remember that to call the parent class constructor, super() must be written as the first statement inside the child class constructor. If it is not written as the first statement, we will get a compilation error.             
***
## A Real Life Example of Use of super Keyword
Suppose we want to store the information about students and teachers in a school. The information to be stored includes the name, age and marks of students and the name, age and salary of the teachers.

Here, name and age have to be stored for both students and teachers and we also know that both students and teachers are persons.

Therefore, we can make **Person** as a class with **name** and **age** as attributes, and can make **Student** and **Teacher** as the subclasses of Person. In the **Student** class, we can define an additional **marks** attribute and in the **Teacher** class an additional **salary** attribute.

Now let’s implement this in Java using `super` wherever necessary.

```java
// superclass
class Person {

    protected String name;
    protected int age;

    public Person(String p_name, int p_age) {
        name = p_name;
        age = p_age;
    }

    public void display() {
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }
}

// subclass 1
class Student extends Person {

    private int marks;

    public Student(String s_name, int s_age, int s_marks) {
        super(s_name, s_age);
        marks = s_marks;
    }

    public void display() {
        System.out.println("#### Details of student ####");
        super.display();
        System.out.println("Marks: " + marks);
    }
}

// subclass 2
class Teacher extends Person {

    private int salary;

    public Teacher(String t_name, int t_age, int t_salary) {
        super(t_name, t_age);
        salary = t_salary;
    }

    public void display() {
        System.out.println("#### Details of teacher ####");
        super.display();
        System.out.println("Salary: " + salary);
    }
}

class Test {

    public static void main(String[] args) {
        // creating object of subclass Student
        Student st = new Student("John", 20, 84);
        st.display();

        // creating object of subclass Teacher
        Teacher tch = new Teacher("Julie", 40, 200000);
        tch.display();
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
Salary: 200000
</pre>
    </details>
</div>

We created two classes `Student` and `Teacher` as the subclasses of the `Person` class.

Let’s first talk about the subclass `Student`.

In the main method, when the object `st` of the subclass `Student` is created, its constructor gets called with the arguments “John”, 20 and 84.

```java
public Student(String s_name, int s_age, int s_marks) {
    super(s_name, s_age);
    marks = s_marks;
}
```

Inside the constructor of `Student`, these passed arguments are assigned to the parameters `s_name`, `s_age` and `s_marks`.

`super(s_name, s_age)` → The first statement calls the constructor of the parent class `Person` by passing `s_name` and `s_age` as the arguments. Inside the constructor of `Person`, the attributes `name` and `age` become “John” and 20 respectively for the object

`st.

marks = s_marks` → The second statement assigns the value of `s_marks` (i.e. 84) to the `marks` attribute for the object `st`.

After this, in the main method, the object `st` of the subclass `Student` calls the `display()` method. Due to method overriding, the `display()` method of `Student` gets called.

```java
public void display() {
    System.out.println("#### Details of student ####");
    super.display();
    System.out.println("Marks: " + marks);
}
```

Inside the `display()` method,

`super.display()` → This statement calls the `display()` method of the parent class `Person`. In the `display()` method of `Person`, the values of the attributes `name` and `age` for the object `st` are printed.

`System.out.println("Marks: " + marks)` → This statement prints the value of the `marks` attribute for the object `st`.

Similarly, the information for the subclass `Teacher` is stored and printed.

In the above program, observe the use of `super`. From this program, you must have got a feel of in which cases `method overriding` and `super` can be used. The more you will practice, the better you will become at it. So make it a habit of practicing questions after every topic.

Since the last few chapters, we have read about inheritance and different concepts related to it. With this chapter, we finish the topic of inheritance. Go through all the concepts related to inheritance we have read till now and [ask us](https://web.archive.org/web/20240416075755/https://www.codesdope.com/discussion/) if you have any query.

> Live as if you were to die tomorrow. Learn as if you were to live forever.
> 
> - Mahatma Gandhi

***
