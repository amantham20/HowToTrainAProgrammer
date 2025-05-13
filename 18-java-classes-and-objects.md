```markdown
# Java Classes and Objects
<hr/>
<p>We discussed the concept of classes and objects in the previous chapter. Before learning to create classes and objects using Java, let’s see one more example.</p>
<p>We know that a student has a name and a roll number. So, we can say that <b>Student</b> is a <b>class</b>, and <b>name</b> and <b>roll number</b> are the <b>attributes</b> of this class. Furthermore, we know that there can be many students and each student will have a name and a roll number. Thus, <b>all students are the objects of the Student class</b>.</p>
<p>So, you must have understood the basic concept of classes and objects. Now, let’s see how to create a class and its objects.</p>
<hr/>
## Creating Classes and Objects in Java
<p>A class is created using the <code>class</code> keyword.</p>
```java
class Student {

    String name;
    int roll_no;
}
```
<p>In the above declaration, <code>Student</code> is the name of a <b>class</b>. In other words, <code>Student</code> is a class.</p>
<p>In the body of the class, the <b>attributes</b> <code>name</code> and <code>roll_no</code> are defined.</p>
<p>So, we can say that each student has a name and a roll number.</p>
<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
             Attributes are variables defined inside a class.
          </div>
</div>
</div>
<p>Now let’s create an object of this class.</p>
```java
// Student class
class Student {

    String name;
    int roll_no;
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating object st of class Student
        Student st = new Student();
    }
}
```
<p>In the above example, <code>Test</code> is the main class containing the <code>main</code> method.</p>
<p>The class which has the main method inside it is known as the main class. Till now we were writing all our code in the main class.</p>
<p>We created the <code>Student</code> class having two attributes - <code>name</code> and <code>roll_no</code>.</p>
<p><code>Student st = new Student()</code> → We created an object <code>st</code> of the <code>Student</code> class. We can also say that <code>st</code> is a Student.</p>
<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
             The terms object and instance are used interchangeably.
          </div>
</div>
</div>
<p>Any number of objects of a class can be created.</p>
```java
// Student class
class Student {

    String name;
    int roll_no;
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating objects st1 and st2 of class Student
        Student st1 = new Student();
        Student st2 = new Student();
    }
}
```
<p>Here, we created two objects of the <code>Student</code> class - <code>st1</code> and <code>st2</code>. Thus, <code>st1</code> and <code>st2</code> are two Students having some name and roll number.</p>
<p>You now know how to create a class with attributes and its objects. Now let’s move forward and assign values to attributes.</p>
<hr/>
## Java Attributes
<p>We know that attributes are variables defined in a class. They specify the features (properties) of the class. For example, name and roll_no are the attributes/features of the <code>Student</code> class.</p>
```java
// Student class
class Student {

    String name = "John";
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating object st of class Student
        Student st = new Student();
        System.out.println(st.name);
    }
}
```
<details><summary>Output</summary>
<pre class="output">John
                      </pre>
</details>
<p>In this example, a class named <code>Student</code> is defined. It has an attribute <code>name</code> having the value “<i>John</i>”.</p>
<p><code>Student st = new Student()</code> → An object <code>st</code> of the <code>Student</code> class is created.</p>
<p><code>System.out.println(st.name)</code> → The object <code>st</code> accesses the attribute <code>name</code> of the class through <code>st.name</code> and its value is printed.</p>
<p>Note that an object of a class can access the attributes of that class using the dot ‘.’ operator. In the above example, the object <code>st</code> accesses the attribute <code>name</code> of the <code>Student</code> class through <code>st.name</code>.</p>
<p><img alt="accessing methods using dot (.) in Java" src="https://web.archive.org/web/20220811203614im_/https://www.codesdope.com/pa-images-bucket/courses/java/p22.png" style="max-width:30%;height:auto;"/></p>
<p>In the above example, we can say that <code>st</code> is a Student whose name is “John”.</p>
<p>Let’s see another way to assign value to attributes.</p>
```java
// Student class
class Student {

    String name;
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating object st of class Student
        Student st = new Student();

        // assigning value to attribute name
        st.name = "John";

        System.out.println(st.name);
    }
}
```
<details><summary>Output</summary>
<pre class="output">John
                      </pre>
</details>
<p>Here, the statement <code>st.name = "John"</code> assigned the value of the attribute <code>name</code> for the object <code>st</code> to “<i>John</i>”.</p>
<p>Look at another example.</p>
```java
// Student class
class Student {

    String name = "John";
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating objects st1 and st2 of class Student
        Student st1 = new Student();
        Student st2 = new Student();
        System.out.println("Student 1 Name: " + st1.name);
        System.out.println("Student 2 Name: " + st2.name);
    }
}
```
<details><summary>Output</summary>
<pre class="output">Student 1 Name: John
Student 2 Name: John
                      </pre>
</details>
<p>Two objects <code>st1</code> and <code>st2</code> of the <code>Student</code> class are created. These objects accessed the value of the attribute name through <code>st1.name</code> and <code>st2.name</code> respectively.</p>
<p>Thus, <code>st1</code> and <code>st2</code> are two Students having the same name i.e. “<i>John</i>”.</p>
<p>Now in the above example, we can define different names for both the objects as shown below.</p>
```java
// Student class
class Student {

    String name;
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating objects of class Student
        Student st1 = new Student();
        Student st2 = new Student();

        // assigning values to attribute name for objects
        st1.name = "John";
        st2.name = "Julie";

        System.out.println("Student 1 Name: " + st1.name);
        System.out.println("Student 2 Name: " + st2.name);
    }
}
```
<details><summary>Output</summary>
<pre class="output">Student 1 Name: John
Student 2 Name: Julie
                      </pre>
</details>
<p>The statement <code>st1.name = "John"</code> assigned the value of the attribute <code>name</code> for the object <code>st1</code> as “<i>John</i>” and the statement <code>st2.name = "John"</code> assigned the value of the attribute <code>name</code> for the object <code>st2</code> as “<i>Julie</i>”.</p>
<p>Thus, <code>st1</code> is a Student having the name “<i>John</i>” and <code>st2</code> is also a Student having the name “<i>Julie</i>”.</p>
<p>If you have understood till here, the rest of the topic will be an easy walk for you. Let’s move further.</p>
<hr/>
## Java Methods in Class
<p>In the above examples, we defined variables (known as attributes) in a class. Similarly, we can also define methods in a class. The variables and methods defined in a class are called <b>members</b> of the class.</p>
<p>Let’s define a method in our <code>Student</code> class.</p>
```java
// Student class
class Student {

    String name = "John";

    void description() {
        System.out.println("This is a student");
    }
}

// Test (Main) class
class Test {

    public static void main(String[] args) {
        // creating object st of class Student
        Student st = new Student();

        // accessing variable name of class
        System.out.println(st.name);

        // accessing method description of class
        st.description();
    }
}
```
<details><summary>Output</summary>
<pre class="output">John
This is a student
                      </pre>
</details>
<p>In this example, the <code>Student</code> class has a variable (attribute) <code>name</code> and a method <code>description()</code> defined in it. This variable and method are the members of the class.</p>
<p>We created an object <code>st</code> of this class. Thus, the object accessed the class attribute by writing <code>st.name</code> and the class method by writing <code>st.description()</code>.</p>
<p>Now let’s look at another example.</p>
```java
class Student {

    String name;

    void setName(String n) {
        name = n;
    }

    String getName() {
        return name;
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();

        st.setName("John");
        String st_name = st.getName();
        System.out.println("Student Name: " + st_name);
    }
}
```
<details><summary>Output</summary>
<pre class="output">Student Name: John
                      </pre>
</details>
<p>We created the <code>Student</code> class having an attribute <code>name</code> and methods <code>getName()</code> and <code>setName()</code>.</p>
<p><code>Student st = new Student()</code> → An object <code>st</code> of the class is created.</p>
<p><code>st.setName("John")</code> → The object <code>st</code> calls the method <code>setName()</code> by passing “John” to it. Inside the <code>setName()</code> method, <code>name = n</code> assigns “John” to the variable <code>name</code>.</p>
<p><code>String st_name = st.getName()</code> → The object <code>st</code> calls the method <code>getName()</code>. Inside the <code>getName()</code> method, <code>return name</code> returns the value of the variable <code>name</code> i.e. “John”. Thus, the value of the variable <code>st_name</code> becomes “John”.</p>
<p>By now, you know how to create classes and its objects. You also know that variables and methods can be defined in a class and can be accessed by the objects of that class. Pretty simple uptil here, right?</p>
<p>Now let’s move onto the next concept.</p>
<hr/>
## Java Constructor
<p>A constructor is a special class method which gets called automatically whenever an object of the class is created. Its <b>name is the same as the class name</b> and it has <b>no return type</b>.</p>
<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
             Constructor is a special type of method which is used to initialize an object. It is invoked at the time of object creation.
          </div>
</div>
</div>
<p>Since the constructor is called at the time of object creation, the part of the code that you want to execute at the time of object creation should be written in it.</p>
<p>An example will help understand the use of a constructor.</p>
```java
class Student {

    String name;

    // constructor
    Student() {
        name = "Unknown";
    }

    void setName(String n) {
        name = n;
    }

    String getName() {
        return name;
    }
}

class Test {

    public static void main(String[] args) {
        // creating object st of Student class
        Student st = new Student();

        // printing value of name of st
        System.out.println("Student Name: " + st.getName());

        // changing value of name of st
        st.setName("John");

        // printing value of name of st
        System.out.println("Student Name: " + st.getName());
    }
}
```
<details><summary>Output</summary>
<pre class="output">Student Name: Unknown
Student Name: John
                      </pre>
</details>
<p>In this example, the <code>Student</code> class is defined with an attribute <code>name</code>, a constructor <code>Student()</code> and two methods <code>getName()</code> (returns the value of <i>name</i>) and <code>setName()</code> (assigns a value to <i>name</i>).</p>
<p>When we created the object <code>st</code> of the class <code>Student</code>, the constructor <code>Student()</code> automatically got called. Inside the constructor, the value of the attribute <code>name</code> is initialized to “Unknown”. Therefore, on printing the value of <code>st.getName()</code> after that, “Unknown” got printed.</p>
<p>Next, <code>st.setName("John")</code> called the <code>setName()</code> method to set the value of <code>name</code> to “John”. Thus, on printing the value of <code>st.getName()</code> after that, “John” got printed.</p>
<p>Therefore, in the above example, we are assigning the name of the objects as “Unknown” by default using the constructor.</p>
<p>Let’s see another example.</p>
```java
class Student {

    String name;
    int age;

    // constructor
    Student() {
        name = "Unknown";
        age = 0;
    }

    void setDetails(String n, int a) {
        name = n;
        age = a;
    }

    void printDetails() {
        System.out.println("My name is " + name + " and my age is " + age);
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student();
        Student st2 = new Student();

        st1.setDetails("John", 25);
        st2.setDetails("Julie", 20);

        st1.printDetails();
        st2.printDetails();
    }
}
```
<details><summary>Output</summary>
<pre class="output">My name is John and my age is 25
My name is Julie and my age is 20
                      </pre>
</details>
<p>You must have understood this program. When the objects <code>st1</code> and <code>st2</code> were created, the constructor <code>Student()</code> got called and assigned <code>name</code> as “Unknown” and <code>age</code> as 0 for both the objects. After that, both the objects called the <code>setDetails()</code> method to set the respective values of <code>name</code> and <code>age</code> and the <code>printDetails()</code> method to print their values.</p>
<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
We can also make a constructor with nothing in its body.             
          </div>
</div>
</div>
<p><code>Student(){ };</code></p>
<p>If we don’t explicitly create any constructor in a class, then the compiler automatically creates a constructor with no parameter and empty body.</p>
### Java Constructor Having Parameters
<p>We can also define constructors having parameters.</p>
```java
class Student {

    String name;
    int age;

    // constructor
    Student(String n, int a) {
        name = n;
        age = a;
    }

    void printDetails() {
        System.out.println("My name is " + name + " and my age is " + age);
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John", 25);
        Student st2 = new Student("Julie", 20);

        st1.printDetails();
        st2.printDetails();
    }
}
```
<details><summary>Output</summary>
<pre class="output">My name is John and my age is 25
My name is Julie and my age is 20
                      </pre>
</details>
<p>Here, the constructor <code>Student()</code> has two parameters, the first parameter of type <i>String</i> and the second parameter of type <i>int</i>. Therefore, when creating an object of the <code>Student</code> class, we have to pass two arguments.</p>
<p>Look at the following statement.</p>
<p><code>Student st1 = new Student("John", 25);</code></p>
<p>This statement creates an object <code>st1</code> and calls the <code>Student()</code> constructor by assigning the value “John” to <code>n</code> and 25 to <code>a</code>. In the constructor, <code>n</code> (“John”) is assigned to <code>name</code> and <code>a</code> (25) is assigned to <code>age</code>. The same is done for the object <code>st2</code> also.</p>
### Using <b>public</b> and <b>private</b> Modifiers
<p>We will discuss modifiers in the chapter <a href="https://web.archive.org/web/20220811203614/https://www.codesdope.com/course/java-access-modifiers/" target="_blank">Access Modifiers</a>. Let's just learn about a few things which are necessary for now. Members (variables and methods) of a class are usually declared as <b>private</b> or <b>public</b>.</p>
<p>Declaring a class variable/method as <b>private</b> means that the variable/method can be accessed only inside the class. Accessing a private variable/method outside the class will result in an error. Whereas, declaring a class variable/method as <b>public</b> means that the variable/method can be accessed outside the class in which it is defined.</p>
<p>Therefore, we can’t access a <code>private</code> variable/method through the class object outside the  class.</p>
<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
Usually, class variables (attributes) are declared <b>private</b> and class methods are declared <b>public</b>. (We will learn about the reason for doing so in the <a href="https://web.archive.org/web/20220811203614/https://www.codesdope.com/course/java-encapsulation/" target="_blank">Encapsulation chapter</a>)             
          </div>
</div>
</div>
<p>Let’s make all class variables as <code>private</code> and class methods as <code>public</code> in the last example.</p>
```java
class Student {

    private String name;
    private int age;

    // constructor
    public Student(String n, int a) {
        name = n;
        age = a;
    }

    public void printDetails() {
        System.out.println("My name is " + name + " and my age is " + age);
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John", 25);
        st1.printDetails();
    }
}
```
<details><summary>Output</summary>
<pre class="output">My name is John and my age is 25
                      </pre>
</details>
<p>In this example, the object <code>st1</code> was able to access the method <code>printDetails()</code> because this method is declared as <code>public</code>.</p>
<p>Now let’s try to access a private attribute outside the class in the above example.</p>
```java
class Student {

    private String name;
    private int age;

    // constructor
    public Student(String n, int a) {
        name = n;
        age = a;
    }

    public void printDetails() {
        System.out.println("My name is " + name + " and my age is " + age);
    }
}

class Test {

    public static void main(String[] args) {
        Student st1 = new Student("John", 25);
        System.out.println(st1.name);
    }
}
```
<details><summary>Output</summary>
<pre class="output">Test.java:19: error: name has private access in Student
        System.out.println(st1.name);
                                ^
1 error
                      </pre>
</details>
<p>We got an error. This is because the object <code>st1</code> tried to access the <code>private</code> attribute <code>name</code> outside the <code>Student</code> class.</p>
<p>From now on, let’s make a habit of declaring class attributes as <code>private</code> and class methods as <code>public</code> in normal conditions. In the rest of the examples, we will follow this pattern.</p>
<p>Let’s see another example.</p>
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
        Rectangle rect = new Rectangle(2, 4);
        System.out.println(rect.getArea());
    }
}
```
<details><summary>Output</summary>
<pre class="output">8
                      </pre>
</details>
<p>This program has a class named <code>Rectangle</code> which has <code>length</code> and <code>breadth</code> as attributes and a method <code>getArea()</code> that returns the area of the rectangle. Try to understand the rest of the code yourself.</p>
<hr/>
## Java static
<p>Declaring a variable/method defined in a class as <b>static</b> means that the variable/method can be accessed without making an object of the class in which it is defined. In other words, <b>static</b> is used so that we can access any variable or method in a class without making an object of that class.</p>
<p>Let's understand with an example.</p>
```java
class Rectangle {

    public static void printArea(int l, int b) {
        System.out.println(l * b);
    }
}

class Test {

    public static void main(String[] args) {
        Rectangle.printArea(2, 4);
    }
}
```
<p>Here, the method <code>printArea()</code> is declared as <code>static</code>. As a result, we were able to access it by directly using the class name <code>Rectangle</code>, without creating an object of the class.</p>
<p>Now let’s get to the last topic of this chapter.</p>
<hr/>
## Returning and passing object in a method
<p>Yes, we can return or pass object(s) to a method.</p>
<p>Let’s see how.</p>
```java
class Account {

    public int balance;

    public Account() {
        balance = 0;
    }

    public static Account getAcc(Account a, Account b) {
        Account ac = new Account();
        ac.balance = a.balance + b.balance;
        return ac;
    }
}

class Test {

    public static void main(String[] args) {
        Account a1 = new Account();
        a1.balance = 50;

        Account a2 = new Account();
        a2.balance = 60;

        Account a3 = Account.getAcc(a1, a2);
        System.out.println(a3.balance);
    }
}
```
<details><summary>Output</summary>
<pre class="output">110
                      </pre>
</details>
<p>In this example, the <code>getAcc()</code> method is taking two <code>Account</code> objects as parameters and returning an <code>Account</code> object. Note that the attribute <code>balance</code> is defined as <code>public</code> because we want the objects to directly access this attribute in this example.</p>
<p><code>Account a3 = Account.getAcc(a1, a2);</code></p>
<p>In the above statement, the <code>getAcc()</code> method is taking the objects <code>a1</code> and <code>a2</code> and is returning a new object of the <code>Account</code> class. The returned object is assigned to <code>a3</code>.</p>
```java
public static Account getAcc(Account a, Account b) {
    Account ac = new Account();
    ac.balance = a.balance + b.balance;
    return ac;
}
```
<p>Inside the <code>getAcc</code> method, a new object <code>ac</code> is created. Then the sum of balances of the two parameter objects is assigned to the <code>balance</code> of <code>ac</code>, and finally <code>ac</code> is returned.</p>
<p>So this completes the topic - classes and objects. If you have understood this chapter, then you have surpassed many beginners who find it difficult.</p>
<p>This might be a heavy chapter, so go through it thoroughly and ask doubts in the <a href="https://web.archive.org/web/20220811203614/http://codesdope.com/discussion/" target="_blank">discussion forum</a>. Also practice questions on classes and objects from the <a href="https://web.archive.org/web/20220811203614/https://www.codesdope.com/practice/" target="_blank">practice section</a> before moving onto the next chapter.</p>
<div id="quote">
<div><span>If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.</span></div>
<div><span>- Steve Jobs</span></div>
</div>
<hr/>
```

<a href="19-java-array-of-objects.md" class="next">Next</a>
