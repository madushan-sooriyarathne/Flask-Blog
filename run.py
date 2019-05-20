from flaskblog import create_app

app = create_app()

if __name__ == '__main__' :
    app.run(debug=True)
    # Running the app in debug mode. 
    # Note: Only run debug mode on Development environments
    # When it's come to production, You should remove this debug flag. 