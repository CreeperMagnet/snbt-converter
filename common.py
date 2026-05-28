import urllib.request, json, os, re
import config

if not os.path.exists(config.target_path) :
  print("The folder specified in config.py does not exist.")
  exit()

snbt_converter_path = os.path.dirname(__file__)

# The link to Mojang's version manifest. This probably shouldn't change.
manifest_url = 'https://piston-meta.mojang.com/mc/game/version_manifest_v2.json'

# A function to read json from a URL
def json_from_url(url) :
    return json.loads(urllib.request.urlopen(url).read())

version_manifest = json_from_url(manifest_url)

valid_input = False
version = None
while valid_input == False :
  user_input_version = input("What version are you working on? : ")

  for version_i in version_manifest['versions'] :
    if version_i['id'] == user_input_version :
      version = version_i
      valid_input = True
      break
  if not valid_input :
    print("That is an invalid version. Try again.")

version_data = json_from_url(version['url'])
server_jar_url = version_data['downloads']['server']['url']

urllib.request.urlretrieve(server_jar_url,os.path.join(snbt_converter_path,"server.jar"))

def remove_matching_files(path,regex) :
  for root, _, files in os.walk(path) :
    for file in files :
      try :
        if re.match(regex,file) != None :
          os.remove(os.path.join(root,file))

      except Exception as e:
        print(e)
        print("Had an error with file: " + os.path.join(root,file))