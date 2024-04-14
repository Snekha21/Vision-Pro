import os
from PIL import Image
import torch
from transformers import OwlViTProcessor, OwlViTForObjectDetection

# Initialize the OwlViT model and processor
processor = OwlViTProcessor.from_pretrained("google/owlvit-base-patch16")
model = OwlViTForObjectDetection.from_pretrained("google/owlvit-base-patch16")

# Path to the folder containing the images
folder_path = "output"

# Iterate through all the image files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):  # Assuming all images are in .jpg format
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)
        
        texts = [["a photo of a bus"]]  # Text prompt for inference
        inputs = processor(text=texts, images=image, return_tensors="pt")
        outputs = model(**inputs)

        # Process object detection outputs
        target_sizes = torch.Tensor([image.size[::-1]])
        results = processor.post_process_object_detection(outputs=outputs, threshold=0.1, target_sizes=target_sizes)

        i = 0  # Retrieve predictions for the first image for the corresponding text queries
        text = texts[i]
        boxes, scores, labels = results[i]["boxes"], results[i]["scores"], results[i]["labels"]

        # Check confidence level and print if greater than 0.5 (50%)
        for box, score, label in zip(boxes, scores, labels):
            if score > 0.5:  # Confidence threshold
                box = [round(coord, 2) for coord in box.tolist()]
                print(f"Detected {text[label]} with confidence {round(score.item(), 3)} at location {box}")
                print(f"Path: {image_path}")
