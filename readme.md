### simple example of using behave for web automation
This is just a simple project to demo using behave with different types of automation, initially selenium. It won't "go deep" into any of the individual types of automation, the purpose is to provide a starting point.

### local setup
Simple-ish setup for now, just using a virtual environment. Will introduce toml if really needed but trying to minimise moving parts. Can install from requirements.txt or as follows. I was on windows.

```DOS
python -m venv venv --prompt .
venv/scripts/activate 
pip install behave
pip install selenium
``````

### first feature
Behave expects features and steps to be in this directory structure (you can alter via a behave.ini or params to behave, keeping defaults for now)
```DOS
mkdir features/steps
```
Create the most simple of features within the features directory (no step/glue code yet). Running behave will generate some boilerplate stepdef code that you can put in a steps file.

e.g. [simple_feature.feature](features/simple_feature.feature) and [simple_steps.py](features/steps/simple_steps.py)
```gherkin
Feature: simple feature
    Scenario: simplest scenario
        Given this simple thing
        When this happens
        Then this is expected
``````

```python
@given(u'this simple thing')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given this simple thing')
```

### logging
This is basic but project shows how to initialise in [environment.py](features/environment.py), have just shown how to use with a config file

Even though the level is set to DEBUG in the file, this was overridden by behave. To see the debug messages run behave with either of the following switches
```DOS
behave --no-logcapture
behave --logging-level DEBUG
```

### running behave and debugging

#### debugging
Normally would have in .gitignore, but I included the [debug launch configuration](.vscode/launch.json), this allows you to run F5 from the feature file and debug within vscode. 


### selenium setup
Initialising the webdriver is quite costly, so here have shown one way how to do it per-feature. Normally wouldn't optimise for 1 scenario but it's common to avoid initialising on every scenario.