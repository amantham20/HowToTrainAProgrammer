# Java Iterator

So far, we have used the for loop to iterate over sequences. So, the for loop is an iterator. In this chapter, we will learn to create our own iterators. However, creating a custom iterator is not that common in programming, but a good programmer should know how to create one. There can be several benefits of creating our own iterator like saving memory which we will discuss later in the chapter.

We know that collections like ArrayList can be iterated using the for loop. Thus, the for loop is the **iterator** and the collection over which it iterates is called the **iterable**.

For example, we can iterate over an ArrayList using a for loop as shown below.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		// iterating the ArrayList
		for(int i = 0; i < colors.size(); i++) {
			System.out.println(colors.get(i));
		}
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Red
Blue
Green
Orange
</pre>
    </details>
</div>

We are well aware of how for loop is used to iterate over a collection like an ArrayList. The arraylist colors is a collection of String values. The for loop iterates over the arraylist and prints its each element. Here, the for loop is the iterator and the arraylist colors is the iterable.

> for loop is the most common iterator used in Java.

Technically speaking, an **iterator** is an object that iterates. It is used to return the data of an iterable by returning one element in each iteration. Whereas, an **iterable** is an object which is a collection of data.

Till now, we have used only for loop as the iterator. Let’s see how we can create a new iterator.

---

## Creating a Java Iterator

To create an iterator, we first need to import the `Iterator` interface from the java.util package as shown below.

`import java.util.Iterator;`

After importing it, we can create a new iterator using the built-in iterator() method. This method iterates over the iterable that calls it and returns the iterator as the output. Look at the following statements.

```java
// creating an ArrayList
ArrayList<String> colors = new ArrayList<>();

// adding elements to the ArrayList

// creating an iterator for the ArrayList
Iterator<String> my_iterator = colors.iterator();
```

Here, an arraylist named colors is created and some elements are added to it. In the last statement, the arraylist colors calls the `iterator()` method and so `iterator()` returns an iterator named `my_iterator` which can be used to iterate over colors.

Summing up, an iterator named `my_iterator` is created which can be used to iterate over the arraylist colors. We can give any other name also to the iterator instead of `my_iterator`.

Cool! But how will we iterate?

To iterate, Java also provides another built-in method `next()` which the iterator returned by the `iterator()` method uses to do iteration over the iterable.

Seems confusing? Ok, it must have been. Just understand that the iterator() method is used to create an iterator and that iterator uses the `next()` method to iterate over an iterable like arraylist, array, etc.

Let’s create a simple iterator.

```java
import java.util.ArrayList;
import java.util.Iterator;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		//creating an iterator named my_iterator
		Iterator<String> my_iterator = colors.iterator();
		
		// iterate over the ArrayList colors using next()
		// 1st iteration
		System.out.println(my_iterator.next());
		
		// 2nd iteration
		System.out.println(my_iterator.next());
		
		// 3rd iteration
		System.out.println(my_iterator.next());
		
		// 4th iteration
		System.out.println(my_iterator.next());
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Red
Blue
Green
Orange
</pre>
    </details>
</div>

The `iterator()` method is called by the arraylist colors and returns an iterator. We named the returned iterator as my_iterator (You can give any other name to the iterator). Hence, we got our iterator.

Now, to iterate over the arraylist, the iterator calls the `next()` method. When the first time `next()` is called by writing `my_iterator.next()`, it returns the first element of the arraylist. On calling `next()` the second time, it returns the second element of the arraylist. This goes on for each call of `next()`.

It was this simple to create an iterator.

If in the above example, we call `next()` one more time, then it will throw the NoSuchElementException exception because there is no more element in the arraylist to iterate through. This is shown below.

```java
import java.util.ArrayList;
import java.util.Iterator;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		//creating an iterator named my_iterator
		Iterator<String> my_iterator = colors.iterator();
		
		// iterate over the ArrayList colors using next()
		// 1st iteration
		System.out.println(my_iterator.next());
		
		// 2nd iteration
		System.out.println(my_iterator.next());
		
		// 3rd iteration
		System.out.println(my_iterator.next());
		
		// 4th iteration
		System.out.println(my_iterator.next());
		
		// 5th iteration
		System.out.println(my_iterator.next());
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Red
Blue
Green
Orange

Exception in thread "main" java.util.NoSuchElementException
	at java.base/java.util.ArrayList$Itr.next(ArrayList.java:1000)
	at Test.main(Test.java:32)
</pre>
    </details>
</div>

So you now know how to create an iterator using the `iterator()` method.

In the above example, there were four elements in the arraylist. Now suppose you want to iterate through an arraylist which has 100 elements. That means you will have to call the `next()` method 100 times which is not feasible. This problem can be solved by looping through the arraylist using the `hasNext()` method as discussed below.

---

## Looping Through a Java Iterator

To avoid calling the `next()` method again and again manually, we can call it inside a while loop, as shown below.

```java
import java.util.ArrayList;
import java.util.Iterator;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		//creating an iterator named my_iterator
		Iterator<String> my_iterator = colors.iterator();
		
		// iterate over the ArrayList colors using next()
		while(my_iterator.hasNext()) {
			System.out.println(my_iterator.next());
		}
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Red
Blue
Green
Orange
</pre>
    </details>
</div>

In this example, the iterator calls the `next()` method inside a while loop. The condition of the loop is `my_iterator.hasNext()`. The `hasNext()` method checks if there are more elements in the iterable (collection). If there are more elements, then it returns true, otherwise it returns false.

**In the first iteration**, the condition `my_iterator.hasNext()` is true. Hence, its body gets executed and `my_iterator.next()` returns "Red".

**In the second iteration**, the condition is again true. So, `my_iterator.next()` returns "Blue".

**In the third iteration**, the condition is again true and so `my_iterator.next()` returns "Green".

**In the fourth iteration**, the condition is true and so `my_iterator.next()` returns "Orange".

After this, when the condition `my_iterator.hasNext()` is checked again, then it returns false because there is no more element after "Orange" in the collection. Hence, the loop got terminated.

So, there are two benefits of using such a loop to iterate.

1.  You don’t have to call next() again and again, saving your effort and making the code more clean.
2.  You don’t need to count the number of elements in the collection to call next() that number of times. It will also prevent the NoSuchElementException exception that gets thrown on calling next() more number of times.

---

## Removing Elements from a Collection

In the topic ArrayList, we saw that elements of an arraylist can be removed by using the `remove()` method. We also know that we can iterate over an arraylist using a for loop or any other loop.

However, we can’t add, modify or remove elements of an arraylist while iterating over it. Let’s try to remove an element of an arraylist while looping over the arraylist.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		// iterating over the ArrayList
		for(String color: colors) {
			if(color == "Blue") {
				// removing element
				colors.remove(color);
			}
		}
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Exception in thread "main" java.util.ConcurrentModificationException
	at java.base/java.util.ArrayList$Itr.checkForComodification(ArrayList.java:1043)
	at java.base/java.util.ArrayList$Itr.next(ArrayList.java:997)
	at Test.main(Test.java:15)
</pre>
    </details>
</div>

In this program, we are using a for-each loop to iterate over the arraylist colors. Inside the loop, we are also checking whether the current element is equal to "Blue". If it is equal, we are removing the element.

On running the above program, we got the ConcurrentModificationException exception because we can’t modify a collection while iterating over it. This is because on modifying, the size of the collection gets changed.

> A collection can’t be modified while iterating over it.

If anyhow you want to modify elements of a collection while iterating, then that can be done using the `remove()` method of an iterator as shown below.

```java
import java.util.ArrayList;
import java.util.Iterator;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		//creating an iterator named my_iterator
		Iterator<String> my_iterator = colors.iterator();
		
		// iterate over the ArrayList colors
		while(my_iterator.hasNext()) {
			if(my_iterator.next() == "Blue") {
				my_iterator.remove();
			}
		}
		
		// printing the ArrayList
		System.out.println(colors);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">[Red, Green, Orange]
</pre>
    </details>
</div>

Here inside the while loop, we are checking if the element returned by the iterator is equal to "Blue". If it is equal, then the statement my_iterator.remove() is removing the element.

In the second iteration of the loop, the element returned by  `my_iterator.next()` is "Blue". Hence this element is removed from the arraylist using the `remove()` method.

Thus, we were able to remove an element from a collection while iterating over it using iterators, which was not possible using a for or a for-each loop. This is an advantage of iterators over for or for-each loops.

The significance of using iterators can be that it helps us save memory. For example, if we want to display all the numbers from 1 to 100, we need not store them all in the memory at once. Instead, only one element is stored in the memory at once.

An iterator is a powerful tool which when used at the correct time can save us a lot of memory. So use iterators with caution.

> A real warrior never quits.
>
> \- Po

---


<a href="41-java-nested-classes.md" class="next">Next</a>
