import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")


API_ID = int(getenv("API_ID", "1605196")) #optional
API_HASH = getenv("API_HASH", "4ec4af4c800fb44cc084bb7f2df035bc") #optional

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "161587624").split()))
OWNER_ID = int(getenv("OWNER_ID", "161587624")
MONGO_URL = getenv("MONGO_URL", "mongodb+srv://bangshimz:Kyosakazi5237_@cluster0.6bt77rf.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = getenv("BOT_TOKEN", "6305086084:AAEeMI2GleMZvNJt_SjWgQIJUKsAH16blhg")
ALIVE_PIC = getenv("ALIVE_PIC", "https://telegra.ph/file/d20de5f389dd032dea489.jpg")
ALIVE_TEXT = getenv("ALIVE_TEXT")
PM_LOGGER = getenv("PM_LOGGER", "1561224881")
LOG_GROUP = getenv("LOG_GROUP", "1001050135159")
GIT_TOKEN = getenv("GIT_TOKEN") #personal access token
REPO_URL = getenv("REPO_URL", "https://github.com/ITZ-ZAID/ZAID-USERBOT")
BRANCH = getenv("BRANCH", "master") #don't change
 
STRING_SESSION1 = getenv("STRING_SESSION1", "BQB3l38fYfaRgcBsr3Z3vlbZBEEmDkLzesgkoEY3pVVWq5NO8qFm7FfE84KVTPNdtbtv0URKsFg4XhnkrE_XMWHa-sT_s4rHdR1ppLL9S1WX06j0l47NdLbgNnsdgp7aKT6E00MK6ssjMUTKh7RtgqiYQmxTbHpoIqvxLqt23-1dTW_-qTideH7vItzbJbGn0o1XEdsjJcQB3z0WIsBGe24LgSG7YZIj_VoeBVdfBDHzYy2orDpVDmSTh8sZMvt-5saPP-Z5pl7fasLq6vpoEazDA3Q2u7zfc-42JM9CEnD5AUtUgRKl4O1WiK8ltuSesWHF79abTTZ9QxLJ9B3O8bsiAAAAAAmhoagA")
STRING_SESSION2 = getenv("STRING_SESSION2", "")
STRING_SESSION3 = getenv("STRING_SESSION3", "")
STRING_SESSION4 = getenv("STRING_SESSION4", "")
STRING_SESSION5 = getenv("STRING_SESSION5", "")
STRING_SESSION6 = getenv("STRING_SESSION6", "")
STRING_SESSION7 = getenv("STRING_SESSION7", "")
STRING_SESSION8 = getenv("STRING_SESSION8", "")
STRING_SESSION9 = getenv("STRING_SESSION9", "")
STRING_SESSION10 = getenv("STRING_SESSION10", "")
