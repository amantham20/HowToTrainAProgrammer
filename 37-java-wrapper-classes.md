# Java Wrapper Classes
<hr/>
Wrapper classes are similar to primitive data types (like *int*, *double*, *char*, *short*, etc.) in Java. Basically, they wrap around or contain primitive data types.

Let’s explain this more clearly. Wrapper classes are predefined classes in Java whose objects store values having some primitive type. For example, `Integer` is a predefined wrapper class and its object is used to store values of type int.

Let’s understand with the help of an example.
```java
// int is primitive type
int num = 10;

// Integer is wrapper class
Integer numObj = 10;
```
In the first statement, *int* is a primitive type and `num` is a variable of type *int*. In the second statement, `Integer` is a wrapper class and `numObj` is its object. Both `num` and `numObj` are assigned an *int* value 10.

From the above example, you can see that an object of the wrapper class `Integer` is used to store a value of type *int*.

This is fine, but **why do we need wrapper classes**? Let’s answer that.
<hr/>
## Use Of Wrapper Classes in Java
The two most important uses of wrapper classes are discussed below.

### Use of Wrapper Class in Collections
Wrapper classes are used instead of primitive types in [collections](https://web.archive.org/web/20240529013128/https://www.codesdope.com/course/java-collection-framework/) like [ArrayList](https://web.archive.org/web/20240529013128/https://www.codesdope.com/course/java-arraylist/), Hashmap, etc. Collections are used to store data; you will learn about collections in the next chapter. For example, in the topic Java ArrayList, we saw that wrapper classes are used instead of primitive types.

Look at the following statements.
```java
// this statement will throw error
ArrayList<int> myList = new ArrayList<>();

// this statement will run successfully
ArrayList<integer> myList = new ArrayList<>();
```
In the first statement, the type of the `ArrayList` is given as *int* which is a primitive type and hence it will throw an error. In the second statement, the type of the `ArrayList` is given as `Integer` which is a wrapper class and hence it will get executed.

### Wrapper Class Objects Store Null Value
The `null` value can’t be stored in a variable of a primitive type, whereas it can be stored in an object of a wrapper class.
```java
// this statement will throw error
int a = null;

// this statement will run successfully
Integer b = null;
```
As you can see from the above statements, the `null` value can’t be assigned to the variable `a` because it is of type *int* whereas it can be assigned to `b` which is an object of the wrapper class `Integer`.

So, whenever we want to store the `null` value, we have to use a wrapper class instead of a primitive type.

These were some of the advantages of wrapper classes over primitive types. Now let’s learn more about wrapper classes.
<hr/>
## Wrapper Classes in Java
We already saw what wrapper classes are in the beginning of this chapter. Let’s again see how to create an object of a wrapper class.

`Integer b = 10;`

In the above statement, `Integer` is a wrapper class and `b` is an object of `Integer`. We assigned an *int* value 10 to it.

Apart from `Integer`, there are other predefined wrapper classes as well for each of the 8 primitive types, as shown below.

| Primitive Type | Wrapper Class |
| --- | --- |
| byte | Byte |
| boolean | Boolean |
| char | Character |
| double | Double |
| float | Float |
| int | Integer |
| long | Long |
| short | Short |

Now let’s see an example.
```java
class Test {

    public static void main(String[] args) {
        // creating objects of wrapper classes
        Integer i = 15;
        Character c = 'e';

        // printing the values stored in the objects
        System.out.println(i);
        System.out.println(c);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">15
e</pre>
    </details>
</div>

We created an object `i` of the wrapper class `Integer` and assigned an integer 15 to it. We also created an object `c` of the wrapper class `Character` and assigned a character ‘e’ to it. Then on printing the objects of both the wrapper classes, the values stored in them get printed.

That was some easy stuff. In case you have any query regarding the concept of wrapper classes, feel free to ask in the [discussion section](https://web.archive.org/web/20240529013128/https://www.codesdope.com/discussion/).

Do you know we can convert a primitive type to a wrapper class object and vice versa? Yes, it is possible and doing that is quite simple.
<hr/>
## Converting Primitive Type to Wrapper Class Object
A primitive type can be converted to a wrapper class object using the `valueOf()` method. `valueOf()` takes a primitive type as parameter and returns the object of the wrapper class that calls the method. Let’s understand with an example.

Consider the following statement.

`int num = 10;`

In this statement, we defined a variable `num` of the primitive type *int* and assigned it the value 10. We can convert it to an object of the wrapper class `Integer` by writing the following code.

`Integer numObj = Integer.valueOf(num);`

On the right hand side, the wrapper class `Integer` calls the `valueOf()` method and `num` is passed to it. As a result, the `valueOf()` method converts the value stored in the primitive type `num` to an object of the wrapper class Integer and returns the object. This returned object is assigned to the `numObj` object of Integer.

Thus, in the above statement, the primitive type `num` is converted to an object of the wrapper class `Integer` which is stored in `numObj`.

This is implemented in the following program.
```java
class Test {

    public static void main(String[] args) {
        // defining int primitive type
        int num = 10;

        // converting int primitive type into wrapper object
        Integer numObj = Integer.valueOf(num);
        System.out.println(numObj);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

As discussed above, the value stored in the variable `num` of type *int* got converted to the object `numObj` of the `Integer` class. Hence, on printing `numObj`, 10 got printed.

Java Autoboxing

Java can also automatically convert a primitive type into the corresponding wrapper class object. This process is known as **autoboxing**. So let’s see when Java automatically converts a primitive type to an object.

Autoboxing can be achieved by directly assigning the primitive type to the wrapper class object as shown in the following example.
```java
class Test {

    public static void main(String[] args) {
        // defining int primitive type
        int num = 10;

        // (autoboxing) converting int primitive type into wrapper object
        Integer numObj = num;
        System.out.println(numObj);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

Look at the following statement in this example.

`Integer numObj = num;`

Here, we are directly assigning the variable `num` of type *int* to the object `numObj` of the `Integer` class. In this case, autoboxing takes place i.e. the value stored in `num` is automatically getting converted to the object `numObj`.

This was fun. Now let’s see how to convert a wrapped class object to a primitive type.
<hr/>
## Converting Wrapper Class Object to Primitive Type
While we used the `valueOf()` method to convert a primitive to a wrapper class object, there are different methods (like `intValue()`, `charValue()`, etc.) to convert a wrapper class object to a primitive type based on the primitive type. These methods convert the wrapper class object that calls the method into the corresponding primitive type.

For example, `intValue()` is used to convert a wrapper class object into an int, `intValue()` to convert to a double, `charValue()` to convert to a *char*, etc.

Look at the following example.
```java
class Test {

    public static void main(String[] args) {
        // creating a wrapper class object
        Integer numObj = 10;

        // converting wrapper class object into int primitive type
        int num = numObj.intValue();
        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

An object named `numObj` of the `Integer` class is created and assigned 10. Now look at the following statement.

`int num = numObj.intValue();`

Here, the `intValue()` method converts the object (10) stored in `numObj` into a primitive type *int* and then returns the int value 10. This returned value is assigned to the variable `num` of type *int*. Hence, `num` now stores the *int* value 10.

### Java Unboxing
**Unboxing** is just the opposite of autoboxing. It is the process in which Java automatically converts a wrapper class object into the corresponding primitive type.

Unboxing can be achieved by directly assigning the wrapper class object to the primitive type.
```java
class Test {

    public static void main(String[] args) {
        // creating a wrapper class object
        Integer numObj = 10;

        // (unboxing) converting wrapper class object into int primitive type
        int num = numObj;
        System.out.println(num);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">10</pre>
    </details>
</div>

Look at the following statement in this example.

`int num = numObj;`

In this statement, we are directly assigning the object `numObj` of the `Integer` class to the variable num of the primitive type *int*. Hence, unboxing takes place here i.e. the object stored in `numObj` is automatically getting converted to an int type.

> Success comes from having dreams that are bigger than your fears.
>
> - Bobby Unser

<hr/>


<a href="38-java-collection-framework.md" class="next">Next</a>
