
"""
    Date: Wed-5-June-2024

    Reference: ChatGPT
"""

import markdown


def EG1_GenerateHTML():
    with open("source/EG1.md", "r") as file:
        markdown_content = file.read()

    #   Convert Markdown to HTML
    html_content = markdown.markdown(markdown_content)

    #   HTML template wit a placeholder for the converted Markdown content
    html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.o">
        <title>Markdown to HTML</title>
    </head>

    <body>
        <!--Insert the converted Markdown content here-->
        {content}
    </body>
    </html>
    """

    #   Insert the converted HTML content into the HTML template
    complete_html = html_template.format(content=html_content)

    #   Write the complete HTML to a file
    with open("source/output.html", "w") as file:
        file.write(complete_html)
    
    print("HTML file has been created successfully!")
    


def main():
    EG1_GenerateHTML()



if __name__=="__main__":
    main()