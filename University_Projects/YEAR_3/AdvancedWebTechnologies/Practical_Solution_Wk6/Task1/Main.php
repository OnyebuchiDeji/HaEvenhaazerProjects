

<!DOCTYPE html>
<html lang="en">

<head>
  <title>Task: Search Engine Optimizations</title>
  <script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
  <script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
  <script src= "https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>
  <style>
    #banner{
      height: 300px;
      width: 650px;
      margin: 5%;
    }

    #banner img{
      height: 100%;
      width: 100%;
      opacity: 80%;
    }

    #root{
      /* margin: 5% 15% 0% 15%; */
      /* margin: 20%; */
      color: whitesmoke;
      background-color: rgb(21, 30, 12);
      padding: 5%;
      width: 100%;
    }
    #content{
      display: grid;
      grid-template-columns: 1fr 1fr;
      width: 100%;
    }
    #collabs{
      width: 100%;
      margin: 20%;
      padding: 5%;
      color:antiquewhite;
      background-color: rgb(21, 21, 21);
      /* gap: 5%; */
    }

    #collabs a{
      color: grey;
      text-decoration: none;
    }
    #collabs a:hover{
      color: white;
      text-decoration: overline;
    }
  </style>
</head>
<body>

<h1 style="margin: 0% 0% 0% 15%">Task: Search Engine Optimizations</h1>
<div id="banner">
  <img src="../res/Keele_Hall_Aerial_2.jpg" alt="Keele Hall">
</div>
<div id="content">

  <div id="root"></div>

  <div id="collabs">
    <h3>Keele's Collaborators</h3>
    <ul>
      <li>
        <a href="https://www.bing.com/ck/a?!&&p=7d6072b59db9dac01b1ab0801eb725be84c4974d7af9331598fdfd2e4bb8491eJmltdHM9MTc0MjA4MzIwMA&ptn=3&ver=2&hsh=4&fclid=2aa5f6f7-d37a-627f-2e29-e346d2ed63a6&psq=nhs&u=a1aHR0cHM6Ly93d3cubmhzLnVrLw&ntb=1">
          NHS: Health Impact</a>
      </li>
      <li>
        <a href="https://www.advance-he.ac.uk/equality-charters/athena-swan-charter">
          Athena Swan Charter</a>
      </li>
      <li>
        <a href="https://www.officeforstudents.org.uk/">
          Office for Students</a>
      </li>
      <li>
        <a href="https://www.bing.com/ck/a?!&&p=8274003f58fb9c94edf187f6e5ba83016239370a4f78d35a3699bcbf2ca231fdJmltdHM9MTc0MjA4MzIwMA&ptn=3&ver=2&hsh=4&fclid=2aa5f6f7-d37a-627f-2e29-e346d2ed63a6&psq=bcs+chartered+institute+for+it&u=a1aHR0cHM6Ly93d3cuYmNzLm9yZy8&ntb=1">
          BCS, The Chartered Institute for IT</a>
      </li>
    </ul>
  </div>
</div>

<script type="text/babel">

function Info(prop)
{
    if (prop.type=='message'){
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
	this.handleChangeMessage = this.handleChangeMessage.bind(this);
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

  handleChangeMessage(event) {
    this.setState({value4: event.target.value});
    var textval = this.state.value4;

  }

//without .preventDefault() the submitted form would be refreshed
  handleSubmit(event) {
    alert('The submitted information:\n' + 
        "User Name: " + this.state.value1 + 
        "\nPhone Number: " + this.state.value2 +
        "\nEmail Address: " + this.state.value3 +
        "\nMessage: " + this.state.value4);

    event.preventDefault();
    var url = "./SaveRecord.php?";
    url += "username=" + this.state.value1;
    url += "&phone=" + this.state.value2;
    url += "&email=" + this.state.value3;
    url += "&message=" + this.state.value4;
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
            <label>User Name: </label>
            <input type="text" value={this.state.value1} onChange={this.handleChangeName} /><br></br>
            <blockquote>{this.state.v1Msg}</blockquote>
            <label>Phone Number: </label>
            <input type="text" value={this.state.value2} onChange={this.handleChangePhone} /><br></br>
            <blockquote>{this.state.v2Msg}</blockquote>
            <label>Email Address: </label>
            <input type="text" value={this.state.value3} onChange={this.handleChangeEmail} /><br></br><br></br>
            <blockquote>{this.state.v3Msg}</blockquote>
            <label>Message: </label>
            <textarea type="text" value={this.state.value4} onChange={this.handleChangeMessage} /><br></br><br></br>
            <input type="submit" value="Submit" />
            </form>  
            <Info type="Name" value={this.state.value1}/>
            <Info type="Phone" value={this.state.value2}/>
            <Info type="Email" value={this.state.value3}/>
            <Info type="Message" value={this.state.value4}/>

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