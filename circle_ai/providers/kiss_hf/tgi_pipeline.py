from transformers import pipeline
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


device = "auto"

# model_name = os.getenv("MODEL_NAME", "distilbert/distilgpt2")
# model_name = os.getenv("MODEL_NAME", "HuggingFaceTB/SmolLM-135M")
# model_name = os.getenv("MODEL_NAME", "microsoft/Phi-3-mini-4k-instruct")
model_name = os.getenv("MODEL_NAME", "openai-community/gpt2")


pipe = pipeline(
    "text-generation",
    model=model_name,
    device_map=device,
)  # torch_dtype=bfloat16,

logger.info("model loaded to memory: " + model_name)

logger.info(
    "model size in memory (GB): "
    + str(round(pipe.model.get_memory_footprint() / 1024**3, 3)),
)
