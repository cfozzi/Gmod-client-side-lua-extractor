import os

ReadDirectory = "Input/"
TempDirectory = "Temp/"
SaveDirectory = "Output/"



x = 0
for filename in os.listdir(ReadDirectory):
	if filename.endswith(".lua"):
		with open(ReadDirectory + filename, "r+b") as rf:
			with open(TempDirectory + str(x) + ".lzma", "w+b") as wf:
				wf.write(rf.read()[32:])
				wf.close()
			os.system(".\\lzma d " + TempDirectory + str(x) + ".lzma " + SaveDirectory + str(x) + ".lua")
			print(str(x) + ".lua")
			x += 1
print("All files extracted.")

for filename in os.listdir(TempDirectory):
	if filename.endswith(".lzma"):
		os.remove(TempDirectory + filename)
print("Temp files removed.\nEmpty output folder before running again to avoid overwriting files!")