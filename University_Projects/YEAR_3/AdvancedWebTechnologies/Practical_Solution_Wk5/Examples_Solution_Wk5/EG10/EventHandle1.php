<!DOCTYPE html>
<html lang="en">

<title>Extracting React Components</title>
<script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src= "https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
<body>

<div id="root1"></div>

<script type="text/babel">
//Creates a toggle button that lets the user toggle between "Enter" and "Exit" states.
class Toggle extends React.Component {
  constructor(props) {
    super(props);
    this.state = {isToggleOn: true};

    // Notice the meaning of 'this' in JSX callbacks. This binding is necessary to make 'this' work in the callback.
	//It is a part of how functions work in JavaScript and not React specific syntax
    this.handleClick = this.handleClick.bind(this);
  }

  /**
   *  The below won't work
   *   handleClick() {
    //  Consider this parameter `prevState`, that it's built-in
    this.setState(prevState => (
      if (prevState.isToggleOn == this.state.isToggleOn){
        {isToggleOn: false}
      }else{
        {isToggleOn: true}
      }
    ));
   * 
   */
  handleClick() {
    //  Consider this parameter `prevState`, that it's built-in
    this.setState(prevState => ({
      isToggleOn: !prevState.isToggleOn
    }));
  }

  render() {
    return (
      <button onClick={this.handleClick}>
        {this.state.isToggleOn ? 'Enter' : 'Exit'}
      </button>
    );
  }
}

ReactDOM.render(
  <Toggle />,
  document.getElementById('root1')
);

</script>

</body>
</html>