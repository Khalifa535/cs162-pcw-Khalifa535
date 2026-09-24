# CS162 Session 6: The Flask Microframework

## Concept Answers

### 1. What is Flask, and why is it a microframework?

Flask is a lightweight Python web framework. It helps an application receive HTTP requests, choose a response with routes, render HTML, and return data. It is a microframework because it includes the core web features without forcing a large project structure or bundling every extra feature. We can add databases, authentication, and other extensions when we need them.

### 2. What are the roles of these Flask parts?

- **Templates:** HTML files with Jinja placeholders and control flow. They define the page sent to the browser.
- **Static files:** CSS, JavaScript, and images that do not need to be generated for each request.
- **`requirements.txt`:** A list of Python packages and versions needed by the project.
- **Virtual environment (`venv`):** An isolated Python environment for this project’s packages.
- **`render_template`:** Loads a template and fills it with data before returning it as a response.
- **`redirect`:** Tells the browser to make a new request to another URL.
- **`url_for`:** Builds a URL from a function’s route name, which is safer than hard-coding URL strings.
- **`session`:** Stores small pieces of user-specific data between requests, such as whether a user is logged in.

### 3. What do these commands do?

```bash
pip3 install -r requirements.txt
```

Installs the packages listed in `requirements.txt`.

```bash
export FLASK_APP=app
```

Tells the Flask command-line tool to find the application in the `app` module, usually `app.py` or an `app` package.

```bash
python3 -m flask run
```

Starts Flask’s development server using the application selected by `FLASK_APP`.

### 4. What is the difference between the two ways of running Flask?

```bash
export FLASK_APP=app.py
python3 -m flask run
```

This uses Flask’s command-line runner. It is convenient for development because it supports Flask options, debug mode, and automatic reloading.

```bash
python3 app.py
```

This runs the Python file directly. It requires the file to call `app.run()` and is useful when the application has its own startup code or when we want to control how it starts.

### 5. Why specify library versions?

Specific versions make the environment reproducible. Without them, a future installation might download a newer version with different behavior and break the application. I can find the version used in an environment with `pip show package-name` or `pip freeze`, then record the tested version in `requirements.txt`.

### 6. What does `@app.route` do?

`@app.route('/')` registers the function below it as the handler for requests to `/`. Flask calls `main()` when a matching request arrives. The decorator must be directly above the function so Python applies it to that function. The default allowed method is `GET`.

### 7. What is a decorator?

A decorator is a function that wraps or modifies another function without requiring us to rewrite the original function. Flask decorators are useful because they attach web behavior, such as a URL route or login requirement, directly to the function that handles it.

### 8. What is Flask’s `config` attribute?

`app.config` stores application settings. For example:

```python
app.config["TESTING"] = True
app.config["SECRET_KEY"] = "abc"
```

`TESTING` enables testing-related behavior. `SECRET_KEY` protects signed session data and should be a private, unpredictable value in a real application.

### 9. What is JSON, and why use it?

JSON is a text format for representing structured data with objects, arrays, strings, numbers, booleans, and `null`. It is useful because Python, JavaScript, browsers, and many other systems can create and parse it consistently. APIs commonly use JSON to exchange data without sending a complete HTML page.

### 10. What are Flask’s default host and port?

Flask’s development server normally uses host `127.0.0.1` and port `5000`. We can change them from the command line:

```bash
python3 -m flask run --host=0.0.0.0 --port=8000
```

The first value controls which network interface accepts connections, and the second controls the port.
