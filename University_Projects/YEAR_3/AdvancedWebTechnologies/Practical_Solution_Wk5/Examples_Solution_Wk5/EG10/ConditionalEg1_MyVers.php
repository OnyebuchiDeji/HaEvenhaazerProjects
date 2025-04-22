<!DOCTYPE html>
<html lang="en">
<!-- 
  This wasn't an alterative solution.
  This demonstrates what they mean by ensuring that the functions be pure.
  Also, keep it simple. Just make each function do its own thing.
  Only add conditional logic where its very clear, like in the `render` method.

-->
<title>Conditional Rendering in React</title>
<script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src= "https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
<body>

<div id="root"></div>

<script type="text/babel">
//Creates a toggle button that lets the user toggle between "Enter" and "Exit" states.
class LoginControl extends React.Component {
  constructor(props) {
    super(props);
    this.handleLoginClick = this.handleLoginClick.bind(this);
    this.handleLogoutClick = this.handleLogoutClick.bind(this);
    // this.handleLoginOrLogoutClick = this.handleLoginOrLogoutClick.bind(this);
    this.state = {isLoggedIn: false};
  }
  // Won't Work
  //  Probably because the isLoggedIn won't be known in the condition variable
  //  when registered with the Event Manager
  handleLoginOrLogoutClick() {
    const isLoggedIn = this.state.isLoggedIn;
    if (isLoggedIn){
      this.setState({isLoggedIn: true});
    }
    else{
      this.setState({isLoggedIn: false});
    }
  }

  handleLoginClick() {
    this.setState({isLoggedIn: true});
  }
  handleLogoutClick(){
    this.setState({isLoggedIn: false});
  }

  render() {
    const isLoggedIn = this.state.isLoggedIn;
    let button;

    // button = <AccountButton onClick={this.handleLoginOrLogoutClick} isLogin={isLoggedIn} />;
    button = <AccountButton onClick={isLoggedIn?this.handleLoginClick:this.handleLogoutClick} isLogin={isLoggedIn} />;

    return (
      <div>
        <Greeting isLoggedIn={isLoggedIn} />
        {button}
      </div>
    );
  }
}

function UserGreeting(props) {
  return <h1>Welcome back!</h1>;
}

function GuestGreeting(props) {
  return <h1>Please sign up.</h1>;
}

function Greeting(props) {
  const isLoggedIn = props.isLoggedIn;
  if (isLoggedIn) {
    return <UserGreeting />;
  }
  return <GuestGreeting />;
}

function AccountButton(props) {
  if (props.isLogin)
  {
    return (
      <button onClick={props.onClick}>
        Login
      </button>
    )
  }
  else
  {  
      return (
        <button onClick={props.onClick}>
          Logout
        </button>
      );
  }
}

ReactDOM.render(
  <LoginControl />,
  document.getElementById('root')
);
</script>

</body>
</html>