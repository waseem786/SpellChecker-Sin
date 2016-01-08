# bottleMain2.py

app = Bottle()

with app:

    # Our application object is now the default
    # for all shortcut functions and decorators

    assert my_app is default_app()

    @route('/')
    def hello():
        return 'Hello World'

    # Also useful to capture routes defined in other modules
    import some_package.more_routes
