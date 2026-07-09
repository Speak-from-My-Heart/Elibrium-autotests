import os
from dotenv import load_dotenv

load_dotenv()

#Cards
BASE_URL = os.getenv("BASE_URL")
CORPORATE_CARDS = "/corporate-cards"
VIRTUAL_CARDS = "/virtual-cards"
TRAVEL_CARDS = "/travel-cards"
CARDS_FOR_ADVERTISING = "/advertising-cards"
CARDS_FOR_SERVICES = "/services-cards"
GLOBAL_READY_CARD = "/global-cards"
#Industries
STARTUPS = "/startups"
MID_SIZE_COMPANIES = "/mid-size-companies"
AFFILIATES_AND_MARKETING = "/affiliates-marketing-agencies"
AFFILIATES_NETWORKS = "/affiliate-networks"
#Addition
PRICING = "/pricing"
FULL_PRICE = "/business"
CONTACT = "/contact"
API_ELIBRIUM = "https://api.elibrium.io/docs"

#Buttons
SIGN_IN = "https://app.elibrium.io/auth/login"
TRY_DEMO = "/try-demo"
OPEN_ACCOUNT = "/open-account"
BOOK_A_CALL = "/book-a-call"

#Support
INFO_EMAIL = "info@elibrium.io"
US_ADDRESS = "1621 Central ave # 56352 Cheyenne, WY 82001"
GB_ADDRESS = "Office FR 412, 1 Phipp Street, London, EC2A 4PS. UK"

#Footer links
PRIVACY_POLICY = "/privacy"
TERMS_OF_SERVICE = "/terms-of-service"
COOKIE_POLICY = "/cookie-policy"
ACH_AUTHORIZATION = "/ach-authorization"
CARTHOLDER_AGREEMENT = "/cardholder-agreement"
CUSTOMER_AGREEMENT = "/customer-agreement"