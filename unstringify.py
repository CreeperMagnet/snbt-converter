import os, shutil
import common, config

os.chdir(common.snbt_converter_path)

os.system('java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server --input "'+ config.target_path +'" --output "'+ config.target_path +'"')

shutil.rmtree('logs')
shutil.rmtree(os.path.join(config.target_path,".cache"))
shutil.rmtree(os.path.join(config.target_path,"data"))

common.remove_matching_files(config.target_path,".+\\.snbt")