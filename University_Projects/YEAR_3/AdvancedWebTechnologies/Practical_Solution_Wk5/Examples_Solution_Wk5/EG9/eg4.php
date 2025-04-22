<!DOCTYPE html>
<html lang="en">

<title>Composing React Components</title>
<script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src= "https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
<body>

<div id="root"></div>

<script type="text/babel">
function Intro(properties) {
  return <h1>Learn Module: {properties.learn}</h1>;
}
//  XNT1_D: Properties can be validated
function Greet(properties){
    if (properties.msg){
        return <h3>Deji Says: {properties.msg}</h3>;
    }
    else if (properties.ques){
        return <h3>Deji Asks: {properties.ques}</h3>;
    }
}

function AppFirst() {
  return (
    <div>
      <Intro learn="Web Technologies" />
      <Intro learn="Computational Intelligence I" />
      <Intro learn="Computational Intelligence II" />
	  <Intro learn="Advance Web Technologies" />
      <Greet msg="Yo!"/>
      <Greet ques="Where do yau say ye fram?"/>
      <Greet ques="From whence didst thou cometh from?"/>
      <Greet msg="From home."/>
      <Greet ques="What is your name?"/>
      <Greet msg="Deji"/>
      <Greet ques="How're you?"/>
      <Greet msg="Okay"/>
      <Greet ques="What you doing?"/>
      <Greet msg="Coding"/>
      <Greet ques="What's up?"/>
      <Greet msg="The clouds"/>
    </div>
  );
}

ReactDOM.render(<AppFirst />, document.getElementById('root'));
</script>

</body>
</html>