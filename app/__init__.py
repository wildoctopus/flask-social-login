from flask import Flask
from app.config.config import ProductionConfig, DevelopmentConfig
from flask_cors import CORS
import os




def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    
    if os.environ.get("FLASK_ENV").upper()=="PRODUCTION":
        #Add URLs to CORS
        #CORS(app,origins=[Constant.workspace_prod_url, Constant.prod_website_url])

        # app configuration
        CORS(app)
        app.config.from_object(ProductionConfig)
        
    else:
        CORS(app)
        app.config.from_object(DevelopmentConfig)
    
    

    with app.app_context():

        #import modules
        from app.auth import main
        from app.auth.fb import fb_auth
        from app.auth.google import google_auth
        #from app.auth.twitter import twitter_auth
        

        #register blueprints    
        app.register_blueprint(main)
        app.register_blueprint(fb_auth)
        app.register_blueprint(google_auth)
        #app.register_blueprint(twitter_auth)
        
        
        return app
