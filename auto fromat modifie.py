import os

# Change directory to the desired path
os.chdir("C:/Users/HP/Desktop/ai/number-plate-detection")

i = 1
for file in os.listdir():
    src = file  # Use 'src' to match the variable case
    dst = "car" + str(i) + ".png"
    os.rename(src, dst)
    i += 1  # Use 'i += 1' instead of 'i=i+1'
