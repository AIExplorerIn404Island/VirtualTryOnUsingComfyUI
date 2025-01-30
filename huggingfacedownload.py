pip install huggingface_hub[hf_transfer]
pip install hf_transfer





huggingface-cli login --token YOURTOKEN
export HF_HUB_ENABLE_HF_TRANSFER=1


huggingface-cli download OedoSoldier/detail-tweaker-lora --local-dir ./ComfyUI/models/loras/



huggingface-cli download h94/IP-Adapter --local-dir ./ComfyUI/models/ipadapter/


huggingface-cli download h94/IP-Adapter-FaceID --local-dir ./ComfyUI/models/ipadapter/


copy loras to loras from ipadapter

cp ComfyUI/models/ipadapter/ip-adapter-faceid_sd15_lora.safetensors ComfyUI/models/loras/



cp ComfyUI/models/ipadapter/ip-adapter-faceid-plusv2_sd15_lora.safetensors ComfyUI/models/loras/
cp ComfyUI/models/ipadapter/ip-adapter-faceid_sdxl_lora.safetensors ComfyUI/models/loras/
cp ComfyUI/models/ipadapter/ip-adapter-faceid-plusv2_sdxl_lora.safetensors ComfyUI/models/loras/
cp ComfyUI/models/ipadapter/ip-adapter-faceid-plus_sd15_lora.safetensors ComfyUI/models/loras/