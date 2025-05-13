# Java Abstraction

In this chapter, we will learn about another important concept of Object Oriented Programming - Abstraction. We will only learn about the conceptual part of the abstraction in this chapter and in the next two chapters, we will implement it. So, let’s get started.

## Abstraction in general

The word “**abstraction**” means something which is theoretical without a concrete existence. For a real life example, even a car is an abstraction. If you want to apply the brake you press the brake pedal and if you want to accelerate you press the accelerator pedal. But do you know how the car speed decreases on pressing the brake pedal or increases on pressing the accelerator pedal? No, right? So, the process of how the pedals work has no concrete existence as per our knowledge but we have a theoretical idea that somehow using this pedal increases or decreases the speed of the car.

Cutting down, abstraction is making things simpler for us. Just a functionality (brake and accelerator functionalities in the above example) is exposed to us  and all the complex process of that functionality is occurring under the hood. And this is where we programmers also use the word abstraction and it is even a core part of object oriented programming.

Let’s understand the word **abstract** with respect to programming.

## Abstraction in Programming

Thinking about something regarding programming where we just have to use a way exposed to us to perform some action, the first thing that comes in our mind is a method. We just call a method and it performs its action. In case of methods written by other programmers or let’s take in-built methods like println, we don’t know how it works. We just know what this method will do and we use the method to perform that action. This is an abstraction in programming.

Till this point, it seems like methods are the only way for abstraction but there are more examples like we use few commands which are exposed to us to interact with a database and all the process occur under the hood.

Let’s look at some of the conceptual examples of the term abstraction.

*   Suppose a programmer wants to use the value of pi in a program. So he can assign the value 3.14 to a variable named Pi and can use that variable throughout the program. In this way, he hid the actual numerical value of pi and used only the variable Pi because the actual numerical value is not required to be remembered. Here, he achieved abstraction by hiding the value of Pi.
*   Suppose a programmer wrote a method named `drawRectangle` to draw a rectangle. Now, whenever he or any other programmer needs to draw a rectangle, he can simply call the method `drawRectangle()` without knowing the implementation code inside the method. Here also, he achieved abstraction by hiding the implementation of the method.
*   When we use any built-in method like `System.out.println()`, we know that this method takes some argument and prints something on the screen. But we don’t know its implementation i.e. how it does that. All that implementation is hidden and Java just provides us the method and tells us how to use it. Same like Java just provides us the built-in methods and tells us only about their use without telling about its implementation details, as a programmer we should also provide the user with only the required functionality by hiding all the unnecessary implementation details.

In all the above examples, we were able to achieve abstraction and reduce the complexity of the code. So, we can achieve abstraction in many ways in programming.

However, when we talk about abstraction, we generally refer to abstraction in design level in programming. Design level abstraction means using abstraction to improve the structure of our code by making it less complex and more scalable. Let’s learn about design level abstraction and what is special about structuring our code.

## Design level abstraction

Till now, the conceptual meaning of abstraction must be clear. In object oriented programming, the concept of abstraction is particularly used to improve the design of classes and subclasses. According to it, we define a superclass or an abstract superclass with the aim that it should serve as a definition and the subclasses inheriting it will implement this definition to make something significant. For example, a vehicle is a theoretical definition that something which is mobile and humans can use to travel. But this definition comes to life only after something like a car or a bike, etc. use it to make something significant.

Let’s think in an object oriented way. An abstract superclass Vehicle is only a definition, so there is no need to make objects of it, we will make objects it its subclasses - Car, Bike, etc. And it has some methods like `moveForward`, `moveBackward`, `turnLeft` and `turnRight` to provide the required mobility. But the way of implementation of these method i.e., the way a bike moves forward and the way a car moves forward will be different. So, these methods will be defined differently for different subclasses. It means an abstract superclass will only specify that these methods must be present in all of its subclasses but they will be defined individually by subclasses themselves.

<img alt="abstraction in Java" src="https://web.archive.org/web/20240416071054im_/https://www.codesdope.com/pa-images-bucket/courses/java/p28.png" style="max-width:55%;height:auto;"/>

It means that abstraction is like a simple inheritance but with more restrictions, so that the definition of the superclass is followed strictly among the subclasses.

With the above example, it is clear that the superclass will only serve as definition and we won’t be creating objects of the superclass itself. The second thing is that the superclass will only contain the method declarations and their definitions will be present in the subclasses itself.

This also fulfills the concept of abstraction in one more way i.e., we are sure that these methods will be present in all the subclasses of a particular abstract superclass and we can directly use them without worrying about their implementation in different subclasses.

Let’s take one more example of a Shape class. An abstract class has to define structure for its subclasses. So, an abstract class has method declarations without their bodies and all its subclasses must have those methods with their definitions according to the subclasses itself.

<img alt="abstract method in Java" src="https://web.archive.org/web/20240416071054im_/https://www.codesdope.com/pa-images-bucket/courses/java/p29.png" style="max-width:60%;height:auto;"/>

The superclass Shape will specify that all of its subclasses will have methods `getPerimeter` and `getArea` but as far as the Shape class is considered itself, we don’t have a definition for area and perimeter.

<img alt="abstract class in Java" src="https://web.archive.org/web/20240416071054im_/https://www.codesdope.com/pa-images-bucket/courses/java/p30.png" style="max-width:30%;height:auto;"/>

Now, suppose classes Circle and Rectangle are inheriting the Shape class. These classes will have their own definitions for `getArea` and `getPerimeter`.

<img alt="abstract method implementation in Java" src="https://web.archive.org/web/20240416071054im_/https://www.codesdope.com/pa-images-bucket/courses/java/p31.png" style="max-width:50%;height:auto;"/>

With this, we have a restricted structure in our superclass and all of the methods must be defined in the subclasses to classify as the subclass of the abstract superclass. So, the superclass itself is acting like a theoretical definition and subclasses are implementing that definition to make that definition available for users.

Let’s sum up the design level abstraction. A superclass should only contain definition. So, there is no need to create objects of the superclass itself. Instead we will have subclasses and create their objects. Now to make a superclass fully abstract, all of its methods should not have body definitions. This way, we will be sure that all the required methods are defined according to the need of individual subclasses.

In Java, abstraction in design level can be achieved by two ways:

1.  Abstract Class
2.  Interface

We will discuss these in next chapters.

Use of Abstraction
At this level it is not possible to explain the use and why do we need abstraction because it is a design level concept. After learning programming, when writing codes in real projects, the way we write our code or the way we structure our code becomes very important and there we need abstraction.

For now, you can understand it by taking the vehicle example we have already discussed. There can be many ways to implement the same thing we did before. But make an abstract Vehicle class guarantee that all of its subclasses either made by us or other programmers will have 4 methods - `moveForward`, `moveBackward`, `turnLeft` and `turnRight`. It means we can use these methods on objects of any of the subclasses. This is a cleaner way to write code and also brings simplicity to our code.

Let’s understand abstract classes, one of the ways to achieve abstraction in Java.        

> You only live once, but if you do it right, once is enough.
>
> - Mae West


<a href="26-java-abstract-class.md" class="next">Next</a>
