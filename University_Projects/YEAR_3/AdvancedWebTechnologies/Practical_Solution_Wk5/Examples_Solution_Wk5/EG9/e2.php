<!DOCTYPE html>
<html lang="en">
<title>JSX Expressions</title>
<script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>

<body>
<div id="tag001"></div>

<script type="text/babel">
const NickName = 'Eben';
const FirstName = 'Ebenezer';

ReactDOM.render(
    <div>
    <h3>
        Consider that variables can also be added. Also, pree how the HTML
        is directly tyyped into the `ReactDOM.render()` function. This is probably where
        Babel's ability to convert markup to JS is needed. <b>:></b> 
    </h3>
    <h3>
        Also, you can only pass one HTMl element to render through this function.
        So if you want to put multiple elements, they have to be inside a single element
        like a div, as in this case.
        O, yes, last thing: using `br` break line tag stops the whole thing from working. <b>:p</b>
        But you can do: '<br></br>'
    </h3>
    <blockquote>
        <b>
            Ah, one more: you can't add inline styling and likewise probably inline javascript.
        </b>
    </blockquote>
    <h1>Yo Yo! My name is {NickName}! Short for {FirstName}!</h1></div>, document.getElementById('tag001'));
</script>

</body>
</html>