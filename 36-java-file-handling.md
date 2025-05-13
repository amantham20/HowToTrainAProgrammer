# Java File Handling
Files are used to store data. We use files in our computer, mobile and other devices to store data like projects, notes or even stories. In this topic, you will learn about reading data from a file and writing data to the file using a Java program. Yes, we can do that in Java.

Let’s start by learning to create a file.

## Creating a File
For creating a new file, the File class available in the java.io package is used. Therefore, it has to be imported by writing the following statement.

`import java.io.File;`

A new file can be created using the `createNewFile()` method. This method returns true if the required file got successfully created and false if the file already exists.

Let’s write a program to create a file.

```java
import java.io.File;

class Test {

    public static void main(String[] args) {
        File fileObj = new File("example.txt");

        try {
            // creating file
            boolean success = fileObj.createNewFile();

            // printing a message on screen
            if (success) {
                System.out.println("File got created");
            } else {
                System.out.println("File already exists");
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">File got created
        </pre>
    </details>
</div>

In the above example, we created a new file named *example.txt*. Let’s understand the entire program.

Look at the following statement from the above example.

`File fileObj = new File("example.txt");`

In this statement, we created an object fileObj of the File class by passing the name of the file to be created to the constructor. In our case, we passed “*example.txt*” because we wanted the file name to be *example.txt*.

Then we wrote the following example inside the try block.

`boolean success = fileObj.createNewFile();`

We called the `createNewFile()` method on the file object fileObj. This method creates a new file with the name *example.txt* and returns true. However, if a file with the name *example.txt* already exists, then this method doesn’t create any file and returns false. So, the value of the variable success is true if a new file gets created and false if no file gets created.

Further based on the value of success, we are also displaying an appropriate message on the screen.

This is how we can create a file with any file name using Java. Now after creating a file, let’s learn to write something in a file.

## Writing to a File
Writing something in a file is also easy. For writing to a file, the FileWriter class available in the java.io package is used. Therefore, it has to be imported by writing the following statement.

`import java.io.FileWriter;`

To write to a file, the `write()` method is used.

```java
class Test {

    public static void main(String[] args) {
        try {
            FileWriter myWriter = new FileWriter("example.txt");

            // writing to a file
            myWriter.write("Hello!!");
            myWriter.write("Welcome to the Java course of CodesDope.");

            // closing the file
            myWriter.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

In this example, we wrote the text *Hello!!* and *Welcome to the Java course of CodesDope* to a file named *example.txt*.

Look at the following statement.

`FileWriter myWriter = new FileWriter("example.txt");`

Here, we created an object myWriter of the FileWriter class by passing the name of the file to which you want to write something. We passed “*example.txt*” because we wanted to write in the *example.txt* file.

Now look at the next statement.

`myWriter.write("Hello!!");`

We called the `write()` method on the object myWriter. This method wrote the text `Hello!!` to the *example.txt* file.

Similarly, the next statement printed Welcome to the *Java course of CodesDope* in the file.

The final contents of the example.txt file become:

**example.txt**

```
Hello!!Welcome to the Java course of CodesDope.
```

If you want to write some of the text on the next line in the file, then write `\n` before that as done in the following example.

```java
import java.io.FileWriter;

class Test {

    public static void main(String[] args) {
        try {
            FileWriter myWriter = new FileWriter("example.txt");
            // writing to a file
            myWriter.write("Hello!!");
            myWriter.write("\nWelcome to the Java course of CodesDope.");

            // closing the file
            myWriter.close();
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

Notice the following statement in this example.

`myWriter.write("\nWelcome to the Java course of CodesDope.");`

Here, instead of `\n`, a new line got printed in the file, making its content as follows.

**example.txt**

```
Hello!!
Welcome to the Java course of CodesDope.
```

Now let’s learn to read the data stored in a file.

## Reading a File
For reading a file, the FileReader class available in the java.io package is used by importing it as follows.

`import java.io.FileReader;`

To write to a file, the `read()` method is used.

Suppose you have a file named example.txt with the following content.

**example.txt**

```
Hello!!
Welcome to the Java course of CodesDope.
```

```java
import java.io.File;
import java.util.Scanner;

class Test {

    public static void main(String[] args) {
        try {
            File fileObj = new File("example.txt");

            Scanner myReader = new Scanner(fileObj);

            // reading and printing data of file
            while (myReader.hasNextLine()) {
                String data = myReader.nextLine(); // reading data
                System.out.println(data); // printing data
            }
        } catch (Exception e) {
            System.out.println(e);
        }
    }
}
```

<div class="collapse">
    <details>
        <summary>Output</summary>
        <pre class="output">Hello!!
Welcome to the Java course of CodesDope.
        </pre>
    </details>
</div>

In the above example, we read the data stored in the file namedexample.txt and printed the read data. Let’s understand this program line by line.

`File fileObj = new File("example.txt");`

In the above statement, we created an object fileObj of the File class by passing the name of the file whose data we want to read.We passed “*example.txt*” because we wanted to read the data of the *example.txt* file.

`Scanner myReader = new Scanner(fileObj);`

Here, we created an object myReader of the Scanner class by passing the file object fileObj created from the previous statement.

Look at the following while loop.

```java
while(myReader.hasNextLine()) {
    String data = myReader.nextLine(); // reading data
    System.out.println(data); // printing data
}
```

The condition of the loop is `myReader.hasNextLine()` which checks if there is an unread line of data in the file. It returns true if there is an unread line of data present and returns false if not. This means that the loop will execute until all the data in the read has been read.

**In the first iteration of the loop**,

In the first statement, `myReader.nextLine()` reads the first line “*Hello!!*” and assigns it to the variable data. The second statement prints the value of data.

**In the second iteration of the loop**,

In the first statement, `myReader.nextLine()` reads the second line “*Welcome to the Java course of CodesDope*” and assigns it to data. The second statement prints the value of data.

Now you know how to do basic file operations in Java. You must also agree that file handling is easy in Java because we just need a few lines of code to read the content of a file or to write something in a file. 

> As we look ahead into the next century, leaders will be those who empower others.
>
> \- Bill Gates


<a href="37-java-wrapper-classes.md" class="next">Next</a>
