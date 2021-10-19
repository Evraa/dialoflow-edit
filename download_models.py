import gdown

model_size = -1
while model_size>2 or model_size <0:
    print ("Pick the size you're interested in: \n \t0: Base   1: Medium   2: Large")
    model_size = int(input())
    
model_urls = ['https://drive.google.com/uc?id=1oieHqMjuz1Egxw7K9W0MJ6FKnk5kfrcB', 
                'https://drive.google.com/uc?id=1a10dpvGtcPwyNjPZKUwGyyDBQwNPkR52',
                'https://drive.google.com/uc?id=1fM_9Y2tNzAqivDEbbWfKE3am3Dl4R_Zu']
url = model_urls[model_size]
output = "model.bin"
gdown.download(url, output, quiet=False)
