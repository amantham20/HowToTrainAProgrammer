# Java Tutorial - Introduction

Java is one of the most popular and important programming language in the world. Due to its distinct features, it is the most widely used language in every corner of the world and human life. From software and web applications to robotics, Java has become the most wanted language in today’s times.

## What make Java distinguishable ?

There are many features of Java which makes it so different from other  programming languages. As a result, it has become a must in software and hardware industries.

Let's have a look at some of those features.

*   **Simple -** It is designed to be easy to learn.
*   **Object-oriented -** In Java, everything is based around Object which has some data and behaviour. Java can be easily extended as it is based on Object Model.
*   **Platform independent -** This means that the same program works on any platform (operating system) without needing any modification.
*   **Robust -** Robust means strong. Java is a robust management as it has a feature of automatic garbage collection and memory management.
*   **Portable -** Programs written in Java are portable i.e., programs written for one type of computer or operating system can be run on another type of computer or operating system.
*   **High-performance -** Java enables high performance with the use of just-in-time compilers.

### Applications of Java

Java is not only used in software but is also widely used in designing hardware controlling software components. According to Sun, 3 billion devices run Java.

Following are some of the usage of Java :

*   Desktop Applications such as acrobat reader, media player, antivirus etc.
*   Web Applications
*   Mobile Operating System like Android
*   Embedded System
*   Robotics
*   Banking applications
*   Games

### JDK, JRE and JVM

Before moving forward, let's first understand the three terminologies - JDK, JRE and JVM.

After writing any program in Java, we need to compile and run it to see the output of the program.

When we write any program in Java language, it needs to be converted to machine language so that the computer can understand and execute it. This conversion is known as compiling and we compile a code with the help of the **compiler**.

Let's look at another term - platform. A **platform** is the hardware or software environment in which a program runs.

Unlike other programming languages such as C, C++, etc which are platform dependent, Java is a platform independent language. Platform dependent languages mean that the program written for one operating system can only run on that operating system. This means that a code written in Linux can only be run on a computer having Linux. A Java program on the other hand, can be run on any operating system.

**Java Development Kit (JDK)**

Java Developer Kit contains tools such as compilers needed to develop the Java programs. A Compiler converts Java code into bytecode.

**Java Virtual machine (JVM)**

It is a virtual machine that runs the Java bytecodes. The JVM doesn't understand Java source code (the language in which we write Java programs), so first, the source code is compiled into bytecode which can be understood by the JVM. The JVM provides a platform-independent way of executing code, thus making Java platform independent.

**Java Runtime Environment (JRE)**

Java Runtime Environment contains JVM, class libraries, and other supporting files. Actually, JVM runs the program and it uses the class libraries and other supporting files provided in JRE. If you want to run any Java program, you need to have JRE installed in the system

## How to Start ?

Once our Java program has been written, it needs to be compiled and run. As Java is platform independent, a Java program written in any operating system can be run on all the operating systems. Now let's learn how to run a Java program on different operating systems.

### Windows

Here, we will talk about running a Java code using NetBeans and Command Prompt.

You may need to install the Java Development Kit from their website. You can download it from [here](https://web.archive.org/web/20220603091236/http://www.oracle.com/technetwork/java/javase/downloads/index.html).

#### NetBeans

1.  Download and start NetBeans IDE.

2.  In the IDE, choose File > New File, as shown in the figure below.

<p>
<img alt="open new java file in Netbeans" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_ide_file.jpg" style="max-width:60%;height:auto;"/>
</p>

3.  Choose Java class

<p>
<img alt="open new java file in Netbeans" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_ide_filee.jpg" style="max-width:60%;height:auto;"/>
</p>

4.  Give the class name Hello.

<p>
<img alt="give class name to java file in Netbeans" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_ide_class.jpg" style="max-width:60%;height:auto;"/>
</p>

Then click on Finish.

5.  Type your Java code in the Source Editor window and save it (**ctrl+s**)

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

<p>
<img alt="writing codes in java file in Netbeans" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_code.jpg" style="max-width:60%;height:auto;"/>
</p>

6.  Now right click on the file and click **Run File**, the IDE automatically compiles it. You can see **Hello World** printed on the bottom of the screen.

<p>
<img alt="compling java file in Netbeans" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_ide_compile.jpg" style="max-width:60%;height:auto;"/>
</p>

<p>
<img alt="output of java file in Netbeans" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_ide_run.png" style="max-width:60%;height:auto;"/>
</p>

#### Command Prompt

1.  Write your Java program ( code given below ) in a text editor like Notepad and save it with a filename with **.java** extension. In our case, we named it as hello.java.

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

2.  Open the Command Prompt Window ( search for **cmd** ).

3.  To check if Java is installed, type **java -version** and press Enter. If Java is installed, you will see a message stating what version of Java is currently installed.

<p>
<img alt="checking java version in cmd" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/java_cmd_version.jpg" style="max-width:60%;height:auto;"/>
</p>

If not, you may need to install the Java Development Kit from their website. You can download it from [here](https://web.archive.org/web/20220603091236/http://www.oracle.com/technetwork/java/javase/downloads/index.html).

4.  Let's assume that you have installed Java in C:\Program files\Java directory.

Right click on My Computer and select properties.

5.  Go to the Advance System Settings tab.

<p>
<img alt="setting path variable in windows" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/path.jpg" style="max-width:60%;height:auto;"/>
</p>

6.  Click on the Environment Variables button.

Now alter the path variable so that it also contains the path to the JDK installed directory. Change the variable value to your folder containing Java (**C:\program files\Java\jdk1.8.0\_25\bin** in our case ).

<p>
<img alt="setting path variable in windows" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/path_var.jpg" style="max-width:60%;height:auto;"/>
</p>

7.  Use the command **cd** followed by the directory name to change your working directory. For example, if you are operating in C:\Users\John\Project and want to get to C:\Users\John\Project\prog ,then you need to type **cd prog** and press Enter. (**This directory should contain your previously created Java file ( hello.java in our case )**).

8.  Once you are in the correct directory in which you have your program, then you can compile and run your program.

To compile, type **javac filename.java** (**javac hello.java** in our case ) and press Enter. Here, our filename is hello.java, so we will write 'javac hello.java'. If it is showing any error, then try to remove that error from your program and then again save and compile your program.

<p>
<img alt="compiling java codes in cmd" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/compile_cmd.jpg" style="max-width:60%;height:auto;"/>
</p>

9.  Once the program is compiled, run the program by typing **java classname** (**java Hello** in our case ) and then pressing Enter. Name of the class is **Hello** written after **class** in java file.

<p>
<img alt="run java codes in cmd" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/run.jpg" style="max-width:60%;height:auto;"/>
</p>

We will get the output as follows. Now, you are ready to go for the next chapter.

### Linux

For Linux, you can write your Java program in various text editors like vim (or vi), gedit or Emacs. For running your Java program in Linux, follow the steps below.

1.  Open Terminal ( `ctrl+alt+T` ).

If you don't have Java installed in your computer, then first install it. [This](https://web.archive.org/web/20220603091236/https://www.digitalocean.com/community/tutorials/how-to-install-java-on-ubuntu-with-apt-get) is a nice tutorial to install java in Ubuntu.

2.  Open a new file with `.java` extension in your favourite text editor ( we are using `gedit` ). The command is :

`gedit hello.java`<br/>**hello.java** is the name of the file.

<p>
<img alt="steps to run Java in Ubuntu" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/inub2.png" style="max-width:100%;height:auto;"/>
</p>

Type the Java code given below and save it.

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

3.  Then to compile the program type `javac filename.java` and press Enter. We will be typing *javac hello.java*.

<p>
<img alt="steps to run Java in Ubuntu" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/inub4.png" style="max-width:100%;height:auto;"/>
</p>

4.  To run the program, type `java classname` ( name of the class is **Hello** which is written after **class** in the code ) in the terminal. It will type **Hello World** on the screen.

<p>
<img alt="steps to run Java in Ubuntu" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/inub6.png" style="max-width:100%;height:auto;"/>
</p>

Pressing Enter will display the output as follows.

### Mac

1.  Open Terminal.

<p>
<img alt="steps to run Java in Mac" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/in1.png" style="max-width:100%;height:auto;"/>
</p>

If you don't have Java installed in your computer, then first install it. You can follow [this](https://web.archive.org/web/20220603091236/https://www.java.com/en/download/help/mac_install.html) for tutorial on installing Java on Mac.

2.  Open a new file with **.java** extension in your favourite text editor ( we are using **VS Code** ). The command is :

`code hello.java`<br/>**hello.java** is the name of the file.

<p>
<img alt="steps to run Java in Mac" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/in2.png" style="max-width:100%;height:auto;"/>
</p>

You don't have to use command to open the file, you can simply open a file and name it with `.java` extension.

Type the Java code given below and save it.

```java
class Hello {

    public static void main(String[] args) {
        System.out.println("Hello World");
    }
}
```

3.  Then compile the program by typing `javac filename.java` in the terminal. We will be typing javac hello.java.

<p>
<img alt="steps to run Java in Mac" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/in3.png" style="max-width:100%;height:auto;"/>
</p>

4.  To run the program, type `java classname` ( name of the class is **Hello** which is written after **class** in the code ). It will type **Hello World** on the screen.

<p>
<img alt="steps to run Java in Mac" src="https://web.archive.org/web/20220603091236im_/https://www.codesdope.com/pa-images-bucket/courses/java/in4.png" style="max-width:100%;height:auto;"/>
</p>

Pressing Enter will display the output as follows.

So, now you can write and run Java codes. We will explain the code in the next chapter.
