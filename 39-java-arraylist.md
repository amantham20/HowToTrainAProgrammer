# Java ArrayList

In the topic [Arrays](https://web.archive.org/web/20240416072046/https://www.codesdope.com/course/java-array/), we saw that arrays are used to store similar types of data. In Java, we also have arraylists which are also used to store similar types of data just like arrays.

Before exploring further, let’s see how arraylists are different from arrays and their significance.

## Use of ArrayList in Java

Consider a case where you want to store the marks of the students of a class. Obviously, you will choose an array for that, with each element of the array storing the marks of a student. But suppose you don’t know the number of students in the class and will be asking the user to enter the number of students when the program gets executed.

Now there is a problem here. We know that we have to specify the size of an array (number of elements in an array) while declaring it. After declaration of the array, we can’t modify its size. In our case, we will only know the number of students (i.e. the size of the array) only when the program executes.

In this scenario, we can declare the array with any number of elements. Now, if the size of the array is smaller than the number of students, then the marks of all the students could not be stored. Also, if the size of the array is much larger than the number of students, then unnecessarily extra memory will be allocated to the array which is not required.

In such cases where we want to modify the size of an array after its declaration, we can use an arraylist.

Arraylists are resizable arrays whose size can be changed after declaration.

Unlike arrays, the size of an arraylist can be changed after declaring it. This is the reason arraylists are also called **dynamic arrays**. For example, suppose we declared an arraylist with 10 elements. After declaration, we can add 2 elements making its number of elements equal to 12 or delete 3 elements making its number of elements equal to 7.

The dynamic behaviour of arraylists is the main reason they are preferred over arrays by programmers in many situations. So let’s learn to create and use an arraylist.

## Declaration of an ArrayList

Arraylists are implemented using the built-in `ArrayList` class from the `java.util` package. To use the `ArrayList` class, it first needs to be imported as shown below.

`import java.util.ArrayList;`

After importing the `ArrayList` class, an arraylist is declared as:

`ArrayList<type> arraylistName = new ArrayList<>();`

Here, **arraylistName** is the name of the arraylist and **Type** is the type of the elements that the arraylist will store.

For example, an arraylist to store integers can be declared as:

`ArrayList<integer> marks = new ArrayList<>();`

In this declaration, `marks` is the name of the arraylist and it stores the elements of type `Integer`. Note that here `Integer` is a wrapper class and not *int*.

In arraylists, primitive types like *int*, *double*, *char*, *boolean*, etc. are not used. Instead of primitive types, the corresponding wrapper classes like `Integer`, `Double`, `Character`, `Boolean`, etc. are used.

We know that each primitive type has a predefined wrapper class in Java and that wrapper class is used instead of the primitive type in arraylists. For example, the wrapper class for the primitive type *int* is `Integer`. Therefore, in an `ArrayList`, we will use `Integer` as the type instead of *int*. Similarly, the wrapper class for char is `Character`.

The list of wrapper classes corresponding to each of the 8 primitive types is given below.

| Primitive Type | Wrapper Class |
| -------------- | ------------- |
| byte           | Byte          |
| boolean        | Boolean       |
| char           | Character     |
| double         | Double        |
| float          | Float         |
| int            | Integer       |
| long           | Long          |
| short          | Short         |

Let’s see some examples of declaring arraylists.

```java
ArrayList<Integer> marks = new ArrayList<>();
```

As already seen earlier, `marks` is the name of an `ArrayList` of type `Integer`. Hence, this `ArrayList` will store int elements like 10, 20, etc.

Look at another example.

`ArrayList<char> alphabets = new ArrayList<>();`

Here, `alphabets` is the name of an `ArrayList` of type `Character`. Hence, it will store *char* elements like ‘e’, ‘f’, etc.

Similarly, we can declare an `ArrayList` of any other type. Apart from these wrapper classes, we can also create an `ArrayList` of type `String`. Let’s declare an `ArrayList` of type `String`.

`ArrayList<string> colors = new ArrayList<>();`

`colors` is the name of an `ArrayList` of type `String`. Therefore, it will store *String* elements like “Blue”, “Red”, etc.

Now that you know how to declare an `ArrayList`, let’s learn to add elements to it.

## Adding Elements to an ArrayList in Java

Adding elements in an `ArrayList` is simple. An element in an `ArrayList` is added using the `add()` method, as shown below.

`marks.add(10);`

The above statement will add 10 at the end of the `ArrayList` named `marks`.

Look at the following example.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<Integer> marks = new ArrayList<>();
		
		// adding elements in the ArrayList
		marks.add(50);
		marks.add(60);
		marks.add(40);
		marks.add(70);
		
		// printing the ArrayList
		System.out.println(marks);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">[50, 60, 40, 70]</pre>
    </details>
</div>

In the above example, we imported the `ArrayList` class from the `java.util` package. Then we created an arraylist named `marks` of type `Integer`, which means that it will store integers. After that, we added 50, 60, 40 and 70 to `marks`. Finally we printed the arraylist `marks` by simply writing `System.out.println(marks)`.

This created our arraylist.

Like arrays, the index of the elements of an ArrayList also starts from 0.

In the last example, the index of the element 50 is 0, 60 is 1, 40 is 2 and 70 is 3.

We can also add an element to an `ArrayList` at a specific index as shown below.

`marks.add(2, 10);`

The above statement will add 10 at the index 2 of the `ArrayList` named `marks`. Let’s show this in an example.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<Integer> marks = new ArrayList<>();
		
		// adding elements in the ArrayList
		marks.add(50);
		marks.add(60);
		marks.add(40);
		marks.add(70);
		
		// printing the ArrayList
		System.out.println(marks);
		
		// adding 80 at index 1
		marks.add(1, 80);
		
		// printing the ArrayList
		System.out.println(marks);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">[50, 60, 40, 70]
[50, 80, 60, 40, 70]</pre>
    </details>
</div>

In this example, initially we added 50, 60, 40 and 70 to the arraylist `marks` making it equal to [50, 60, 40, 70]. After that, we added 80 at index 1 to `marks` making it equal to [50, 80, 60, 40, 70].

This was easy. Did you also notice that we added elements to an `ArrayList` after declaring it? This is the beauty of an `ArrayList`.

## <type><integer><integer><char><string><integer><integer>Changing Elements in an ArrayList</integer></integer></string></char></integer></integer></type>

An element of an `ArrayList` can be changed using the `set()` method. This method takes two arguments - the first argument is the index of the element that you want to change and the second argument is the new element.

Take the following statement

`colors.add(2, “Green”);`

The above statement will replace the element present at the index 2 of the `ArrayList` named `colors` by the new element “Green”.

Let’s see an example in which an element of an `ArrayList` is changed.

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
		
		// printing the ArrayList
		System.out.println(colors);
		
		// changing element at index 1 to "Brown"
		colors.set(1, "Brown");
		
		// printing the ArrayList
		System.out.println(colors);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">[Red, Blue, Green, Orange]
[Red, Brown, Green, Orange]</pre>
    </details>
</div>

Initially the element at the index 1 of `colors` is "Blue". It is changed to "Brown" by writing `colors.set(1, "Brown")`.

## <type><integer><integer><char><string><integer><integer><string>Removing Elements from an ArrayList</string></integer></integer></string></char></integer></integer></type>

An element can be removed from an `ArrayList` by using the `remove()` method. This method takes one argument. In the argument, we can either pass the element to be removed or the index of the element to be removed.

For example, take the following two statements.

`colors.remove(“Green”);`

The above statement will remove the element "Green" from the `ArrayList` named `colors`.

`colors.remove(2);`

The above statement will remove the element present at index 2 from `colors`.

This is implemented in the following example.

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
		colors.add("Yellow");
		colors.add("Brown");
		
		// printing the ArrayList
		System.out.println("Initial ArrayList: " + colors);
		
		// removing "Blue"
		colors.remove("Blue");
		
		// printing the ArrayList
		System.out.println("After removing Blue: " + colors);
		
		// removing element at index 2 i.e. "Green"
		colors.remove(1);
		
		// printing the ArrayList
		System.out.println("After removing element at index 1: " + colors);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Initial ArrayList: [Red, Blue, Green, Orange, Yellow, Brown]
After removing Blue: [Red, Green, Orange, Yellow, Brown]
After removing element at index 1: [Red, Orange, Yellow, Brown]</pre>
    </details>
</div>

Here, the statement `colors.remove("Blue")` removed the element "Blue" from the arraylist `colors`. After that, the statement `colors.remove(1)` removed the element at index 1 from `colors`.

## Accessing Elements of an ArrayList

An element of an `ArrayList` can be accessed using the `get()` method. This method takes an index as the argument and returns the element present at that index.

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
		
		// accessing the element at index 2
		String color = colors.get(2);
		
		System.out.println(color);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Green</pre>
    </details>
</div>

Here, `` returns the element at index 2 in the arraylist `colors`. The returned element "Green" is assigned to the variable `color`.

## Java Size of an ArrayList

The size of an `ArrayList` means the number of elements in it. The `size()` method is used to return the size of an `ArrayList`.

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
		
		int num = colors.size();
		
		System.out.println("Number of elements in ArrayList: " + num);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number of elements in ArrayList: 4</pre>
    </details>
</div>

In this example, `colors.size()` returned 4 because the number of elements in `colors` is 4.

Now you know how to add, change, remove and access elements of an `ArrayList`. Now let’s see how we can iterate over an `ArrayList` in Java.

## Java Iterating an ArrayList

An `ArrayList` can be iterated using loops just like an array. We can iterate over an `ArrayList` using `while`, `do...while`, `for` and `for-each` loops.

The following example iterates over an `ArrayList` using a `for` loop.

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
Orange</pre>
    </details>
</div>

We created an arraylist `colors` and added four elements to it. A `for` loop is used to print the four elements.

**In the first iteration**, the value of *i* is 0, thus printing colors.get(0), i.e., "*Red*".

**In the second iteration**, the value of *i* is 1, thus printing colors.get(1), i.e., "*Blue*".

**In the third iteration**, the value of *i* is 2, thus printing colors.get(2), i.e., "*Green*".

**In the fourth iteration**, the value of *i* is 3, thus printing colors.get(3), i.e., "Orange".

The next example shows iteration over an `ArrayList` using a `for-each` loop.

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
		for(String color: colors) {
			System.out.println(color);
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
Orange</pre>
    </details>
</div>

Here, the variable `color` goes to each element in the arraylist `colors` and takes its value, and that value is printed.

In the first iteration, the value of `color` is "Red", in the second iteration its value is "Blue", and so on.

## Built-in Methods of Java ArrayList

The methods provided by Java which can be used with an `ArrayList` are described below.

### Java size()

It returns the size of an arraylist.

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
		
		int num = colors.size();
		
		System.out.println("Number of elements in ArrayList: " + num);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Number of elements in ArrayList: 4</pre>
    </details>
</div>

### Java sort()

It sorts the elements of an arraylist.

#### Java sort() Syntax

To sort an arraylist in ascending order:

`arrayListName.sort(Comparator.naturalOrder())`

Here `arrayListName` is the name of the arraylist and `Comparator` is an interface. The `naturalOrder()` of `Comparator` specifies that the elements of the arraylist will get sorted in ascending order.

To sort an arraylist in ascending order:

`arrayListName.sort(Comparator.reverseOrder())`

Here `arrayListName` is the name of the arraylist and `Comparator` is an interface. The `reverseOrder() `of `Comparator` specifies that the elements of the arraylist will get sorted in descending order.

#### Java sort() Example

```java
import java.util.ArrayList;
import java.util.Comparator;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		// sorting arraylist in ascending order
		colors.sort(Comparator.naturalOrder());
		System.out.println("Ascending order: " + colors);
		
		// sorting arraylist in descending order
		colors.sort(Comparator.reverseOrder());
		System.out.println("Descending order: " + colors);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Ascending order: [Blue, Green, Orange, Red]
Descending order: [Red, Orange, Green, Blue]</pre>
    </details>
</div>

As you can see, the statements `colors.sort(Comparator.naturalOrder())` and `colors.sort(Comparator.reverseOrder())` sorted the arraylist in ascending and descending orders respectively.

### Java contains()

It checks whether an element is present in an arraylist. If the element is present, it returns true, otherwise it returns false.

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
		
		System.out.println(colors.contains("Blue"));
		System.out.println(colors.contains("Yellow"));
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">true
false</pre>
    </details>
</div>

In this example, `colors.contains("Blue")` returned true because "Blue" is present in the arraylist `colors` and `colors.contains("Yellow")` returned false because "Yellow" is not present in the arraylist.

### Java isEmpty()

It checks whether an arraylist is empty or not. If the arraylist is empty, it returns true, otherwise it returns false.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named marks
		ArrayList<String> colors = new ArrayList<>();
		
		System.out.println("Is ArrayList empty? " + colors.isEmpty());
		
		// adding elements in the Array List
		colors.add("Red");
		colors.add("Blue");
		colors.add("Green");
		colors.add("Orange");
		
		System.out.println("Is ArrayList empty? " + colors.isEmpty());
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Is ArrayList empty? true
Is ArrayList empty? false</pre>
    </details>
</div>

Initially when the arraylist `colors` was empty, `colors.isEmpty()` returned true. After adding elements to it, `colors.isEmpty()` returned false.

### Java indexOf()

It returns the index of the specified element in an arraylist.

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
		
		System.out.println(colors.indexOf("Green"));
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">2</pre>
    </details>
</div>

`colors.indexOf("Green")` returned the index of "Green" in the arraylist `colors`.

If the specified element occurs more than once in an arraylist, then the index of its first occurrence is returned as shown below.

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
		colors.add("Green");
		
		System.out.println(colors.indexOf("Green"));
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">2</pre>
    </details>
</div>

In the above example, "Green" is present at indices 2 and 4 in the arraylist `colors`. However, the `indexOf()` method returned the index of only the first occurrence i.e. 2.

Finally, let’s talk about **autoboxing** and **unboxing** that we read in the chapter [Wrapper Classes](https://web.archive.org/web/20240416072046/https://www.codesdope.com/course/java-wrapper-classes/), and see how these two phenomena are useful in collections like arraylists.

## Autoboxing in Java ArrayList

Autoboxing is quite useful in collections. Let’s see how.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named mylist
		ArrayList<Integer> mylist = new ArrayList<>();
		
		// (autoboxing) add elements in the ArrayList
		mylist.add(5);
		mylist.add(10);
		
		// printing the ArrayList
		System.out.println(mylist);
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">[5, 10]</pre>
    </details>
</div>

In this example, we created an `ArrayList` named `mylist` of type `Integer`. This means that `mylist` will contain objects of the `Integer` class. Here autoboxing is taking place in the following two statements.

`mylist.add(5);`

`mylist.add(10);`

In the first statement, a primitive value 5 is passed to the `add()` method. Since `mylist` can contain only objects of the `Integer` class, 5 got automatically converted into an `Integer` object and got added to `mylist`.

## Unboxing in Java ArrayList

Like autoboxing, unboxing is also used in collections as shown in the next example.

```java
import java.util.ArrayList;

class Test {
	public static void main (String[] args) {
		// creating an ArrayList named mylist
		ArrayList<Integer> mylist = new ArrayList<>();
		
		// (autoboxing) add elements in the ArrayList
		mylist.add(5);
		mylist.add(10);
		
		// printing the ArrayList
		System.out.println("ArrayList: " + mylist);
		
		// (unboxing) return an element from ArrayList
		int num = mylist.get(1);
		
		// printing the returned element
		System.out.println("Element at index 1 of ArrayList: " + num);
		
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">ArrayList: [5, 10]
Element at index 1 of ArrayList: 10</pre>
    </details>
</div>

This program is the same as what we saw in autoboxing, except the last two statements. Here unboxing is taking place in the following statement.

`int num = mylist.get(1);`

In this statement, the `get()` method converts the object stored at index 1 in `mylist` to the primitive type *int* and then returns the *int* value. The returned value is assigned to the variable `num`.

Don’t Quit.

- Grand Master Oogway
