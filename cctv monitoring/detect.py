from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image
import torch
import os

processor = DetrImageProcessor.from_pretrained("facebook/detr-resnet-50", revision="no_timm")
model = DetrForObjectDetection.from_pretrained("facebook/detr-resnet-50", revision="no_timm")

prompt = "human"

folder_path = "output"

for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"): 
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        inputs = processor(images=image, return_tensors="pt")
        outputs = model(**inputs)

        target_sizes = torch.tensor([image.size[::-1]])
        results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

        for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
            if score >= 0.5 and model.config.id2label[label.item()] == prompt:
                box = [round(coord, 2) for coord in box.tolist()]
                print(
                    f"Detected {model.config.id2label[label.item()]} with confidence "
                    f"{round(score.item(), 3)} at location {box} in {image_path}"
                )
