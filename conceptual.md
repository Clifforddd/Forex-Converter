### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
    Python: For server-side scripting, Python is commonly used. Client-side scripting is the most common use of Javascript.
    Javascript: Client-side scripting is the most common use of Javascript. It has the UTF-16 encoding.

- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.
  s = {"a": 1, "b": 2}
  s.c;
  s['c'];

- What is a unit test?
  A unit test is a way of testing a unit - the smallest piece of code that can be logically isolated in a system. In most programming languages, that is a function, a subroutine, a method or property.
    
- What is an integration test?
  Integration Testing is defined as a type of testing where software modules are integrated logically and tested as a group.

- What is the role of web application framework, like Flask?
  A web framework (WF) or web application framework (WAF) is a software framework that is designed to support the development of web applications including web services, web resources, and web APIs.

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
    Query is better to use in an application, because it is easy to access the param.

- How do you collect data from a URL placeholder parameter using Flask?
  @app.route('/landingpage<id>') 
    def landing_page(id):
    ...

- How do you collect data from the query string using Flask?
    from flask import Flask, request
    # ...
    @app.route('/search', methods=['GET'])
    def search():
        args = request.args
        return args

- How do you collect data from the body of the request using Flask?
    request.data

- What is a cookie and what kinds of things are they commonly used for?
    Cookies are text files with small pieces of data — like a username and password — that are used to identify your computer as you use a computer network. Specific cookies known as HTTP cookies are used to identify specific users and improve your web browsing experience.

- What is the session object in Flask?
    In the flask, a session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their associated values.
- What does Flask's `jsonify()` do?
    Flask jsonify is defined as a functionality within Python's capability to convert a json output into a response object with application/json mimetype by wrapping up a dumps function for adding the enhancements.
