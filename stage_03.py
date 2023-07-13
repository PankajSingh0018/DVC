with open('artifact.txt',"r") as f:
    text = f.read()


with open('artifact.txt',"w") as f:
    f.write(text + " minor changes on the text file")

print(f'This is the stage 03 testing with text as : {text}')

print("\n")

print(f'This is the end of Stage 03')