Flask-Mistune
=============

Flask interface for mistune markdown parser

[![Build Status](https://travis-ci.org/ellisonleao/flask-mistune.svg?branch=master)](https://travis-ci.org/ellisonleao/flask-mistune)
[![PyPi version](https://img.shields.io/pypi/v/Flask-Mistune.svg)](https://crate.io/packages/flask-mistune/)
[![PyPi downloads](https://img.shields.io/pypi/dm/Flask-Mistune.svg)](https://crate.io/packages/flask-mistune/)

## How to install:  
``` pip install flask-mistune ```

## How to use:  
```python 
# import the packages
from flask_mistune import Mistune, markdown
```

```python 
# register the app
Mistune(app)
```

```html 

<!--use as a filter-->
<p>{{ text| markdown }}<p>

```


