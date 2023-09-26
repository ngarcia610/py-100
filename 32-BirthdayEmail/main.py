from dotenv import dotenv_values

secrets = dotenv_values(".env")


print(secrets["EMAIL"])
print(secrets["PASSWORD"])
print(secrets["APPKEY"])
