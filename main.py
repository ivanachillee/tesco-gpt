from decouple import config
from TescoController import TescoController
from PersonalShopper import PersonalShopper

#Initialise things
openai_api_key= config("OPENAI_API_KEY")
controller = TescoController(config("TESCO_IE_AUTH_TOKEN_COOKIE_VALUE"),config("TESCO_IE_REFRESH_TOKEN_COOKIE_VALUE"))

#Create a personal shopper instance
shopper = PersonalShopper(openai_api_key=openai_api_key,tesco_controller_instance=controller)

#Run the personal shopper
shopper.start_shopping()