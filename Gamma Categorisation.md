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


### Prototype Pattern


### Singleton Pattern


## Structural Patterns
`Concerned with the structure (e.g. class members)`
`Many patterns are wrappers that mimic the underlying class' interface`
`Stress the importance of good API design`

## Behavioral Patterns
`They are all different; no central theme`



