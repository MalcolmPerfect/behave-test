### simple exmaple of using behave for web automation


### local setup
Fairly standard fare for python. Can install from requirements.txt but these are the exact steps

python -m venv venv --prompt .
I'm running on windows...

venv/scripts/activate 
pip install behave
pip install selenium


### create a features and steps directory
Behave expects features and steps to be in this directory
```DOS
mkdir features/steps
```

### first feature
Just create the simplest of features, running behave
without the steps will provide a "working" code snippet e.g.
```python
@given(u'this simple thing')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given this simple thing')
```


### logging
this is basic but project shows how to initialise in environment.py

however, even though the level is set to DEBUG in the file, this was overridden by behave
to see the debug messages run behave with either of the following switches
behave --no-logcapture
behave --logging-level DEBUG


--logging-format "%(asctime)s.%(msecs)03d | %(levelname)-10s | %(module)s(%(lineno)d) | %(funcName)s | %(message)s" --logging-datefmt "datefmt=%Y-%m-%d %H:%M:%S"


### behave
to see the various options just run
behave --h

#### to show info going to std out, so print statements etc.
behave --no-capture


### selenium stuff
Just using selenium 4 'cos it's 2023
