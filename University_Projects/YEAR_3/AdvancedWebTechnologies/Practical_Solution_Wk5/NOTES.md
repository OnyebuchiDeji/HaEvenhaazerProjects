#   Date Started: Sun-16-March-2025


#   Practical 5: React Framework and Its Application

#   Lecture 9

React is generally a JavaScript library used for building UI components because it makes it easier.
It's developed by Facebook released in 2013.

It's resolves the a UI component's state at any point in time by dividing the UI into a collection of components.

To use the React library, three different parts need to be loadsed into the source:
1.  The React API
2.  The React DOM (Document Object MOdel)
3.  The Babel Compiler -- able to translate markup and different programming languages into JS. In this case, Babel converts JSX (JavaScript XML) into JavaScript.
    JSX is an XML/HTML like extension to JavaScript.
    JSX brings full features of ECMAScript6.

```
    <!– Loading the React API-->
    <script src= 
    "https://unpkg.com/react@16/umd/react.production.min.js">
    </script>

    <!– Loading the React Document Object Model (DOM)-->
    <script src= "https://unpkg.com/react-dom@16/umd/reactdom.production.min.js">
    </script>

    <!– Loading the Babel Compiler -->
    <script src="https://unpkg.com/babelstandalone@6.15.0/babel.min.js">
    </script>
```

To use Babel code:
```
    <script type="text/babel">
        // JSX Babel code goes here…
    </script>
```

##  React DOM Render
-   React Dom Renderer extracts and displays HTML
```
    ReactDOM.render(element, container [, callback])
```
EG:
    ```
        <script type="text/babel">
            ReactDOM.render(document.getElementById('tag01'));
        </script>
    ```

There are many intuitive and familiar methods that this library comes with.
1.  The elements to be displayed are defined in the `ReactDOM.render()` function.
2.  Changes of an element are captured using the `onChange()` function
3.  The event handler updatets some internal state
4.  The new values that are saved in state are used to update the view displayed by the renderer.

##  Things to Know
1.  Elements themselves that are created using React are immutable (they cannot be changed during runtime). Only their data or values can.
    This means any changes to the data can only be seen on that element after rendering that element anew.

2.  React Components can be given properties. Components in this case refer to 'Objects' that can be written as functions or Classes.
    Each Component has its template definition, which is like that of every other programming language. Like howone defines a function or a class.
        In the case of a function, a single `properties` parameter is given it. 
    Then there is the instantiation, which is like writing an HTML tag. In this instantiation, the properties arguments are written like how an HTML element's properties like its type, class, etc. would be written.

3.  The Components defined as functions are written as pure functions. This means the properties parameter is not changed within the function nor does it store a state. So it always returns the same results for the same input.

##  React State and Lifecycle Methods
-   `render`: A function that every Component ought to have.
-   State stores info about a component's behaviour (how and what it renders).
    `setState` is a built-in function that allows one to modify a Cmponent's state. But htis is for Components defined as classes.
    *   I'll test if it also works on Closures.
-   `componentDidMount()`: Mounting is the time when the Component gets rendered for the first time in the browser.
    `componentDidMount()` runs after the component gets Mounted.
-   `componentWillUnmount()` - runs once the DOM produced by the Component is removed.
    Any functions attached to this is ran once this runs.

*   All the above functions are called 'Life Cycle Functions'
##  Advantages of React
-   It allows one to declare user interfaces in self-contained independent Components.
-   Since every UI is composed of components, there is no multiple-type mismatch. This is demonstrated in`TimeEg5` where the Clock Component is instantiated many times with the same identifier.
-   It allows OOP design patterns which is neat and cool. ;p
    

#   Lecture 10

##  Events Handling in React

```
In HTML:
    <button onclick="activateRainfall()">
        Activate Rainfall 
    </button>
```

```
In React:
    <button onClick={activateRainfall}>
    Activate Rainfall 
    </button>
```

```
In HTML:
    <a href="#" onclick="console.log('The link was clicked.'); 
    return false">
        Click here 
    </a>
```

```
In React:
    function ActionLink() { 
        function handleClick(e) { //e is a synthetic event
            e.preventDefault(); //helps not to refresh the page
            console.log('The link was clicked.');
        } 
            
        return ( 
            <a href="#" onClick={handleClick}>
                Click here 
            </a>
        ); 
    }
```

In JS:
```
    const numbers = [1, 2, 3, 4, 5]; 
    const doubled = numbers.map((number) => number * 2); 
    console.log(doubled);
```

In React:
```
    const numbers = [1, 2, 3, 4, 5]; 
    const listItems = numbers.map((number) => 
    <li>{number}</li>
);
```
#   Finished: Sun-16-March-2025