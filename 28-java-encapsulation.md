# Java Encapsulation
***
**Encapsulation** is nothing new to what we have read. It is the way of combining the data (variables) and methods inside a class. In encapsulation, the data (variables) gets hidden from being accessed directly from outside the class. This is similar to a capsule where several medicines are kept inside the capsule thus hiding them from being directly consumed from outside.

![encapsulation in Java](https://web.archive.org/web/20240422034337im_/https://www.codesdope.com/pa-images-bucket/courses/java/e1.png)

Encapsulation can be achieved by using [access modifiers](https://web.archive.org/web/20240422034337/https://www.codesdope.com/course/java-access-modifiers/). When a member (variable or method) in a class is declared as **private**, it can’t be accessed from outside the class.

Let's see an example of Encapsulation.

```java
class Student {

    // private variable
    private String name;

    // public method
    public void setName(String n) {
        name = n;
    }

    // public method
    public String getName() {
        return name;
    }
}

class Test {

    public static void main(String[] args) {
        Student st = new Student();

        // accessing public method
        st.setName("John");

        // accessing public method
        System.out.println(st.getName());
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

In the class `Student`, we declared the variable `name` as `private` so that it can’t be accessed outside the class. Due to this, we declared the methods `setName()` and `getName()` as public so that these can be accessed outside the class to modify and print the value of the private class variable `name` respectively.

Here we are preventing anyone from directly accessing the variable `name` outside the class `Student`. If someone wants to modify or get the value of `name`, then he can do that by calling the methods `setName()` or `getName()`. This is **encapsulation**.

Okay, so this is a simple concept; but why should encapsulation be used in our code?
***
## Why Encapsulation
Encapsulation is necessary to keep the details of an object hidden from the users of that object. Details of an object are stored in its variables defined in a class. This is the reason we normally make all the variables in a class **private** and most of the methods in a class **public**. Variables in a class are made private so that these cannot be directly accessed from outside the class (to hide the details of any object of that class) and therefore most methods in a class are made public to allow the users to access the class variables through these methods.

Take an example of a mobile. We have a main camera app. Now let’s suppose we have installed a 3<sup>rd</sup> party camera app. This camera app will need access to the camera to work but would you expose all of the camera variables like megapixel, light sensitivity to the 3rd party camera app? No.

A good way would be to make all these variables private and just expose a method which can use these variables according to itself to the 3<sup>rd</sup> party camera app.

Some of you might also wonder - **When both abstraction and encapsulation are used for hiding information, then how are they different?**

**<br/>**A very good question though. This is explained in the next section.
***
## How Encapsulation is Different from Abstraction
In the last three chapters, we read about abstraction and ways to achieve it. Let’s have a quick recap.

Abstraction is mainly used to hide unnecessary details of an application or program by making changes at the design level i.e. by structuring the code using abstract classes or interfaces.

Let’s again take an example of a mobile. Whenever we buy a mobile, we don’t actually buy a mobile. We buy either an iPhone, a Samsung mobile or some other company mobile. All these mobile companies provide the same functionalities but in different ways (i.e. with different implementations). For example, a Samsung mobile and an iPhone both provide the video recording functionality, but the quality and features in video recording differs for both the mobile types.

So, here mobile is an abstract concept but Samsung and iPhone are concrete entities.

Look at the following program.

```java
// abstract class
abstract class Mobile {

    abstract void recordVideo();
}

// class Samsung extends Mobile
class Samsung extends Mobile {

    void recordVideo() {
        // implementation code of video recording of Samsung
    }
}

// class iPhone extends Mobile
class iPhone extends Mobile {

    void recordVideo() {
        // implementation code of video recording of iPhone
    }
}
```

Here we created an abstract class named Mobile (because mobile is an abstract concept) with the method recordVideo() defined in it. This tells us that a mobile has a video recorder functionality. This video recording functionality is implemented by different subclasses of Mobile differently.

Hence, the abstract class acts like a base that defines all the functionalities (in the form of methods) of a mobile without defining the internal working of these methods (because no definition is provided to the methods in the abstract class).

In this way, we are able to hide irrelevant implementation details using abstraction.

Coming to the main point, we already discussed what encapsulation is. Now let’s see how it is different from abstraction.

Abstraction tells us what all functionalities (like video recording functionality) an object offers. It focuses on what an object does (on design level), not on how it does it (on implementation level).

On the other hand, encapsulation is used to hide the important information of an object using access modifiers. It is completely unrelated to abstraction. In the above example, when the Samsung and iPhone classes will be implementing the recordVideo() method, we can hide the circuits and other entities used in the respective mobiles by making them private using the private access modifier. This will prevent users, other programmers or anyone else from accessing these internal circuits outside of their class.

Summing up, abstraction is used to provide an interface that tells us about the different types of functionalities of an object. Whereas, encapsulation is used to hide unnecessary and confidential details of an object from being accessed.

Hope the difference is clear to you.
***
## Benefits of Encapsulation
There are various benefits of **encapsulated classes**.

*   **Encapsulated classes reduce complexity**.
*   **Help protect our data**. A client cannot change an Account's balance if we encapsulate it.
*   **Encapsulated classes are easier to change**. We can change the privacy of the data according to the requirement without changing the whole program by using access modifiers (public, private, protected). For example, if a data member is declared private and we wish to make it directly accessible from anywhere outside the class, we just need to replace the specifier `private` by `public`.

Enough reasons to use encapsulation!

Security Is Mostly A Superstition. Life Is Either A Daring Adventure Or Nothing.

\- Helen Keller
***