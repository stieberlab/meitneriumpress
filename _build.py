import os
import shutil
import subprocess
import argparse

outDir = "site"
stylesDir = "styles"
imagesDir = "img"

def buildPage(page, template):
    cmd = []
    cmd.append("pandoc")
    cmd.append("--from=markdown")
    cmd.append("--to=html")
    cmd.append(f"--output={outDir}/{page}.html")
    cmd.append(f"--template=templates/{template}.html")

    cmd.append(f"pages/{page}.md")

    subprocess.run(cmd)

argParser = argparse.ArgumentParser()
args = argParser.parse_args()

# Create output site directory
if os.path.isdir(outDir): shutil.rmtree(outDir)
os.makedirs(outDir)
shutil.copytree(imagesDir, f"{outDir}/{imagesDir}")
shutil.copytree(stylesDir, f"{outDir}/{stylesDir}")

buildPage("index", "index")
