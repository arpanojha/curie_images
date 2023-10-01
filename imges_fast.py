from fastapi import FastAPI
from fastapi.responses import FileResponse
import os

app = FastAPI()

list_of_files ={}

directory_path='./src'
if os.path.isdir(directory_path):
    file_list = os.listdir(directory_path)
    for i in file_list:
       k = i.split('.')
       list_of_files[k[0]] = i
else:
    print("The specified path is not a directory.")

#print(list_of_files)
image_folder = "src"  # Replace with the actual folder path

@app.get("/")
def perfect_motorcycle():
    return {"message":"works"}

@app.get("/images/{image_filename}")
def serve_image(image_filename: str):
    image_path = os.path.join(image_folder, list_of_files[image_filename])
    
    if os.path.exists(image_path):
        return FileResponse(image_path)
    else:
        return {"message": "Image not found"}, 404

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
