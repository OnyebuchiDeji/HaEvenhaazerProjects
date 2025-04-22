
Date: wed-5-June-2024

Heading Types
#   Heading 1
##   Heading 2
###   Heading 3
####   Heading 4
#####   Heading 5
######   Heading 6
#######   Heading 1 <- Just text

Bolding and Italics
Yo, here is a sentence: **woke up** blessed!
I feel good... so __good__
I *feel* so _good*

##  Can even use HTML
I've been revived <span style="color: red">So Truuuueee</span>

##  Hard Breaks Vs. Soft breaks

Here is line 1.
Here is line 2.
They are separated in md text.
But not in the actual markdown render.

Here is line 1.

Here is line 2.

This is a hard break. But I want a soft break, so I use <br>.

This is line 1.<br>
This is line 2.<br> 
Can even use <br>, for soft breaks.


##  These are for links:

First way to do a link
[this is a random link](https://google.com/)

Second way:

The `alink` can be used from anywhere in the md file

[Pree from alink anwhere](alink)

For this second way, it was used here
[Link to pree](alink)


Link defined here:
[alink](https://google.com/)

##  Adding comments
First way to add comments:

[comment]: <> (Just a random comment)

Second way:
[//]: <>(Second random comment)


##  Adding/linking images

[MyPic1](../resources/2003289.jpg)

Same image, but rendered and displayed in the markdown file:
![MyPic1](../resources/2003289.jpg)

Can even reference the image link from anywhere in markdown file.
Check it:
![MyPic1][imageRef]

Ref defined here:
[imageRef]: ../resources/2003289.jpg


##  Block quoutes -- uses angled brackets

> "There is a Spirit in man, and the breath of the Almiighty gives him understanding. That breath has been given to me."
>
> "- Elihu"

##  Making lists:

#### First way:<br>
- item 1
- item 2

#### Second way:<br>
* item 2
* item 3
* item 4

#### Can even stack:<br>
* item 5
    * Consistuent 1
        * bolts
        * diodes
        * microcontroller board (raspberry pi)
            * fan
            * exoskeleton/casing
* item 6
* item 7

#### Numbered lists:<br>

#####   Steps to making the static site:
1.  Create base HTML, CSS, JS
    1. Make base html
    2. Structure using template elements
    3. write JS to load each corresponding element appropriately.
    4. Add topbar button and theme button elements.
        1. Download icons
        2. Add to template.
        3. Write JS to load them from template element.
        4.  Write JS to add or remove class appropriately to notify it on when the topbar toggle button is clicked or note
    5. Implement resizeing function and the removing of topbar nav items when size shrinks past 769px
        1.  Use JS to create and remove classes appropriately to indicate when resizing has occured, and using the class from the topbar button, to know in what way to display the nav elements in different size thresholds.
            * A long explanation

## Code Snippets:

####    For Python:
```python

print("Yo! Revived!")

```

####    For Java
```java
System.out.println("Yh! this is Jaja!\n");
```

####  For C++:
```cpp

#include <iostream>

int main()
{
    std::cout << "BRUH!\n";
}

```

####    Code Without Syntax Highlighting

```
pip install vidstream
```

```sh
curl `some_link`
```


##  Tables in Markdown<br>
|Name|Age|Height|
|----|---|------|
|Jonathan|21|180|
|Keneth|20|182|

Here is a seperator to seperate sections:

```

Here is something with strike-through style<br>
~~Struck Through~~

```


##  For Check Lists -- Marking Milestone <br>
Pree the check boxes <br>

- [x] Milestone 1
- [x] Milestone 2
- [x] Milestone 3
- [] Milestone 4
- [x] Milestone 5
- [] Milestone 6
- [] Milestone 7

```
This didn't evaluate because I put it in a section
surrounded by these "``` ```" quotes
##  Subscription and Superscribtion <br>
X<sub>1</sub> and X<sub>2</sub>

X<sup>2</sup> = X * X


```

##  Subscription and Superscribtion Now Working<br>
X<sub>1</sub> and X<sub>2</sub>

X<sup>2</sup> = X * X


##  Rendering Math Formulas

LateX in MD Inline $\Phi^{2} + x = 3$

Putting two dollars shows the eqation in a separate line <br>

It does it in Display mode:<br>

LateX in MD Display $$\Phi^{2} + x = 3$$

Though Inline mode does wortk: <br>
LateX in MD Inline $$\Phi^{2} + x = 3$$