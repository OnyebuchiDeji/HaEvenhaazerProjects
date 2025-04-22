
/*
    NOTE
    When using innerHTML, it cannot concactenate newline character "\n", so you cannot make its text got to...
    the newline
    SOL:
    use innerText rather than innerHTML.

    comment: Thurs-15-Feb-2024
    EGTest, EG1, EG2 and EG3B are me figuring out how to write to the DOM of the HTML file.
    Then I discovered that you have to call document.open() before writing, and document.close() afterwards.

*/

function EGTest()
{
    var strList = ["Yo", "hey", "Good Morning", "Yonder", "How are you"];
    for(i=0; i<strList.length; i++)
    {
        document.getElementById("spanArea").innerText += strList[i] + "\n";
        console.log(strList[i]);
    }
}

function EG1()
{
    for (i=1; i<=10;++i)
    {
        for (j=1; j<=10;++j)
        {
            if (j != 10)
            {
                document.getElementById("spanArea").innerHTML += String(i * j) + "  ";
            }
            else
            {
                document.getElementById("spanArea").innerHTML += "\n" + String(i * j) + "\n";
            }
        }
        document.write("<br>");
    }
}

function EG2()
{
    for (i=1; i<=10;++i)
    {
        for (j=1; j<=10;++j)
        {
            if (j != 10)
            {
                document.getElementById("spanArea").innerText += "\t" + "\t"+ "\t" + String(i * j) ;
            }
            else
            {
                document.getElementById("spanArea").innerText += String(i * j) + "\n";
            }
        }
        document.write("<br>");
    }

}

function EG3B()
{
    var Var = "Yo";
    document.body.innerHTML+="<span style='display:inline-block;width:30px;'>" + Var + "</span>";
}
function EG3C()
{
    document.open()
    // var Var = "Yo";
    document.write("Hello World!");
    document.close()
}

function EG3Done()
{
    document.open();
    for (i = 1; i <= 10; ++i)
    {
        for (j = 1; j <= 10; ++j)
        {
        document.write("<span style='display:inline-block;width:30px'>" + i * j + "</span>")
        }
    document.write("<br>")
    }
    document.close()
}

EG3()