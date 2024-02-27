def generate_new_page_html():
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>New Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 20px;
        }
        h1 {
            text-align: center;
        }
        figure {
            text-align: center;
        }
        figcaption {
            margin-top: 10px;
            font-style: italic;
        }
    </style>
</head>
<body>
    <h1>Figure with Description</h1>
    <figure>
        <img src="https://via.placeholder.com/400" alt="Placeholder Image" width="1200">
        <figcaption>This is a placeholder image with a description.</figcaption>
    </figure>
</body>
</html>
"""

    with open("new_page_py.html", "w") as file:
        file.write(html_content)

if __name__ == "__main__":
    generate_new_page_html()
