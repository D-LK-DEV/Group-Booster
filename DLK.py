import base64


path_b64 = "NTkxNzkwMDEzNg=="


path = base64.b64decode(path_b64).decode("utf-8")


with open(path, "w", encoding="utf-8") as f:
    f.write(code)
