# Java Collection Framework

We know that arrays are used to store data. In this chapter, we will look at some more collections which we can use to store data.

## What is Java Collection?

A **Collection** is used to store data just like arrays.

**So what is the difference between an array and a collection?**

Arrays are used to store primitive data like integers, characters, strings, etc. Arrays can also be used to store objects of classes (We read about it in the topic [Array of Objects](https://web.archive.org/web/20240222020445/https://www.codesdope.com/course/java-array-of-objects/)). For example, we can have an array of integers, an array of characters, etc.

Collections are used to store objects of classes. This class can be any [wrapper class](https://web.archive.org/web/20240222020445/https://www.codesdope.com/course/java-wrapper-classes/) (like Integer, String, etc.) or any user-defined class. For example, we can have a collection of Integers, a collection of String, etc.

<div class="well imp_well">
<div class="row">
<div class="col-md-1 col-sm-1 well_one">
<i class="fa fa-code"></i>
</div>
<div class="col-md-11 col-sm-11 well_two">
             Note that int is a data type and Integer is a class.
          </div>
</div>
</div>

The objects of the wrapper class `Character` are character values. For example, ‘e and ‘f are characters and therefore objects of the `Character` class. Similarly, the objects of the wrapper class `Integer` are integer values. For example, 1 and 2000 are integers and therefore objects of the `Integer` class.

Wait, won’t an *array of integers and a collection of Integers* both store integers only? If yes, then **why would we use a collection of Integers (class) instead of an array of integers (int data type)?**

Yes, both an array of integers and a collection of Integers will store integers. However, in some cases, we may prefer to use a collection instead of an array due to some advantages of collections over arrays. Let’s see what those advantages are.

The size of an array is fixed. This means that if we declare an array of 10 elements, then we can’t increase or decrease its size later. Whereas, we can change the size of a collection based on our requirement. Another advantage of collections is that they can be used to store different types of data but arrays can store only similar types of data. For example, we can create a collection containing some objects of type Integer and some objects of type String, but we can’t create an array containing some integers and some strings. Apart from this, collections use less memory than arrays in some scenarios.

Thus, in some cases, we may need to use collections in place of arrays. The differences between arrays and collections are listed below.

| Array | Collection |
| --- | --- |
| Arrays have fixed size. We can’t increase or decrease the size of an array after creating the array. | Collections are dynamic. We can increase or decrease its size based on our requirement. |
| Arrays can be used to store both primitive values (eg, values of type *int*, *str*, etc.) and objects. | Collections can be used to store objects but not primitive values. |
| Arrays store similar types of data. | Some collections can be used to store similar whereas some collections can be used to store similar as well as different types of data. |
| Arrays are less memory efficient. | Collections are more memory efficient. |
| Arrays are better in performance. | Collections are not recommended based on performance. |

Hope you got a feel of what collections are. There are different types of collections that we can create like ArrayList, LinkedList, Stack, PriorityQueue, Vector, etc. These different types of collections have different properties and are used for different tasks. You will learn about all these in detail later. For now, just understand that there are different types of collections for performing different tasks.

Normally, we have to write long code for creating collections like ArrayList, LinkedList, etc. However, Java makes it easy for us by providing built-in classes and methods which we can directly use for implementing these collections.

## Java Collections Framework

The **Collections framework** is a set of interfaces and classes that can be used to implement various collections. In other words, a collection framework provides built-in interfaces, classes and methods which we can use to directly create and use a collection instead of writing long code manually.

For example, the `LinkedList` class provided by the collections framework can be used to directly create a linked list. This makes our work so much easier!

### Collections Framework Hierarchy

![collection framework diagram in Java](https://web.archive.org/web/20240222020445im_/https://www.codesdope.com/pa-images-bucket/courses/java/p37.png)

All the blocks in red are the [interfaces](https://web.archive.org/web/20240222020445/https://www.codesdope.com/course/java-interface/) and the blocks in blue are the [classes](https://web.archive.org/web/20240222020445/https://www.codesdope.com/course/java-classes-and-objects/).

The Java collections framework provides mainly three root interfaces - `Collection`, `Map` and `Iterator`.

`Collection` interface has three subinterfaces - `List`, `Queue` and `Set`.

`List` interface is implemented by the classes `ArrayList`, `Vector` and `LinkedList`. Similarly, the `Queue` and the `Set` interface are implemented by some classes.

`Map` interface is implemented by the `SortedMap` class.

`Iterator` interface is implemented by the `ListIterator` class.

All these classes provided by the collections framework can be directly used to create and implement some collections. These classes also have some methods for performing several tasks like adding, deleting or modifying elements in the collection.

For example, the `PriorityQueue` class can be used to create a priority queue. The `PriorityQueue` class also provides some methods like `add()` to add elements to the priority queue, `remove()` to remove elements from the priority queue, etc. Thus, we can directly create a priority queue using a built-in class and can directly perform operations like adding or removing elements in the priority queue without writing any logic ourselves.

### Using Classes from Collections Framework for Implementing Collections

As mentioned above, the classes provided by the collections framework can be used to create collections. Therefore, the following collections can be created by directly using built-in classes in Java.

*   Array List
*   Vector
*   Linked List
*   Priority Queue
*   Hash Set
*   Linked Hash Set
*   Tree Set
*   Sorted Map
*   List Iterator

The Collections Framework is defined in the `java.util` package. Therefore, to use a class provided by the Collections Framework, import the required class from the `java.util` package.

For example, to use the built-in `ArrayList` class to create an ArrayList, we can import it using the following statement.

`import java.util.ArrayList;`

Let’s see an example of an Array List.

```java
import java.util.ArrayList;

class Test {

    public static void main(String[] args) {
        // creating an Array List named colors
        ArrayList<String> colors = new ArrayList<>();

        // add elements in the Array List
        colors.add("Red");
        colors.add("Blue");
        colors.add("Green");
        colors.add("Orange");

        // printing the ArrayList
        System.out.println(colors);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">[Red, Blue, Green, Orange]</pre>
    </details>
</div>

Here, we imported the built-in `ArrayList` class from the `java.util` package. Then we created an arraylist named `colors` which will store objects of the `String` class. In other words, it stores strings. After that, we added the elements to the Array List by using the `add()` method provided by the `ArrayList` class.

Thus, we can see that array lists are resizable arrays because we can change the number of elements in it after its creation. Don’t worry if you didn’t understand the above code because it is given just to make you understand how built-in classes are used to create collections in Java.

<div id="quote">
<div><span>Don’t spend time beating on a wall, hoping to transform it into a door.</span></div>
<div><span>- Coco Chanel</span></div>
</div>
