# only import if running as a custom node
from .comfyui_nunchaku.lora import NunchakuFluxLoraLoader
from .comfyui_nunchaku.models import (
    NunchakuFluxDiTLoader,
    NunchakuPulidApply,
    NunchakuPulidLoader,
    NunchakuTextEncoderLoader,
    NunchakuTextEncoderLoaderV2,
)
from .comfyui_nunchaku.preprocessors import FluxDepthPreprocessor
from .comfyui_nunchaku.tools import NunchakuModelMerger

NODE_CLASS_MAPPINGS = {
    "NunchakuFluxDiTLoader": NunchakuFluxDiTLoader,
    "NunchakuTextEncoderLoader": NunchakuTextEncoderLoader,
    "NunchakuTextEncoderLoaderV2": NunchakuTextEncoderLoaderV2,
    "NunchakuFluxLoraLoader": NunchakuFluxLoraLoader,
    "NunchakuDepthPreprocessor": FluxDepthPreprocessor,
    "NunchakuPulidApply": NunchakuPulidApply,
    "NunchakuPulidLoader": NunchakuPulidLoader,
    "NunchakuModelMerger": NunchakuModelMerger,
}
NODE_DISPLAY_NAME_MAPPINGS = {k: v.TITLE for k, v in NODE_CLASS_MAPPINGS.items()}
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
