# Java this Keyword
<hr/>
Like [super](https://web.archive.org/web/20240416064058/https://www.codesdope.com/course/java-static-keyword/) refers to an object of the parent class, `this` keyword refers to an object of the current class. It is used to access the attributes, methods and constructors of the current class.

Let’s see what are the different scenarios where `this` keyword can be used.

<hr/>
## Uses of this Keyword
1.  To access the current class attributes.
2.  To access the current class methods.
3.  To access the current class constructors.
4.  To refer to the object of current class

These points are explained in detail in this chapter.

### Accessing Current Class Attributes

`this` keyword is used to access the member variables (attributes) of the current class. Its use will become clear from the following examples.

```java
class Account {

    String name;
    int balance;

    Account(String n, int b) {
        name = n;
        balance = b;
    }

    void printInfo() {
        System.out.println("Name: " + name + ", Balance: " + balance);
    }
}

class Test {

    public static void main(String[] args) {
        Account ac = new Account("Peter", 5000);
        ac.printInfo();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: Peter, Balance: 5000
</pre>
    </details>
</div>

Here, when the object `ac` of the class `Account` gets created, its constructor gets called with the arguments “Peter” and 5000.

```java
Account(String n, int b) {
    name = n;
    balance = b;
}
```

Inside the constructor, the passed arguments are assigned to the parameters `n` and `b`. The values of `n` (i.e. “John”) and `b` (i.e. 5000) are assigned to the `name` and `balance` attributes of the class respectively.

There is nothing new in this program. Now look at another example.

```java
class Account {

    String name;
    int balance;

    Account(String name, int balance) {
        name = name;
        balance = balance;
    }

    void printInfo() {
        System.out.println("Name: " + name + ", Balance: " + balance);
    }
}

class Test {

    public static void main(String[] args) {
        Account ac = new Account("Peter", 5000);
        ac.printInfo();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: null, Balance: 0
</pre>
    </details>
</div>

This is similar to the previous example. Look at the constructor of the `Account` class.

```java
Account(String name, int balance) {
    name = name;
    balance = balance;
}
```

Here, since the parameter and attribute names are the same, the compiler gets confused between the two and hence we got the incorrect output.

In such cases where the parameter and attributes names are the same, we need to distinguish between them. For that, `this` keyword can be used,

```java
class Account {

    String name;
    int balance;

    Account(String name, int balance) {
        this.name = name;
        this.balance = balance;
    }

    void printInfo() {
        System.out.println("Name: " + name + ", Balance: " + balance);
    }
}

class Test {

    public static void main(String[] args) {
        Account ac = new Account("Peter", 5000);
        ac.printInfo();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Name: Peter, Balance: 5000
</pre>
    </details>
</div>

Look at the constructor of the `Account` class.

```java
Account(String name, int balance) {
    this.name = name;
    this.balance = balance;
}
```

Here, since the parameter and attribute names are the same, we segregated the two using `this` keyword.

In the statement `this.name = name`, `this.name` refers to the attribute `name` of the class whereas `name` on the right side of the equality operator (=) is the parameter. In this way, the value of the parameter gets assigned to the attribute.

Note that since the constructor gets called by the creation of the object `ac`, `this` in the constructor refers to the object `ac`. Therefore, writing `this.name` is equivalent to writing `ac.name`.

Thus, the values “Peter” and 5000 gets assigned to the attributes `name` and `balance` respectively. Or, we can say that the name and balance of the object `ac` are “Peter” and 5000 respectively.

So this solved our problem. Let’s look at other uses of `this` keyword.

### Calling Current Class Methods

Like class variables, `this` keyword can also be used to call the class methods.

```java
class Method {

    void method1() {
        System.out.println("This is method 1");
    }

    void method2() {
        this.method1();
    }
}

class Test {

    public static void main(String[] args) {
        Method m = new Method();
        m.method2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is method 1
</pre>
    </details>
</div>

Look at the method `method2()` of the class `Method`.

```java
void method2() {
    this.method1();
}
```

Inside this method, the statement `this.method1()` calls the method `method1()` of the current class `Method`.

Again, since the object `m` calls the method `method2()`, `this` in the method refers to the object `m`. Therefore, writing `this.method1()` is equivalent to writing `m.method1()`.

Though we don’t need to add `this` keyword before `method1()` in the above program because the compiler does that automatically.

Let’s rewrite the above example without using `this` keyword.

```java
class Method {

    void method1() {
        System.out.println("This is method 1");
    }

    void method2() {
        method1();
    }
}

class Test {

    public static void main(String[] args) {
        Method m = new Method();
        m.method2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is method 1
</pre>
    </details>
</div>

### Calling Current Class Constructor

While methods and attributes of the current class can be accessed using `this` keyword, the constructor of the current class can be accessed using `this()`.

We know that in [Constructor Overloading](https://web.archive.org/web/20240416064058/https://www.codesdope.com/course/java-constructor-overloading/), a class can have multiple constructors with different parameters. In some cases, we might want to call a constructor from another constructor, but it is not possible to call a constructor from another constructor explicitly in Java.

While we can call a constructor of the superclass from a constructor of a subclass explicitly using super(), we can call a constructor from another constructor of the same class using `this()`.

`this()` is used to call a constructor of a class from within another constructor of the same class.

```java
class Account {

    String name;
    int balance;

    Account(String n) {
        name = n;
        System.out.println("This is a constructor with single parameter");
    }

    Account(String n, int b) {
        this(n);
        balance = b;
    }

    void printInfo() {
        System.out.println("Name: " + name + ", Balance: " + balance);
    }
}

class Test {

    public static void main(String[] args) {
        Account ac = new Account("Peter", 5000);
        ac.printInfo();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is a constructor with single parameter
Name: Peter, Balance: 5000
</pre>
    </details>
</div>

In this example, when the object `ac` of the class `Account` is created, the constructor with two parameters is called (because two arguments “John” and 5000 are passed).

```java
Account(String n, int b) {
    this(n);
    balance = b;
}
```

Inside this constructor,

`this(n)` → This statement calls the constructor of the same class having one parameter i.e. `Account(String n)` (because one argument `n` is passed).

Inside the constructor `Account(String n)`, the value of `n` (i.e. “John”) is assigned to the attribute `name` and *This is a constructor with single parameter* gets printed.

`balance = b` → This statement assigns the value of `b` (i.e. 5000) to the attribute `balance`.

Finally, the object `ac` calls the `printInfo()` method to print the values of the attributes.

When we call one constructor inside another, it should be the first statement of the constructor in which we are calling.

Suppose we are calling a constructor inside another constructor, then writing the following code will result in a Compile Time error because the constructor is called in the second statement.

```java
Account(String n, int b) {
    balance = b;
    this(n);
}
```

Cool, now we can call a constructor from another constructor within a class. Let’s see another example.

```java
class Rectangle {

    private int length;
    private int breadth;

    public Rectangle(int l, int b) {
        length = l;
        breadth = b;
    }

    public Rectangle(int side) {
        this(side, side);
    }

    public int getArea() {
        return length * breadth;
    }
}

class Test {

    public static void main(String[] args) {
        Rectangle rect = new Rectangle(4, 5);
        Rectangle sq = new Rectangle(5);

        System.out.println(rect.getArea());
        System.out.println(sq.getArea());
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">20
25
</pre>
    </details>
</div>

In this example, we used `this` keyword to call the constructor `Rectangle(int l, int b)` from the constructor `Rectangle(int side)`.

### Passing and Returning Class Object

We know that `this` refers to the object of the current class. That means we can use `this` to pass the current class object to a method of the class or return the current class object from a method of the class.

Let’s see how.

```java
class Rectangle {

    int length, breadth;

    Rectangle(int l, int b) {
        length = l;
        breadth = b;
    }

    Rectangle getObj() {
        return this;
    }
}

class Test {

    public static void main(String[] args) {
        Rectangle r1 = new Rectangle(15, 20);
        Rectangle r2;
        r2 = r1.getObj();
        System.out.println("length: " + r1.length + " breadth: " + r1.breadth);
        System.out.println("length: " + r2.length + " breadth: " + r2.breadth);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">length: 15 breadth: 20

length: 15 breadth: 20
</pre>
    </details>
</div>

Look at the `getObj()` method in this example.

```java
Rectangle getObj() {
    return this;
}
```

Since the object `r1` calls the `getObj()` method and `this` keyword represents the current object, here `this` keyword refers to the object `r1`.

Thus, the statement `return this` is equivalent to the statement `return r1` and thus returns the object `r1`.

Now look at the following statement in the main method.

`r2 = r1.getObj();`

We saw that the `getObj()` method returns the object `r1`. Therefore the above statement is equivalent to the statement `r2 = r1`.  Thus, the length and breadth of `r2` also become 15 and 20 respectively.

So, in the above program, `this` refers to the object that calls the `getObj()` method.

Let’s see another example.

```java
class Method {

    void method1(Method m1) {
        System.out.println("This is method 1");
    }

    void method2() {
        method1(this);
    }
}

class Test {

    public static void main(String[] args) {
        Method m = new Method();
        m.method2();
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">This is method 1
</pre>
    </details>
</div>

Look at the `method2()` method in this example.

```java
void method2() {
	method1(this);
}
```

Since the object `m` calls the `method2()` method, `this` refers to the object `m`.

Therefore, the statement` method1(this)` calls the method `method1()` by passing the object `m` as the argument.

So there were different cases in which we can use `this` keyword. `this` is most commonly used to help distinguish between attributes and parameters when both have the same name in a method, to call a constructor inside another in constructor overloading and to deal with (pass, return, etc.) the current object in a method (current object is the object that calls the method).

> Do What You Can With All You Have, Wherever You Are.
>
> \- Theodore Roosevelt

<hr/>


<a href="31-java-final-keyword.md" class="next">Next</a>
