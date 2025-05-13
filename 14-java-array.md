# Java Array

In English, array means collection. In Java also, an array is a collection of similar types of data. For example, an array of *int* is a collection of integers, an array of *double* is a collection of doubles, etc.

![array in Java](https://web.archive.org/web/20220811213715im_/https://www.codesdope.com/pa-images-bucket/courses/java/a1.png)

To understand the need of an array, let’s look at an example.

Suppose you want to store the marks of a student, then you can store it in a variable. This you already know.

Now, suppose you have 100 students in a class and you want to store the marks of all the students. One way to do this is to store the marks of 100 students in 100 different variables. Using 100 variables is not a good choice. A better solution is to use an array to store these 100 values (marks) and then store that array in a variable. Yes, a really good work around!

So let’s see how we can create and use arrays in Java.

## Declaration of an Array in Java

In Java, an array is declared as:

```java
type[] arrayName = new type[array_size];
```

Here, **arrayName** is the name of the array, **type** is the data type of the values that the array will store and **array_size** is the number of values that the array will store.

For example, an array to store 6 integers can be declared as:

`int[] arr = new int[6];`

Let’s understand this declaration.

`int[] arr` → An array of integers named arr is declared.

`new int[6]` → A memory space to store 6 integers is assigned to the array.

![allocation of space to array in Java](https://web.archive.org/web/20220811213715im_/https://www.codesdope.com/pa-images-bucket/courses/java/p20.png)

We can also do the same in two different lines.

```java
class Test {

    public static void main(String[] args) {
        int[] arr;
        arr = new int[6];
    }
}
```

Similarly, an array named `words` to store 5 English words can be declared as:

`String[] words = new String[5];`

Now that we know how to declare an array, the next section shows the ways we can assign values to an array.

## Initialization of an Array in Java

We can declare and initialize an array at the same time as:

`int[] arr = new int[]{8, 10, 2, 7, 4, 56};`

Or even as:

`int[] arr = {8, 10, 2, 7, 4, 56};`

Both the above statements declare an array named `arr` and store the integers 8, 10, 2, 7, 4 and 56 in it. We can also say that 8, 10, 2, 7, 4 and 56 are the elements of the array.

The pictorial view of the array `arr` is shown below.

| element | 8   | 10  | 2   | 7   | 4   | 56  |
| :------ | :-: | :-: | :-: | :-: | :-: | :-: |
| index   | 0   | 1   | 2   | 3   | 4   | 5   |

Every element in an array has a unique index. Indices start from 0. Therefore, the index of the first element is 0, the index of the second element is 1, and so on.

In the above example of array `arr`, the index of 8 is 0, 10 is 1, 2 is 2, 7 is 3, 4 is 4 and 56 is 5. Thus, the index of the elements in the array is from 0 to 5.

Index of an array starts with 0.

An element of an array can be accessed using the following syntax.

```java
arrayName[index]
```

Therefore, the 1<sup>st</sup> element of the array `arr` can be accessed by writing `arr[0]`, the 2<sup>nd</sup> element can be accessed by writing `arr[1]`, and so on.

We can also declare an array once and then initialize it if we don’t know the elements with which we have to initialize it at the time of declaration. Let’s see how.

```java
// declaration of array int[]
arr = new int[6];
```

```java
// initialization of array
arr[0] = 8;
arr[1] = 10;
arr[2] = 2;
arr[3] = 7;
arr[4] = 4;
arr[5] = 56;
```

The above set of statements first declared an array `arr` of size 6 and then assigned values to its 6 elements.

`arr[0] = 8` → `arr[0]` represents the first element of the array `arr` and is assigned the value 8. So, the first element of the array becomes 8. Similarly, values to the other elements are also assigned.

Summing up, we discussed three ways we can initialize an array. For example, an array named `myarray` can be initialized with integers 10, 20 and 30 by three methods.

#### Method 1

```java
int[] myarray = new int[]{10, 20, 30};
```

#### Method 2

```java
int[] myarray = {10, 20, 30};
```

#### Method 3

```java
int[] myarray = new int[3];
myarray[0] = 10;
myarray[1] = 20;
myarray[2] = 30;
```

## Accessing Elements of an Array in Java

As already seen above, the elements of an array can be accessed using their index. For example, the first element of an array `myarray` can be accessed through `myarray[0]`, the second element through `myarray[1]`, etc.

Let’s see an example.

```java
class Test {

    public static void main(String[] args) {
        int[] myarray = { 10, 20, 30 };
        System.out.println("First element: " + myarray[0]);
        System.out.println("Second element: " + myarray[1]);
        System.out.println("Third element: " + myarray[2]);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">First element: 10
Second element: 20
Third element: 30
</pre>
    </details>
</div>

Here, `myarray[0]` returns the 1<sup>st</sup> element (having index 0), `myarray[1]` returns the 2<sup>nd</sup> element (having index 1) and `myarray[2]` returns the 3<sup>rd</sup> element (having index 2) of the array.

Look at another example.

```java
class Test {

    public static void main(String[] args) {
        int[] x = new int[10];
        x[0] = 223;
        x[1] = 23;
        int[] y = { 23, 32, 43, 12, 43 };
        System.out.println(x[0]);
        System.out.println(x[1]);
        System.out.println(y[3]);
        System.out.println(y[0]);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">223
23
12
23
</pre>
    </details>
</div>

In this example, we declared an array named `x` with 10 elements but assigned values to only the first and second elements (`x[0]` and `x[1]`). We declared another array `y` with 5 elements and initialized all its elements.

Now let’s create an array of strings.

```java
class Test {

    public static void main(String[] args) {
        String[] fruits = { "Apple", "Banana", "Orange" };
        fruits[1] = "Grapes"; // changing value of 2nd element (having index 1)

        System.out.println("First element: " + fruits[0]);
        System.out.println("Second element: " + fruits[1]);
        System.out.println("Third element: " + fruits[2]);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">First element: Apple
Second element: Grapes
Third element: Orange
</pre>
    </details>
</div>

Here, we created an array named `fruits` having 3 elements - "Apple", "Banana" and "Orange". After that, we changed the value of the second element by writing `fruits[1] = "Grapes"`.

## Iterating through an Array in Java

If we want to go through each element of an array to print it, assign it a value, increase its value by 1, etc., then it can be done by iterating over the array using loops.

### for, while, do...while Loops

Look at the following example.

```java
class Test {

    public static void main(String[] args) {
        int[] myarray = { 10, 20, 30 };

        System.out.println("Elements of the array are:");

        // printing elements of array
        for (int i = 0; i < 3; i++) {
            System.out.println(myarray[i]);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Elements of the array are:
10
20
30
</pre>
    </details>
</div>

We created an array `myarray` having three elements, and used a `for` loop to print the three elements.

**In the first iteration**, the value of i is 0, thus printing myarray[0], i.e., 10.

**In the second iteration**, the value of i is 1, thus printing myarray[1], i.e., 20.

**In the third iteration**, the value of i is 2, thus printing myarray[2], i.e., 30.

Look at another example.

```java
class Test {

    public static void main(String[] args) {
        int[] myarray = { 10, 20, 30 };

        System.out.println("Elements of the array are:");

        // printing elements of array
        for (int i = 0; i < myarray.length; i++) {
            System.out.println(myarray[i]);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Elements of the array are:
10
20
30
</pre>
    </details>
</div>

`length` is a method in Java which returns the number of elements in an array. In the above example, `myarray.length` returns the number of elements in `myarray` i.e. 3. The rest of the code is the same as in the previous example.

Now that you know how to iterate over an array, let’s write a program to create an array of 5 integers entered by the user.

```java
import java.util.Scanner;

class Test {
	public static void main(String[] args) {
		int[] myarray = new int[5];
		Scanner s = new Scanner(System.in);
		
		System.out.println("Enter 5 integers of array");
		
		// taking input
		for(int i = 0; i < 5; i++) {
			myarray[i] = s.nextInt();
		}
		
		System.out.println("Elements of the array are:");
		
		// printing elements of array
		for(int i = 0; i < 5; i++) {
			System.out.println(myarray[i]);
		}
	}
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter 5 integers of array
<span style="color:#ce9d9d;">11</span>
<span style="color:#ce9d9d;">34</span>
<span style="color:#ce9d9d;">20</span>
<span style="color:#ce9d9d;">50</span>
<span style="color:#ce9d9d;">60</span>
Elements of the array are:
11
34
20
50
60
</pre>
    </details>
</div>

There are two `for` loops in this example. In the first loop, we are assigning the values entered by the user to the elements of the array. In the second loop, we are printing the values of the elements of the array.

**In the first for loop**, there are five iterations from *i = 0* till *i = 4*.

In the first iteration, the value of i is 0. The statement `myarray[i] = s.nextInt()` reads the integer entered by the user and assigns it to *myarray[0]* (first element of the array).

In the second iteration, the value of i is 1. Again an integer entered by the user is read and assigned to *myarray[1]* (second element of the array).

In this way, values are assigned to all the five elements of the array in the five iterations.

**In the second for loop**, there are five iterations from *i = 0* till *i = 4*. In each iteration, an element of the array is printed.

In this way, we used the first `for` loop for taking user input for the elements of the array and the second `for` loop to print the elements of the array.

Similarly, we can iterate over an array using `while` and `do...while` loops as well.

### for-each Loop

There is a new form of `for` loop. There is no official name of this loop, but the term `for-each` is used most often. It is used to iterate over an array. Let's see its example.

```java
class Test {

    public static void main(String[] args) {
        int[] myarray = { 10, 20, 30, 40, 50, 60, 70, 80, 90, 100 };

        System.out.println("Elements of the array are:");

        // printing elements of array
        for (int num : myarray) {
            System.out.println(num);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Elements of the array are:
10
20
30
40
50
60
70
80
90
100
</pre>
    </details>
</div>

The explanation is simple. Here, the variable `num` goes to each element in the array `myarray` and takes its value, and that value is printed.

![for-each animation in Java](https://web.archive.org/web/20220811213715im_/https://www.codesdope.com/pa-images-bucket/courses/java/p21.gif)

In the first iteration, the value of `num` is 10, in the second iteration its value is 20, and so on. Just focus on the syntax of this loop, the rest of the part is easy.

If you have understood all about arrays uptil now, that means you are doing great. If not, re-read the topic and ask your doubts in the [discussion forum](https://web.archive.org/web/20220811213715/https://www.codesdope.com/discussion/).

## Java Passing Array in Method

We can pass a single element of an array or the entire array as argument to a method.

### Passing a Single Element of an Array to a Method

Passing an element of an array means passing a normal value to the method.

```java
class Test {

    public static void display(int n) {
        System.out.println(n);
    }

    public static void main(String[] args) {
        int[] myarray = { 1, 2, 3, 4, 5 };

        // calling display() method
        display(myarray[2]);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">3
</pre>
    </details>
</div>

We passed `myarray[2]` to the `display()` method. `myarray[2]` is an integer and so is passed just like a normal value is passed.

### Passing an Array to a Method

An entire array can be passed to a method by passing the array name as argument, and giving an additional `[ ]` after the data type of the array in the parameter definition.

The following program stores the marks of five students in an array and prints the average of the marks of the students.

```java
class Test {

    public static double getAverage(double[] arr) {
        double sum = 0, avg = 0;

        // calculating sum of marks
        for (int i = 0; i < arr.length; i++) {
            sum += arr[i]; // same as sum = sum + arr[i]
        }

        // calculating average of marks
        avg = sum / arr.length;

        // returning average
        return avg;
    }

    public static void main(String[] args) {
        double[] marks = { 80.5, 90, 74, 46.5, 80 };

        // calling getAverage() method
        System.out.println(getAverage(marks));
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">74.2
</pre>
    </details>
</div>

Here, the marks of five students are stored in an array named `marks`. We defined a method named `getAverage()` that takes the array and returns the average of the elements (marks of the students) of the array.

`getAverage(marks)` → To pass the array to the method, simply the name of the array, i.e. `marks`, is passed as the argument.

`getAverage(double[] arr)` → Since the parameter takes an array, *double[]* is written instead of just *double*.

You can understand the rest of the code from comments.

## Returning Array from Method

An array can be returned from a method by returning the array name as argument, and writing the return type as the data type of the array followed by `[ ]`.

```java
class Test {

    public static int[] getArray() {
        double sum = 0, avg = 0;

        int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8 };

        // returning array
        return arr;
    }

    public static void main(String[] args) {
        int[] arr1 = getArray();

        for (int i = 0; i < arr1.length; i++) {
            System.out.println(arr1[i]);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">1
2
3
4
5
6
7
8
</pre>
    </details>
</div>

In this example, the `getArray()` method returns an array named arr.

`return arr` → This statement returns the array `arr`.

`int[] getAverage()` → Since the array returned by the method is of type int, the return type of the method is written as *int[]* instead of just *int*.

## Java 2D Arrays

The arrays we studied till now were 1-dimensional, as shown below.

| element | 8   | 10  | 2   | 7   | 4   | 56  |
| :------ | :-: | :-: | :-: | :-: | :-: | :-: |
| index   | 0   | 1   | 2   | 3   | 4   | 5   |

A 2-dimensional array is generally known as a matrix. It stores data in the form of rows and columns as shown below.

|         | Column 0 | Column 1 | Column 2 | Column 3 |
| :------ | :------- | :------- | :------- | :------- |
| Row 0   |          |          |          |          |
| Row 1   |          |          |          |          |

So let’s see how to declare and initialize a 2-dimensional array.

### Declaration of a 2D Array

A 2-dimensional array is declared as:

```java
type[][] arrayName = new type[row_size][column_size];
```

Here, **arrayName** is the name of the array, **type** is the data type of the values that the array will store, **row_size** is the number of rows in the array and **column_size** is the number of columns in the array.

Let’s define a 2-dimensional array.

`int[][] a = new int[2][4];`

This is a 2-dimensional array of type int having 2 rows and 4 columns as shown below.

|         | Column 0 | Column 1 | Column 2 | Column 3 |
| :------ | :------- | :------- | :------- | :------- |
| Row 0   | a[0][0]  | a[0][1]  | a[0][2]  | a[0][3]  |
| Row 1   | a[1][0]  | a[1][1]  | a[1][2]  | a[1][3]  |

The second way is to declare and assign values at the same time where each inner curly braces represent one row.

```java
int a[][] = {
    {1, 2, 3},
    {4, 5, 6}
};
```

Here, the value of *a[0][0]* is 1, *a[0][1]* is 2, *a[0][2]* is 3, *a[1][0]* is 4, *a[1][1]* is 5 and *a[1][2]* is 6.

The third way is shown below.

```java
int a[][] = new int[][]{
    {1, 2, 3},
    {4, 5, 6}
};
```

### Applications of 2D Arrays

Suppose there are 3 students and all the students are studying 2 subjects (*Subject 1* and *Subject 2*). We want to display the marks of all the students in the two subjects which we will be taking from the user. We can use a 2-dimensional array for that as done in the following example.

```java
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        double[][] marks = new double[3][2];
        Scanner s = new Scanner(System.in);

        // taking input
        for (int i = 0; i < 3; i++) {
            System.out.println("Enter marks of student : " + (i + 1));
            for (int j = 0; j < 2; j++) {
                System.out.println("Subject : " + (j + 1));
                marks[i][j] = s.nextDouble();
            }
        }

        // printing output
        for (int i = 0; i < 3; i++) {
            System.out.println("Student" + (i + 1));
            for (int j = 0; j < 2; j++) {
                System.out.println("Subject" + (j + 1) + ":" + marks[i][j]);
            }
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Enter marks of student : 1
Subject : 1
<span style="color:#ce9d9d;">10</span>
Subject : 2
<span style="color:#ce9d9d;">20</span>
Enter marks of student : 2
Subject : 1
<span style="color:#ce9d9d;">30</span>
Subject : 2
<span style="color:#ce9d9d;">10</span>
Enter marks of student : 3
Subject : 1
<span style="color:#ce9d9d;">20</span>
Subject : 2
<span style="color:#ce9d9d;">40</span>
Student1
Subject1:10.0
Subject2:20.0
Student2
Subject1:30.0
Subject2:10.0
Student3
Subject1:20.0
Subject2:40.0
</pre>
    </details>
</div>

In this example, an array named `marks` having 3 rows and 2 columns is defined by writing `double[][] marks = new double[3][2]`.

The elements of the array will contain the marks of the 3 students in the 2 subjects as shown below.

|         | Subject 1 | Subject 2 |
| :------ | :-------- | :-------- |
| Student 1 | 10        | 20        |
| Student 2 | 30        | 20        |
| Student 3 | 20        | 40        |

First, the array is initialized with the values entered by the user using a `for` loop inside another for loop.

**In the first iteration of the outer `for` loop**, the value of i is 0. In its body, “*Enter marks of student : 1*” gets printed and the inner `for` loop gets executed.

**In the first iteration of the inner for loop**, the value of  `i` is 0 and that of  `j` is 0, and thus `marks[i][j]` is *marks[0][0]*. In its body, “*Subject : 1*” gets printed and the statement `marks[i][j] = s.nextDouble()` assigns the value entered by the user to *marks[0][0]*.

**In the second iteration of the inner for loop**, the value of  `i` is 0 and that of  `j` is 1, and thus `marks[i][j]` is *marks0][1]*. In its body, “*Subject : 2*” gets printed and the value entered by the user is assigned to *marks[0][1]*.

**In the third iteration of the inner for loop**, the value of  `i` is 0 and that of  `j` is 2, and thus `marks[i][j]` is *marks[0][2]*. In its body, “*Subject : 3*” gets printed and the value entered by the user is assigned to *marks[0][3]*.

Similarly, in the second and third iterations of the outer `for` loop, the same process is repeated for student 2 and student 3 respectively.

After assigning the values to the elements of the array, the values of the elements of the array are printed in the same way using a `for` loop inside another `for` loop.

Let’s see another example of a 2-dimensional array.

Suppose there are 2 factories and each of these factories produces items of 4 different types, like some items of type 1, some items of type 2 and so on. We have to calculate the total products of each factory i.e. sum of the items of all types that a factory produces.

```java
class Test {

    public static void main(String[] args) {
        int[][] items = new int[2][4];
        items[0][0] = 2;
        items[0][1] = 5;
        items[0][2] = 7;
        items[0][3] = 4;
        items[1][0] = 9;
        items[1][1] = 3;
        items[1][2] = 2;
        items[1][3] = 8;

        int sum1 = 0, sum2 = 0;

        // calculating sum of items produced in first factory
        for (int i = 0; i < 4; i++) {
            sum1 += items[0][i];
        }
        System.out.println("Total items produced in first factory: " + sum1);

        // calculating sum of items produced in second factory
        for (int i = 0; i < 4; i++) {
            sum2 += items[1][i];
        }
        System.out.println("Total items produced in first factory: " + sum2);
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Total items produced in first factory: 18
Total items produced in first factory: 22
</pre>
    </details>
</div>

Here, `items[0][i]` represents the number of items of the first factory of type `i`, where `i` takes value from 0 to 3 and `items[1][i]` represents the number of items of the second factory of type `i`. For example, `items[0][2]` represents the items of the first factory of type 3 and `items[1][2]` represents the items of the second factory of type 3.

`sum1` is the sum of all the items of the first factory and `sum2` is the sum of all the items of the second factory.

This completes the topic of Arrays. Arrays are quite useful to store similar types of data in a single variable, thus also saving memory. You will be using arrays a lot in programming.

> It's not about how much we lost. It's about how much we have left.
>
> - Tony Stark


<a href="15-java-strings.md" class="next">Next</a>
