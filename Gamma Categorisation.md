# Gamma Categorisation
`Design patterns are typically split into three categories`

## Creational Patterns
`Deal with the creation (construction) of objects`
`Explicit (constructor) vs. implicit (DI, reflection, etc.)`
`Wholesale (single statement) vs. piecewise (step-by-step)`

### Builder Pattern
`Let's imagine we need to build a house. There are various types of houses, such as those with a swimming pool, a garage, a garden, or a fancy design. There are two approaches to constructing the house: one is to define a constructor with all the parameters, and the other is to use multiple constructors for different features. If we use the single constructor method, many parameters will often remain empty. On the other hand, if we use multiple constructors, we'll end up with too many of them, and adding new features means adding a lot of new constructors.`
`To address this issue, we can create a House builder with several methods like buildWalls(), buildDoors(), buildWindows(), buildRoof(), buildGarage(), and getResult(). By using only the required methods, we can efficiently build the house.`
`Builder Facets vs Builder Inheritance`

### Factories Pattern
`In the factory pattern the whole object created at a time it is not create piecewise.`
`In this pattern at run it is decided which class instance is actually is required.`
`For example if there multiple method of transportation like: Roadways, Railways and Waterways (i.e. Truck, Train and Ship)`
`At the run time it is decided which instance is to be create and the factory method create the object and return it.`
`There are two type of factory design pattern, 1. Factory design pattern and abstract factory design pattern.`
`In the abstract design pattern we extend the base abstract class (ex: Transport) via the concrete implementation (ex: Truck, Ship, Train)`
`Abstract factory design pattern doesnot makes much sense in python as python is duck typed language`


### Prototype Pattern
`In this design pattern whenever we need to create similar object we use a object as reference, deep copy it and then make changes in the new one.`


### Singleton Pattern
`This is use when we need only one instance of a class. Like database connector. Service methods.`
`It helps to save resources.`
`Look for its implementation method`

## Structural Patterns
`Concerned with the structure (e.g. class members)`
`Many patterns are wrappers that mimic the underlying class' interface`
`Stress the importance of good API design`
### Adaptor
`In this design pattern we build a transformer to transform the data or the class to a different usable form.`
`Like I have US style plug but I have Europe style socket, what shall I do? I will build a converter to make them compatible.`
`That converter is Adapter.`
### Bridge
`Study more not clear`
### Composite
`Study more not clear`
### Decorator
### Facade
### Flyweight
### Proxy

## Behavioral Patterns
`They are all different; no central theme`
### Chain of Responsibility
### Command
### Iterator
### Mediator
### Memento
### Observer
### State
### Strategy
### Template Method
### Visitor

## Summary
`Here is the summary`


