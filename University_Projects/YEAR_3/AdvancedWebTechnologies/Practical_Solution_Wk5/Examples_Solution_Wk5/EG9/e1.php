<!-- 
	This is me going through the code and experimenting.

	Experiments are marked by XNT.
	Consecutive experiments are suffixed with their number.
		E.g XNT19
	Experiments that yield a discovery are marked as XNT_D
 -->

<!DOCTYPE html>
<html lang="en">
<title>Introduction of React Framework</title>
<script src= "https://unpkg.com/react@16/umd/react.production.min.js"></script>
<script src= "https://unpkg.com/react-dom@16/umd/react-dom.production.min.js"></script>
<script src="https://unpkg.com/babel-standalone@6.15.0/babel.min.js"></script>

<body>
<div id="tag01"><h1>Welcome to CSC - 30025: Advance Web Technologies!</h1></div> <!-- Note that the texts are not in quotations  -->
<br><br>
<div id="tag02"><h3>Consider how this `ReactDOM.render()` function works</h3></div> <!-- Note that the texts are not in quotations  -->
<div id="tag04"><h3>The last two tags were in the html body.</h3></div>
<div id="tag05"></div>

<script type="text/babel">
	// XNT2 Changing the rendering order did not change the order in the DOM
	// ReactDOM.render(document.getElementById('tag01'));
	// ReactDOM.render(document.getElementById('tag04'));
	// ReactDOM.render(document.getElementById('tag02'));
	// ReactDOM.render(document.getElementById('tag03'));
	ReactDOM.render(
		<h3><b>
			This is it. So it only works by replacing the contents inside the element being modified,
			and, since there is only one DOM, this `ReactDOM.render()` function is
			rightly to be only called once.
		</b></h3>,
		document.getElementById('tag05'));

	//	XNT3_D
</script>

</body>

<!-- XNT1: This did not work with the following associated render call -->
<!-- <template>
	<div id="tag03"><h3>The last two tags were in the html body. This one was in a template</h3></div>

</template> -->
</html>