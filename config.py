# type: ignore
import os
import pymysql

# Below is the sqlite configuration to be used in github code space
basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    """Base configuration for the Flask application."""

    


    @classmethod
    def init_app(cls, app):
        """Initialize the Flask application."""
        
        cls.app = app

        # General configuration for app

        ####### UPDATE NEEDED BELOW #######
        # Add a global environment variable in Windows  (and linux for testing)
        cls.app.config['SECRET_KEY'] = os.environ.get("TIMESHEET_MASTER_SECRET_KEY")

        # Database configuration
        cls.configure_database()

        

    @classmethod
    def configure_database(cls):
        """Configure the database URI based on the environment."""
        # env = os.getenv('FLASK_ENV', 'development')

        # Hint: try to set FLASK_ENV to 'development' as a fixed global env variable
        env = os.getenv('FLASK_ENV')
        if env == 'development':


            ####### UPDATE NEEDED BELOW #######
            # Setup Mysql on Windows and create and activate the root user with all grants
            # Create new Database on mysql for both Windows and linux
            # Create a deamon user as a temp backdoor for testing all feature locally
            # Create and restore all sensitive data like the mysql data base login as global env variables stored locally

            # cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{user}:{password}@localhost/iticket_database_development"
            #cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('DEV_USER')}:{os.environ.get('DEV_PASS')}@localhost/{os.environ.get('FULL_ITICKET_DEV_DB')}"
            cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://dev_root_user_daemon:dev_root_password_daemon@localhost/timesheet_master_database_development"
            #cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://ahmed:ahmed@localhost/iticket_database_development"

            
        elif env == 'testing':
            cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('TST_USER')}:{os.environ.get('TST_PASS')}@localhost/{os.environ.get('FULL_TICKETTREK_TST_DB')}"
        elif env == 'production':  # Assuming 'production'
            cls.app.config['SQLALCHEMY_DATABASE_URI'] = f"mysql+pymysql://{os.environ.get('PROD_USER')}:{os.environ.get('PROD_PASS')}@localhost/{os.environ.get('FULL_TICKETTREK_PROD_DB')}"
        else:
            print("configuration env is not defined")

        cls.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    @classmethod
    def get_app(cls):
        """Return the Flask application instance."""
        return cls._app

class DevelopmentConfig(Config):
    """Development configuration for the Flask application."""

    @classmethod
    def init_app(cls, app):
        super().init_app(app)


class TestingConfig(Config):
    """Testing configuration for the Flask application."""

    @classmethod
    def init_app(cls, app):
        super().init_app(app)


class ProductionConfig(Config):
    """Production configuration for the Flask application."""

    @classmethod
    def init_app(cls, app):
        super().init_app(app)


# Map configuration names to their respective classes
config_env_name = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig  
}


# Add this function to export the config
def get_config(env='development'):
    return config_env_name[env]()