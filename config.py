import os


class Config:
    DOMAIN_URL = 'http://localhost:5000'

    SECRET_KEY = os.environ.get('SECRET_KEY')
    # link to mysql
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')

    # offical tell me to set to true
    SQLALCHEMY_TRACK_MODIFICATIONS = True

    # enabling chinese char
    RESTFUL_JSON = dict(ensure_ascii=False)

    # about upload
    UPLOAD_FOLDER = 'upload/'
    DOWNLOAD_FOLDER = 'download/'
    ALLOWED_EXTENSIONS = set(
        ['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'psd', 'bmp','tif', 'tiff', 'tga', 'sai2'])
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024
    THUMBNAIL_SIZE=[1024, 512, 256]
    
    # RequestParser error https://flask-restplus.readthedocs.io/en/stable/parsing.html
    BUNDLE_ERRORS = True
    # disable fields mask https://flask-restplus.readthedocs.io/en/stable/mask.html
    RESTPLUS_MASK_SWAGGER = False
    # validation fields or args https://flask-restplus.readthedocs.io/en/stable/swagger.html
    RESTPLUS_VALIDATE = True

    # wechat Oauth 2.0
    WX_GZ_APPID = 'wxe2e76dfd60ec74b1'
    WX_GZ_APPSECRET = '8795414bc52b98b92cc7918a13a01d7d'

    WX_KF_APPID = 'wx9c88c3320f959b7c'
    WX_KF_APPSECRET = 'e79669c7d74a548e0a95aa2bf4952913'

    # CORS_HEADER = 'Content-Type, auth'
    CORS_RESOURCES = {r"/*": {"origins": "http://localhost:3000"}}
    CORS_METHODS = "GET,POST,OPTIONS"
    CORS_SUPPORTS_CREDENTIALS = True


class DevelopmentConfig(Config):
    pass


class TestingConfig(Config):
    pass


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
}
