import gradio as gr
import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration

# ---------------------------------------------------------
# Step 2: Load the pretrained processor and model
# ---------------------------------------------------------
print("Loading model...")
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# ---------------------------------------------------------
# Step 3: Define the image captioning function
# ---------------------------------------------------------
def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')
    
    # Process the image
    text = "the image of"
    inputs = processor(images=raw_image, text=text, return_tensors="pt")
    
    # Generate a caption for the image
    outputs = model.generate(**inputs, max_length=50)
    
    # Decode the generated tokens to text and store it into `caption`
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    
    return caption

# ---------------------------------------------------------
# Step 4: Create the Gradio interface
# ---------------------------------------------------------
iface = gr.Interface(
    fn=caption_image, 
    inputs=gr.Image(), 
    outputs="text",
    title="Image Captioning",
    description="This is a simple web app for generating captions for images using a trained model."
)

# ---------------------------------------------------------
# Step 5: Launch the Web App
# ---------------------------------------------------------
iface.launch(server_name="0.0.0.0", server_port=7860)

