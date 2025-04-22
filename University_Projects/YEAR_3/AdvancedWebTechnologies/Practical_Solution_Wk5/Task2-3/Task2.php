

<!DOCTYPE html>
<html lang="en">

<title>Task2: Reactive Forms</title>
<script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src= "https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
<body>

<h1>Task2: Reactive Forms</h1>
<div id="root"></div>

<script type="text/babel">

function Info(prop)
{
    if (prop.type=='Comment'){
        return <div><h3>{prop.type}:</h3> <p>{prop.value}</p></div>;
    }
   return  <h3>{prop.type}: {prop.value}</h3>;
}
class NameForm extends React.Component {
  constructor(props) {
    super(props);
	this.state = {value1: '', value2:'', value3:'', value4:'', v1Msg:'', v2Msg:'', v3Msg:''};

    this.handleChangeName = this.handleChangeName.bind(this);
	this.handleChangePhone = this.handleChangePhone.bind(this);
	this.handleChangeEmail = this.handleChangeEmail.bind(this);
	this.handleChangeComment = this.handleChangeComment.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChangeName(event) {
	  this.setState({value1: event.target.value});
	  //this.setState({value: event.target.value.toLowerCase()});
		var textval = this.state.value1;
		//user validation of the special characters
		var iChars = "!@#$%^&*()+=-[]\\\';,./{}|\":<>?";		
		for (var i = 0; i < textval.length; i++) {
			if (iChars.indexOf(textval.charAt(i)) != -1) {
				// alert ("Your username should not have !@#$%^&*()+=-[]\\\';,./{}|\":<>? \nThese are not allowed.\n Please remove them and try again.");
                this.setState({v1Msg: "Your username should not have !@#$%^&*()+=-[]\\\';,./{}|\":<>? \nThese are not allowed.\n Please remove them and try again."});
				//return false;
			}else{
                this.setState({v1Msg: ""});
            }
		}
  }
  
  handleChangePhone(event) {
	  this.setState({value2: event.target.value});
		var textval = this.state.value2;
		//user validation of the special characters
		if(isNaN(textval)){
			// alert("Please! Numbers should only have numbers.");
            this.setState({v2Msg: "Please! Numbers should only have numbers."});
        }else{this.setState({v2Msg: ""});}
  }

  handleChangeEmail(event) {
    this.setState({value3: event.target.value});

    var textval = this.state.value3;
    //user validation of the special characters
    if(textval.length >= 15 && (textval.indexOf('@')==-1 || textval.indexOf('.')==-1)){
        // alert("Please, write an actual email! Please!");
        this.setState({v3Msg: "Please, write an actual email! Please!"});
    }else{
        this.setState({v3Msg: ""});
    }
  }

  handleChangeComment(event) {
    this.setState({value4: event.target.value});
    var textval = this.state.value4;

  }

//without .preventDefault() the submitted form would be refreshed
  handleSubmit(event) {
    alert('The submitted information:\n' + 
        "User Name: " + this.state.value1 + 
        "\nPhone Number: " + this.state.value2 +
        "\nEmail Address: " + this.state.value3 +
        "\nComment: " + this.state.value4);

    event.preventDefault();
    var url = "./SaveRecord.php?";
    url += "username=" + this.state.value1;
    url += "&phone=" + this.state.value2;
    url += "&email=" + this.state.value3;
    url += "&comment=" + this.state.value4;
    console.log("The URL: ", url);
    fetch(url)
      .then(response => response.json())
      .then(data=>{
        console.log("Response: ", data.MSG);
        alert("Success!");
      })
      .catch(error=>{
        console.log("Error: ", error);
      });
    
    var newUrl = "View.php?uname="+this.state.value1+ "&post="+this.state.value4;
    window.location.href = newUrl;
  }

  render() {
    return (
        <div>
            <form onSubmit={this.handleSubmit}>
            <label>User Name:</label>
            <input type="text" value={this.state.value1} onChange={this.handleChangeName} /><br></br>
            <blockquote>{this.state.v1Msg}</blockquote>
            <label>Phone Number:</label>
            <input type="text" value={this.state.value2} onChange={this.handleChangePhone} /><br></br>
            <blockquote>{this.state.v2Msg}</blockquote>
            <label>Email Address:</label>
            <input type="text" value={this.state.value3} onChange={this.handleChangeEmail} /><br></br><br></br>
            <blockquote>{this.state.v3Msg}</blockquote>
            <label>Comment:</label>
            <textarea type="text" value={this.state.value4} onChange={this.handleChangeComment} /><br></br><br></br>
            <input type="submit" value="Submit" />
            </form>  
            <Info type="Name" value={this.state.value1}/>
            <Info type="Phone" value={this.state.value2}/>
            <Info type="Email" value={this.state.value3}/>
            <Info type="Comment" value={this.state.value4}/>

        </div>
    );
  }
}

ReactDOM.render(
  <NameForm />,
  document.getElementById('root')
);


</script>

</body>
</html>